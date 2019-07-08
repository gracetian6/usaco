"""
ID: graceti1
LANG: PYTHON3
TASK: milk2
"""

fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')
rounds = int(fin.readline())


#read data
times = []
for i in range(rounds):
    h, t = map(int, fin.readline().split())
    times.append((h, t))

#times = [(100, 200)]
#times = [(300, 1000), (700, 1200), (1500, 2100)]
#times = [(1,10), (2,3), (4,5), (6,9), (12,13), (14,15)]
#times = [(2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (1, 20)]
#times = [(100, 200), (200, 400), (400, 800), (800, 1600), (50, 100), (1700, 3200)]

#sort times by head of every tuple
times.sort(key=lambda tup: tup[0])

tmilk = 0
tidle = 0
h1, t1 = times[0]
for h2, t2 in times:
    # gap between h1,t1 and h2, t2
    if h2 > t1:
        t = h2 - t1
        if t > tidle:
            tidle = t
        t = t1 - h1
        if t > tmilk:
            tmilk = t
        h1, t1 = h2, t2
    # overlap between two intervals
    elif t2 >= t1:
        t1 = t2
# final milking period
t = t1 - h1
if t > tmilk:
    tmilk = t

"""
print("Milk time: " + str(max_milk))
print("Idle time: " + str(max_idle))
"""


fout.write (str(tmilk) + ' ' + str(tidle) + '\n')
fout.close()
