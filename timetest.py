import time
import os

tests = 100

start_time_read = time.time()
for i in range(tests):
    # Permtest.txt already exists locally with user
    os.system("python main.py -r permtest.txt")
end_time_read = time.time() - start_time_read

start_time_write = time.time()
for i in range(tests):
    # Permtest.txt already exists on directory server
    os.system("python main.py -w permtest.txt -m 'commit " + str(i) + "'")
end_time_write = time.time() - start_time_write

print("Read: " + str(end_time_read))
print("Write: " + str(end_time_write))
