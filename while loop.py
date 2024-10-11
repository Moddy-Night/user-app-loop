
numbes=str(list(range(0,10)))
things=str(list("+,-,/,*,.,"))
aprove=str(list("yes,ye,y,YES,YE,Y,Yes,YEs,yES,yeS,yEs"))
print("hello guys i'm  about to do some coding ")
while True:
    while True:
        username=input("please enter your username: ")
        if not username:
            print("please eneter a valid username")
        elif username.find(" ")==0:
            print("please make sure that you do not enter spaces in your username")
        elif username[0] in numbes or username[0] in things:
            print("pleace let your first elment a letter")
        else:
            break
    print(f"welcome:  {username:^10}")
    print("wanna try again")
    answer=input("Y/N:  ")
    if answer in aprove:
        continue   
    else:
        break
print("bye")