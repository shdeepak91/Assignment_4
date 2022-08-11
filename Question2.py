a = int(input("enter a number:"))
m = map(lambda x : x*3 ,range(1,a+1))
for x in m :
    print(x ,end =" ")