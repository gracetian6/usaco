"""
ID: graceti1
LANG: PYTHON3
TASK: milk2
"""

# returns whether (h1, t1) (h2, t2) should be
# ordered like (h1 (h2 t1) t2) instead
def does_overlap(h1, t1, h2, t2):
    return ((h1 <= h2) and (h2 <= t1) and (t1 <= t2))

def is_seperate(h1, t1, h2, t2):
    return (h1 < t1) and (t1 < h2) and (h2 < t2)


fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')
rounds = int(fin.readline())


#read data
times = []
for i in range(rounds):
    h, t = map(int, fin.readline().split())
    times.append((h, t))


#times = [(300, 1000), (700, 1200), (1500, 2100)]
#times = [(1,10), (2,3), (4,5), (6,9), (12,13), (14,15)]
#times = [(2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (1, 20)]
#times = [(100, 200), (200, 400), (400, 800), (800, 1600), (50, 100), (1700, 3200)]

#sort times by head of every tuple
times.sort(key=lambda tup: tup[0])
print(times)

max_milk = 0
max_idle = 0
h1, t1 = times[0]
for h2, t2 in times:
    # if overlaps and t2 > t1 then set t1 to t2
    #update milk_time
    milk_time = t1 - h1
    if milk_time > max_milk:
        max_milk = milk_time
    #swap h1, t1 with h2, t2
    if h2 < h1:
        h2, h1 = h1, h2
        t2, t1 = t1, t2
    if does_overlap(h1, t1, h2, t2):
        t1 = t2
    elif is_seperate(h1, t1, h2, t2):
        # update idle times
        idle_time = h2 - t1
        if idle_time > max_idle:
            max_idle = idle_time
        # reset h1 and t1
        h1 = h2
        t1 = t2

"""
print("Milk time: " + str(max_milk))
print("Idle time: " + str(max_idle))
"""


fout.write (str(max_milk) + ' ' + str(max_idle) + '\n')
fout.close()
