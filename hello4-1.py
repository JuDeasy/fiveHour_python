#### immutable variable (int, float, str, tuple) ###
a = 1
def vartest1(a):
	a = a + 1
vartest1(a)
print(a) # 1

#### mutable variable (list, dictionary, 집합) ###
b = [1,2,3]
def vartest2(b):
	b = b.append(4)
vartest2(b)
print(b) # [1,2,3,4] -- local b vs global b 둘 다 같은 변수가 아니지만(메모리 주소 다름) mutable 변수라서 값이 변한것
