***Mailroom Part 2 Program***

Update your mailroom program to:
Use dicts where appropriate
See if you can use a dict to switch between the users selections. See Using a Dictionary to switch for what this means.
Try to use a dict and the .format() method to do the letter as one big template rather than building up a big string in parts.
Example:
In [3]: d
Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}


In [5]: "My name is {first_name} {last_name}".format(**d)
Out[5]: 'My name is Chris Barker'
Don’t worry too much about the “**” – we’ll get into the details later, but for now it means, more or less, pass this whole dict in as a bunch of keyword arguments.
Update Mailroom with File Writing
Write a full set of letters to everyone to individual files on disk.
In the first version of mailroom, you generated a letter to someone who had just made a new donation, and printed it to the screen.
In this version, add a function (and a menu item to invoke it), that goes through all the donors in your donor data structure, generates a thank you letter, and writes it to disk as a text file.
Your main menu may look something like:
Choose an action:

1 - Send a Thank You
2 - Create a Report
3 - Send letters to everyone
4 - Quit
The letters should each get a unique file name – derived from the donor’s name, and maybe a date.
After running the “send letters to everyone” option, you should get a bunch of new files in the working dir – one for each donor.
After choosing (3) above, I get these files in the dir I ran it from:
Jeff_Bezos.txt
Mark_Zuckerberg.txt
Paul_Allen.txt
William_Gates_III.txt
(If you want to get really fancy, ask the user for a directory name to write to!)
An example looks like this:
Dear Jeff Bezos,

        Thank you for your very kind donation of $877.33.

        It will be put to very good use.

                       Sincerely,
                          -The Team
Feel free to enhance it with some more information about past generosity, etc….
The idea is to require you to structure your code so that you can write the same letter to the screen or to disk (and thus anywhere else) and also exercise a bit of file writing.
