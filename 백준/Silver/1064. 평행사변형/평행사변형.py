import sys
import math

cordinates = list(map(int, sys.stdin.readline().split()))

Ax = cordinates[0] 
Ay = cordinates[1]

Bx = cordinates[2]
By = cordinates[3]

Cx = cordinates[4]
Cy = cordinates[5]



if ((Ax-Bx)*(Ay-Cy) == (Ay-By)*(Ax-Cx)) :
    print(-1.0)
    exit(0)

distance_ab= math.sqrt(((Ax-Bx)**2 +(Ay-By)**2))
distance_ac= math.sqrt(((Ax-Cx)**2+(Ay-Cy)**2))
distance_bc = math.sqrt(((Bx-Cx)**2+(By-Cy)**2))

lengths = [distance_ab+distance_ac, distance_ab+distance_bc, distance_ac+distance_bc]

result = max(lengths) - min(lengths)

print(2*result)

