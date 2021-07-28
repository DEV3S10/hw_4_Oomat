import random
import calculator

rand_list = []

for i in range(20):
    number1 = random.randint(0, 100)
    rand_list.append(number1)


num1 = random.choice(rand_list)
num2 = random.choice(rand_list)

num_of_user = int(input("Напишите число для операции: "))
sum_list = []

for i in range(num_of_user):
    num = random.choice(rand_list)
    sum_list.append(num)

print(sum_list)
add = calculator.P()
sub = calculator.M()
div = calculator.D()
mul = calculator.U()
sub = sub.sub(num1, num2)
de = div.div(num1, num2)
Um = mul.mult(num1, num2)


add = add.add(sum(sum_list))
print(f'Plus: {add}')
print(f'Minus: {sub}')
print(f'Delenie: {de}')
print(f'Umnojenie: {Um}')