import argparse
import os
import socket

arg = argparse.ArgumentParser()
arg.add_argument("-s", "--search", type=str, help="Search for a file")
arg.add_argument("-d", "--download", type=str, help="Download a file")
arg.add_argument("-r", "--read", type=str, help="Read a file")
arg.add_argument("-c", "--create", type=str, help="Create a file")

args = arg.parse_args()

directory_server = "192.168.1.6"


def search(query):
    # files = os.listdir("files/")
    files = os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " ls /home/cmsc626/Desktop/files").read().split('\n')
    print(files)
    for file in files:
        print(file)
        if file.lower() == str(query).lower():
            users = os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " ls /home/cmsc626/Desktop/files/" + file).read().split('\n')
            for user in users:
                print(user)
                ping = os.popen("ping -c 1 -w 1 " + str(user)).read()
                if "100% packet loss" in ping:
                    print("Could not connect to " + user)

                else:
                    print("File " + query + " has been found")
                    return [user, file]

    print("File " + query + " not found")
    return 0


def read(query):
    location = search(query)
    if location:
        return os.popen("sshpass -p 12345 ssh cmsc626@" + location[0] + " cat /home/cmsc626/Desktop/" + location[1]).read()


def create(file):
    if search(file):
        print(file + " already exists.")
        return 0
    else:
        ip = socket.gethostbyname(socket.gethostname()+".")
        os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " mkdir /home/cmsc626/Desktop/files/" + file ).read()
        os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " touch /home/cmsc626/Desktop/files/" + file + "/" + ".version").read()
        os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " \"echo \'1\n" + ip + "\' > /home/cmsc626/Desktop/files/" + file + "/" + ".version\"").read()
        os.popen("sshpass -p 12345 ssh cmsc626@" + directory_server + " touch /home/cmsc626/Desktop/files/" + file + "/" + ip).read()
        os.popen("touch " + file)
        return 1


if __name__ == "__main__":
    if args.search:
        print(search(args.search))
    elif args.read:
        print(read(args.read))
    elif args.create:
        print(create(args.create))
    elif args.download:
        print("Need to insert a download")
    else:
        print("Bruh")
