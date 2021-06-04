# By : Ahmed Mohammed Ali / 20184020
for i in range(0,4):
    for j in range(0,4):
        if((i==0 and j<3)or(i==1 and j<2)or(i==2 and j<1)):
            print(" ",end="")
        else:
            print("*",end="")
    print()