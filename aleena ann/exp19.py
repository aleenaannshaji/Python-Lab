n=int(input("Enter the limit "))
print("Enter the elements ")
list1=[]
list2=[]
for i in range(0,n):
    element=int(input())
    list1.append(element)
    if(element%2!=0):
        list2.append(element)
print(list1)
print(list2)
