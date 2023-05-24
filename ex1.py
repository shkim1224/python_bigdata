
import turtle
t = turtle #.Turtle()
t1 = turtle #.Turtle()
t1.shape("circle")
t.shape("turtle")

s = input("몇각형을 원하시나요?:")
n=int(s)

for i in range(n):
	t1.forward(100)
	t1.left(360/n)

for i in range(n):
	t.forward(100)
	t.left(360/n)	

turtle.mainloop()
turtle.bye()

