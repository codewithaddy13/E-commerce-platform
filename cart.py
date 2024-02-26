from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import customtkinter as ctk
import random
from mysql.connector import IntegrityError
from tkinter import filedialog
from PIL import Image, ImageTk




class cart:
    

    def __init__(self, root):
        # Login.signin page
        self.root = root
        self.root.title("TechKart")
        self.root.geometry("1540x800+0+0")
        lbtitle = Label(self.root,  relief=RIDGE, text="TechKart", fg="black", bg="light yellow", font=("Riona Sans",50,"bold","italic"))
        lbtitle.pack(side=TOP, fill=X)
        


        self.usermail = StringVar()
        self.userpassword = StringVar()
        self.email = StringVar()
        self.user_id = IntVar()

        self.product_id = IntVar()
        self.gmail = StringVar()
        self.price = IntVar()
    

        dataframeleft = Frame(self.root,  relief=RIDGE, bg="grey")
        dataframeleft.place(relx=0.1,rely=0.2,width=600, height=600)


        dfl = Label(dataframeleft, anchor="center", text="LOG IN", font=("times new roman", 42, "bold"), bg="grey", fg="white")
        dfl.pack(side=TOP, fill=X)
        email_label = Label(dataframeleft, text="Email ID", font=("times new roman", 12, "bold"), padx=2, bg="grey")
        email_label.place(relx=0.3, rely=0.4, anchor="center") 
        email_entry = Entry(dataframeleft, textvariable=self.usermail, font=("times new roman", 13, "bold"), width=35)
        email_entry.place(relx=0.63, rely=0.4, anchor="center")

        password_label = Label(dataframeleft, text="Password", font=("times new roman", 12, "bold"), padx=2, bg="grey")
        password_label.place(relx=0.3, rely=0.5, anchor="center")
        password_entry = Entry(dataframeleft, textvariable=self.userpassword, font=("times new roman", 13, "bold"), width=35, show="●")
        password_entry.place(relx=0.63, rely=0.5, anchor="center")

        contbtn = Button(dataframeleft,text="Log In",command=self.show_page2, bg="orange", fg="black",font=("times new roman",12,"bold"), width=23, height=1, padx=2, pady=6)
        contbtn.place(relx=0.53, rely=0.75, anchor="center")
        
        self.usermail2 = StringVar()
        self.userpassword2= StringVar()
        dataframeright = Frame(self.root,  relief=RIDGE, bg="grey")
        dataframeright.place(relx=0.5,rely=0.2,width=600, height=600)


        dfr = Label(dataframeright, anchor="center", text="SIGN UP", font=("times new roman", 42, "bold"), bg="grey", fg="white")
        dfr.pack(side=TOP, fill=X)
        email_label = Label(dataframeright, text="Email ID", font=("times new roman", 12, "bold"), padx=2, bg="grey")
        email_label.place(relx=0.3, rely=0.4, anchor="center") 
        email_entry = Entry(dataframeright, textvariable=self.usermail2, font=("times new roman", 13, "bold"), width=35)
        email_entry.place(relx=0.63, rely=0.4, anchor="center")

        password_label = Label(dataframeright, text="Password", font=("times new roman", 12, "bold"), padx=2, bg="grey")
        password_label.place(relx=0.3, rely=0.5, anchor="center")
        password_entry = Entry(dataframeright, textvariable=self.userpassword2, font=("times new roman", 13, "bold"), width=35, show="●") 
        password_entry.place(relx=0.63, rely=0.5, anchor="center")

        contbtn = Button(dataframeright,command=self.signupfunction,text="Sign Up", bg="orange", fg="black",font=("times new roman",12,"bold"), width=23, height=1, padx=2, pady=6)
        contbtn.place(relx=0.53, rely=0.75, anchor="center")

        # -------------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        
        self.page2 = Toplevel(self.root)  # Create a new Toplevel window
        self.page3 = Toplevel(self.root)
        self.page4 = Toplevel(self.root)
        self.page5 = Toplevel(self.root)
        
        # Page 2 widgetss
        self.label2 = Label(self.page2, text="Welcome to TechKart", font=("Helvetica", 28, "bold", "italic"))
        self.label2.pack()
        dataframe = Frame(self.page2,  relief=RIDGE, bg="grey")
        dataframe.place(relx=0.5, rely=0.5, anchor="center", width=900, height=500)
        msg_label = Label(dataframe, text="Do you want to sell/buy a product?", font=("times new roman", 32, "bold"), padx=2, bg="grey")
        msg_label.place(relx=0.48, rely=0.4, anchor="center")
        selltbtn = Button(dataframe,command=self.sellpage,text="Sell", bg="orange", fg="black",font=("times new roman",12,"bold"), width=23, height=1, padx=2, pady=6)
        selltbtn.place(relx=0.35, rely=0.6, anchor="center")
        buytbtn = Button(dataframe,command=self.buypage,text="Buy", bg="orange", fg="black",font=("times new roman",12,"bold"), width=23, height=1, padx=2, pady=6)
        buytbtn.place(relx=0.65, rely=0.6, anchor="center")

        # -----------------------------------------------------------------------------------------------------------------------------
        #  -----------------------------------------------------------------------------------------------------------------------------

        # Page 3 widgets
        self.brand = StringVar()
        self.model = StringVar()
        self.phonenum = StringVar()
        

        dataframe = Frame(self.page3, relief=RIDGE, bg="grey")
        dataframe.place(relx=0.5, rely=0.5, anchor="center", width=950, height=750)

        addpost = Label(dataframe, anchor="center", text="POST YOUR ADD", font=("times new roman", 42, "bold"), bg="grey", fg="white")
        addpost.pack(side=TOP, fill=X)

        brandlabel = Label(dataframe, text="Brand", font=("times new roman",18,"bold"), padx=2, bg="grey")
        brandlabel.place(relx=0.3, rely=0.2, anchor="center")
        combrand = ttk.Combobox(dataframe, textvariable=self.brand, state="readonly", font=("times new roman",13,"bold"), width=35)
        combrand["values"] = ("Asus", "BlackBerry", "Gionee", "Google Pixel", "Honor", "HTC", "Huawei", "Infinix", "Intex", "iPhone", "Karbonn","Lava", "Lenovo", "LG", "Mi", "Micromax", "Motorola", "Nokia", "One Plus", "Oppo", "Realme", "Samsung", "Sony", "Techno", "Vivo")
        combrand.place(relx=0.58, rely=0.2, anchor="center")

        modlabel = Label(dataframe, text="Model", font=("times new roman",18,"bold"), padx=2, bg="grey")
        modlabel.place(relx=0.3, rely=0.25, anchor="center")
        modentry = Entry(dataframe, textvariable=self.model, font=("times new roman", 13, "bold"), width=35)
        modentry.place(relx=0.57, rely=0.25, anchor="center")

        adtitle = Label(dataframe, text="Ad title", font=("times new roman",18,"bold"), padx=2, bg="grey")
        adtitle.place(relx=0.3, rely=0.4, anchor="center")
        adtitle_entry = Text(dataframe,  font=("times new roman", 13, "bold"), width=50, height=4)
        adtitle_entry.place(relx=0.66, rely=0.4, anchor="center")
        addtitle_msg = Label(dataframe, text="Mention the key features of your item (e.g. brand, model, age, type)", font=("times new roman",9,"bold"), bg="grey")
        addtitle_msg.place(relx=0.61, rely=0.47, anchor="center")

        desclabel = Label(dataframe, text="Description", font=("times new roman",18,"bold"), padx=2, bg="grey")
        desclabel.place(relx=0.3, rely=0.54, anchor="center")
        desctext = Text(dataframe, font=("times new roman", 13, "bold"), width=58, height=5)
        desctext.place(relx=0.7, rely=0.56, anchor="center")
        desc_msg = Label(dataframe, text="Include condition, features and reason for selling", font=("times new roman",9,"bold"), bg="grey")
        desc_msg.place(relx=0.56, rely=0.64, anchor="center")

        addimglabel = Label(dataframe, text="Add Images", font=("times new roman",18,"bold"), padx=2, bg="grey")
        addimglabel.place(relx=0.3, rely=0.74, anchor="center")
        self.upload_btn = Button(dataframe,command=self.open_image, text="Upload Image", bg="white", fg="black",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
        self.upload_btn.place(relx=0.5, rely=0.74, anchor="center")

        phonenum_label = Label(dataframe, text="Your Contact No.", font=("times new roman",15,"bold"), padx=2, bg="grey")
        phonenum_label.place(relx=0.3, rely=0.9, anchor="center")
        phonenum_entry = Entry(dataframe, textvariable=self.phonenum, font=("times new roman", 13, "bold"), width=10)
        phonenum_entry.place(relx=0.47, rely=0.9, anchor="center")

        posttbtn = Button(dataframe,command=self.register, text="POST", bg="orange", fg="black",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
        posttbtn.place(relx=0.89, rely=0.95, anchor="center")

        # ---------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------

        #page 4 widgets
        detailsframe = Frame(self.page4, bd=20, relief=RIDGE)
        detailsframe.place(x=0, y=0, width=1530, height=800)
        self.products = ttk.Treeview(detailsframe, column=("product_id", "email", "phonenum", "brand", "model", "price"))
        

        

        self.products.heading("product_id", text="Product ID")
        self.products.heading("email", text="Email")
        self.products.heading("phonenum", text="Contact")
        self.products.heading("brand", text="Brand")
        self.products.heading("model", text="Model")
        self.products.heading("price", text="Price(INR)")
        


        self.products["show"] = "headings"
        self.products.column("product_id", width=200)
        self.products.column("email", width=200)
        self.products.column("phonenum", width=200)
        self.products.column("brand", width=200)
        self.products.column("model", width=200)
        self.products.column("price", width=200)

        self.products.pack(fill=BOTH, expand=1)
        self.products.bind("<ButtonRelease>", self.getcursor)
        self.fetchdata()

        # page 5 widgets
        payframe = Frame(self.page5, relief=RIDGE, bg="grey")
        payframe.place(relx=0.5, rely=0.5, anchor="center", width=950, height=750)

        paylabel = Label(payframe, anchor="center", text="PAYMENT DETAILS", font=("times new roman", 42, "bold"), bg="grey", fg="white")
        paylabel.pack(side=TOP, fill=X)

        # Cardholder Name: The name of the person whose payment card is being used.

        # Card Number: The unique number printed on the front of the payment card.

        # Expiration Date: The date when the payment card expires. Usually, this includes the month and year.

        # CVV/CVC: The Card Verification Value (CVV) or Card Verification Code (CVC) is a security code printed on the back of most payment cards.

        # Billing Address: The address associated with the payment card for billing purposes.

        # Amount: The total amount to be paid.
        

        
    

    def show_page2(self):
        if self.usermail.get() == "" or self.userpassword.get() == "":
            messagebox.showerror("Error","Enter Email and Password!")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
            mycursor = conn.cursor()
            self.email = self.usermail.get()
            password = self.userpassword.get()
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            mycursor.execute(query, (self.email, password))
            res = mycursor.fetchone()

            if res:
                messagebox.showinfo("Login", "Login Successful!")
                self.page2.lift()  # Show page 2
            else:
                messagebox.showerror("Login", "Please sign up first!")

    def signupfunction(self):
        if self.usermail2.get() == "" or self.userpassword2.get() == "":
            messagebox.showerror("Error","Enter Email and Password!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
                mycursor = conn.cursor()
                self.email = self.usermail2.get()
                password = self.userpassword2.get()
                self.user_id = random.randint(1032222000, 1032223000)
                query = "insert into users values(%s, %s, %s)"
                mycursor.execute(query, (self.user_id, self.email, password))
                conn.commit()
                messagebox.showinfo("Sign Up","Sign Up Successful!")
                self.page2.lift()
            except IntegrityError:
                messagebox.showerror("Error", "User ID already exists. Please try again.")
               
            finally:
                conn.close()
                

    def sellpage(self):
        self.page3.lift()

    def register(self):
        if self.brand.get() == "" or self.model.get() == "" or self.phonenum.get() == "":
            messagebox.showerror("Error","All fields compulsory")
        else:
         self.price = random.randint(20000, 30000)
         reg = messagebox.askyesno("",f"Your product evaluated to INR {self.price}, Do you want to confirm registeration?")
         if reg > 0:
             try:
                 conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
                 mycursor = conn.cursor()
                 product_id = random.randint(1034444000, 1034448999)

             
                 query = "insert into products values (%s, %s, %s, %s, %s, %s)"
                 phonenumber = self.phonenum.get()
                 mobilebrand = self.brand.get()
                 brandmodel = self.model.get()
                 mycursor.execute(query, (product_id, self.email, phonenumber, mobilebrand, brandmodel, self.price))
                 conn.commit()
                 messagebox.showinfo("","Product resgistered for sale!")
             except IntegrityError:
                messagebox.showerror("Error", "Product ID already exists. Please try again.")
               
             finally:
                conn.close()

    def buypage(self):
        self.page4.lift()

    def fetchdata(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
        mycursor = conn.cursor()
        mycursor.execute("select *from products")
        row = mycursor.fetchall()
        if len(row) != 0:
            self.products.delete(*self.products.get_children())
            for i in row:
                self.products.insert("", END, values=i)
            conn.commit()
        conn.close()

    def open_image(self):
      filepath = filedialog.askopenfilename(parent=self.page3, filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
      if filepath:
        # Open the image file
        image = Image.open(filepath)
        # Optionally, resize the image if necessary
        # image = image.resize((300, 300), Image.ANTIALIAS)  # Adjust size as needed
        #messagebox.showinfo("Success", "Image upload successful!")
        self.upload_btn.config(text="Uploaded")
        # Return the PIL Image object
        return image
      
    def getcursor(self, event=""):
        cursor_row = self.products.focus()
        content = self.products.item(cursor_row)
        row = content["values"]
        self.product_id.set(row[0])
        self.gmail.set(row[1])
        self.phonenum.set(row[2])
        self.brand.set(row[3])
        self.model.set(row[4])
        self.price.set(row[5])
        
        conf = messagebox.askyesno(f"{self.brand.get()} {self.model.get()}", f"Pay {self.price.get()}?")
        if conf > 0:
            self.page5.lift()
        else:
            self.page4.lift()

        

             


        

root = Tk()
obj = cart(root)
root.mainloop() 



 