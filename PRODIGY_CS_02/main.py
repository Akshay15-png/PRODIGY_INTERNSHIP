# Encrypt or Decrypt Image

from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import os
import random

class MyApp:
    def __init__(self, root):
        try:
            self.root = root
            self.root.title("Encrypt or Decrypt Image")
            
             # logo icon
            logo_image = Image.open("PRODIGY_CS_02\logo1.png")
            logo = ImageTk.PhotoImage(logo_image)
            root.iconphoto(True, logo)

            # choose file
            self.label1 = Label(text="Image: ", font="Morpheus 10")
            self.label1.grid(row=0, column=0, padx=30, pady=10, sticky='w')
            self.choose_button = Button(text="Choose File", command=self.show_image, font="Morpheus 10")
            self.choose_button.grid(row=0, column=1, pady=10, sticky='w')

            # choose directory to store encrypted file 
            self.label2 = Label(text="Save File:", font="Morpheus 10")
            self.label2.grid(row=2, column=0, padx=30, pady=10, sticky="w")
            self.choose_button2 = Button(text="Location", font="Morpheus 10", command=self.store_location)
            self.choose_button2.grid(row=2, column=1, pady=10, sticky="w")

            # buttons for encryption and decryption
            self.encrypt_button = Button(text="Encrypt", font="Morpheus 10", bg="#57B763", command=self.encrypt_image)
            self.encrypt_button.grid(row=3, column=0, padx=30, pady=10, sticky="w")
            self.decrypt_button = Button(text="Decrypt", font="Morpheus 10", bg="#57B763", command=self.decrypt_image)
            self.decrypt_button.grid(row=3, column=2, padx=30, pady=10, sticky="e")

            # variables to store image path and location
            self.image_path = None
            self.location_path = None

        except Exception as e:
            print(f"Something Wrong: {e}")

    def show_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if self.image_path:
            try:
                self.get_image = Image.open(self.image_path)
                self.get_image2 = self.get_image.resize((200, 200))
                self.img = ImageTk.PhotoImage(self.get_image)
                self.img2 = ImageTk.PhotoImage(self.get_image2)

                self.your_img_label = Label(text="Your Image:", font="Morpheus 10")
                self.your_img_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
                self.img_label = Label(image=self.img2)
                self.img_label.grid(row=1, column=1, padx=20, pady=20, sticky="w")

            except Exception as e:
                print(f"Error loading image: {e}")

    def store_location(self):
        self.location_path = filedialog.askdirectory()
        if self.location_path and self.image_path:
            try:
                # create new filename as original filename
                original_filename = os.path.basename(self.image_path)
                new_filename = f"encrypted_{original_filename}"  # filename
                self.full_save_path = os.path.join(self.location_path, new_filename)  #  filename path

            except Exception as e:
                print(f"Saved location is not set. {e}")

    def encrypt_image(self):
        if not hasattr(self, 'get_image'):
            print("Select an image for encryption")
            return

        pixels = self.get_image.load()
        width, height = self.get_image.size
        
        random.seed(12345)
        for _ in range(width * height * 5): 
            x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
            x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
            pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

        encrypted_image_path = self.full_save_path
        self.get_image.save(encrypted_image_path)
        self.save_to_label= Label(text=f"Encrypted image saved to: {encrypted_image_path}",font="Morpheus 10")
        self.save_to_label.grid(row=4, column=1, pady=10, sticky="w")
        

    def decrypt_image(self):
        if not hasattr(self, 'get_image'):
            print("Select an image for decryption.")
            return

        pixels = self.get_image.load()
        width, height = self.get_image.size

        random.seed(12345)  
        swaps = []
        for _ in range(width * height * 5):
            x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
            x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
            swaps.append((x1, y1, x2, y2))

        for x1, y1, x2, y2 in reversed(swaps):  
            pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
            
        decrypted_image_path = self.location_path + "/decrypted_image.png"
        self.get_image.save(decrypted_image_path)
        self.save_to_label= Label(text=f"Decrypted image saved to: {decrypted_image_path}",font="Morpheus 10")
        self.save_to_label.grid(row=4, column=1, pady=10, sticky="w")

if __name__ == "__main__":
    root = Tk()
    root.minsize(500, 400)
    app = MyApp(root)
    root.mainloop()
