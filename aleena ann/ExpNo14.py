n = int(input("Input an integer : "))
sum = 0
for i in range(3):
  a = int(pow(n, i+1))
  print(a)
  sum = sum + a
print("Sum is:",sum)