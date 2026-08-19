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
                           5. Press any other key to exit \n
                           """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
            
    def signup(self):
        email = input("Enter your email here: ")
        password = input("Setup your password here: ")
        
        self.username = email
        self.password = password
        
        print("\nYou have signed up successfully")
        print("\n")
        
        # now calling menu() method
        self.menu()
        
    def signin(self):
        if self.username == "" and self.password == "":
            print("Please , Signup first by Pressing 1.")
            
        else:
            check_user = input("Enter your username")
            check_pass = input("Enter you password")
            
            if check_user == self.username and check_pass == self.password:
                print("You have successfully signed up")
                self.loggedin = True
            else:
                print("Please enter correct credentials")
                
        print("\n")
        self.menu()
        
        
obj = chatbook()
        
        
            
    