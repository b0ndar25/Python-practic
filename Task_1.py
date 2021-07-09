
print("Please, numbers from symbols input separately: ")
s = input()
word_list = s.split()
num_list = []
for word in word_list:
	if word.isdigit():
		num_list.append(int(word))
print ("\nList of the numbers: ", num_list)

m = num_list[0] 
for i in num_list:
	if i>m:
		m=i
print ("\nMax number in list:", m)

p=0
stp = []
for i in range(len(num_list)):
	x = pow(num_list[i],p)
	p+=1
	stp.append(x)
print("\nNumbers in power:",stp)


sym_list= []
for symb in word_list:
	if symb.isalpha():
		sym_list.append(symb)
print("\nList of the words : ", sym_list)
for word in sym_list:
        newstring = ''
        if len(word) > 1:
            word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            word = word[0].upper()
        newstring += word
        print(word)