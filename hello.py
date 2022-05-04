# slicing -- a[x: y: z], x 이상 y 미만 z 간격 // string type에서만 사용 가능
a = '123456789';
print(a[:4]); #123
print(a[4:]); #56789
print(a[1:5]); #2345

#formatting
# %d, %f, %s -- 정수, 실수, 문자 // %s 쓰면 모두 사용 가능
number = 3;
day = 10;
a = "I ate %d apples. So I was sick for %s days." % (number, day); #more than 2 variables, use paranthesis.
a = "I ate %d apples." % number;
print(a);

#{}
a = "{name} is {age} years old".format(name="이시형", age=13);
print(a);

#%0.4f -- 소수점 4째 자리에서 반올림, 숫자 변경 가능
a = "%0.4f" %3.141592
print(a)

#count() -- 몇 개 있는지 출력
a = "hobby";
print(a.count("b"));

#find() -- 첫 값이 몇 번째 인덱슨지 알려줌
a = "apple";
print(a.find('l'));

#join() -- 값을 넣어줌
a = ",".join('abcd');
print(a);

#replace(a, b) -- a를 b로 바꿈
a = "Life is too short";
print(a.replace("Life", "Your Leg"));

#split() -- 파라미터를 기준으로 list로 만듦. default는 공백
print(a.split());