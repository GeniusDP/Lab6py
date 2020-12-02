#inputing coords of points
def myInput(n, sx, sy):
    n=int(input("Please, input number of points n: "))
    print("Input coords of points: ")
    for i in range(0, n):
        print("x y : ", end="")
        x, y=input().split()
        x=int(x)
        y=int(y)
        sx.append(x)
        sy.append(y)
    return n, sx, sy


#does length AB cross a point (0,0) (origin)
def crossesOrigin(x1, y1, x2, y2):
    return x1 * ( y2 - y1 ) == y1 * ( x2 - x1 )


#point A is on an axe
def onAxe(x, y):
    if x*y==0:
        return True
    else:
        return False


#does length AB cross an axe
def crossesOneAxe(x1, y1, x2, y2):
    res=0
    if( crossesOrigin(x1, y1, x2, y2) and (x1 * x2<0) and (y1 * y2<0) ):
        #crossed (0,0);
        res=0
    else:
        res=(x1 * x2<0) ^ (y1 * y2<0) #in different quarters
    return res
    
    
#brute force algorithm    
def bruteForce(n, sx, sy):
    res=0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if( not(onAxe(sx[i], sy[i])) and not(onAxe(sx[j], sy[j])) and crossesOneAxe(sx[i], sy[i], sx[j], sy[j]) ):
                res+=1
    return res



#****************************************
#main block-----------------------------*
#****************************************

#arrays of coordinates
sx=[]
sy=[]
#number of points
n=0
#inputing information
n, sx, sy = myInput(n, sx, sy)


cnt=bruteForce(n, sx, sy)
print("Your answer is: ", cnt)

