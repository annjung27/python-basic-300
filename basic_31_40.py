# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.

a = "3"
b = "4"
print(a + b)

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.

print("Hi" * 3)

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.

print("_" * 80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.

t1 = 'python'
t2 = 'java'

# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.

# 실행 예:
# python java python java python java python java

t3 = t1 + " " + t2 + " "

print(t3 * 4)

# 35 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.

print("이름: {name} 나이: {age}".format(name=name1, age=age1))
print("이름: {} 나이: {}".format(name2, age2))
print("이름: {0} 나이: {1}".format(name2, age2))

# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.

print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
