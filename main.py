# day_3_love_calculator_project

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is her name? \n")

lower_case_name_1 = name1.lower()
lower_case_name_2 = name2.lower()
total_lowercase_names = lower_case_name_1 + lower_case_name_2

letter_t = total_lowercase_names.count("t")
letter_r = total_lowercase_names.count("r")
letter_u = total_lowercase_names.count("u")
letter_e = total_lowercase_names.count("e")

total_letter_true =int(letter_t + letter_r + letter_u + letter_e)

letter_l = total_lowercase_names.count("l")
letter_o = total_lowercase_names.count("o")
letter_v = total_lowercase_names.count("v")
letter_e = total_lowercase_names.count("e")

total_letter_love =int(letter_l + letter_o + letter_v + letter_e)

total_letter_true_love = str(total_letter_true) + str(total_letter_love)

score = int(total_letter_true_love)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 or score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")