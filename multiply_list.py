x = 2
original = [2,4,1,6]
multiplied = []

for num in original:
        answer = num * x
        multiplied.append(answer)

print(multiplied)

#alternative way
my_list = [1, 2, 3, 4, 5]
my_new_list = [i * 5 for i in my_list]

print(my_new_list)