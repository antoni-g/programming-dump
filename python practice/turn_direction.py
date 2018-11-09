import sys

# 						11.8.18									#
#																#
# This script was written to help manually debug a convex hull  #
# implementation using the Graham Scan Method.					#
#																#

# processes args
def process_args(args):
	points = []
	for i in args:
		point = i.split(',')
		try:
			add = [float(i) for i in point]
			if not len(add) == 2:
				print('Input in incorrect format: Points are not in "x,y" form. Exiting')
				sys.exit(1)
			points.append(add)
		except:
			print('Input in incorrect format: Points are not valid numbers. Exiting')
			sys.exit(1)
	return points	

# function
def direction(x,y,z):
	return (y[1]-x[1])*(z[0]-y[0]) - (z[1]-y[1])*(y[0]-x[0])

# main
def main():
	print()
	if not len(sys.argv[1:]) == 3:
		print('Input in incorrect format: Expected 3 points, got '+ str(len(sys.argv[1:])) +'. Exiting')
		sys.exit(1)
	raw = process_args(sys.argv[1:])	
	res = direction(raw[0],raw[1],raw[2])
	if (res == 0):
		print('The three points are colinear.')
	elif (res < 0):
		print('The three points form a counterclockwise, or left, turn.')
	else:
		print('The three points form a clockwise, or right, turn.')

main()