import string

password = "password123"

# going through all the characters in the password and checking for each  of them if they
# are contained in ascii upper case if so it will add one otherwise 0
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])


charchters =[upper_case, lower_case,special,digits]

length = len(password)

score = 0

with open('common.txt','r') as f: 
    common = f.read().splitlines()

if password in common:
    print("password was found in a common list. score: 0/7 ")
    exit()

if length> 8:
    score+=1
if  length> 12:
    score+=1
if length > 17:
    score+=1
if length > 20:
    score +=1   

print(f"password length is {str(length)}, adding{str(score)} points!")

if sum(charchters) > 1:
    score +=1
if sum(charchters)> 2:
    score +=1
if sum(charchters)> 3:
    score +=1
print(f"password has {str(sum(charchters))} diffrent charchter types, adding {str(sum(charchters-1))}points")


if score <4:
    print(f"the password is weak score: {str(score)}/7")
elif score ==4:
    print(f"the password is ok score: {str(score)}/7")
elif score >4 and score <6:
    print(f"the password is pretty good score: {str(score)}/7 ")
    
elif  score >6:
    print(f"the password is strong score: {str(score)}/7 ")
