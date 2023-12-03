# CMSC626-Team8
The official repository for CMSC 626 Team 8. 

Members: Devon Slonaker, Chris Abili, Yukta Medha, Jay Paun

To set up the environment to be able to test this file system, it is recommended to have at least 3 VMs running Linux. One of them will be a `directory` VM, and the other two will be `client` VMs.<br>
Each VM should be logged in with a user of `cmsc626` and the password of the `cmsc626` user should be `12345`.<br>
You will need to have the `argparse`, `os`, and `socket` Python libraries installed on your client VMs. to be able to run the file system.<br>
Put a `files` directory on the desktop of every VM.<br>
File system away!<br>

usage: main.py [-h] [-s SEARCH] [-d DOWNLOAD] [-r READ] [-c CREATE] [-w WRITE] [-m MESSAGE]

optional arguments:
-h, --help            show this help message and exit<br>
example: `python main.py --help`<br>
<br>
-s SEARCH, --search SEARCH<br>
Search for a file<br>
example: `python main.py -s test.txt`<br>
<br>
-d DOWNLOAD, --download DOWNLOAD<br>
Download a file<br>
example: `python main.py -d test.txt`<br>
<br>
-r READ, --read READ<br>
Read a file<br>
example: `python main.py -r test.txt`<br>
<br>
-c CREATE, --create CREATE<br>
Create a file<br>
example: `python main.py -c test.txt`<br>
<br>
-w WRITE, --write WRITE<br>
Write to a file (must be used with -m)<br>
example: `python main.py -w test.txt -m "This is text in a file`<br>
<br>
-m MESSAGE, --message MESSAGE<br>
Message to write to a file (to be used with -w)<br>
example: `python main.py -w test.txt -m "This is text in a file"`<br>
<br>
-x DELETE, --delete DELETE<br>
Delete a file from the file system<br>
example: `python main.py -x test.txt`<br>
<br>
-z RECOVER, --recover RECOVER<br>
Restore a file previously deleted from the file system<br>
example: `python main.py -z test.txt`<br>
<br>
-g GENERATE, --generate GENERATE<br>
Generates a Public/Private key-pair<br>
example: `python main.py -g True`<br>


