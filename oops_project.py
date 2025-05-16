class Chatbook():
    def __init__(self):
        self.username = ''
        self.password = ''
        self.logged_in = False
        self.menu()
        
        
    def menu(self):
        self.user_input = input("""Welcomt to Chatbook! How would you like to proceed?
                                1. Press 1 to singup
                                2. Press 2 to singin
                                3. Press 3 to write a post
                                4. Press 4 to message a friend
                                5. Press any other key to exit \n""")
        if self.user_input == '1':
            pass
        elif self.user_input == '2':
            pass
        elif self.user_input == '3':
            pass
        elif self.user_input == '4':
            pass
        else:
            exit()
            
obj = Chatbook()
