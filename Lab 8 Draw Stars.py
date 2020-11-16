import turtle

# These are global variables we use in each code. The data is populated from
# the read_coords function
x_y_coordinates = {}
magnitude = {}
star_num = {}
names = {}

# This creates our turtle object
t = turtle.Turtle()


def read_coords(file):
    # This function opens the file, reads the data, and puts the data in the
    # proper variables and form, making it useable by our program
    star_file = open(file, 'r')
    for index in star_file:
        index = index.split()
        # gets the coordinates int0 coordinates_dict
        x_y_coordinates[float(index[3])] = (float(index[0]), float(index[1]))
        # gets the magnitude into magnitude
        magnitude[float(index[3])] = float(index[4])
        # gets the star numbers into star_num
        try:
            star_num[float(index[3])] = index[6]
        except IndexError:
            pass
    # closes the file
    star_file.close()


def plot_plain_stars(picture_size, coordinates_dict):
    # This function takes the list of stars, and plots them all the same
    # magnitude or size
    turtle.setworldcoordinates(-1, -1, 1, 1)
    # sets the picture size and background color
    turtle.screensize(picture_size, picture_size, 'black')
    turtle.tracer(0)
    t.color('white')

    for entry in coordinates_dict:
        t.pu()
        t.setpos(coordinates_dict[entry])
        t.pd()
        t.begin_fill()
        i = 0
        while i < 4:
            t.forward(1/500)
            t.left(90)
            i += 1
        t.pu()
        t.end_fill()
    turtle.update()
    turtle.exitonclick()


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    # This function takes the list of coordinates, and their magnitudes, and
    # plots them accordingly, in a scaled version.
    turtle.setworldcoordinates(-1, -1, 1, 1)
    turtle.screensize(picture_size, picture_size, 'black')
    turtle.tracer(0)
    t.color('white')
    for entry in coordinates_dict:
        t.pu()
        t.setpos(coordinates_dict[entry])
        t.pd()
        t.begin_fill()
        i = 0
        while i < 4:
            # scaling the magnitudes against the screen size. We found that
            # dividing by 500 made them look too big!
            t.forward(magnitudes_dict[entry]/1000)
            t.left(90)
            i += 1
        t.pu()
        t.end_fill()
    turtle.update()
    turtle.exitonclick()


def menu():
    # Because both of the functions plot_plain_stars and plot_by_magnitude
    # cannot be run at the same time, we added a menu to our code so that the
    # user can choose which one to run, an can run both functions without
    # killing the program
    answer = input("Would you like to plot plain stars or by magnitude? \
(enter 'p' or 'm', or 'e' to exit): ")
    if answer.lower() == 'p':
        plot_plain_stars(500, x_y_coordinates)
        # runs the menu again, so you can see the other option!
        menu()
    elif answer.lower() == 'm':
        plot_by_magnitude(500, x_y_coordinates, magnitude)
        # runs the menu again, so you can see the other option!
        menu()
    elif answer.lower() == 'e':
        pass
        # Do nothing and end the program
    else:
        # if there is an invalid response, nothing will happen and the question
        # will be asked again
        menu()


def main():
    read_coords('stars.txt')
    menu()

if __name__ == "__main__":
    main()
