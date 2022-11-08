print("python first program")

print('djgcjsgvjksdvh')


cource='hello'
print(cource)


""" name=input('what is your name? ')
print('hii ' + name)


fav_color=('what is ur fav color ')
fav_color=input('what is ur fav color ')
print(name  + 'likes ' +  fav_color) """


i=1
while i<=5:
    print(i)
    i=i+1

print("Done")


i=1
while i<=5:
    print('*' * i)
    i=i+1

print("Done")




#while looop---------------------------------------------------



""" secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('guess:'))
    guess_count+=1
    if guess==secret_number:
        print("you won")
        break
else:
    print('sorry u failed') """


#for loop-----------------------------------------------------

for item in("ravi", "pankaj","satya"):
    print (item)


prices=[10,20,30]
total=0

for price in prices:
    total +=price
    print(f"total:{total}")


name='raviraj'
surname='panchal'
print(name + surname)


# Nested Loop------------------------------------------------------------------------

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

        #----------exercise-------------------
number=[5,2,5,2,2]
for x_count in number:
    print('x' * x_count)

    #--OR--


number=[5,2,5,2,2]
for x_count in number:
    output=''
    for count in range(x_count):
        output +='x'
    print(output)


number=[1,1,1,1,5]
for x_count in number:
    output=''
    for count in range(x_count):
        output +='x'
    print(output)

 #-------LIST----------------------

name=['raj','ani','satya','ved','sani']
print(name[:])

name=['raj','ani','satya','ved','sani']
print(name[0:])

name=['raj','ani','satya','ved','sani']
print(name[2:4])

name=['raj','ani','satya','ved','sani']
print(name[2:-1])

name=['raj','ani','satya','ved','sani']
print(name[-1])

name=['raj','ani','satya','ved','sani']
print(name[-3])


#------To Find Largest Number In Given List---------------

numbers=[3,2,6,4,9,10,7]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
        print(max)


numbers=[3,2,6,8,4,9,10,7]
min=numbers[0]
for number in numbers:
    if number<min:
        min=number
        print(min)


#----2D List-----------------------------------
matrix= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix [0][1]=20
print(matrix[0][1])

matrix= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for items in row:
        print(items )


#-----------------------

numbers=[5,2,6,9,7]
numbers.append(20)
print(numbers)

numbers=[5,2,6,9,7]
numbers.insert(0,10)
print(numbers)

print(numbers.index(6))

 #---Remove Duplicates Of the given Array--------------

numbers=[2,2,4,6,3,4,6,7]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        
print(uniques)


#-----------unpacking-------------------------

coordinates=(1,2,3)
x,y,z=coordinates
print(y)

coordinates=(1,2,3)
x,y,z=coordinates
print(x,z)


#---------Dictionary-------------------------------
custmoer={
    "name":"raj kumar",
    "age":30,
    "is_varified":True

}

print(custmoer["name"])
print(custmoer["age"])


print(custmoer.get("birthdate"))


#------------convert no in to words------------
""" phone=input("phone: ")
digit_mapping = {
    "1":"one",
    "2":"two",
    "3":"three"
  }
output= ""
for ch in phone:
    output +=digit_mapping.get(ch,"!")+""
    print(output)
 """

#--------------FUNCTION-------------
def greet_user():
    print("hii there!")
    print("welcome ")

print("start")
greet_user()
print("finish")


#------------------PARAMETER-----------

def greet_user(first_name, last_name):
    print(f'hii {first_name}{last_name}')
    print("welcome ")

print("start")
greet_user("ravi","kumar")
print("finish")

#-----------------Keyword Agument-------------
def greet_user(first_name, last_name):
    print(f'hii {first_name}{last_name}')
    print("welcome ")

print("start")
greet_user(last_name="kumar",first_name="Ravi")
print("finish")

#----------------Try Except Error Handling-------------

""" try:
    age=int(input('age: '))
    print(age)
   
except ValueError:
    print('invalid values')


try:
    age=int(input('age: '))
    income=20000
    risk=income/age
    print(age)
   
except ZeroDivisionError:
    print('age cannot devide by 0')
except ValueError:
    print('invalid values')
 """


    #-----------------------classes--------------

class point:
        def move(self):
            print("move")
        
        def draw(self):
            print("draw")

point1=point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()


