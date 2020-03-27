# -*- coding: utf-8 -*-

import turtle

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)

def make_square(dave):
    length = int(input('TamaÃ±o de cuadrado: '))
    for i in range(4):
        make_line_and_turn(dave, length)

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    make_square(dave)
    turtle.mainloop()

if __name__ == '__main__':
    main()