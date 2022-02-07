from cube import Cube
import numpy as np


class Big_cube(Cube):
    def __init__(self, x1, y1, z1, a):
        super().__init__(a)
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

BigC = Big_cube(10, 10, 0, 5)

#print(BigC.cube_vol())


class Small_cube(Cube):
    def __init__(self, x2, y2, z2, a):
        super().__init__(a)
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

SmallC = Small_cube(8, 9, 0, 2)

#print(SmallC.cube_vol())


xb_max = BigC.x1 + BigC.a_side/2
yb_max = BigC.y1 + BigC.a_side/2  

xb_min = BigC.x1 - BigC.a_side/2
yb_min = BigC.y1 - BigC.a_side/2 # vertices of big cube on xy plane

#print([xb_max,yb_max, xb_min, yb_min])

xs_min = SmallC.x2 - SmallC.a_side/2
ys_min = SmallC.y2 - SmallC.a_side/2



xs_max = SmallC.x2 + SmallC.a_side/2
ys_max = SmallC.y2 + SmallC.a_side/2  # vertices of small cube on xy plane

#print([xs_max,ys_max, xs_min, ys_min])


def intersect():
    if ((xb_max-xs_min) > (BigC.a_side + SmallC.a_side)):
        print("The cubes don't intersect")

    elif ((xb_max-xs_min) < (BigC.a_side + SmallC.a_side)):
        print("The cubes intersect")

#intersect()


cxb = np.arange(xb_min, xb_max+1, 0.5)
cyb = np.arange(yb_min, yb_max, 0.5)

#print('points on X_axis : ', cxb)
#print('points on Y_axis : ', cyb)

cxs = np.arange(xs_min, xs_max+1, 0.5)
cys = np.arange(ys_min, ys_max, 0.5)

#print('points on X_axis : ', cxs)
#print('points on Y_axis : ', cys)

xcl = (np.intersect1d(cxb, cxs))
ycl = (np.intersect1d(cyb, cys))

#print(xcl)
#print(ycl)

xl = xcl.tolist()
yl = ycl.tolist()

#print(xl)
#print(yl)


def in_vol():

    return(((xl[-1]-xl[0])*(yl[-1]-yl[0])*SmallC.a_side))
print('The volume of common cube is : ', ((xl[-1]-xl[0])*(yl[-1]-yl[0])*SmallC.a_side), + 'm^3')
#in_vol()


intersect()


