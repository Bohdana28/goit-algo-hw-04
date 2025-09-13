import turtle

# Визначаємо кольори для різних рівнів рекурсії
COLORS = ["blue", "green", "red", "purple", "orange", "brown"]

def koch_curve(t, order, size, level):
    """Малює одну лінію фрактала Коха з кольором за рівнем"""
    t.pencolor(COLORS[level % len(COLORS)])  # обираємо колір
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3, level + 1)
        t.left(60)
        koch_curve(t, order - 1, size / 3, level + 1)
        t.right(120)
        koch_curve(t, order - 1, size / 3, level + 1)
        t.left(60)
        koch_curve(t, order - 1, size / 3, level + 1)

def draw_koch_snowflake(order, size=300):
    """Малює повну сніжинку Коха з кольорами"""
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Сніжинка Коха - рівень {order}")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size, 0)  # передаємо початковий рівень 0
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (0-5): "))
        if level < 0:
            level = 0
        draw_koch_snowflake(level)
    except ValueError:
        print("Будь ласка, введіть ціле число для рівня рекурсії.")