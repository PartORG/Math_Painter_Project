from canvas import Canvas
from shapes import Rectangle, Square


def main():
    canvas_width = int(input("Enter canvas width: "))
    canvas_height = int(input("Enter canvas height: "))

    colors = {"white": [255, 255, 255], "black": [0, 0, 0]}
    canvas_color = input("Enter canvas color (black or white): ")

    canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

    while True:
        shape_type = input("What do you like to draw? Enter quit to quit: ")

        if shape_type.lower() == "rectangle":
            rec_x = int(input("Enter x of the rectangle: "))
            rec_y = int(input("Enter y of the rectangle: "))
            rec_width = int(input("Enter width of the rectangle: "))
            rec_height = int(input("Enter height of the rectangle: "))
            red = int(input("Enter how much red should rectangle have: "))
            green = int(input("Enter how much green should rectangle have: "))
            blue = int(input("Enter how much blue should rectangle have: "))

            r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
            r1.draw(canvas)

        if shape_type.lower() == "square":
            sq_x = int(input("Enter x of the square: "))
            sq_y = int(input("Enter y of the square: "))
            sq_side = int(input("Enter side of the square: "))
            red = int(input("Enter how much red should square have: "))
            green = int(input("Enter how much green should square have: "))
            blue = int(input("Enter how much blue should square have: "))

            s1 = Square(x=sq_x, y=sq_y, side=sq_side, color=(red, green, blue))
            s1.draw(canvas)

        if shape_type.lower() == "quit":
            break

    canvas.make('result.png')


if __name__ == '__main__':
    main()
