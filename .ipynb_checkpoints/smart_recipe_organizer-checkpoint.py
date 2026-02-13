import re 
import secrets
import os

# ABSTRACT CLASS
from abc import ABC , abstractmethod
class Display(ABC):
    @abstractmethod
    def display_recipe(self,file_name,recipe_id):
        pass
        
# AUTHENTICATION

class Auth:
    def check_email(self,email):
        if not email.endswith(('@gmail.com','@yahoo.com')):
            return False,"Invalid email , enter valid email"
        else:
            return True,"Email successfully checked"
    def check_password(self,password):
        if ' ' in password:
            return False,"Space are not allowed in password"
        elif len(password) < 6:
            return False,"Password length should be greater than 6"
        elif not re.search(r"\d",password):
            return False,"Password should include alteast one digit"
        elif not re.search(r"[a-z]",password):
            return False,"Password should include atleast one lower case letter"
        elif not re.search(r"[A-Z]",password):
            return False,"Password should include atleast one upper case letter"
        elif not re.search(r"[!@#$$%^&*()_]",password):
            return False,"Password should include atleast one special character"
        else:
            return True , "Strong Password"

# USER INFO

class User:
    def __init__(self,name,email,password,user_id=None):
        self.name = name
        self.email = email
        self.password = password
        self.user_id = user_id
    def saveUser(self):
        userName = self.name.strip().lower()
        secret_id = secrets.token_hex(3)
        userId = f"{userName}_{secret_id}"
        self.user_id = userId
        print(f"Your user id is {self.user_id}")
        userDataList={
            "user_id" : self.user_id,
            "email":self.email,
            "name":self.name,
            "password":self.password
        }
        with open("userData.txt","a") as f:
            line = f"{userDataList['user_id']}|{userDataList['email']}|{userDataList['name']}|{userDataList['password']}\n"
            f.write(line)
        print("--------------------------------")
        print("User successfully saved")
        print("--------------------------------")

# USER RECIPE

class UserRecipe:
    def __init__(self,userId):
        self.userId = userId
            
    def createRecipe(self):
        title = input("Enter the name of the recipe: ")
        ingredients = input("Enter the ingredients used in recipe: ")
        description = input("Enter full detail of the recipe: ")
        category = input("Enter its category: ")

        recipe = {
            "id" : self.userId,
            "title":  title,
             "ingredients": ingredients,
              "description": description,
              "category" : category
        }
        with open("userRecipes.txt","a") as f:
            line = f"{recipe['id']}|{recipe['title']}|{recipe['ingredients']}|{recipe['description']}|{recipe['category']}\n"
            f.write(line)
        print("--------------------------------")
        print("Recipe added successfully")
        print("--------------------------------")


# DISPLAY RECIPE
class DisplayRecipe(Display):
    def __init__(self,file_name,id):
        self.file_name = file_name
        self.id = id
    def display_recipe(self):
        found = False
        if not os.path.exists(self.file_name):
            with open(self.file_name,"w"):
                pass
                       
        with open(self.file_name,"r") as f:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            for line in f:
                data = line.strip().split("|")
                if data[0] == self.id:
                    print(f"Title: {data[1]} ")
                    print(f"Ingredients:  {data[2]} ")
                    print(f"Description:    {data[3]} ")
                    print(f"Category: {data[4]} ")
                    print('\n')
                    found = True
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print('\n')
        if not found:
            print("--------------------------------")
            print("No recipes found for this user.")
            print("--------------------------------")


# RECIPE SUGGESTION
class RecipeSuggestion():
    def suggestRecipes(self):
        while True:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("Which type of recipe you want")
            print("1. Breakfast")
            print("2. Lunch ")
            print("3. Dinner")
            print("4. Midnight cravings")
            print("5. Exit")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    self.breakfastChoice()
                case 2:
                    self.lunchChoice()
                case 3:
                    self.dinnerChoice()
                case 4:
                    self.cravingChoice()
                case 5:
                    print("---------------------")
                    print("successfully exited...")
                    print("---------------------")
                    return
                   
                case _:
                    print("Invalid choice")
                
    def breakfastChoice(self):
        while True:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("Breakfast menu: ")
            print("1. Aloo Paratha")
            print("2. Masala Dosa")
            print("3. Poha ")
            print("4. Vegetable Upma ")
            print("5. Oats Porridge")
            print("6. Exit")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            choice = int(input("Enter your choice which recipe you want: "))
            file_name = "breakfast.txt"
            match choice:
                case 1:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 2:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                    
                case 3:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 4:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 5:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 6:
                    print("---------------------")
                    print("exit successfully")
                    print("---------------------")
                    break
                case _:
                    print("Invalid choice")
    def lunchChoice(self):
        while True:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("Lunch  menu: ")
            print("1. Veg Biryan")
            print("2. Rajma Chawal")
            print("3. Paneer Butter Masala with Naan ")
            print("4. Dal Tadka with Jeera Rice ")
            print("5. Chole Bhature")
            print("6. Exit")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            choice = int(input("Enter your choice which recipe you want: "))
            file_name = "lunch.txt"
            match choice:
                case 1:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 2:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                    
                case 3:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 4:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 5:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 6:
                    print("---------------------")
                    print("exit successfully")
                    print("---------------------")
                    break
                case _:
                    print("Invalid choice")
    def dinnerChoice(self):
        while True:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("Dinner menu: ")
            print("1. Veg Pulao with Raita")
            print("2. Palak Paneer with Roti")
            print("3. Vegetable Khichdi")
            print("4. Matar Paneer with Jeera Rice ")
            print("5. Veg Hakka Noodles")
            print("6. Exit")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            choice = int(input("Enter your choice which recipe you want: "))
            file_name = "dinner.txt"
            match choice:
                case 1:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 2:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                    
                case 3:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 4:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 5:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 6:
                    print("---------------------")
                    print("exit successfully")
                    print("---------------------")
                    break
                case _:
                    print("Invalid choice")
    def cravingChoice(self):
        while True:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("Midnight craving menu: ")
            print("1. Maggi Masala Noodles")
            print("2. Cheese Grilled Sandwich")
            print("3. French Fries with Dip")
            print("4. Chocolate Brownie ")
            print("5. Cold Coffee")
            print("6. Exit")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            choice = int(input("Enter your choice which recipe you want: "))
            file_name = "midnight.txt"
            match choice:
                case 1:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                   
                case 2:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                    
                case 3:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 4:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 5:
                    r1 = DisplayRecipe(file_name,str(choice))
                    r1.display_recipe()
                case 6:
                    print("---------------------")
                    print("exit successfully")
                    print("---------------------")
                    break
                case _:
                    print("Invalid choice") 

