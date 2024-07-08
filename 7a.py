# import math
# class Shape:
#     def area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         return 0.5*self.base*self.height
            
# class Rectangle(Shape):
#     def __init__(self,base,height):
#          self.base=base
#          self.height=height
#     def area(self):
#         return self.base*self.height           
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return math.pi*self.radius**2

# print("1.area of Traiangle")            
# print("2.area of Recangle")            
# print("3.area of Circle")            
# ch=int(input("enter the choice"))
# if ch==1:
#     b=int(input("enter the base"))
#     h=int(input("enter the height"))
#     triangle=Triangle(b,h)
#     print("area of triangle",triangle.area())
# elif ch==2:
#     b=int(input("enter the base"))
#     h=int(input("enter the height"))
#     rectangle=Rectangle(b,h)
#     print("area of recangle",rectangle.area())
# elif ch==3:
#     r=int(input("enter the radius"))        
#     circle=Circle(r)
#     print("area of circle",circle.area())
# else:
#     print("invalid choice")    


import math
class Shape:
    def area(self):
        pass
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height        
    
class Rectangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return self.base*self.height   
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    
print("1.area of Triangle")        
print("2.area of Rectangle")        
print("3.area of Circle")        
ch=int(input("enter the choice"))
if ch==1:
    b=int(input("enter the base"))
    h=int(input("enter the height"))
    triangle=Triangle(b,h)
    print("area of triangle",triangle.area())
elif ch==2:
    b=int(input("enter the base"))
    h=int(input("enter the height"))
    rectangle=Rectangle(b,h)
    print("area of rectangle",rectangle.area())    
elif ch==3:
    r=int(input("enter the radius"))    
    circle=Circle(r)
    print("area of circle",circle.area())
else:
    print("invalid choice")    