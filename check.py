# check.py
# --------------------
# Set of decorators to check inputs of the shell
#
# Author: Maxime Bourguignon
# Date: 2019-11-29
# --------------------

from .color import colored_error

def check_length( length ):
    def decorator ( func ):
        def wrapper ( args ):
            if len( args ) == length:
                return func( args )
            else:
                print( colored_error( "arguments not correct" ) + ", we expecting " + str(length) + " args" )
                return False
        return wrapper
    return decorator

def check_int( func ):
    def wrapper( args ):
        try:
            args = [ int( arg ) for arg in args ]
        except Exception as e:
            print( colored_error( "arguments not correct" ) + ", we excpecting int\n" + str( e ))
            return False
        return func( args )
    return wrapper
