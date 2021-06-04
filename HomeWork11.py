# By : Ahmed Mohammed Ali  / 20184020
Numbers = 0
entry = "" # string type

while(entry != "Out"): # Enter "Out" to Exit ...

    entry=input("Enter a Number to add it to the Numbers value or Enter exit to terminate program :")

    if entry.isdigit(): # Verify that the entry is a number, not a letter

        Numbers+=int(entry)

    print("Numbers is:",Numbers)