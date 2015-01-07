# PyShellScript
This is a Python based shell script to run "grep"  command on a file. It takes the keywords to Search from an xlsx (excel) file. 

This is not a Bash Script because bash has limitations when it comes to reading excel files.
This script reads the cells from 1st column of the excel file and searches that string using grep in another (database) file.

If the value in the cell of xls file is present in the database file, then the script rights "Live" in the 2nd column of xls file against it. else it writes "not Live"

USE: $ ./Pyscript.py PATH/TO/the_xlsx_file PATH/TO/the_Database_file suffix

*suffix mentioned above in the use is another parameter which can be passed along.

The string searched with suffix will be like "suffix + the sting/integer in the cell of excel file"


This Script uses xlrd, xlwt and xlutils modules of python for reading and writing xls files.
These are neither pre-installed in linux nor in windows

Please install them using pip

sudo apt-get install python-pip           // to install pip in Ubuntu, you can google how to install pip in windows.Its easy

sudo pip install xlrd                     // to install xlrd in python
sudo pip install xlwt                     // to install xlwt in python
sudo pip install xlutils                  // to install xlutils in python


Please read their licenses as well. I dont know anything about licenses and all. I just wanna make the world a better place.

for any queries @chetanbansiwal on twitter (I used to use facebook alot, but now I am a twitter fan)
or chetanbansiwal on Quora
