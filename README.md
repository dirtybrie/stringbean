![stringbean.png](https://github.com/dirtybrie/stringbean/blob/%7Bdirt%7D/img/stringbean.png)
<!--?raw=true-->
A simple random string generator

> stringBEAN is a python3 script<br/>
> Compatable with any version after python3.4<br/>
> [confirmed] works for POSIX-compliant OS and NTFS (Linux/Mac, Windows)<br/>
> [confirmed] works for iSH and Termux

> [!IMPORTANT]
> 1. The output for this script on windows is exponentially slower than linux. Just be mindful when you
> want to generate anything above 5000 lines. If your using linux it will spit out a 200,000 lines in a file like nothing.<br/>
> 2. I have not tested stringbean on a Mac yet, however macOS's core is a
> POSIX-compliant operating system so the exceptions in this code should still follow through.
> gnu/linux is based off of unix, Not to be construed as the same but the commands are similar
> and files are structured the same way. So there shouldn't be an issue as long as you have any version after python3.4 intalled on your Mac.<br/>
> Just follow the same instructions for Linux below.

### QUICK UPDATES
>10/19/23

stringBEAN has options now!!!<br/> It also uses the colorama module for text color
I put in an auto-install feature for colorama if you do not have it<br/>
to skip the auto-intall feautre simply execute the code below:

```
python -m pip install colorama
```

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
* __You have to give give it 3 arguments the 1st is an option, 2nd and 3rd must be integers__.
* The first argument is an option(i.e. -c, -cn, -cns), the option specifies wether your texts will 
  have numbers, characters+numbers, number+special characters etc.. 
* The second argument is the length of the text.
* The third argument is how many lines per text file.
* stringbean detects your OS then prompts you to name the file containing the texts,
* then it will create a directory in Documents called 'stringBEAN' and puts your file there.
> [!NOTE]
> __If your root files will be exported to the /opt directory instead__
```
OPTION:   DESCRIPTION:
-c       | Characters Only
-n       | Numbers Only
-s       | Special Characters Only
-cn      | Characters + Numbers
-cs      | Characters + Special Characters
-ns      | Numbers + Special CHaracters
-cns     | Characters + Numbers + Special Characters

ex: stringbean -cn 8 10000
                   |   |
length of text-----'   |
lines per file---------'

```
## Description

This is a random string generator, it is geared towards an aid for aircrack-ng 
dictionary attacks for hotspots with default generated passwords.
I cracked 32 out of 81 Hotspots, I sh*t you not.
However the actual odds are very, very, VERY devestating for us.
(and yes I had permission to do so)

Hotspots, modems and routers a lot of the time come with a default password that 
consists of Characters(uppercase & lowercase) and Numbers only. people tend to not
change them (suprisingly) and the libraries that give out hotspots tell the recipient 
not to change the passwords either. If a hotspot has the default ESSID like
ATT-WIFI-aX4D chances are they kept the password since they didn't bother
changing the ESSID.
 
This program will generate randome strings/texts over and over and append those
strings to a file with a string combination, text length and line limit of your chosing.

> [!WARNING]
> If for some reason you do not have the Documents folder in your username directory
> This program will throwback an error. Just make one or edit the script for it to go somewhere else.<br/>
> If your root I've the slightest clue how you wouldn't have an /opt
> directory but the same thing above applies just make one or edit the script.

> [!NOTE]
> Just FYI the file stringBEAN writes to is in append mode so as long
> as the name you give the .txt file remains the same and is in the
> stringBEAN directory.
> stringBEAN won't overwrite but instead append to it.<br/>
> DO NOT CHANGE IT TO OVERWRITE MODE("w+")
>
> I know telling you NOT to do something just makes you want to do it even more<br/>
> however if it's in overwrite it will keep overwriting the file it puts the strings in,<br/>
> meaning the end result is just one line of text.
> 
> -db

## QUICK DISCLAIMER:

> [!WARNING]
> I do not encourage anyone to use this as ammunition for a dictionary attack on networks you<br/>
> DO NOT HAVE ACCESS TO or DO NOT HAVE PERMISSION BY THE OWNER TO DO SO.<br/>
> It's for educational purpose only kiddo's.

Plus as I stated earlier about our odds your hitting a random generated text with a list of random generated texts so your odds are pathetic unless your a firm believer in the chaos theory.<br/>
However effective it may be ;)

> Tips for me on better programming? Contact me ;)

__UPDATES__<br/>

<sup>
10/16/23 OS detection<br/>
10/17/23 root detection<br/>
10/19/23 options for argv[1]
</sup>

