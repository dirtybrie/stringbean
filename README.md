# stringbean
![stringbean.png](https://github.com/dirtybrie/stringbean/blob/%7Bdirt%7D/img/stringbean.png)
<!--?raw=true-->
A simple random string generator

> stringbean is a python3 script<br/>
> Compatable with any version after python3.4<br/>
> Works for POSIX-compliant OS and NTFS (Linux/Mac, Windows)<br/>

> [!IMPORTANT]
> 1. The output for this script on windows is much longer than it is for linux just be mindful when you
> want to generate anything above 5000 lines. If your using linux it will spit out a 200,000 line file like nothing.<br/>
> 2. I have not tested stringbean on Mac yet, however macOS's core is a
> POSIX-compliant operating system so the exceptions in this code should still follow through.
> gnu/linux is based off of unix, Not to be construed as the same but the commands are similar
> and files are structured the same way. So there shouldn't be an issue as long as you have python3 intalled on your Mac.<br/>
> Just follow the same instructions for Linux below.

### COMPATABILITY CHECK

__MAC/LINUX__
```python
python
import os
os.name
```
If the return is 'posix' you're good to go!<br>

__WINDOWS__
```python
py
import os
os.name
```
If it returns 'nt' your all set!

## TO RUN IT

__LINUX__
```
sudo chmod +x stringbean
./stringbean
```
-or-
```
python stringbean
```
__WINDOWS__
```
py stringbean
```
For linux you can also copy/cut paste it to your bin folder and it will run fine :)
 
### COMMANDS
* __You have to give give it 2 arguments and they must be integers__.
* The first argument is the length of the text
* The second argument is how many lines per text file
* stringbean detects the OS and prompts you to name the file containing the texts
* then it will create a directory in Documents called stringbean and put your file there.
> [!NOTE]
> __If your root files will be exported to the /opt directory instead__
```
| cmd               | descriton                                                |
|stringbean 8 10000 | generate a random text with the length of 8, 10000 times |
|stringbean 13 300  | generate a random text with the lengtrh of 13, 300 times |
```
## Description

This is a random string generator, it is geared towards an aid for aircrack-ng 
dictionary attacks for hotspots with default generated passwords.
the success rate I've had is about 34.22% on 82 ATT&T Hotspots, I sh*t you not.
However the actual odds are very, very devestating for us.
 
Hotspots, modems and routers a lot of the times come with a default password that 
consists of Characters(uppercase & lowercase) and Numbers only. people tend to not
change them (suprisingly) and the libraries that give out hotspots tell the recipient 
not to change the passwords either. If a hotspot has the default ESSID like
ATT-WIFI-aX4D chances are they kept the password since they didn't bother
changing the ESSID.
 
This program will generate randome strings/texts over and over and append those
strings to a file with a text length and line limit of your chosing.
The strings by default consist of upper-lowercase characters and numbers only.
(Since thats how most hotspots generate their passwords)

> [!WARNING]
> If for some reason you do not have the Documents folder in your User directory
> This program will throwback an error. Just make one
> or edit the script for it to go somewhere else.<br/>
> If your root I've the slightest clue how you wouldn't have an /opt
> directory but the same thing above applies just make one or edit the script.

> [!NOTE]
> Just FYI the file stringbean writes to is in append mode so as long
> as the name you give the .txt file remains the same and is in the
> stringbean directory.
> stringbean won't overwrite but instead append to it.
> -db

## Manipulating The Script

Very doable, any script can be manipulated. getting it to work is another thing.<br/>
Fortunately this is a very basic script and I made it even easier for manipulation.</br>
Go head and pull up the code of stringbean while your reading.

Ok so our variables between line 23-41 is commented as the ASCII Table.
If you don't know what ASCII is, it's just a fancy way of saying letters, numbers and punctuation.
Say you want more than just uppercase/lowercase letters and numbers
you want to throw in special characters as well. To do so, you would
swap **charnumb** in lines 162 & 178 (if your using Linux, line 195 for Windows) which is:<br/>
```
stringbean = random_string_generator(args.strlen, charnumb)<br/>
```
with the variable **cns**:<br/>
```
stringbean = random_string_generator(args.strlen, cns)<br/>
```
If you just want numbers you'd swap it with numb, etc,etc...<br/>

You can also alter the limit for text length and lines in a file
by changing the values of the str_limit and lst_limit.

> Tips for me on better programming? Contact me ;)

__UPDATES__<br/>

<sup>
10/16/23 OS detection<br/>
10/17/23 root detection<br/>
</sup>

