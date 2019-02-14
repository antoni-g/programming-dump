# The following method get the manhatten distance betwen two points (x1,y1) and (x2,y2)
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# Enter your code here. Read input from STDIN. Print output to STDOUT
sizeOfWorld = int(input())

class Event:
  def __init__(self,eid,x,y,tickets):
    self.eid = eid
    self.x = x
    self.y = y
    self.tickets = tickets
events = []
numberOfEvents = int(input())
for i in range(numberOfEvents) :
    raw = input().strip().split(" ")
    el = [int(i) for i in raw]
    # ignore events with no tickets
    if len(el) > 3:
        events.append(Event(el[0],el[1],el[2],sorted(el[3:])))
    
buyers = []
numberOfBuyers = int(input())
for i in range(numberOfBuyers) :
    raw = input().strip().split(" ")     
    el = [int(i) for i in raw]
    buyers.append(el)
    

# for reach buyer, calculate distances and distribute a ticket
for buyer in buyers:
    if len(events) == 0:
        print(-1,0)
    # calc distances to all events
    dists = []
    for i in range (0,(len(events))):
        dists.append([i,manhattan_distance(buyer[0],buyer[1],events[i].x,events[i].y)])
    dists.sort(key=lambda x: x[1])
    # find the cheapest ticket and attribute/remove
    res = dists[0]
    tgt_ev = events[res[0]]
    print(tgt_ev.eid,tgt_ev.tickets.pop(0))
    if (len(tgt_ev.tickets) <= 0):
        del events[res[0]]


# The solution to the first sample above would be to output the following to console:
# (Obviously, your solution will need to figure out the output and not just hard code it)

