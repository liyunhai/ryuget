import os

# This is an *overly* simplistic scripts to read a text file with a list of urls from Ryushare
# and downloads each file in sequence as listed. This script is meant for educational/proof of concept purposes.
# This script will not be maintained and is licensed under CC share alike


#################
# remove empty lines and redirect output to temp file which then overwrites list
# http://soft.zoneo.net/Linux/remove_empty_lines.php
# http://en.kioskea.net/faq/1451-sed-delete-one-or-more-lines-from-a-file
# instead of some loop using list.pop()
os.system("sed '/^$/d' list > list.temp")
# remove leading and trailing white space for each line
os.system("sort list.temp | uniq list.temp > list")
os.system("rm list.temp")

list_file = open("list", "r")
list = [i.strip() for i in list_file.readlines()]

for i in range(len(list)):
    print>>list_file, list[i]
list_file.write("list")
list_file.close()

# remove dupicate lines
os.system("awk '!x[$0]++' list > list.temp; mv list.temp list")
list_file.open("list","r")
# check for and strip duplicates

for i in list:
    os.system("wget " + list[i]) # test line
    os.system("echo "+list+" > list")
    os.system("cat list")


if __name__ == '__main__':
  main()
