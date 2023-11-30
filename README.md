# CMSC626-Team8
The official repository for CMSC 626 Team 8. 

Members: Devon Slonaker, Chris Abili, Yukta Medha, Jay Paun

usage: main.py [-h] [-s SEARCH] [-d DOWNLOAD] [-r READ] [-c CREATE] [-w WRITE] [-m MESSAGE]

optional arguments:
  -h, --help            show this help message and exit\n
  example: `python main.py --help`\n
  \n
  -s SEARCH, --search SEARCH\n
                        Search for a file\n
  example: `python main.py -s test.txt`\n

  -d DOWNLOAD, --download DOWNLOAD
                        Download a file
  example: `python main.py -d test.txt`
                        
  -r READ, --read READ  
                        Read a file
  example: `python main.py -r test.txt`
  
  -c CREATE, --create CREATE
                        Create a file
  example: `python main.py -c test.txt`
  
  -w WRITE, --write WRITE
                        Write to a file (must be used with -m)
  example: `python main.py -w test.txt -m "This is text in a file`
                        
  -m MESSAGE, --message MESSAGE
                        Message to write to a file (to be used with -w)
  example: `python main.py -w test.txt -m "This is text in a file`

