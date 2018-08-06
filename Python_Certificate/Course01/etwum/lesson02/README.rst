***Series Program***

The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us:
0, 1, 1, 2, 3, 5, 8, 13, ...
We will write a function that computes this series – then generalize it.

The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
2, 1, 3, 4, 7, 11, 18, 29, ...
In your series.py module, add a new function, lucas, that returns the nth value in the lucas numbers series.
Ensure that your function has a well-formed docstring.

Both the fibonacci series and the lucas numbers are based on an identical formula.
Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series.

Add a block of code to the end of your series.py module. Use the block to write a series of assert statements that demonstrate that your three functions work properly.
Use comments in this block to inform the observer what your tests do.


***Grid Program***

Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.
For example, print_grid2(3,4) results in:
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
(three rows, three columns, and each grid cell four “units” in size)

***Fizz Buzz Program***

Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
