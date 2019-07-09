"""
ID: graceti1
LANG: PYTHON3
TASK: milk2
"""

class Milking:
  def __init__(self, begin, end):
    self.begin = begin
    self.end = end

fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')
rounds = int(fin.readline())


#read data
times = []
for i in range(rounds):
    begin, end = map(int, fin.readline().split())
    times.append(Milking(begin, end))

#times = [(100, 200)]
#times = [(300, 1000), (700, 1200), (1500, 2100)]
#times = [(1,10), (2,3), (4,5), (6,9), (12,13), (14,15)]
#times = [(2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (1, 20)]
#times = [(100, 200), (200, 400), (400, 800), (800, 1600), (50, 100), (1700, 3200)]

#sort times by beginning of milking period
times.sort(key=lambda tup: tup.begin)

# walk over list, looking for long periods of times
# tmilk = longest milking time
# tnomilk = longest non-milking time
# cur = current span of milking time being considered
# milking = element traversed in list
tmilk = 0
tidle = 0
cur = times[0]
for milking in times:
    # gap between cur and milking
    if milking.begin > cur.end:
        t = milking.begin - cur.end
        if t > tidle:
            tidle = t
        t = cur.end - cur.begin
        if t > tmilk:
            tmilk = t
        cur = milking
    # overlap between two intervals
    elif milking.end > cur.end:
        cur.end = milking.end
# final milking period
t = cur.end - cur.begin
if t > tmilk:
    tmilk = t

"""
print("Milk time: " + str(max_milk))
print("Idle time: " + str(max_idle))
"""

fout.write (str(tmilk) + ' ' + str(tidle) + '\n')
fout.close()
