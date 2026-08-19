class chatbook:
    def __init__(self): # this is called dunder method  , also called constructor
        self.username = ""  # this is called attributes  , we create 3 attributes
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):   # this is called method 
        user_input = input("""how would do you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message to friend
                           5. Press any other key to exit
                           """)
        
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
        
        
obj = chatbook()
        
        
            
    