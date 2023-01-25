"""
Purpose: Create a program for plotting stock prices
Authors: Adonte Mays
Date: 9/17/2022
"""
import turtle

from stock_preprocess import create_prices_list

min_price, max_price, prices, length = create_prices_list()

screen = turtle.Screen()
screen.title('Stock Price Visualization')
screen.setup(1000, 1000)
screen.setworldcoordinates(0, min_price * 0.9, length, max_price * 1.1)
turtle.speed(0)

adonte = turtle.Turtle()
yesterday_close = 0
x = 0

for today in prices:
    if yesterday_close < today:
        adonte.pencolor('green')
        adonte.goto(x, today)
    else:
        if yesterday_close > today:
            adonte.pencolor('red')
            adonte.pensize(yesterday_close - today)
            adonte.goto(x, today)
            yesterday_close += 1

    x += 1
    yesterday_close = today

# Iterate through the prices list and plot each price point
# If the price point is larger than the previous price, the line should be green
# Otherwise the line should be red
# HINT:
#       if statements follow the following syntax:
#           if x > y:
#               max = x
#           else:
#               max = y
# BONUS:
#      Make your lines thicker based on the amount of the price increase or decrease
