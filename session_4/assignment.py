'''
과제 1. 별찍기
- 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
**********
*********
********
*******
*****
****
***
**
*
'''

print("\n과제 1\n")

i = 10

while i > 0:
    print("*"*i)
    i -= 1


'''
과제 2. 구구단
- 구구단 2단을 출력해보세요!
'''

print("\n과제 2\n")

i = 1

while i < 10:
    print("2 * ", i, "= ", 2*i)
    i += 1

'''
과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요.
'''

print("\n과제 3\n")

sum = 0
i = 1

while i <= 1000:
    if i % 3 == 0:
        sum += i
        i += 1
    else:
        i += 1
        continue

print(sum)

'''
과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요.
- mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
'''

print("\n과제 4\n")

mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

i = 0
sum = 0

for i in range(len(mutsa_scores)):
    sum += mutsa_scores[i]
    i += 1

average = sum / len(mutsa_scores)
print(average)

'''
과제 5. input.py 문제 2개 풀기

print('문제 1. 전화번호 받기')
print('조건 1. 저장할 때는 공백 문자 없이')
print('조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!')

print('문제 2. 영어 이름 받기')
print('choi juwon 을 입력 받으면,')
print('first name : Choi, last name: Juwon 이 출력되게 만들기')
'''

print("\n과제 5")
print("\n문제 1\n")

available_number = []
phone_number = input("전화번호를 입력해주세요: ")
fixed_number = []

for i in range (10):
    j = str(i)
    available_number.append(j)

for element in phone_number:
    if element in available_number:
        fixed_number.append(element)
    else:
        continue

print("".join(fixed_number))

print("\n문제 2\n")

name = input("영어 이름을 입력해주세요: ")
name = name.split(" ")
name[0]=name[0].capitalize()
name[1]=name[1].capitalize()

print("first name: %s, last name: %s" % (name[0], name[1]))
