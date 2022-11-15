n1 = int(input("Enter the limit: "))
list1=[]
print("Enter the colours: ")
for i in range(0, n1):
    i = input()
    list1.append(i)
print(list1)
n2 = int(input("Enter the limit: "))
list2=[]
print("Enter the colours: ")
for i in range(0, n2):
    i = input()
    list2.append(i)
print(list2)
print("colours present in list 1 but not in list 2 are:")
c=list(set(list1).difference(list2))
print(c)