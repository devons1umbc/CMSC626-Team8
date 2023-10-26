import argparse
import os
import socket

arg = argparse.ArgumentParser()
arg.add_argument("-s", "--search", type=str, help="Search for a file")
arg.add_argument("-d", "--download", type=str, help="Download a file")
arg.add_argument("-r", "--read", type=str, help="Read a file")
arg.add_argument("-c", "--create", type=str, help="Create a file")
arg.add_argument("-w", "--write", type=str, help="Write to a file")
arg.add_argument("-m", "--message", type=str, help="Message to write to a file")

args = arg.parse_args()

directory_server = "192.168.1.6"


def getip():
    ip = os.popen("ip a").read().split('\n')
    for i in ip:
        i = i.strip()
        if "inet" in i:
            if "127.0.0.1" in i or "::" in i:
                continue
            else:
                return i.split(" ")[1].split("/")[0]
    return 0


def search(query):
    files = os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " ls /home/cmsc626/Desktop/files").read().split('\n')
    for file in files:
        print(file)
        if file.lower() == str(query).lower():
            users = os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " ls /home/cmsc626/Desktop/files/" + file).read().split('\n')
            for user in users:
                if user != '':
                    print(user)
                    ping = os.popen("ping -c 1 -w 1 " + str(user)).read()
                    if "100% packet loss" in ping:
                        print("Could not connect to " + user)
                    else:
                        print("File " + query + " has been found")
                        return [user, file]
    return 0


def read(query):
    location = search(query)
    print(location)
    if location:
        if location[0] == socket.gethostbyname(socket.gethostname() + "."):
            return os.popen("cat files/"+location[1]+"/"+location[1]).read()
        else:
            return os.popen("sshpass -p 12345 ssh cmsc626@" + location[0] + " cat /home/cmsc626/Desktop/" + location[1]).read()
    else:
        print("File " + query + " not found")
        return 0


def create(file):
    if search(file):
        print(file + " already exists.")
        return 0
    else:
        ip = getip()
        os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " mkdir /home/cmsc626/Desktop/files/" + file ).read()
        os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " touch /home/cmsc626/Desktop/files/" + file + "/" + ip).read()
        # Combine everything cause race conditions
        os.popen("mkdir " + "files/" + file + " && " + "touch " + "files/" + file + "/" + file + " && " + "touch " + "files/" + file + "/" + ".version" + " && "
                + "echo \'1\n" + ip + "\' > " + "files/" + file + "/" + ".version" + " && "
                + "sshpass -p 12345 rsync files/" + file + "/" + ".version" + " cmsc626@" + directory_server + ":/home/cmsc626/Desktop/files/" + file + "/.version")
        return 1


def write(file, text):
    location = search(file)
    if location:
        version = open("files/" + location[1] + "/" + ".version").read().split()
        print(version[0])
        ip = getip()

        newfile = open("files/" + location[1] + "/" + location[1], "w")
        newfile.write(text)
        newfile.close()

        updated = open("files/" + location[1] + "/" + ".version", "w")
        updated.write(str(int(version[0])+1) + "\n" + ip)
        updated.close()

        version = open("files/" + location[1] + "/" + ".version").read().split()
        print(version)
        remoteversion = os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " cat /home/cmsc626/Desktop/files/" + location[1] + "/" + ".version").read().split("\n")

        print(remoteversion)

        if int(version[0]) > int(remoteversion[0]):
            os.popen("sshpass -p 12345 rsync files/" + location[1] + "/" + ".version" + " cmsc626@" + directory_server + ":/home/cmsc626/Desktop/files/" + location[1] + "/.version")
            users = os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " ls /home/cmsc626/Desktop/files/" + location[1]).read().split('\n')
            remoteversion = os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " cat /home/cmsc626/Desktop/files/" + location[1] + "/" + ".version").read().split("\n")
            # Exclude the user from the purge who just pushed the file
            exclude = remoteversion[1]
            # Remove users from list of people with file who no longer have latest update
            print("Exclude", exclude)
            print("Users", users)
            for user in users:
                if user != exclude and user != ".version" and user != location[1]:
                    os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " rm -f /home/cmsc626/Desktop/files/" + location[1] + "/" + user).read()
            print("Updated the file!")
            return 1
        else:
            print("File has been modified. Please pull the updated version")
            downgraded = open("files/" + location[1] + "/" + ".version", "w")
            downgraded.write(remoteversion[0] + "\n" + remoteversion[1])
            downgraded.close()
            return 0
    print("File does not exist")
    return 0


def download(file):
    location = search(file)
    if location:
        if os.path.exists("files/" + location[1] + "/" + ".version"):
            remoteversion = os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " cat /home/cmsc626/Desktop/files/" + location[1] + "/" + ".version").read().split("\n")
            version = open("files/" + location[1] + "/" + ".version").read().split()
            ip = getip()
            if version[0] < remoteversion[0] and ip != remoteversion[1]:
                ip = getip()
                # Combine everything cause race conditions
                os.popen("sshpass -p 12345 rsync -r cmsc626@" + location[0] + ":/home/cmsc626/Desktop/files/" + location[1] + " files/" + " && "
                         + "sshpass -p 12345 rsync cmsc626@" + directory_server + ":/home/cmsc626/Desktop/files/" + location[1] + "/.version" + " files/" + location[1] + "/.version" + " && "
                         + "sshpass -p 12345 ssh cmsc626@" + directory_server + " touch /home/cmsc626/Desktop/files/" + location[1] + "/" + ip).read()
                return 1
            else:
                print("You already have the latest version")
                return 0
        else:
            ip = getip()
            print(location)
            # Combine everything cause race conditions
            os.popen("sshpass -p 12345 rsync -r cmsc626@" + location[0] + ":/home/cmsc626/Desktop/files/" + location[1] + " files/")
            # os.popen("sshpass -p 12345 rsync -r cmsc626@" + location[0] + ":/home/cmsc626/Desktop/files/" + location[1] + " files/" + " && "
                     # + "sshpass -p 12345 rsync cmsc626@" + directory_server + ":/home/cmsc626/Desktop/files/" + location[1] + "/.version" + " files/" + location[1] + "/.version" + " && "
                     # + "sshpass -p 12345 ssh cmsc626@" + directory_server + " touch /home/cmsc626/Desktop/files/" + location[1] + "/" + ip).read()
            return 1
    else:
        print("File not found")
        return 0


if __name__ == "__main__":
    getip()
    if args.search:
        print(search(args.search))
    elif args.read:
        print(read(args.read))
    elif args.create:
        print(create(args.create))
    elif args.write:
        print(write(args.write, args.message))
    elif args.download:
        print(download(args.download))
    else:
        print("Bruh")
