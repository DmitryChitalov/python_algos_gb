"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
from random import randint


def quess_numb(atempts, rand_numb):
	print(rand_numb, f'You attempts is: {atempts}!')
	user_numb = input("Write your number: ")
	user_numb = int(user_numb)
	if user_numb == rand_numb or atempts >= 10:
		if atempts >= 10:
			return "Your attempts is empty!!You lost!!"
		return f"Congratulation!!! You quessed the number!! from {atempts} attempt"
	else:
		prompt = "You number less than hidden number!!" if user_numb < rand_numb else "You number is bigger!!"

		print(prompt)
		return quess_numb(atempts + 1, rand_numb)


print(quess_numb(1, (randint(0, 100))))
##########################################
print('############next_block###########')
##########################################
# rand_num = int(random.random() * 100)
rand_num = randint(0, 100)
print(rand_num)
user_attempts = 1

while user_attempts <= 10:
	print("Try to ques the number!")
	user_number = int(input("Write your number: "))
	if user_number == rand_num:
		print(f"Congratulation!!! You quessed the number!! from {user_attempts} attempt")
		break
	elif user_number > rand_num:
		print("You number is bigger!!")
		user_attempts += 1

	elif user_number < rand_num:
		print("You number less than hidden number!!")
		user_attempts += 1

else:
	print("You did not quess the number(((")
	print(f"Correct number is {rand_num}")
##############################################
