from colorama import Fore

def help():
    print(Fore.YELLOW + """
Thank you for using Py Percentage.
----------------------------------
Commands:

percent({number}, {total})""", end='')
    print(Fore.MAGENTA + """--> Get equivalent of a vlue in percentage (%)""")
    print(Fore.YELLOW + """
value({total}, {percentage})""", end='')
    print(Fore.MAGENTA + """--> Get the value of a certain percentage or find total from value and it's percentage equivalent""")
    
    print(Fore.YELLOW + """
Example:
    percent(24, 100)
    
    value(129, 20)
    
    value(38, 100)
    
>>> 24.0%
>>> 645.0
>>> 38.0""")
    
    print(Fore.WHITE, end='')

def percent(x, y):
    print(str((x/y)*100)+'%') #Get value in percentage

def value(x, y):
    print((x/y)*100) #Get get value of certain percentage
