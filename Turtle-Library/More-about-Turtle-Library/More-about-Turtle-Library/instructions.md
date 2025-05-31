# Introduction to Turtle Graphics Library
The Turtle graphics library is a powerful tool for creating simple graphics and drawings. It is especially suitable for beginners learning about coordinates, shapes, and colors.

# Instructions
1. Import the turtle library using `import turtle`.
2. Create a turtle screen using `screen = turtle.Screen()`.
3. Set up a turtle instance using `t = turtle.Turtle()`.

## Coordinates
- Turtle graphics work with Cartesian coordinates, with the initial position (0,0) being at the center of the screen.
- You can move the turtle to different coordinates using `t.goto(x, y)`.

## Drawing a Dotted Line
- Use a loop to move the turtle forward a small amount, lift the pen up, move forward again, and put the pen down to create a dotted line effect.

## Drawing a Cross
- Use the `t.forward(distance)` and `t.right(angle)` or `t.left(angle)` to draw lines and angles to form a cross.

## Writing Text on Screen
- Use `t.write("Your Text", move=False, align='left', font=('Arial', 10, 'normal'))` to write text at the turtle's current position.

## Drawing Shapes
- Use loops and `t.forward(distance)` along with `t.right(angle)` to draw various shapes like squares, triangles, etc.

## Example
### Draw a Dotted Line
```python
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

for i in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

screen.mainloop()
```

## Challenge
1. Try drawing a cross.
2. Write text on the screen using turtle graphics.
3. Experiment with drawing different shapes and colors.

## Hint
1. Use `t.pencolor("color_name")` to change the color of the pen.
2. For drawing a square, you need to move forward and turn right 90 degrees, four times.


