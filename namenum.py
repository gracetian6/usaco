"""
ID: graceti1
LANG: PYTHON3
TASK: namenum
"""

# read the input
fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')
target = fin.readline().strip()

# maps string to number (ex: GREG to "4734")
def str_to_num(string):
    str_num = ""
    for ch in string:
        if ch == 'A' or ch == 'B' or ch == 'C':
            num = '2'
        elif ch == 'D' or ch == 'E' or ch == 'F':
            num = '3'
        elif ch == 'G' or ch == 'H' or ch == 'I':
            num = '4'
        elif ch == 'J' or ch == 'K' or ch == 'L':
            num = '5'
        elif ch == 'M' or ch == 'N' or ch == 'O':
            num = '6'
        elif ch == 'P' or ch == 'R' or ch == 'S':
            num = '7'
        elif ch == 'T' or ch == 'U' or ch == 'V':
            num = '8'
        else:
            num = '9'
        str_num = str_num + num
    return str_num

# search through dict and map each name to number
# check if any of the numbers work
names = []
with open('dict.txt') as dict:
    for name in dict:
        name = name.strip('\n')
        if len(name) == len(target):
            if str_to_num(name) == target:
                names.append(name)

# output result
if len(names) == 0:
    fout.write("NONE" + '\n')
else:
    for name in names:
        fout.write(name + '\n')

fout.close()
