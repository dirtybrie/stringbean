# stringbean
![alt text](https://github.com/dirtybrie/stringbean/blob/%7Bdirt%7D/img/stringbean.png?raw=true)

A simple random string generator

## Usage
> Stringbean is a python3 script<br/>
> you should have any version after 3.6<br/>
> This is for linux distro's only I'll have to throw in some exceptions for OS detection later<br/>

you can run it by:<br/>

```bash
./stringbean
```
-or-
```bash
python stringbean
```
You can also copy/cut paste it to your bin folder and it will run fine :)

* __You have to give give it 2 arguments and they must be integers__.
* The first argument is the length of the text
* The second argument is how many lines per text file
* stringbean will ask you what the file name will be
* then it will create a directory in Documents called stringbean and put your file there.

| cmd | descriton |
| --- | --- |
|stringbean 8 10000 | generate a random text with the length of 8, 10000 times |
|stringbean 13 300 | generate a random text with the lengtrh of 13, 300 times |

## Description

This is a random string genorator is geared towards an aid for aircrack-ng 
dictionary attacks for hotspot default generated passwords.
the success rate I've had is about 34.22% on 82 ATT&T Hotspots, I sh*t you not
However the actual odds are very, very devestating for us.
 
Hotspots, modems and routers a lot of the times come with a default password that 
consists of Characters(uppercase & lowercase) and Numbers only. people tend to not
change them (suprisingly) and the libraries that give out hotspots tell the recipient 
not to change the passwords either.
 
This program will generate randome strings.
The strings consist of uppercase;lowercase characters and numbers only.

If for some reason you do not have a Documents in your /home/user directory
This program will through an error. Just make one
or edit the script for it to go somewhere else

Just FYI the file stringbean writes to is in append mode so as long
as the name you give the .txt file remains the same and is in the
stringbeans directory.
stringbean won't overwrite but instead append to it.
-db

## Manipulating The Script

Very doable, any script can be manipulated. getting it to work is another thing<br/>
Fortunately this is a very basic script and I made it even easier to manipulate</br>
Go head and pull up the raw script of stringbean while your reading.

Ok so our variables between line 19-30 is declared is the ASCII Table.
If you don't know what ASCII is, it's just a fancy way of saying letters, numbers and punctuation.<br/>
Say you want more than just uppercase/lowercase letters and numbers
you want to through in special characters as well. To do so, you would
swap **charnumb** in line 112 which is:<br/>

stringbean = random_string_generator(args.strlen, charnumb)<br/>

with the variable **cns**:<br/>

stringbean = random_string_generator(args.strlen, cns)<br/>

If you just want numbers you'd swap it with numb, etc,etc...<br/>
The only thing is you cant just print uppercase or lower case characters<br/>

You can also alter the limit for text length and lines in a file
by changing the values of the lst_limit and str_limit.

> Tips for me on better programming? Contact me ;).

