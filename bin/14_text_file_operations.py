"""
Text file operations: Read/Write to text files with extension like
.txt, .log, .yourlog, .mylog
"""

"""
We have functions for each operation
    For Writing: 1) write 2) writelines 3) print-function
    For Reading: 1) read 2) readlines 3) readline 4) for-loop to read line by line
"""

"""
We need to follow 3 steps
Step-1: connect to file
Step-2: Read/Write
Step-3: Disconnect
"""

print("All write operations")
print("-"*20)
# --------------

# Step-1: connect to file
# --------------
# my_file_handle = open("txt file name OR txt file path here", "mode")
my_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write only, It will create new file, IMPORTANT it will erase existing file content
# mode 'r': Read only, It will NOT create new file
# mode 'a': Append mode, It will create new file only if file not present
# mode 'w+': RW, It will create new file, IMPORTANT it will erase existing file content
# mode 'r+': RW, It will NOT create new file
# mode 'a+': RW, It will create new file only if file not present
#       RW means: using same file handle we can call read methods to read
#           and write methods to write

# Step-2: Write
# --------------

# our data
x = 10
y = "Python"

# Convert other type of data to string because write() writelines() methods
#   requires data in string format
x = str(x)

# 1. write : We can pass one string/value only
my_file_handle.write(x+"\n")
my_file_handle.write(y+"\n")

# 2. writelines: we can pass any collection of values like list/tuple etc
my_data_in_list = [x+"\n", y+"\n"]
my_file_handle.writelines(my_data_in_list)

# 3. print-function
print(x, y, 20, "Java", sep="\n", file=my_file_handle)

# Step-3: Disconnect
# --------------
my_file_handle.close()

print("""
All write operations are completed.
Please check
my_out_file.txt
""")

print("#"*40, end="\n\n")
################################

print("Reading from file using 1) read()")
print("-"*20)
# --------------

# Step-1: connect to file
# --------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# --------------
file_content = my_file_handle.read()
# returns entire content in one string
print("file_content:", file_content, end="\n\n")
print("file_content in RAW FORMAT:", repr(file_content), end="\n\n")

# Step-3: Disconnect
# --------------
my_file_handle.close()

print("#"*40, end="\n\n")
################################

print("Reading from file using 2) readlines()")
print("-"*20)
# --------------

# Step-1: connect to file
# --------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# --------------
file_content = my_file_handle.readlines()
# returns entire content in list
print("file_content:", file_content, end="\n\n")

# Step-3: Disconnect
# --------------
my_file_handle.close()

print("#"*40, end="\n\n")
################################

print("Reading from file using 3) readline()")
print("-"*20)
# --------------

# Step-1: connect to file
# --------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# --------------
file_content = my_file_handle.readline()
# returns one line
print("1st line:", file_content, end="\n\n")

file_content = my_file_handle.readline()
# returns one line
print("2nd line:", file_content, end="\n\n")

file_content = my_file_handle.readline()
# returns one line
print("3rd line:", file_content, end="\n\n")

# Step-3: Disconnect
# --------------
my_file_handle.close()

print("#"*40, end="\n\n")
################################

print("Reading from file using 4) read line by line using for-loop")
print("-"*20)
# --------------

# Step-1: connect to file
# --------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# --------------
for each_line in my_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# --------------
my_file_handle.close()

print("#"*40, end="\n\n")
################################
