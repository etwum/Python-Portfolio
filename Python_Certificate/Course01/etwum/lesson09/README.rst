***Mail Room Part 5 - Object Oriented***

Refactor the mailroom program using classes to help organize the code.

This time, we want to use an OO approach to better structure the code to make it more extensible.

It was quite reasonable to build the simple mailroom program using a single module, a simple data structure, and functions that manipulate that data structure.

But if one were to expand the program with additional functionality, it would start to get a bit unwieldy and hard to maintain.

So it’s a pretty good candidate for an object-oriented approach.

As you design appropriate classes, keep in mind these three guidlines for good code structure:

Encapsulation: you have a data structure that holds your data, and you have functions that manipulate that data – you want them “bundled up” in a neat package, so that the rest of the code doesn’t need to know about the data structure you are using.

Separation of Concerns: The user interaction code should be cleanly separated from the data handling code.

There should be no input function in the class that holds the data!

As always: DRY – Don’t repeat yourself – anywhere you see repeated code – refactor it!
