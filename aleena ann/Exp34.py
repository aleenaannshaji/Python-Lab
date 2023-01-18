class Rectangle:

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return (2 * (self.l + self.b))


l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
o = Rectangle(l, b)
x = o.area()
y = o.perimeter()
print("Area is: ", x)
print("Perimeter is: ", y)

a = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
o1 = Rectangle(a, b)
p = o1.area()
q = o1.perimeter()
print("Area is: ", p)
print("Perimeter is: ", q)

if (x > p):
    print("The first rectangle is greater than the second")
else:
    print("The second rectangle is greater than the first")