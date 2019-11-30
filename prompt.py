# prompt.py
# --------------------
# Class for an interactive prompt
# --------------------
# this class is a "library" to create interactive prompt dynamicly
# and more easily.
#
# Author: Maxime Bourguignon
# Date: 2019-11-29
# --------------------

from sys import exit
from .color import colored_command, colored_error

class Prompt():

    def __init__( self, name="Prompt Application", query="Input > ", debug=False ):
        self.settings = dict()
        self.database = dict()
        self.running = True

        self.set( "app_name", name )
        self.set( "query", query )
        self.set( "debug", debug )

        self.addApp( "help", self.__helpMenu, "Print help list" )
        self.addApp( "exit", self.__exitMenu, "Exit the prompt" )
        if debug:
            self.addApp( "setting", self.__settingMenu, "Show setting list" )

    # Methods to configure the internal behaviour

    def addApp( self, call, app, explanation ):
        self.database[call] = { "app": app, "help": explanation }

    def set( self, name_setting, value ):
        self.settings[name_setting] = str(value)

    # Usefull applications for a prompt

    def __helpMenu( self, args ):
        print( "Help list\n{:-<20}".format(""))
        for key in sorted( self.database.keys()):
            print( "{cmd:<34} {msg}".format( cmd=colored_command( key ), msg=self.database[key]["help"] ))

    def __settingMenu( self, args ):
        print( "Setting list\n{:-<20}".format(""))
        for key in sorted( self.settings.keys()):
            print( "{cmd:<34} {msg}".format( cmd=colored_command( key ), msg=self.settings[key] ))

    def __exitMenu( self, args ):
        self.running = False

    # Methods for the prompt routine

    def __execute( self, call ):
        call = call.split()
        if call[0] in self.database.keys():
            return self.database[call[0]]["app"]( call[1:] )
        else:
            print( colored_error( "Command not supported" ) + ", please execute command " + colored_command( "help" ) + " to see the help menu" )
            return False

    def __startup ( self ):
        print( self.settings["app_name"] + "\n" )
        print( "execute command " + colored_command( "help" ) + " to see the help menu\n{:-<20}".format(""))

    def __exit( self ):
        print( "Goodbye" )
        exit()

    def run( self ):
        self.__startup()
        while self.running:
            text = input( self.settings["query"] )
            self.__execute( text )
        self.__exit()
