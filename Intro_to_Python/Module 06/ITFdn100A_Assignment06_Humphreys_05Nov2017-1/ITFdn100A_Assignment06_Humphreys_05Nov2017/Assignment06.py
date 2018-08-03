# Title: Assignment06.py
# Dev:   John Humphreys
# Date:  11/04/2017
# Desc:  This program takes code from Assignment 05 and puts relevant parts of the code into a class with functions.
# ChangeLog:  JHumphreys, 11/05/2017, Added more code>

# -- Data -- #
# declare variables and constants
lst_table = []
str_item = ''
str_priority = ''
str_choice = 0

# -- Processing -- #
# open text file, read each row of data, write each row to individual dictionary, and
# write each dictionary to one master list
obj_file = open('ToDo.txt', 'r')
for row in obj_file:
    row = row.split(',')
    dic = {row[0]: row[1].rstrip('\n')}
    lst_table.append(dic)
obj_file.close()


class MenuChoice(object):
    """ This class enables user to view current contents of table,
    add a new item, remove an existing item, save current table data to text file,
    and exit.
    """

    @staticmethod
    def view_table():
        """ This function prints the current table of dictionaries. """
        print('Here\'s the current table:')
        print(lst_table)

    @staticmethod
    def add_item():
        """ This function adds a new task: priority dictionary to the table. """
        str_item = input('Enter a new item ')
        str_priority = input('Assign a priority [high, medium, or low] - ')
        dic = {str_item: str_priority}
        lst_table.append(dic)
        print(str_item + ' added to Table')

    @staticmethod
    def remove_item():
        """ This function removes an existing task: priority dictionary from the table. """
        str_item = input('Enter name of item to be removed ')
        for dic in lst_table:
            if str_item in dic:
                lst_table.remove(dic)
                print(str_item + ' found and removed from Table')
    
    @staticmethod
    def save_data():
        """ This function saves the current table of dictionaries to ToDo.txt file. """
        obj_file = open('C:\\_PythonClass\\Mod5\\ToDo.txt', 'w')
        for dic in lst_table:
            str_dic = str(dic)
            str_dic = str_dic.replace('{', '')
            str_dic = str_dic.replace('}', '')
            str_dic = str_dic.replace('\'', '')
            str_dic = str_dic.replace(':', ',')
            str_dic = str_dic.replace(', ', ',')
            obj_file.write(str_dic + '\n')
        obj_file.close()
        print('Data saved to ToDo.txt')

    @staticmethod
    def exit_program():
        """ This function closes the program. """
        print('Program execution completed.')


# -- Presentation (I/O) -- #
# get user input
# send program output
obj_table = MenuChoice()
while True:
    print('''
               Menu of Options
               1) Show current data.
               2) Add a new item.
               3) Remove an existing item.
               4) Save Data to File.
               5) Exit Program.
               ''')
    str_choice = str(input('Which option would you like to perform? [1 to 5] - '))
    print()  # adding a new line

    # Show the current items in the table
    if str_choice.strip() == '1':
        obj_table.view_table()
    elif str_choice.strip() == '2':
        obj_table.add_item()
    elif str_choice.strip() == '3':
        obj_table.remove_item()
    elif str_choice.strip() == '4':
        obj_table.save_data()
    elif str_choice.strip() == '5':
        obj_table.exit_program()
        break
