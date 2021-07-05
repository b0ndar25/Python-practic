from random import randint

numbers = []

for i in range(30):
    numbers.append(randint(-100, 100))
print ("LIST:", numbers)

m = numbers[0] 
for i in numbers:
	if i>m:
		m=i
print ("Max number in list:", m)
lis = []
for i in numbers:
	if i%2!=0:
		lis.append(i)
lis.sort(reverse = True)
print ("Odd numbers in list:", lis)
