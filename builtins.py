# 내장 함수 : import 하지 않고 쓸 수 있는 함수들

# # input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir())
import pickle
print(dir())

# import 하면 할수록 어떤 함수를 가지고 있는지 늘어나는 것을 볼 수 있음!

print(dir(random))
# random 안에 무슨 함수가 있는지 볼 수도 있음

lst = [1,2,3]
print(dir(lst)) #리스트로 할 수 있는 것들

name = "Jim"
print(dir(name)) # name에 대해서 실행할 수 있는 것들

# google에 list of python builtins 치면 내장함수 목록을 볼 수 있음!
