# Encrypt Or Decrypt Caesar Cipher Text

from tkinter import *
from PIL import Image,ImageTk

class Myapp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encrypt or Decrypt Caesar Cipher")
        
        # logo icon
        logo_image = Image.open("PRODIGY_CS_01\logo1.png")
        logo = ImageTk.PhotoImage(logo_image)
        root.iconphoto(True, logo)
        
        frame = Frame(root)
        frame.pack(padx=20, pady=20)
        
        self.l = Label(frame, text="Text:", font="Morpheus 10 ")
        self.l.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        
        # input text
        self.input_text = Text(frame, height=5, width=50, wrap=WORD)
        self.input_text.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        
        self.s = Label(frame, text="Shift Value:", font="Morpheus 10 ")
        self.s.grid(row=1, column=0, sticky=W, padx=10, pady=10)
        
        # input shift value
        self.input_shift_value = Text(frame, height=1, width=10)  
        self.input_shift_value.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        
        self.l2 = Label(frame, text="Output:", font="Morpheus 10 ")
        self.l2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
        
        # output value
        self.output_text = Text(frame, height=5, width=50, wrap=WORD)
        self.output_text.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        
        # encrypt button
        self.encrypt = Button(frame, text="Encrypt", fg="black", bg="#57B763", relief=SUNKEN, command=self.do_encryption)
        self.encrypt.grid(row=3, column=0, padx=30, pady=90, sticky=W)
        
        # decrypt button
        self.decrypt = Button(frame, text="Decrypt", fg="black", bg="#57B763", relief=SUNKEN, command=self.do_decryption)
        self.decrypt.grid(row=3, column=1, padx=30, pady=90, sticky=E)
    
    def caesar_cipher(self, text, shift, mode='encrypt'):
        result = ""
        for char in text:
            if char.isalpha():
                shift_amount = shift if mode == 'encrypt' else -shift
                start = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
            else:
                result += char
        return result
    
    # encryption fcuntion
    def do_encryption(self):
        input_text_content = self.input_text.get("1.0", END).strip()
        shift_value = self.input_shift_value.get("1.0", END).strip()
        
        try:
            shift_value = int(shift_value)
        except ValueError:
            self.output_text.delete("1.0", END)
            self.output_text.insert(END, "Invalid shift value")
            return
        
        encrypted_text = self.caesar_cipher(input_text_content, shift_value, mode='encrypt')
        self.output_text.delete("1.0", END)
        self.output_text.insert(END, encrypted_text)
        
    # decryption function
    def do_decryption(self):
        input_text_content = self.input_text.get("1.0", END).strip()
        shift_value = self.input_shift_value.get("1.0", END).strip()
        
        try:
            shift_value = int(shift_value)
        except ValueError:
            self.output_text.delete("1.0", END)
            self.output_text.insert(END, "Invalid shift value")
            return
        
        decrypted_text = self.caesar_cipher(input_text_content, shift_value, mode='decrypt')
        self.output_text.delete("1.0", END)
        self.output_text.insert(END, decrypted_text)

if __name__ == "__main__":
    root = Tk()
    root.minsize(500, 500)
    root.maxsize(800, 600)
    app = Myapp(root)
    root.mainloop()
    print("Exit")
