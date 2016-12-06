import sys

total = 0
possible = 0


def prepare_triangle(raw_triangle):
    triangle = [ int(x) for  x in raw_triangle]
    triangle.sort()
    return triangle

def check_triangle(triangle):
    # check if the 2 smaller sides (index 0 and 1) are smaller than the largest one
    global total
    global possible
    total += 1
    if triangle[0] + triangle[1] > triangle[2]:
        possible += 1
    sys.stdout.write('.')
    sys.stdout.flush()

with open('data.txt') as f:
    for line in f:
        triangle = line.split()
        triangle = prepare_triangle(triangle)
        check_triangle(triangle)

print ''
print str(possible)+' triangles of a total of '+str(total)+' are possible'
