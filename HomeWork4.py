# By : Ahmed Mohammed Ali / 20184020
Number = int(input("Enter an integer : "))
n1 = int( "%s" % Number )
n2 = int( "%s%s" % (Number,Number) )
n3 = int( "%s%s%s" % (Number,Number,Number) )
print (n1+n2+n3)