print("Welcome to  Love Calculator")

name1 = input("Enter your name\n")
name2 = input("Enter their name\n")

names = name1 + name2

lower_case_string = names.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"your score is {score}%, you go together like coke and fanta")
elif (score >= 40) and (score <= 50):
    print(f" our score is {score}% you are alright together")
else:
    print(f"your score is {score}%")



