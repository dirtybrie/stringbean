# stringbean
![alt text](https://github.com/dirtybrie/stringbean/blob/%7Bdirt%7D/img/stringbean.png?raw=true)
A simple random string generator

#Usage
Stringbean is a python script
you can run it by:
$./stringbean
$python stringbean
you can also copy/cut paste it to your bin folder and it will run fine :)

You have to give give it 2 arguments and they must be integers.
The first argument is the length of the text
The second argument is how many lines per text file
stringbean will ask you what the file name will be
stringbean will create a directory in Documents called stringbean
and put your file there.

ex:                    descrition:
stringbean 8 10000   | 8 letters, 10000 lines
string bean 13 300   | 13 letters, 300 lines

This is for linux distro's only
I'll have to throw in some exceptions for OS detection later

#Description
This is a random string genorator is geared towards an aid for aircrack-ng 
dictionary attacks for hotpot default generated passwords.
the success rate I've had is about 34.22% on 82 ATT&T Hotspots, I sh*t you not
However the actual 'odds' are very, very devestating for us.
 
Hotspots, modems and routers a lot of the times come with a default password that 
consists of Characters(uppercase & lowercase) and Numbers only. people tend to not
change them (suprisingly) and the libraries that give out hotspots tell the recipient 
not to change the passwords either.
 
This program will generate randome strings.
The strings consist of uppercase;lowercase characters and numbers only. 
To change that, simply swap charnumb at line 138 with one of the variables at the 
ASCII Table (Lines 58-69)
You can also alter the limit for text length and lines in a file
by changing the values of lst_limit and str_limit

If for some reason you do not have a Documents directory
This program will through an error. Just make one
or edit the script for it to go somewhere else

Just FYI the file stringbean writes to is in append mode so as long
as the name you give the .txt file remains the same and is in the
stringbeans directory.
stringbean won't overwrite but instead append to it
-db

Tips for me on better programming? Contact me ;)

