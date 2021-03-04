#IMPORT ARG FROM SYS MODULE TO WORK WITH FILES
from sys import argv

#ARGUMENTS TO BE USED WHEN CALLING THE SCRIPT
script, input_file = argv

#FUNCTION THAT PRINTS CONTENTS OF FILE 
def print_all(f):
    print(f.read())

#FUNCTION THAT READS FIRST LINE OF FILE
def rewind(f):
    f.seek(0)

#FUNCTION THAT PRINTS SPECIFIC LINE IN THE FILE
def print_a_line(line_count, f):
    print(line_count, f.readline())

#ASSIGNING CURRENT FILE TO ARGV PARAMETER CALLED WHEN CALLING SCRIPT
current_file = open(input_file)

print("First, let us print the whole file: \n")
#READ WHOLE FILE
print_all(current_file)

print("Now let us rewind, just like a tape.")
#GO TO FIRST LINE OF FILE
rewind(current_file)

print("Print three lines from the file: ")
#DEFINE LINE, THE PRINT THAT LINE FROM FILE
current_line = 1
print_a_line(current_line, current_file)

current_line +=1
print_a_line(current_line, current_file)

current_line +=1
print_a_line(current_line, current_file)