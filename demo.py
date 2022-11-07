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



secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('guess:'))
    guess_count+=1
    if guess==secret_number:
        print("you won")
        break
else:
    print('sorry u failed')



