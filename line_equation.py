#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This program calculates slope and y-intercept


# Defining the function that calculates the slope
def calc_slope(x_1, y_1, x_2, y_2):
       slope = (y_2 + ( -1 * y_1)) / (x_2 + ( -1 *x_1))
       return slope
# Defining the function that calculates the y-int
def calc_b(x_1, y_1, slope):
       b = y_1 - (x_1 * slope)
       return b
       
       

if __name__ == "__main__":
       while True:
              # Getting input
              user_x_1 = input("Enter x1 : ")
              user_y_1 = input("Enter y1 : ")
              user_x_2 = input("Enter x2 : ")
              user_y_2 = input("Enter y2 : ")
              
              try:
                     # Casting to float
                     x_1_float = float(user_x_1)
                     y_1_float = float(user_y_1)
                     x_2_float = float(user_x_2)
                     y_2_float = float(user_y_2)
                     
                     # Calling slope function
                     m = calc_slope(x_1_float, y_1_float, x_2_float, y_2_float)
                     
                     # Calling y-int function
                     y_int = calc_b(x_1_float, y_1_float, m)
                     
                     # Displaying result
                     print("For a line with the points ({}, {}) and ({}, {}) the y-intercept is {:.2f} and the slope is m = {:.2f}".format(x_1_float, y_1_float, x_2_float, y_2_float, y_int, m))
                     
                     
              except:
                     # Invalid input message and continue to let the user try again
                     print("Invalid input\nPlease try again with proper numbers.")
                     continue
              
              break