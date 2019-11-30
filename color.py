# color.py
# --------------------
# Set of functions to colored the ouptut on a shell
#
# Author: Maxime Bourguignon
# Date: 2019-11-29
# --------------------

c_style = {
    "normal" : 0,
    "bold" : 1,
    "italic" : 4
    }

c_fg = {
    "black" : 30,
    "red" : 31,
    "green" : 32,
    "yellow" : 33,
    "blue" : 34,
    "white" : 37
    }

c_bg = {
    "black" : 40,
    "red" : 41,
    "green" : 42,
    "yellow" : 43,
    "blue"  : 44,
    "white" : 47
    }

def colored( msg, fg="white", style="normal", bg="black" ):
    print_format = ';'.join([ str( c_style[ style ]), str( c_fg[ fg ]), str( c_bg[ bg ])])
    return "\x1b[{}m{}\x1b[0m".format( print_format, msg )

def colored_command( msg ):
    return colored( msg, "blue", "bold" )

def colored_error( msg ):
    return colored( msg, "red", "bold" )
