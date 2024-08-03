import turtle

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length)
    t.right(30)
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1)
    t.left(60)
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1)
    t.right(30)
    t.backward(branch_length)

def main():
    level = int(input("Enter the level of recursion: "))
    window = turtle.Screen()
    window.bgcolor("#ffffff")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.left(90)
    t.pendown()
    draw_pythagoras_tree(t, 100, level)
    window.mainloop()

if __name__ == "__main__":
    main()