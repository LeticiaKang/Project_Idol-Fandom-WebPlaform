import os

def route():
    result = os.path.dirname(os.path.realpath(__file__))
    return result

    #현재경로
    #학원: C:\Users\user\Desktop\프로젝트\HappyVirus\최종(웹)\web\myapp\Route.py
    #집: c:\Users\user\OneDrive\바탕 화면\프로젝트\HappyVirus\최종(웹)\web\myapp\Route.py

# print("경로 === ",route)
# print("경로 === ",os.getcwd())