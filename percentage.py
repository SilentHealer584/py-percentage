class color:
    MAGENTA = "\033[35m"
    YELLOW = "\033[93m"
    WHITE = "\033[37m"
    STOP = "\033[0m"

def help() -> None:
    print(color.YELLOW + """
Thank you for using Py Percentage.
----------------------------------
Commands:

percent({number}, {total})""", end='')
    print(color.MAGENTA + """--> Get equivalent of a vlue in percentage (%)""")
    print(color.YELLOW + """
value({total}, {percentage})""", end='')
    print(color.MAGENTA + """--> Get the value of a certain percentage or find total from value and it's percentage equivalent""")
    
    print(color.YELLOW + """
Example:
    print(percent(24, 100))
    
    print(value(129, 20))
    
    print(value(38, 100))
    
>>> 24.0%
>>> 645.0
>>> 38.0""")
    print(color.STOP, end='')
    return

def percent(x, y) -> str:
    return f"{(x/y)*100}%" #Get value in percentage

def value(x, y) -> float:
    return (x/y)*100 #Get get value of certain percentage
