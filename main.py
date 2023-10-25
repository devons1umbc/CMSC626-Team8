import argparse
import os

arg = argparse.ArgumentParser()
arg.add_argument("-s", "--search", type=str, help="Search for a file")
arg.add_argument("-d", "--download", type=str, help="Download a file")
arg.add_argument("-r", "--read", type=str, help="Read a file")

args = arg.parse_args()


def search(query):
    files = os.listdir("files/")
    for file in files:
        if file.lower() == str(query).lower():
            users = os.listdir('files/' + file)
            for user in users:
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


if __name__ == "__main__":
    if args.search:
        print(search(args.search))
    elif args.read:
        print(read(args.read))
    elif args.download:
        print("Need to insert a download")
    else:
        print("Bruh")
