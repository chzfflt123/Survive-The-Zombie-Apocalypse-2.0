import tkinter

from start_page import StartPage
from how_to_play import How_To_Play
from bg_info_screen import BackgroundInfo

class Main (object):
    def __init__ (self):
        self.root = tkinter.Tk()
        self.current_screen = None
    
    def setup_start_page (self):
        '''
        This method is called to set up the Character Selection screen. 
        This also initializes the character_roster property.
        '''
        # Changes the window's title
        self.root.title ("Start")
        # Creates and displays a Character Selection screen
        self.current_screen = StartPage(master = self.root)
               
    def onclose_character_selection (self, selected_char_index):
        # Destroys the Character Selection window
        self.current_screen.destroy()

        # Continue on - set up the Prepare To Battle screen!
        self.setup_how_to_play()

    def setup_how_to_play(self):
        ''' This method is called to set up the Prepare To Battle screen. '''

        # Changes the window's title
        self.root.title ("How to Play")

        # Creates and displays a Prepare To Battle screen
        self.current_screen = How_To_Play(master = self.root, callback_on_commence_battle = self.onclose_how_to_play)
    
    def onclose_how_to_play (self):
        ''' 
        This method is called when the user presses the button on the Prepare to Battle screen.
        The method closes the Prepare To Battle screen and creates the Battle screen.
        '''
        # Destroys the Prepare To Battle screen
        self.current_screen.destroy()

        # Continue on - set up the Battle screen!
        self.setup_bg_info_screen()


    def setup_bg_info_screen(self):
        ''' This method is called to set up the Battle screen. '''
        # Changes the window's title
        self.root.title ("Background Info")

        # Creates and displays a Battle screen
        self.current_screen = BackgroundInfo(master= self.root,  callback_on_exit = self.onclose_bg_info_screen)

    def onclose_bg_info_screen (self):
        # Destroy the entire program's window, which includes the Battle screen.
        self.root.destroy()
        
def main():
    # Create the battle manager, which creates the tkinter window.
    main = Main()
    # The program begins with the Character Selection screen!
    main.setup_character_selection()
    # Run the program!
    main.root.mainloop()
 
main()
    