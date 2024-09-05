#! /usr/bin/python3

# stringBEAN v 0.7.2
# by Dirty Brie
# https://github.com/dirtybrie
#
# Licensed under the:
# GNU GENERAL PUBLIC LICENSE v3.0
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation
#
# This program is distributed
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

import random
import string
from argparse import ArgumentParser as AP
from getpass import getuser
from itertools import cycle
from threading import Thread
from time import sleep
import socket
import sys
import os
os.getcwd()

# Varibles for directory paths
user = getuser()
path = f"/home/{user}/Documents/stringBEAN"
chk_path = f"/home/{user}/Documents"
r_path = "/opt/stringBEAN"
r_chkpath = "/opt"
win_chkpath = f"C:\\Users\\{user}\\Documents"
winpath = f"C:\\Users\\{user}\\Documents\\stringBEAN"

# ASCII TABLE
# Uppercase and Lowercase letters
char = string.ascii_letters
# you can obviously see what that is...
numb = '0123456789'
# Special Characters
spec = string.punctuation
# Characters and Numbers
charnumb = char + numb
# Characters and Special Characters
c_spec = char + spec
# Numbers and Special Characters
n_spec = numb + spec
# Characters, Numbers and Special Characters.
cn_spec = char + numb + spec

# LIMITS
str_limit = 501
lst_limit = 800001
winlst_limit = 50001

# stringBEAN help and final output banners
class banners():
	def __init__(self):
		pass

	def str_machine(self):
		print(
|[###################################|
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|
|######             .         ##### #|
|# #####           n           ######|
|######             nm        ##### #|
|# ##### stringBEAN  MM        ######|
|######               ###     ##### #|
|# #####             f#$$#     ######|
|######           __$$$$      ##### #|
|# #####          | \##        ######|
|######    _______|  |____    ##### #|
|# #####   |___X     X __|     ######|
|######    |____xxxxx____|    ##### #|
|# #####   |r C 3 f $ # 6|     ######|
|######    |v_v_v_v_v_v_v|    ##### #|
|# #####   |_____________|     ######|
|######                       ##### #|
|<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|
|####################################|

		''')
		print(Style.RESET_ALL)
	def help_sb(self):
		print( V.7.2 XxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
XXXXxx  Copyright (C) 2023  xxXXXXXXXXXXXF
XXXXXxXX  {hex_a[2]}by dirty brie{hex_a[0]}  XXXXXxxXXXXXXXXXXXXx
XX     x x     xxXXXXXxxXxXX2
XxxX  `.X.  XXxxxXXXX
______________________________________________
-c     | Characters (Upper & Lower case)
-n     | Numbers
-s     | Special Characters
-cn    | Characters + Numbers
-cs    | Characters + Special Characters
-ns    | Numbers + Special Characrers              
-cns   | Characters + Numbers + Special Characters 
_______|___________________________________________
                               ######  X     x
ex: stringbean -cn 8 12000  	####### xxxxx
                   |   |         ###############
Length of Text-----'   |       ###############	
Lines per File---------'    #############
________________________________________
LIMITS:
Length of Text: 500
lines/File: 800,000/50,000 (lin-mac/win)
______________________________________________
		''')
		print(Style.RESET_ALL)

# Our generator, curtosy of python's 'random' module
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for i in range(str_size))

# Check directories for existence, make stringBEAN dir, checks the OS and wether user is root or not
class checkdir(object):
	def __init__(self):
		pass
	# Check Documents dir existence 
	def chkdir(self, chkpath):
		if not os.path.isdir(chkpath):
			print(f"stringBEAN needs a Documents directory in /home/{user}")
			sys.exit(1)
		else:
			return

	# check stringBEAN dir existence, mkdir stringBEAN or proceed
	def mkdir(self, path):
		if not os.path.isdir(path):
			os.mkdir(path)
			print(f"Creating Directory: /home/{user}/Documents/stringBEAN")
		elif os.path.isdir(path):
			return

	# Check /opt dir existence
	def sudo_chkdir(self, chkpath):
		if not os.path.isdir(r_chkpath):
			print("You need an /opt directory")
			sys.exit(1)
		elif os.path.isdir(r_chkpath):
			return

	# mkdir stringBEAN in opt/ directory unless stringBEAN exists, proceed
	def sudo_mkdir(self, path):
		if not os.path.isdir(r_path):
			os.mkdir(r_path)
			print(f"Creating Directory: /opt/stringBEAN")
		elif os.path.isdir(r_path):
			return

	# check Documents directory for windows user
	def win_chkdir(self, chkpath):
		if not os.path.isdir(win_chkpath):
			print(f"stringBEAN needs a Documents directory in C:\\Users\\{user}")
			sys.exit(1)
		else:
			return

	# check stringBEAN existence mkdir stringBEAN, unless it exists then proceed
	def win_mkdir(self, path):
		if not os.path.isdir(path):
			os.mkdir(winpath)
			print(f"Creating Directory: C:\\Users\\{user}\\Documents\\stringBEAN")
		elif os.path.isdir(path):
			return

	# OS and root detection
	def chk_os(self):
		if os.name == 'nt':
			return 3
		elif os.name == 'posix':
			if getuser() == 'root':
				return 2
			else:
				return 1
		
		else:
			print("Incompatable OS. sorry...")
			sys.exit(1)

