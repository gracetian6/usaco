"""
ID: graceti1
LANG: PYTHON3
TASK: transform
"""



fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
N = int(fin.readline())


#read data
before = []
after = []
for _ in range(N):
    line = list(fin.read(N))
    before.append(line)
    fin.readline()
for _ in range(N):
    line = list(fin.read(N))
    after.append(line)
    fin.readline()

"""
N = 5
before = [['-', '@', '@', '@', '-'], ['-', '@', '@', '-', '-'], ['-', '@', '-', '-', '-']
          ,['-', '-', '-', '-', '-'],['-', '-', '-', '-', '-']]
after =  [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '@'], ['-', '-', '-', '@', '@']
          ,['-','-', '@', '@', '@'], ['-', '-', '-', '-', '-']]
"""
print(N)
print(before)
print(after)

def rotate(sq):
    sq_rotated = []
    # nth row in sq_rotated = reversed nth column in sq
    for n in range(N):
        # nth column in sq becomes ith row in sq_rotated
        sq_col_n = [] # nth col of sq
        # traverse sq
        for i in range(N):
            sq_col_n.append(sq[i][n])
        sq_col_n.reverse() # reverse column n
        sq_rotated.append(sq_col_n)
    return sq_rotated

def reflect(sq):
    sq_refl = []
    # nth row in sq_reflected = reversed nth row in sq
    for n in range(N):
        sq[n].reverse()
        sq_refl.append(sq[n])
    return sq_refl


# times = # of times changed
# cur_sq = changed sq
# sq = original sq
def check_transf(sq, cur_sq, times):
    # base cases
    if times > 0 and cur_sq == after:
        if times <= 4:
            return times
        else:
            return 5
    elif times >= 8:
        return 7
    # reflect sq
    elif times == 3:
        return check_transf(sq, reflect(sq), times + 1)
    # rotate sq
    elif times <= 2 or times >= 4:
        return check_transf(sq, rotate(cur_sq), times + 1)

fout.write(str(check_transf(before, before, 0)) + '\n')
fout.close()
