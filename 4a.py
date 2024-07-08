# def insertionsort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and key<arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key    
    
# def mergesort(x):
#     if len(x)>1:
#         mid=len(x) // 2
#         left=x[:mid]
#         right=x[mid:]
#         mergesort(left)        
#         mergesort(right)  
#         i,j,k=0,0,0
#         while i<len(left) and j<len(right) :
#             if left[i]<right[j]:
#                 x[k]=left[i]
#                 i+=1
#                 k+=1     
#             else:
#                 x[k]=right[j]
#                 j+=1
#                 k+=1
#         while i<len(left):
#                 x[k]=left[i]
#                 i+=1
#                 k+=1  
#         while j<len(right):
#             x[k]=right[j]
#             j+=1
#             k+=1             
#         return x


# import random
# n=int(input("enter the number"))
# mylist=[]
# for i in range(n):
#     mylist.append(random.randint(0,999))
# print("unsorted list")
# print(mylist)    
# print("sorting usisng insertion sort")
# insertionsort(mylist)
# print(mylist)


# my_list=[]
# for i in range(n):
#     my_list.append(random.randint(0,999))
# print("unsorted list")
# print(my_list)    
# print("sorting usisng merge sort")
# mergesort(my_list)
# print(my_list)
          
          
def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

def mergesort(x):
    if len(x)>1:
        mid=len(x)//2
        left=x[:mid]          
        right=x[mid:]
        mergesort(left)
        mergesort(right)
        i,j,k=0,0,0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                x[k]=left[i]
                i+=1
                k+=1
            else:
                x[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
               x[k]=left[i]
               i+=1
               k+=1         
        while j<len(right):
               x[k]=right[j]
               j+=1
               k+=1   
        return x
    
import random
num=int(input("enter the size of array"))
myList=[]

for i in range(num):
    myList.append(random.randint(0,999))

print("unsorted list")
print(myList)
print("sorting using insertion sort")
insertionsort(myList)
print(myList)

myList=[]

for i in range(num):
    myList.append(random.randint(0,999))

print("unsorted list")
print(myList)
print("sorting using merge sort")
mergesort(myList)
print(myList)

           