# This block is the final output.
class strgen(object):
	def __init__(self,choice=False, strlen=False, lstlen=False):
		self.strlen = strlen
		self.lstlen = lstlen

	# Our new and imporoved loader that actually doesnt load anything lol
	def loadr(self):
		for c in cycle([Fore.RED + Style.BRIGHT + 'Working...','w0rking...','woRking...', 'worKing...', 'workIng...', 'workiNg...', 'workinG...', 'working...', 'working...','working...']):
			if count == args.lstlen or '':
				break
			sys.stdout.write('\r' + c)
			sys.stdout.flush()
			sleep(0.3)
		if vl_ret == 1:
			sys.stdout.write('\r')
			print(Style.RESET_ALL)
		else:
			sys.stdout.write('\rDONE!            ')
			print(Style.RESET_ALL)
		
	# The reason I'm being repitive like this is because nesting functions
	# within functions, using return and arg tricks and the like does't beat
	# the performance of simpler code.
	# Final output for non-root user
	def spitrun(self):
		global count
		count = 0
		t = Thread(target=self.loadr)
		# -cn argument (which is the default)
		if args.chnmb and args.strlen < str_limit and args.lstlen < lst_limit:
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, charnumb)
				output = stringBEAN + "\n"
				with open(f"/home/{user}/Documents/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /home/{user}/Documents/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")

		# -n argument
		elif args.nmb and args.strlen < str_limit and args.lstlen < lst_limit:
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, numb)
				output = stringBEAN + "\n"
				with open(f"/home/{user}/Documents/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /home/{user}/Documents/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
			
		# -c argument
		elif args.chr and args.strlen < str_limit and args.lstlen < lst_limit:
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, char)
				output = stringBEAN + "\n"
				with open(f"/home/{user}/Documents/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /home/{user}/Documents/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
		
		# -s argument
		elif args.sp and args.strlen < str_limit and args.lstlen < lst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, spec)
				output = stringBEAN + "\n"
				with open(f"/home/{user}/Documents/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /home/{user}/Documents/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
		
		# -cs argument
		elif args.chS and args.strlen < str_limit and args.lstlen < lst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, c_spec)
				output = stringBEAN + "\n"
				with open(f"/home/{user}/Documents/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			banners.str_machine()
			print(f"OUTPUT: /home/{user}/Documents/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
		
		# -ns argument
		elif args.nmS and args.strlen < str_limit and args.lstlen < lst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				print(count)
				stringBEAN = random_string_generator(args.strlen, n_spec)
				output = stringBEAN + "\n"
				with open(f"/home/{user}/Documents/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /home/{user}/Documents/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
		
		# -cns argument
		elif args.cns and args.strlen < str_limit and args.lstlen < lst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, cn_spec)
				output = stringBEAN + "\n"
				with open(f"/home/{user}/Documents/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /home/{user}/Documents/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
			
		else:
			print("stringBEAN: EXCEEDED MAX LIMIT: string length: 100, lines/file: 500,000 \nQUITING!!!")

	# Final output for root user
	def sudo_spitrun(self):
		global count
		count = 0
		t = Thread(target=self.loadr)
		if args.chnmb and args.strlen < str_limit and args.lstlen < lst_limit:
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, charnumb)
				output = stringBEAN + "\n"
				with open(f"/opt/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /opt/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
			
		elif args.nmb and args.strlen < str_limit and args.lstlen < lst_limit:
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, numb)
				output = stringBEAN + "\n"
				with open(f"/opt/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /opt/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")

		elif args.chr and args.strlen < str_limit and args.lstlen < lst_limit:
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, char)
				output = stringBEAN + "\n"
				with open(f"/opt/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /opt/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")

		elif args.sp and args.strlen < str_limit and args.lstlen < lst_limit:
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, spec)
				output = stringBEAN + "\n"
				with open(f"/opt/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /opt/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
			
		elif args.chS and args.strlen < str_limit and args.lstlen < lst_limit:
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, c_spec)
				output = stringBEAN + "\n"
				with open(f"/opt/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /opt/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
			
		elif args.nmS and args.strlen < str_limit and args.lstlen < lst_limit:
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, n_spec)
				output = stringBEAN + "\n"
				with open(f"/opt/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /opt/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
			
		elif args.cns and args.strlen < str_limit and args.lstlen < lst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, cn_spec)
				output = stringBEAN + "\n"
				with open(f"/opt/stringBEAN/{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: /opt/stringBEAN/{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
			
		else:
			print("stringBEAN: EXCEEDED MAX LIMIT: string length: 100, lines/file: 500,000 \nQUITING!!!")

	# Final output for windows user
	def win_spitrun(self):
		from colorama import just_fix_windows_console
		just_fix_windows_console()
		print("\nWARNING: Windows python performance is drasticly slower than using linux")
		print("Just be mindful that anything above 5,000 lines will take a WHILE!\n")
		t = Thread(target=self.loadr)
		if args.chr and args.strlen < str_limit and args.lstlen < winlst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, char)
				output = stringBEAN + "\n"
				with open(f"C:\\Users\\{user}\\Documents\\stringBEAN\\{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: C:\\Users\\{user}\\stringBEAN\\{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")
			
		elif args.nmb and args.strlen < str_limit and args.lstlen < winlst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, numb)
				output = stringBEAN + "\n"
				with open(f"C:\\Users\\{user}\\Documents\\stringBEAN\\{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: C:\\Users\\{user}\\stringBEAN\\{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")

		elif args.sp and args.strlen < str_limit and args.lstlen < winlst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, spec)
				output = stringBEAN + "\n"
				with open(f"C:\\Users\\{user}\\Documents\\stringBEAN\\{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: C:\\Users\\{user}\\stringBEAN\\{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")

		elif args.chnmb and args.strlen < str_limit and args.lstlen < winlst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, charnumb)
				output = stringBEAN + "\n"
				with open(f"C:\\Users\\{user}\\Documents\\stringBEAN\\{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: C:\\Users\\{user}\\stringBEAN\\{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")

		elif args.chS and args.strlen < str_limit and args.lstlen < winlst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, c_spec)
				output = stringBEAN + "\n"
				with open(f"C:\\Users\\{user}\\Documents\\stringBEAN\\{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: C:\\Users\\{user}\\stringBEAN\\{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")

		elif args.nmS and args.strlen < str_limit and args.lstlen < winlst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, n_spec)
				output = stringBEAN + "\n"
				with open(f"C:\\Users\\{user}\\Documents\\stringBEAN\\{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: C:\\Users\\{user}\\stringBEAN\\{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")

		elif args.cns and args.strlen < str_limit and args.lstlen < winlst_limit:
			count = 0
			filename = input("name the file: ")
			t.start()
			while count != args.lstlen:
				stringBEAN = random_string_generator(args.strlen, cn_spec)
				output = stringBEAN + "\n"
				with open(f"C:\\Users\\{user}\\Documents\\stringBEAN\\{filename}.txt", "a+") as text_file:
					text_file.write(output)
				count += 1
			sleep(0.3)
			banners.str_machine()
			print(f"OUTPUT: C:\\Users\\{user}\\stringBEAN\\{filename}.txt with", args.strlen, "text length and", args.lstlen, "lines")

		else:
			print("\nstringBEAN: EXCEEDED MAX LIMIT: string length: 500, lines/file: 50,000 \nQUITING!!!")

