n = int(input("Enter a number \n"))
if n%2==1:
    print("Weird")
elif n%2==0 and 2 >= n <=5:
    print("not weird")
elif n%2==0 and 6 >= n <= 20:
    print("weird")
elif n%2==0 and n>20:
    print("Not Weird")

else:
    print(" Not Weird")
