# Password complexity checker
import re
from tkinter import *
from PIL import Image, ImageTk

class MyApp:
    def __init__(self,root):
        self.root=root
        
        # logo icon
        logo_image = Image.open("PRODIGY_CS_03/logo1.png")
        logo = ImageTk.PhotoImage(logo_image)
        root.iconphoto(True, logo)
        
        self.root.title("Password Complexity Checker")
        
        self.label1=Label(text="Password:" ,font="Morpheus 10")
        self.label1.grid(row=0,column=0,padx=30,pady=10)
        
        self.input_pass=Text(height=1,width=20,wrap=WORD)
        self.input_pass.grid(row=0,column=1,padx=30,pady=10)
        
        self.button=Button(text="check",bg="#57B763",font="Morpheus 10",command=self.button)
        self.button.grid(row=0,column=2,pady=30)
        
        with open("PRODIGY_CS_03\wordlist.txt",'r') as f:
            self.pass_list=f.read().splitlines()

    def calculate_combinations(self, password):
        length = len(password)
        char_set_size = 0
        
        if re.search(r'[A-Z]', password):
            char_set_size += 26
        if re.search(r'[a-z]', password):
            char_set_size += 26 
        if re.search(r'[0-9]', password):
            char_set_size += 10  
        if re.search(r'[~`!@#$%^&*()_\-+=}{[\]|;:/?.>,<]', password):
            char_set_size += 32 
        
        return char_set_size ** length

    def estimate_crack_time(self, password):
        attempts_per_second = 1e9 
        combinations = self.calculate_combinations(password)
        time_seconds = combinations / attempts_per_second
        
        return time_seconds

    def format_time(self, seconds):
        if seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.2f} minutes"
        elif seconds < 86400:
            hours = seconds / 3600
            return f"{hours:.2f} hours"
        elif seconds < 31536000: 
            days = seconds / 86400
            return f"{days:.2f} days"
        else:
            years = seconds / 31536000
            return f"{years:.2f} years"
    
    def check_strength(self):
        password = self.input_pass_content
        check_uppercase = re.search(r'[A-Z]', password) is not None
        check_lowercase = re.search(r'[a-z]', password) is not None
        check_number = re.search(r'[0-9]', password) is not None
        check_character = re.search(r'[~`!@#$%^&*()_\-+=}{[\]|;:/?.>,<]', password) is not None
        
        # approx value because passwd is in wordlist
        if password in self.pass_list:
            return "Few minutes"

        time_to_crack = self.estimate_crack_time(password)
        formatted_time_to_crack = self.format_time(time_to_crack)
        # print(formatted_time_to_crack)
        return formatted_time_to_crack
        
    def button(self):
        self.input_pass_content = self.input_pass.get("1.0", END).strip()
        formatted_time_to_crack = self.check_strength()
        
        # time to crack
        self.label2 = Label(text="Time to crack:", font="Morpheus 10")
        self.label2.grid(row=2,column=0,padx=30,pady=20)
        
        self.label3 = Text(height=2, width=20, font="Morpheus 10")
        self.label3.insert(END,formatted_time_to_crack)
        self.label3.grid(row=2,column=1,padx=30,pady=20)
        
        # password's level
        self.label4 = Label(text="Level:", font="Morpheus 10")
        self.label4.grid(row=3,column=0,padx=30,pady=20)
        
        self.label5 = Text(height=2, width=20, font="Morpheus 10")
        self.label5.insert(END,"Very Weak" if "seconds" in self.check_strength() else ("Weak" if "minutes" in self.check_strength() else("Medium" if "hours" in self.check_strength() else("Strong" if "days" in self.check_strength() else "Out of the world"))))
        self.label5.grid(row=3,column=1,padx=20,pady=20)
        

if __name__=="__main__":
    root=Tk()
    root.minsize(500,400)
    root.maxsize(500,400)
    app=MyApp(root)
    root.mainloop()
