# in statement
from email import message


a = [1, 2, 3]

if 1 in a:
  print("Ture")
else:
  print("False")

# pass
a = [1, 2, 3]

if 1 in a:
  pass
else:
  print("False")

# elif
a = ["money", "cellphone"]
if 'card' in a:
  pass
elif 'money' and 'cellphone' in a:
  print('Now you can go home')
else:
  print('Look again')

# 조건문 표현식
score = 70
if score > 60:
  message = 'success'
else:
  message = 'fail'
print(message)

result = 'success' if score > 60 else 'fail'
print(result)

# while statement
treeHit = 0
while treeHit < 10:
  treeHit += 1
  print("You hit tree {treeHit} times".format(treeHit=treeHit))
  if treeHit == 10:
    print("You have done")
