# function
def sayHi():
	print('Hello')

def sum(a, b):
	result = a + b
	return result

# many arguments -- *args : 파라미터가 몇 개인지 모를 때 다 넣고싶은 경우에 사용
def sum_many(*args):
	sum = 0
	for i in args:
			sum = sum + i
	return sum
print(sum_many(1, 2, 3))

# lmada function -- 익명 함수가 생김. lmada 파라미터: 리턴값
def abc(a, b): return a + b
print(abc(1, 2))

#input()
# a = input("숫자를 입력하세요: ")
# print(a)

#create file
#w: 쓰기모드 r: 읽기모드 a: 추가모드
# f = open("new file.txt", 'w')
# f.close() -- open 하면 close 꼭 해야함

#write
f = open("./new file.txt", 'w', encoding="UTF-8")
for i in range(1,11):
	data = "%d번째 줄입니다. \n" % i
	f.write(data)
f.close()

#read -- 1 줄만 읽음
f = open("./new file.txt", 'r', encoding="UTF-8")
line = f.readline()
print(line)
f.close()

#while 을 이용한 여러줄 읽기
f = open("./new file.txt", 'r', encoding="UTF-8")
while True:
	line = f.readline()
	if not line: break # line이 없으면 ""(empty str)이 되어 False로 인식되므로 not을 붙여 break를 만든다.
	print(line)
f.close()

#readlines() 를 이용한 여러줄 읽기
f = open("./new file.txt", 'r', encoding="UTF-8")
lines = f.readlines() #배열 생성	
for line in lines:
	print(line)
f.close()

#read() 를 활용하면 통째로 가져옴
f = open("./new file.txt", 'r', encoding="UTF-8")
data = f.read()
print(data)
f.close()

#with 문을 사용해서 close() 사용하지 않기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
#같은 코드 -- f는 local variable로 global variable 아님
with open("foo.txt", "w") as f:
	f.write("Life is too short, you need python")