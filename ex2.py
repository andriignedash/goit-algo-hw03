import turtle

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level-1)
        t.left(60)
        koch_snowflake(t, length, level-1)
        t.right(120)
        koch_snowflake(t, length, level-1)
        t.left(60)
        koch_snowflake(t, length, level-1)

def draw_snowflake(t, length, level):
    for _ in range(3):
        koch_snowflake(t, length, level)
        t.right(120)

def main():
    level = int(input("Введіть рівень рекурсії: "))

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    length = 400  # Довжина сторони сніжинки
    draw_snowflake(t, length, level)

    turtle.done()

if __name__ == "__main__":
    main()
