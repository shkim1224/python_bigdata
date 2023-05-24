
import turtle
t = turtle.Turtle()
t.shape("turtle")

def draw_rect(shape):
	t.shape(shape)
	for i in range(4):
		t.forward(100)
		t.right(90)


def test_kwargs(**kwargs):
	
	for shape in kwargs.values():
		print(shape)
		draw_rect(shape=shape)

# test_kwargs(shape="circle")
# test_kwargs(shape="turtle")
# test_kwargs(shape="arrow")/

turtle.mainloop()
turtle.bye()