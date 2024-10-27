from tkinter import *
from tkinter import filedialog
from tkinter import messagebox 
import tkinter.font as tkFont



from PIL import Image

def vigenere(text: str, key: str, encrypt=True):

    result = ''

    for i in range(len(text)):
        letter_n = ord(text[i])
        key_n = ord(key[i % len(key)])

        if encrypt:
            value = (letter_n + key_n) % 1114112
        else:
            value = (letter_n - key_n) % 1114112

        result += chr(value)

    return result
    

def cipher(text,key):
    return vigenere(text=text, key=key, encrypt=True)


def decipher(text,key):
    return vigenere(text=text, key=key, encrypt=False)


def encrypt(m,pa):
    org_img = Image.open(pa)

    # Loading pixel values of original image, each entry is pixel value ie., RGB values as sublist
    org_pixelMap = org_img.load()

    # Creating new image object with image mode and dimensions as that of original image
    enc_img = Image.new( org_img.mode, org_img.size)
    enc_pixelsMap = enc_img.load()

    # Reading message to be encrypted from user
    msg=m
    msg_index=0

    # Finding the lenght of message
    msg_len=len(msg)

    # Traversing through the pixel values
    for row in range(org_img.size[0]):
        for col in range(org_img.size[1]):

            # Fetching RGB value a pixel to sublist
            list=org_pixelMap[row,col] 
            r=list[0] 	# R value
            g=list[1]	# G value
            b=list[2]	# B value
          
            if row==0 and col==0:		# 1st pixel is used to store the lenght of message
                ascii=msg_len
                enc_pixelsMap[row,col] = (ascii,g,b)
            elif msg_index<=msg_len:	# Hiding our message inside the R values of the pixels
                c=msg[msg_index-1]
                ascii=ord(c)
                enc_pixelsMap[row,col] = (ascii,g,b)
            else:				# Assigning the pixel values of old image to new image
                enc_pixelsMap[row,col] = (r,g,b)
            msg_index+=1
    org_img.close()

    # Display the image
    enc_img.show()  

    # Save the image        
    enc_img.save("encrypted_image.png") 
    enc_img.close()

def decrypt(k):
    enc_img = Image.open(k)

    # Loading pixel values of original image, each entry is pixel value ie., RGB values as sublist
    enc_pixelMap = enc_img.load()


    # Creating an empty String for our hidden message
    msg = ""
    msg_index = 0 


    # Traversing through the pixel values
    for row in range(enc_img.size[0]):
        for col in range(enc_img.size[1]):

            # Fetching RGB value a pixel to sublist
            list = enc_pixelMap[row,col]
            r = list[0]	# R value

            if col==0 and row==0:		# 1st pixel was used to store the length of message
                msg_len = r
                
            elif msg_len>msg_index:		# Reading the message from R value of pixel
                msg =msg+ chr(r)		# Converting to character
                msg_index = msg_index+1

    enc_img.close()

    return msg


###########################################################################################################

# create root window
r = Tk()


# root window title and dimension
r.title("Kryptos")
# Set geometry (widthxheight)34!!~
#r.geometry('350x200')2342`


default_font = tkFont.nametofont( "TkDefaultFont")
default_font.configure(size=32)



def e1():
     
    # Toplevel object which will 
    # be treated as a new window
    nw1 = Toplevel(r)
    #nw1.geometry('350x400')
    # sets the title of the
    # Toplevel widget
    nw1.title("Encrypt")

    i1 = Text(nw1, height=3, width=30, font=("Helvetica", 32))
    i1.pack(pady=20)
    i2 = Text(nw1, height=2, width=15, font=("Helvetica", 32))
    i2.pack(pady=20)
    

    def n():
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File",filetypes = (("Image files","*.jpg*"),("all files","*.*")))
        m = i1.get(1.0, "end-1c")
        p = i2.get(1.0, "end-1c")
        x = cipher(m, p)
        encrypt(x,filename)
    

        

    btn2 = Button(nw1, text ="Encrypt!", command=n).pack(pady=20)    
 
    # sets the geometry of toplevel
        

def e2():
     
    # Toplevel object which will 
    # be treated as a new window
    nw2 = Toplevel(r)
    #nw2.geometry('350x200')
 
    # sets the title of the
    # Toplevel widget
    nw2.title("Decrypt")


    i3 = Text(nw2, height=2, width=15, font=("Helvetica", 32))
    i3.pack(pady=20)

    def f1():
        filename1 = filedialog.askopenfilename(initialdir = "/", title = "Select a File",filetypes = (("Image files","*.png*"),("all files","*.*")))
        y = decrypt(filename1)
        g = i3.get(1.0, "end-1c")
        m = decipher(y,g)
        #messagebox.showinfo("Message", m)
        label = Label(nw2, text=m).pack(pady=20)
        

        

    btn21 = Button(nw2, text ="Decrypt!", command=f1).pack(pady=20)
 
    # sets the geometry of toplevel
    #nw2.geometry("200x200")
 


btn = Button(r, text ="Encrypt", command=e1).pack(pady=20, padx=20)
btn1 = Button(r, text ="Decrypt", command=e2).pack(pady=20, padx=20)

# all widgets will be here
# Execute Tkinter
r.mainloop()
