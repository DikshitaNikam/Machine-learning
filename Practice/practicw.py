name = "john"

print(type(name))

age = 23
print(type(age))

a = "123"
b = 1.23
print(type(a))
print(type(b))

a = float(a)
print("After conversion",type(a))

c = a+b
print(c)
print(type(c))

name1 = "john"
age1 = 23
address = "654 lake strret"
print(name1)
print(age1)
print(address)

# swapping methid 1
x = 12
y = 13
temp = x
x = y
print(temp)
print (x)
y = temp
print(y)
print ("value of x is", x)
print ("value of y is", y)

# swapping method two
a = 30
b = 40
a,b = b,a
print(a)
print(b)

x = 12.4
print(type(x))
x = int(x)
print(type(x))
print(x)


name = input("Enter the name of the student: ")
grade = input("Enter the grade of the student: ")
age =  int(input("Enter the age :"))
email = int(("Enter the email of the student"))
print("Student Identify Card")

print(not(3>4 and 3<4) )   

score = 1
score += 1
print(score)

score = 1
score -= 1
print(score)

score = 3
score *= 2
print(score)

a =1234
b ="1234"
print (a is b)

a =1234
b ="1234"
print (a is not b)


marks = 87

if marks >= 80:
    print("You will get a mobile phonr")
print("thank you")
