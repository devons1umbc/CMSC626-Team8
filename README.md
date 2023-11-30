# CMSC626-Team8
The official repository for CMSC 626 Team 8. 

Members: Devon Slonaker, Chris Abili, Yukta Medha, Jay Paun

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
example: `python main.py -w test.txt -m "This is text in a file`<br>

