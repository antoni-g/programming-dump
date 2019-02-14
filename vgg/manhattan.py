# The following method get the manhatten distance betwen two points (x1,y1) and (x2,y2)
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def convert(l):
	try:
		l[0] = float(l[0])
		l[1] = float(l[1])
	except ValueError:
		print("An input character was not a number.")
		exit()

# Enter your code here. Read input from STDIN. Print output to STDOUT
point1AsAString = input().strip()
point2AsAString = input().strip()

# Need to parse each point and find the distance between them using the supplied manhattan_distance method
l1=point1AsAString.split(" ")
l2=point2AsAString.split(" ")

# verify
if (len(l1) != 2 or len(l2) != 2):
	print ("Invalid number of arguments for coordinates. Need x and y space separated with one point per line")
	exit()
#convert and verify
convert(l1)
convert(l2)

print(manhattan_distance(l1[0],l1[1],l2[0],l2[1]))

