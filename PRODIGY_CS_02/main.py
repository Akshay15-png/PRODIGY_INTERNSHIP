# Encrypt or Decrypt Image 

from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk

class Myapp:
    def __init__(self,root):
        try:
            self.root=root
            self.root.title("Encrypt Image")
            
            self.label1=Label(text="Image: ",font="Morpheus 10")
            self.label1.grid(row=0 , column=0,padx=30 , pady=10,sticky='e')
            self.choose_button=Button(text="choose file",command=self.show_image,font="Morpheus 10")
            self.choose_button.grid(row=0 , column=1, pady=10,sticky='w')
        except Exception as e:
            print(f"Something Wrong: {e}")
    
    
    def show_image(self):
        self.image_path=filedialog.askopenfilename(filetypes=[("Image files","*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if self.image_path:
            try:
                self.get_image=Image.open(self.image_path)
                self.get_image = self.get_image.resize((100, 100))
                self.img=ImageTk.PhotoImage(self.get_image)
                
                self.your_img_label=Label(text="Your Image:")
                self.your_img_label.grid(row=1, column=0,padx=20,pady=20)
                self.img_label=Label(image=self.img)
                self.img_label.grid(row=1, column=1,padx=20,pady=20)

            except Exception as e:
                print(f"Error loading image: {e}")

                
if __name__ == "__main__":
    root=Tk()
    root.minsize(400,400)
    root.maxsize(500,500)
    app=Myapp(root)
    root.mainloop()