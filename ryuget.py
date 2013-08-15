import os

os.chdir('/your/dir/path/of/choice/')
file = "list"

list = [i.strip() for i in open(file).readlines()]


for i in range(len(list)):
    os.system("wget --load-cookies cookies.txt "+list[i])

if __name__ == '__main__':
  main()
