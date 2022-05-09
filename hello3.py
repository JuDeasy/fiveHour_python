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

# for statement
test_list = ['one', 'two', 'three']
for i in test_list:
  print(i)

# range function (아래 1이상 11미만)
sum = 0
for i in range(1, 11):
  sum = sum + i

# 구구단
for i in range(1, 10):
  for j in range(1, 10):
    print(i*j, end=" ")
  print('')

# List Comprehension(리스트 내포)
result = [num * 3 for num in a]
print(result)
