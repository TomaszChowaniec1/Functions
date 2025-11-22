import turtle
import figures   


window = turtle.Screen()
window.bgcolor("lightgreen")


pen = turtle.Turtle()
pen.speed(5)



pen.penup()
pen.goto(-150, 100)
pen.pendown()
figures.draw_square(pen, 70)

pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_square(pen, 80)



pen.penup()
pen.goto(-150, -50)
pen.pendown()
figures.draw_triangle(pen, 100)


pen.penup()
pen.goto(100, -50)
pen.pendown()
figures.draw_triangle(pen, 100)



pen.penup()
pen.goto(-150, -200)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)


pen.penup()
pen.goto(100, -200)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)


pen.hideturtle()
window.mainloop()