if __name__ == '__main__':

	sB_ver = 0.7

	# Using argparse for argument designation
	# i was going to go with classic sys.argv but this makes it easier only thing I hate about it
	# is the forced help option. if you try to supress it our code could possibly break in
	# future argparse updates.
	AP = AP(prog="stringBEAN",
			description=f"stringBEAN v{sB_ver}: A simple R4nD0m string generator", 
            usage="stringBEAN [option] [integer] [integer] | run stringbean without -h for more info",
			epilog="ex: stringBEAN -cn 8 10000")
	
	#Arguments
	AP.add_argument("-c", help="Generate string(s) with Characters", action="store_true", default=False, dest="chr")
	AP.add_argument("-n", help="Generate string(s) with Numbers", action="store_true", default=False, dest="nmb")
	AP.add_argument("-s", help="Generate string(s) with Special Characters", action="store_true", default=False, dest="sp")
	AP.add_argument("-cn", help="Generate string(s) with Characters and Numbers", action="store_true", default=False, dest="chnmb")
	AP.add_argument("-cs", help="Generate string(s) with Numbers", action="store_true", default=False, dest="chS")
	AP.add_argument("-ns", help="Generate string(s) with Numbers", action="store_true", default=False, dest="nmS")
	AP.add_argument("-cns", help="Generate string(s) with Characters Numbers and Special Characters", action="store_true", default=False, dest="cns")
	AP.add_argument("strlen", metavar="2nd arg[integer]", help="String Length", type=int, default=0, nargs="?")
	AP.add_argument("lstlen", metavar="3rd arg[integer]", help="List Length/Lines", type=int, default=0, nargs="?")
	args = AP.parse_args()
	banners = banners()
	checkdir = checkdir()
	vl_ret = 0
	
	# If niether length and list integers or given display the help banner
	if not (args.strlen and args.lstlen):
		checkdir.chk_os()
		if checkdir.chk_os() != 3:
			Tfg = ''
			hex_a = ['\033[38:5:208m','\033[48;5;236m', '\033[38;5;72m','\033[0:0m']
			banners.help_sb()
			
		elif checkdir.chk_os() == 3:
			Tfg = Fore.RED + Style.BRIGHT
			hex_st = ['','','','']
			from colorama import just_fix_windows_console
			just_fix_windows_console()
			banners.help_sb()
		
	elif (args.strlen and args.lstlen) and not (args.chr or args.nmb or args.sp or args.chnmb or args.chS or args.nmS or args.cns): 
		print("\nstringBEAN: You need To specify an option first, then 2 integers silly!.")
		
	else:
		# Try running these functions (Described above)
		try:
			checkdir.chk_os()
			# Our exceptions are relying on return values if its 1 non-root, posix
			if checkdir.chk_os() == 1:
				checkdir.chkdir(chk_path)
				checkdir.mkdir(path)
				strgen = strgen(choice=args.chr or 
				args.nmb or 
				args.sp or 
				args.chnmb or 
				args.chS or 
				args.nmS or 
				args.cns, 
				strlen=args.strlen, 
				lstlen=args.lstlen)
				Tfg = ''
				hex_a = ['\033[38:5:208m','\033[48;5;236m', '\033[38;5;72m','\033[0:0m']
				strgen.spitrun()

			# if it's 2 root, posix
			elif checkdir.chk_os() == 2:
				checkdir.sudo_chkdir(r_chkpath)
				checkdir.sudo_mkdir(r_path)
				strgen = strgen(choice=args.chr or 
				args.nmb or 
				args.sp or 
				args.chnmb or 
				args.chS or 
				args.nmS or 
				args.cns, strlen=args.strlen, lstlen=args.lstlen)
				Tfg = ''
				hex_a = ['\033[38:5:208m','\033[48;5;236m','\033[38;5;72m','\033[0:0m']
				strgen.sudo_spitrun()

			# if it's 3 Windows
			elif checkdir.chk_os() == 3:
				from colorama import just_fix_windows_console
				just_fix_windows_console()
				checkdir.win_chkdir(win_chkpath)
				checkdir.win_mkdir(winpath)
				strgen = strgen(choice=args.chr or 
				args.nmb or 
				args.sp or 
				args.chnmb or 
				args.chS or 
				args.nmS or 
				args.cns, strlen=args.strlen, lstlen=args.lstlen)
				Tfg = Fore.RED + Style.BRIGHT
				hex_a = ['','','','']
				strgen.win_spitrun()

		except KeyboardInterrupt:
			args.lstlen = count
			vl_ret = 1
			print("\n\nQUITTING!")
			sys.exit(1)
		    