# RECIPE APP MAIN CLASS

class RecipeApp:
    def __init__(self):
        pass
    def menu(self):
        self.auth = Auth()
        print("\t**************************************")
        print("\t\tSMART RECIPE ORGANIZER")
        print("\t**************************************")
        while True:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("WELCOME TO OUR RECIPE PAGE")
            print("Here we provide the best recipes")
            print("You can also create your own recipe")
            print("ENJOY...")
            print("Choose the option below which service you want ")
            print("1. Create an account")
            print("2. Login to existing account")
            print("3. Exit")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print('\n')
            choice = int(input("Enter any choice from above: "))
            match choice:
                case 1:
                    name = input("Enter your name: ")
                    max_attempts = 3
                    attempt = 0
                    while True:
                        userEmail = input("Enter your email id: ")
                        found = False
                        if not os.path.exists("userData.txt"):
                            with open("userData.txt","w"):
                                pass                            
                          
                        with open("userData.txt","r") as f:
                            for line in f:
                                data = line.strip().split("|")
                                email = data[1]
                                if userEmail == email:
                                    print("Account already exist please sign in")
                                    found = True
                                    break
                                    
                        if not found: 
                            emailStatus,emailMsg = self.auth.check_email(userEmail)
                            if emailStatus:
                                print("----------------------------------")
                                print(emailMsg)
                                print("----------------------------------")
                                break
                            else:
                                if attempt == max_attempts:
                                    print("----------------------------------")
                                    print("Too many attempts try again later")
                                    print("----------------------------------")
                                    return
                                    
                                attempt +=1
                                print(emailMsg)
                    while True:
                        password = input("Enter password: ")
                        passwordStatus,passwordMsg = self.auth.check_password(password)
                        if passwordStatus:
                            print(passwordMsg)
                            user1 = User(name,userEmail,password)
                            user1.saveUser()
                            break
                        else:
                            print("----------------------------------")
                            print(passwordMsg)
                            print("----------------------------------")
                            
                case 2:
                    inputUserId = input("Enter your user id: ")
                    inputPassword = input("Enter password: ")
                    found = False
                    if not os.path.exists("userData.txt"):
                        with open("userData.txt","w"):
                            pass
                    with open("userData.txt","r") as f:
                        for line in f:
                            data = line.strip().split("|")
                            userId,password = data[0],data[3]
                            if inputUserId == userId and  inputPassword == password:
                                print("----------------------------------")
                                print("Login successfully")
                                print("----------------------------------")
                                found = True
                                break
                    if not found:
                        print("Invalid user Id or password")
                        return
               
                    while True:
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        print("Choose the below options")
                        print("1. Create Your own recipes")
                        print("2. Suggest Recipes")
                        print("3. Your Recipes")
                        print("4. Exit")
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        print('\n')
                        choice = int(input("Enter Your choice: "))
                        match choice:
                            case 1:
                                userRecipe = UserRecipe(userId)
                                userRecipe.createRecipe()
                                
                            case 2:
                                recipe = RecipeSuggestion()
                                recipe.suggestRecipes()
                            case 3:
                                try:
                                    r1 = DisplayRecipe("userRecipes.txt",inputUserId)
                                    r1.display_recipe()
                                                                       
                                except:
                                    print("----------------------------------")
                                    print("No recipes created")
                                    print("----------------------------------")
                            
                                
                            case 4:
                                print("---------------------")
                                print("Exit successfully")
                                print("---------------------")
                                return
                            case _:
                                print("Invalid choice choose wisely")
                case 3:
                    print("----------------------------------")
                    print("Exit successfully...")
                    print("----------------------------------")
                    break
                    
                case _:
                    print("Invalid choice ")
                
        
    
        
                
                                        



