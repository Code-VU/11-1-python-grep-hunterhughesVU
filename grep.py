from fileinput import filename
import re
import string
import sys


def countpatterninfile():
    regular_expression = input("Enter a regular expression: ")
    count = 0
    fileName = "mbox-long.txt"
    f = open(fileName,"r")
    for line in f:
        line = line.rstrip()
        if(re.search(regular_expression,line)):
            count += 1

    print(fileName,"had",count,"lines that matched",regular_expression)


if __name__ == '__main__':
    # this is called a main method
    # This is another way of telling python THIS IS WHERE YOU SHOULD START RUNNING
    # When this is included, python will begin with the code in this block first
    countpatterninfile()