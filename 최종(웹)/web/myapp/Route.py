import os

def route():
    result = os.path.dirname(os.path.realpath(__file__))
    return result

    # 현재 경로 : C:\Users\user\Desktop\프로젝트\HappyVirus\최종(웹)\web\myapp\Route.py

# print("경로 === ",route)
# print("경로 === ",os.getcwd())