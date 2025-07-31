import turtle
import random
import time

# 그림을 그리는 '거북이' 도구를 가져와요.
t = turtle.Turtle()
# 색깔 목록을 만들어요.
colors = ["red", "blue", "green", "purple", "orange"]

while True:  # 무한 반복해요.
    t.clear()  # 화면을 깨끗하게 지워요.
    for _ in range(5):  # 5번 반복해요.
        t.forward(100)  # 100만큼 앞으로 가요.
        t.right(144)  # 오른쪽으로 144도 돌아요.
    # 펜 색깔을 목록에서 무작위로 골라요.
    t.pencolor(random.choice(colors))
    time.sleep(1)  # 1초 동안 잠시 멈춰요.

