#tuple -- 배열 닮았지만 수정이 안됨
b = (1,2,'a',5);
#b[0] = a; #오류 나옴
print(b)

#dictionary -- 매우 중요!! 자료형의 형태
#key : value 로 이뤄짐
dic = {'name':'Eric', 'age':'15'};
print(dic['name']) #Eric이 나옴
#dictionary 할당 방법
a = {1:'a'};
a['name'] = '익명';
print(a);
#삭제하려면 del a[key값] 을 입력해야 함!!
# a.keys() -- key만 따로 뽑음
# a.values() -- value만 따로 뽑음
print(a.get(4,'없음')); #key 값이 없으면 파라미터 값을 출력

#set -- 집합
s1 = set([1,1,1,2,3,2]);
print(s1);
newS1 = list(s1);
print(newS1);
#다른 언어에서 하기 어려운 것들
#교집합
s1 = set([1,2,3,4,5,6]);
s2 = set([4,5,6,7,8,9]);
print(s1 & s2);
#합집합
s1 = set([1,2,3,4,5,6]);
s2 = set([4,5,6,7,8,9]);
print(s1 | s2);
#차집합
s1 = set([1,2,3,4,5,6]);
s2 = set([4,5,6,7,8,9]);
print(s1 - s2);

#주소 -- 변수라는 것은 값을 주는게 아닌 주소를 주는 것!!
a = [1,2,3];
b = a;
a[0] = 4;
print(a is b); #True
#새롭게 할당하려면?
b = a[:];#slicing을 통해 새로운 값 배정 = 새로운 주소 배정
print(a is b); #False

#변수를 바꾸는 법 -- 파이썬에만 있는 쉬운 기능
c = 5;
d = 6;
c,d = d, c;
print(c) #6
