"""
Purpose: Create a program for plotting stock prices
Authors: Adonte Mays
Date: 9/17/2022
Updated:
"""
import turtle

from stock_preprocess import create_prices_list

min_price, max_price, prices, length = create_prices_list()

screen = turtle.Screen()
screen.title('Stock Price Visualization')
screen.setup(1000, 1000)
screen.setworldcoordinates(0, min_price * 0.9, length, max_price * 1.1)
turtle.speed(0)

stock_line = turtle.Turtle()
previous_price = 0
x = 0

for today in prices:
    if previous_price < today:
        stock_line.pencolor('green')
        stock_line.goto(x, today)
    else:
        if previous_price > today:
            stock_line.pencolor('red')
            stock_line.pensize(previous_price - today)
            stock_line.goto(x, today)
    x += 1
    previous_price = today
