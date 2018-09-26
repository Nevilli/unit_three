import turtle


turtle.speed(10)


def side_length():
    length = input("What is the side length of the hexagons?")
    return float(length)


def center_color():
    color_of_center = input("What is the center color of the flower?")
    return color_of_center


def petal_color():
    color_of_petal = input("What is the color of the petals?")
    return color_of_petal


def draw_hexagon(side, color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(side)
        turtle.right(60)
    turtle.end_fill()


def main():
    length = side_length()
    c_color = center_color()
    p_color = petal_color()
    draw_hexagon(length, c_color)
    turtle.left(120)
    draw_hexagon(length, p_color)
    turtle.left(120)
    draw_hexagon(length, p_color)
    turtle.forward(100)
    turtle.left(60)
    draw_hexagon(length, p_color)
    turtle.forward(100)
    turtle.left(60)
    draw_hexagon(length, p_color)
    turtle.forward(100)
    turtle.left(60)
    draw_hexagon(length, p_color)
    turtle.forward(100)
    turtle.left(60)
    draw_hexagon(length, p_color)

    turtle.exitonclick()

main()
