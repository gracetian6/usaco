"""
ID: graceti1
LANG: PYTHON3
TASK: transform
"""


"""
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
N = int(fin.readline())


#read data
before = []
after = []
for i in range(N):
    row = fin.readline().split()
    before.append(row)
for i in range(N):
    row = fin.readline().split()
    after.append(row)
"""
N = 3
before = [['@', '-', '@'], ['-', '-', '-'], ['@', '@', '-']]
after = [['@', '-', '@'], ['@', '-', '-'], ['-', '-', '@']]

def rotate_90(sq):
    sq_rotated = []
    # ith row in sq_rotated is reversed ith column in sq
    for n in range(len(sq)):
        # nth column in sq becomes ith row in sq_rotated
        sq_col_n = [] # nth col of sq
        # traverse sq
        for i in range(N):
            sq_col_n.append(sq[i][n])
        sq_col_n.reverse() # reverse column n
        sq_rotated.append(sq_col_n)
    return sq_rotated

print(before)
print(rotate_90(before))
print(after)

"""
fout.write ('output \n')
fout.close()
"""
