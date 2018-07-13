def safun(dim):
    #surface area function
    surfacea=(dim[0]*dim[1]+dim[1]*dim[2]+dim[0]*dim[2])*2
    return surfacea
    
def volfun(dim):
    #volume function
    volume=dim[0]*dim[1]*dim[2]
    return volume

def main():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    rect=[length,width,height]
    surfaceArea=safun(rect)
    print("The surface area is "+ str(surfaceArea)) 
    print("The volume is "+ str(volfun(rect)))
    print(volfun((5,2,6)))
    
main()