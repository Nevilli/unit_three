# Liam Neville
# 9/28/18
# This program makes a flower using turtle based off of user input
import turtle


turtle.speed(10)


def side_length():
    """
    This function gets the side length from the user
    :return: length as a float
    """
    length = input("What is the side length of the hexagons?")
    return float(length)


def center_color():
    """
    This function gets the center color for the flower from the user
    :return: color_of_center
    """
    color_of_center = input("What is the center color of the flower?")
    return color_of_center


def petal_color():
    """
    This function gets the color of the petals from the user
    :return: color_of_petal
    """
    color_of_petal = input("What is the color of the petals?")
    return color_of_petal


def draw_hexagon(side, color):
    """
    This function draws the hexagons
    :param side: This is the side length of the hexagon
    :param color: This is the color of the hexagon
    :return: none
    """
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

    # This is the center hexagon
    draw_hexagon(length, c_color)
    turtle.left(120)

    # petal 1
    draw_hexagon(length, p_color)
    turtle.left(120)

    # petal 2-5
    for x in range(4):
        draw_hexagon(length, p_color)
        turtle.forward(length)
        turtle.left(60)

    # petal 6
    draw_hexagon(length, p_color)

    turtle.exitonclick()


main()
