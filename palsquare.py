"""
ID: graceti1
LANG: PYTHON3
TASK: palsquare
"""

fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')
B = int(fin.readline())


digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# returns integer N in base B as a string
def to_base(N, B, result):
    div = N // B
    r = N % B
    result = digit[r] + result
    if div <= 0:
        return result
    else:
        return to_base(div, B, result)


# checks whether str is a palindrome
def is_pal(str):
    str_len = len(str)
    for i in range(str_len // 2):
        if str[i] != str[str_len - i - 1]:
            return False
    return True


for i in range(1, 300):
    sq_string = to_base(i*i, B, "")
    if is_pal(sq_string):
        # print out cur and square(cur)
        #print(to_base(i, B, "") + " " + sq_string)
        fout.write(to_base(i, B, "") + " " + sq_string + '\n')
