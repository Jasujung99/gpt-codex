import turtle
import random
import time

# 기본 예제는 ex/star_drawing.py 파일을 참고하세요.
# 이 파일은 여러 크기의 별을 순차적으로 그리는 심화 버전입니다.

# 거북이 그래픽 화면을 설정해요.
screen = turtle.Screen()
screen.bgcolor("black")

# 거북이 객체를 만들고 속도를 최고로 설정해요.
t = turtle.Turtle()
t.speed(0)

# 사용할 색깔 목록입니다.
colors = ["red", "blue", "green", "purple", "orange", "yellow"]


def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

# 크기를 키워 가며 무작위 색의 별을 그려요.
for size in range(50, 151, 20):
    t.pencolor(random.choice(colors))
    draw_star(size)
    t.right(36)  # 다음 별을 그리기 전 약간 돌려요.
    time.sleep(0.5)

turtle.done()
