# def fn(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fn(n-1)+fn(n-2)
# num=int(input("enter the number "))    
# if num>0:
#     print(fn(num))
# else:
#     print("error in input")   


# def fn(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fn(n-1)+fn(n-2)

# num=int(input("enter the number to find value"))
# if(num>0):
#     print(fn(num))     
# else:
#     print("error in input") 



def fn(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fn(n-1)+fn(n-2)
    
num=int(input("enter the number"))   
print(fn(num))
