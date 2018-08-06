***Slicing Program***

Perform different task using python slicing


***List Lab Program***

Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.

Series 2
Using the list created in series 1 above:
Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

Series 3
Again, using the list from series 1:
Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.

Series 4
Once more, using the list from series 1:
Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.

***String Format Lab Program***

Performs different task using string formatting


***Mailroom Part 1 Program***
Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:
It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)

Sending a Thank You
If the user (you) selects ‘Send a Thank You’, prompt for a Full Name. 
If the user types ‘list’, show them a list of the donor names and re-prompt
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
Once an amount has been given, add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
It is fine (for now) to forget new donors once the script quits running.

Creating a Report
If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount. 
Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
