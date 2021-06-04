# By : Ahmed Mohammed Ali / 20184020
first = int(input("Enter First Number :"))
last = int(input("Enter Last Number :"))

sum_even = 0
avg_even = 0 # Average Even Number = Sum Even Number / Len Even Number

sum_odd = 0
avg_odd = 0 # Average Odd Number = Sum Odd Number / Len Odd Number

len_even = 0
len_odd = 0

for i in range(first , last+1):
    if(i % 2 == 0):
        len_even+=1
        sum_even=sum_even+i
        avg_even = sum_even / len_even
    else:
        len_odd+=1
        sum_odd=sum_odd+i
        avg_odd=sum_odd/len_odd

print("The Sum Of Even Number Is :" , sum_even)
print("The Average Of Even Number Is :" , avg_even)
print("The Sum Of Odd Number Is :" , sum_odd)
print("The Average Of Odd Number Is :" , avg_odd)