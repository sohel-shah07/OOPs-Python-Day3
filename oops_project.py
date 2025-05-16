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
            self.signup()
        elif self.user_input == '2':
            self.signin()
        elif self.user_input == '3':
            pass
        elif self.user_input == '4':
            pass
        else:
            exit()
            
    def signup(self):
        email = input("Enter your email: ")
        password = input("Setup your password: ")
        self.username = email
        self.password = password
        print('You have successfully signed up!')
        print('\n')
        self.menu()     
        
    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1")
        else :
            username = input("Enter your email: ")
            password = input("Enter your password: ")
            
            if self.username == username and self.password == password:
                print("You have successfully signed in!")
                self.logged_in = True
            else :
                print("Please input correct credentials")
        
        print('\n')
        self.menu()
    
            
obj = Chatbook()
