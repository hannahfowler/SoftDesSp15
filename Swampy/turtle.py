"""Turtle World Demo"""
from swampy.TurtleWorld import *

def position(turtle, start_x, start_y, angle):
	turtle.x = start_x
	turtle.y = start_y
	turtle.heading = angle

def draw_line(turtle, line_length):
	turtle.fd(line_length)

def turn_right(turtle, angle):
	turtle.rt(angle)

def turtle_text(letter):
	position(beth, -150, -100, 60)
	draw_line(beth, 200)
	turn_right(beth, 120)
	draw_line(beth, 200)
	position(beth, )



	
world = TurtleWorld()
beth = Turtle()
beth.set_pen_color = 'red'
turtle_text('A')
wait_for_user()