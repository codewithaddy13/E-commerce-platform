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
from tkinter import PhotoImage
import re
from camspec import extract_integers
from searchtrack import model_price
from price_report import adjust_price, pricereport
from cartrec import rec
import pandas as pd
import pickle

with open('model.pickle', 'rb') as file:
    model = pickle.load(file)



class Cart:
    


    def __init__(self, root):
        # Login/signup page
        self.root = root
        self.homepage = Frame(self.root)
        self.root.title("Phonekart")
        self.root.geometry("1540x800+0+0")
        self.homepage.pack(fill="both", expand=True)

        self.islogin = 0
        self.image_paths = ["C:\\Users\\HP\\OneDrive\\Desktop\\adheesh_phonekart\\ad2.jpg", "C:\\Users\\HP\\OneDrive\Desktop\\adheesh_phonekart\\ad3.jpg",  "C:\\Users\\HP\\OneDrive\\Desktop\\adheesh_phonekart\\ad1.jpg", "C:\\Users\\HP\\OneDrive\\Desktop\\adheesh_phonekart\\ad4.jpg"]

        

        #home page widgets
        # Create header frame

        header_frame = Frame(self.homepage, bg="blue")
        header_frame.pack(fill="x")

        # Create hamburger icon
        hamburger_icon = Label(header_frame, text="\u2630", font=("Helvetica", 18), fg="white", bg="blue")
        hamburger_icon.pack(side="left", padx=10, pady=10)

      #   # Create header label
        header_label = Label(header_frame, text="Phonekart", font=("Helvetica", 22), fg="white", bg="blue")
        header_label.pack(side="left", padx=10, pady=10)

      #   # Create search entry
      #   search_entry = Entry(header_frame, font=("Helvetica", 12), relief=FLAT)
      #   search_entry.pack(side="left", padx=10, pady=10)

        # Create Buy button
        buy_button = Button(header_frame, text="Buy", command=self.become_a_buyer,  bg="blue", fg="white", padx=10, pady=5, font=("Helvetica", 12), relief=FLAT)
        buy_button.pack(side="right", padx=10, pady=10)


        # Create Become a Seller button
        seller_button = Button(header_frame, text="Become a Seller",command=self.become_a_seller,  bg="blue", fg="white", padx=10, pady=5, font=("Helvetica", 12), relief=FLAT)
        seller_button.pack(side="right", padx=10, pady=10)

        # Create Contact button
        contact_button = Button(header_frame, text="Contact Us ",  bg="blue", fg="white", padx=10, pady=5, font=("Helvetica", 12), relief=FLAT)
        contact_button.pack(side="right", padx=10, pady=10)

        # Create Log In Button
        islogin_button = Button(header_frame,command=self.login_logout,text="Log In/Log Out", bg="blue", fg="white", padx=10, pady=5, font=("Helvetica", 12), relief=FLAT)
        islogin_button.pack(side="right", padx=10, pady=10)
        # if self.islogin == 0:
        #    islogin_button.config(text="Log In")
        # else:
        #    islogin_button.config(text="Log Out")

        # Create a frame to hold the content below the header
        content_frame = Frame(self.homepage)
        content_frame.pack(fill="both", expand=True)

        # Create first frame below the header
        first_frame = Frame(content_frame, bg="light yellow", padx=20, pady=20)
        first_frame.pack(fill="both", expand=True,padx=10, pady=10, ipady=5)

        # Add content to the first frame
        first_label = Label(first_frame, text="𝓤𝓹𝓰𝓻𝓪𝓭𝓮 𝓨𝓸𝓾𝓻 𝓓𝓮𝓿𝓲𝓬𝓮, 𝓡𝓮𝓷𝓮𝔀 𝓨𝓸𝓾𝓻 𝓔𝔁𝓹𝓮𝓻𝓲𝓮𝓷𝓬𝓮!\n𝓨𝓸𝓾𝓻 𝓞𝓷𝓮 𝓢𝓽𝓸𝓹 𝓓𝓮𝓼𝓽𝓲𝓷𝓪𝓽𝓲𝓸𝓷 𝓯𝓸𝓻 𝓡𝓮𝓯𝓾𝓻𝓫𝓲𝓼𝓱𝓮𝓭 𝓢𝓶𝓪𝓻𝓽𝓹𝓱𝓸𝓷𝓮𝓼 𝓗𝓮𝓻𝓮!", font=("Helvetica", 18), bg="light yellow")
        first_label.pack()
        self.slidingimages(first_frame, self.image_paths, interval=2000)

        # Create second frame below the header
      #   second_frame = Frame(content_frame, bg="white", padx=20, pady=20)
      #   second_frame.pack(fill="both", expand=True,padx=10, pady=10)

      #   # Add content to the second frame
      #   second_label = Label(second_frame, text="Second Frame Content", font=("Helvetica", 12))
      #   second_label.pack()
        # ------------------------------------------------------------------------------------------------------------------
        


        self.page1 = Frame(self.root)
        self.page2 = Frame(self.root)  
        self.page3 = Frame(self.root)
        self.page4 = Frame(self.root)
        self.page5 = Frame(self.root)
        self.page6 = Frame(self.root)
        self.page7 = Frame(self.root)

        self.usermail = StringVar()
        self.userpassword = StringVar()
        self.email = None
        self.contact = None
        self.user_id = IntVar()

        self.product_id = IntVar()
        self.gmail = StringVar()
        self.price = IntVar()
        self.img = None
        self.adtitle = StringVar()
        self.descp = StringVar()
        self.current_month = StringVar()
        self.current_year = StringVar()
        self.fname = StringVar()
        self.lname = StringVar()
        self.numcode = 0

        self.batcap = IntVar()
        self.screensize = StringVar()
        self.storage = IntVar()
        self.ram = IntVar()
        self.cam = StringVar() 
        self.relyr = IntVar()
        self.daysused = IntVar()

        self.latest_model = StringVar()
        self.latest_brand = StringVar()
        self.latest_price = IntVar()      
        self.is_signup = 0 

        self.searchbrand = StringVar()
        
        self.current_page = self.homepage
        self.page_stack = []  # Stack to store visited pages
        # ---------------------------------------------------------------------------------------------------------------------

        #page1 widgets
        lbtitle = Label(self.page1,  relief=RIDGE, text="Phonekart", fg="black", bg="light yellow", font=("Riona Sans",50,"bold","italic"))
        lbtitle.pack(side=TOP, fill=X)
        backbtn = Button(lbtitle,text="<",command=self.go_back, bg="black", fg="white",font=("times new roman",25,"bold"), width=2,height=1, padx=2, pady=3)
        backbtn.pack(side=LEFT)
    

        dataframeleft = Frame(self.page1,  relief=RIDGE, bg="grey")
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

        contbtn = Button(dataframeleft,text="Log In",command=self.loginfunction, bg="orange", fg="black",font=("times new roman",12,"bold"), width=23, height=1, padx=2, pady=6)
        contbtn.place(relx=0.53, rely=0.75, anchor="center")
        
        self.usermail2 = StringVar()
        self.userpassword2= StringVar()
        dataframeright = Frame(self.page1,  relief=RIDGE, bg="grey")
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

        
        

        # -----------------------------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------------------
        
        # Page 2 widgetss
        canvas = Canvas(self.page2, width=self.page2.winfo_screenwidth(), height=self.page2.winfo_screenheight())
        canvas.pack(fill=BOTH, expand=True)
        self.label2 = Label(canvas, text="Welcome to Phonekart", font=("Helvetica", 28, "bold", "italic"))
        self.label2.pack()
        backbtn = Button(canvas,text="<",command=self.go_back, bg="black", fg="white",font=("times new roman",25,"bold"), width=2,height=1, padx=2, pady=6)
        backbtn.place(relx=0.1, rely=0.35)
        dataframe = Frame(canvas,  relief=RIDGE, bg="grey")
        dataframe.place(relx=0.5, rely=0.5, anchor="center", width=900, height=500)
        msg_label = Label(dataframe, text="Do you want to sell/buy a product?", font=("times new roman", 32, "bold"), padx=2, bg="grey")
        msg_label.place(relx=0.48, rely=0.4, anchor="center")
        selltbtn = Button(dataframe,command=self.sellpage,text="Sell", bg="orange", fg="black",font=("times new roman",12,"bold"), width=23, height=1, padx=2, pady=6)
        selltbtn.place(relx=0.35, rely=0.6, anchor="center")
        buytbtn = Button(dataframe,command=self.buypage,text="Buy", bg="orange", fg="black",font=("times new roman",12,"bold"), width=23, height=1, padx=2, pady=6)
        buytbtn.place(relx=0.65, rely=0.6, anchor="center")

        

        self.create_circle_button(canvas, 1500, 50, 20, "brown", "A", 12)

        # -----------------------------------------------------------------------------------------------------------------------------
        #  -----------------------------------------------------------------------------------------------------------------------------

        # Page 3 widgets
      #   canvas = Canvas(self.page3, width=self.page3.winfo_screenwidth(), height=self.page3.winfo_screenheight())
      #   canvas.pack(fill=BOTH, expand=True)
      #   self.brand = StringVar()
      #   self.model = StringVar()
      #   self.phonenum = StringVar()
        

      #   dataframe = Frame(canvas, relief=RIDGE, bg="grey")
      #   dataframe.place(relx=0.5, rely=0.5, anchor="center", width=950, height=750)
      #   backbtn = Button(canvas,text="<",command=self.go_back, bg="black", fg="white",font=("times new roman",25,"bold"), width=2,height=1, padx=2, pady=6)
      #   backbtn.place(relx=0.1, rely=0.35)

      #   addpost = Label(dataframe, anchor="center", text="POST YOUR ADD", font=("times new roman", 42, "bold"), bg="grey", fg="white")
      #   addpost.pack(side=TOP, fill=X)

      #   brandlabel = Label(dataframe, text="Brand", font=("times new roman",18,"bold"), padx=2, bg="grey")
      #   brandlabel.place(relx=0.3, rely=0.2, anchor="center")
      #   combrand = ttk.Combobox(dataframe, textvariable=self.brand, state="readonly", font=("times new roman",13,"bold"), width=35)
      #   combrand["values"] = ("Asus", "BlackBerry", "Gionee", "Google Pixel", "Honor", "HTC", "Huawei", "Infinix", "Intex", "iPhone", "Karbonn","Lava", "Lenovo", "LG", "Mi", "Micromax", "Motorola", "Nokia", "One Plus", "Oppo", "Realme", "Samsung", "Sony", "Techno", "Vivo")
      #   combrand.place(relx=0.58, rely=0.2, anchor="center")

      #   modlabel = Label(dataframe, text="Model", font=("times new roman",18,"bold"), padx=2, bg="grey")
      #   modlabel.place(relx=0.3, rely=0.25, anchor="center")
      #   modentry = Entry(dataframe, textvariable=self.model, font=("times new roman", 13, "bold"), width=35)
      #   modentry.place(relx=0.57, rely=0.25, anchor="center")

      #   adtitle = Label(dataframe, text="Ad title", font=("times new roman",18,"bold"), padx=2, bg="grey")
      #   adtitle.place(relx=0.3, rely=0.4, anchor="center")
      #   self.adtitle_entry = Text(dataframe, font=("times new roman", 13, "bold"), width=50, height=4)
      #   self.adtitle_entry.place(relx=0.66, rely=0.4, anchor="center")
      #   addtitle_msg = Label(dataframe, text="Mention the key features of your item (e.g. brand, model, age, type)", font=("times new roman",9,"bold"), bg="grey")
      #   addtitle_msg.place(relx=0.61, rely=0.47, anchor="center")
        
      # #   desclabel = Label(dataframe, text="Description", font=("times new roman",18,"bold"), padx=2, bg="grey")
      # #   desclabel.place(relx=0.3, rely=0.54, anchor="center")
      # #   self.desctext = Text(dataframe, font=("times new roman", 13, "bold"), width=58, height=5)
      # #   self.desctext.place(relx=0.7, rely=0.56, anchor="center")
      # #   desc_msg = Label(dataframe, text="Include condition, features and reason for selling", font=("times new roman",9,"bold"), bg="grey")
      # #   desc_msg.place(relx=0.56, rely=0.64, anchor="center")

      #   batcaplabel = Label(dataframe, text="Battery Capacity(mAh)", font=("times new roman",14,"bold"), padx=2, bg="grey")
      #   batcaplabel.place(relx=0.35, rely=0.54, anchor="center")
      #   batcapentry = Entry(dataframe, textvariable=self.batcap, font=("times new roman", 13, "bold"), width=7)
      #   batcapentry.place(relx=0.5, rely=0.54, anchor="center")

      #   screensizelabel = Label(dataframe, text="Screen Size(inches)", font=("times new roman",14,"bold"), padx=2, bg="grey")
      #   screensizelabel.place(relx=0.65, rely=0.54, anchor="center")
      #   screensizeentry = Entry(dataframe, textvariable=self.screensize, font=("times new roman", 13, "bold"), width=7)
      #   screensizeentry.place(relx=0.8, rely=0.54, anchor="center")

      #   storagelabel = Label(dataframe, text="Storage(GB)", font=("times new roman",14,"bold"), padx=2, bg="grey")
      #   storagelabel.place(relx=0.3, rely=0.64, anchor="center")
      #   storageentry = Entry(dataframe, textvariable=self.storage, font=("times new roman", 13, "bold"), width=7)
      #   storageentry.place(relx=0.4, rely=0.64, anchor="center")

      #   ramlabel = Label(dataframe, text="RAM(GB)", font=("times new roman",14,"bold"), padx=2, bg="grey")
      #   ramlabel.place(relx=0.5, rely=0.64, anchor="center")
      #   ramentry = Entry(dataframe, textvariable=self.ram, font=("times new roman", 13, "bold"), width=7)
      #   ramentry.place(relx=0.6, rely=0.64, anchor="center")

      #   camlabel = Label(dataframe, text="Camera(MP)", font=("times new roman",14,"bold"), padx=2, bg="grey")
      #   camlabel.place(relx=0.7, rely=0.64, anchor="center")
      #   camentry = Entry(dataframe, textvariable=self.cam, font=("times new roman", 13, "bold"), width=7)
      #   camentry.place(relx=0.8, rely=0.64, anchor="center")

      #   relyrlabel = Label(dataframe, text="Release Year", font=("times new roman",14,"bold"), padx=2, bg="grey")
      #   relyrlabel.place(relx=0.3, rely=0.74, anchor="center")
      #   combrand = ttk.Combobox(dataframe, textvariable=self.relyr, state="readonly", font=("times new roman",13,"bold"), width=10)
      #   combrand["values"] = (2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024)
      #   combrand.place(relx=0.46, rely=0.74, anchor="center")

      #   daysusedlabel = Label(dataframe, text="No. Of Days Used", font=("times new roman",14,"bold"), padx=2, bg="grey")
      #   daysusedlabel.place(relx=0.7, rely=0.74, anchor="center")
      #   daysusedentry = Entry(dataframe, textvariable=self.daysused, font=("times new roman", 13, "bold"), width=7)
      #   daysusedentry.place(relx=0.83, rely=0.74, anchor="center")

        

      #   addimglabel = Label(dataframe, text="Add Images", font=("times new roman",18,"bold"), padx=2, bg="grey")
      #   addimglabel.place(relx=0.3, rely=0.84, anchor="center")
      #   self.upload_btn = Button(dataframe,command=self.open_image, text="Upload Image", bg="white", fg="black",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
      #   self.upload_btn.place(relx=0.5, rely=0.84, anchor="center")

      #   phonenum_label = Label(dataframe, text="Your Contact No.", font=("times new roman",15,"bold"), padx=2, bg="grey")
      #   phonenum_label.place(relx=0.3, rely=0.95, anchor="center")
      #   phonenum_entry = Entry(dataframe, textvariable=self.phonenum, font=("times new roman", 13, "bold"), width=10)
      #   phonenum_entry.place(relx=0.47, rely=0.95, anchor="center")

      #   posttbtn = Button(dataframe,command=self.register, text="POST", bg="orange", fg="black",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
      #   posttbtn.place(relx=0.89, rely=0.95, anchor="center")

      #   self.create_circle_button(canvas, 1500, 50, 20, "brown", "A", 12)

        # Create a canvas to hold all elements
        # Create a canvas to hold all elements
        canvas = Canvas(self.page3, bg="#f0f0f0", width=self.page3.winfo_screenwidth(), height=self.page3.winfo_screenheight())
        canvas.pack(fill=BOTH, expand=True)

        self.brand = StringVar()
        self.model = StringVar()
        self.phonenum = StringVar()

        # Frame for content with padding and relief
        dataframe = Frame(canvas, bg="#34495e", relief=RIDGE, bd=10)
        dataframe.place(relx=0.5, rely=0.5, anchor="center", width=900, height=700)

        # Back Button Styling
        backbtn = Button(canvas, text="<", command=self.go_back, bg="#16a085", fg="white", font=("Arial", 16, "bold"), width=2, height=1)
        backbtn.place(relx=0.05, rely=0.1)

        # Add Post Label
        addpost = Label(dataframe, text="POST YOUR AD", font=("Arial", 30, "bold"), bg="#34495e", fg="white")
        addpost.pack(side=TOP, fill=X, pady=20)

        # Brand Label and Combobox
        brandlabel = Label(dataframe, text="Brand", font=("Arial", 16, "bold"), bg="#34495e", fg="white")
        brandlabel.place(relx=0.25, rely=0.15, anchor="center")
        combrand = ttk.Combobox(dataframe, textvariable=self.brand, state="readonly", font=("Arial", 12), width=30)
        combrand["values"] = ("Asus", "BlackBerry", "Gionee", "Google Pixel", "Honor", "HTC", "Huawei", "Infinix", "Intex", "iPhone", "Karbonn","Lava", "Lenovo", "LG", "Mi", "Micromax", "Motorola", "Nokia", "One Plus", "Oppo", "Realme", "Samsung", "Sony", "Techno", "Vivo")
        combrand.place(relx=0.65, rely=0.15, anchor="center")

        # Model Label and Entry
        modlabel = Label(dataframe, text="Model", font=("Arial", 16, "bold"), bg="#34495e", fg="white")
        modlabel.place(relx=0.25, rely=0.22, anchor="center")
        modentry = Entry(dataframe, textvariable=self.model, font=("Arial", 12), width=30, relief="groove", bd=2)
        modentry.place(relx=0.65, rely=0.22, anchor="center")

         # Ad Title Section
        adtitle = Label(dataframe, text="Ad Title", font=("Arial", 16, "bold"), bg="#34495e", fg="white")
        adtitle.place(relx=0.25, rely=0.32, anchor="center")
        self.adtitle_entry = Text(dataframe, font=("Arial", 12), width=40, height=2, relief="groove", bd=2)
        self.adtitle_entry.place(relx=0.65, rely=0.32, anchor="center")
        addtitle_msg = Label(dataframe, text="Mention key features (e.g. brand, model, age)", font=("Arial", 9, "bold"), bg="#34495e", fg="lightgrey")
        addtitle_msg.place(relx=0.65, rely=0.38, anchor="center")

         # Battery Capacity
        batcaplabel = Label(dataframe, text="Battery Capacity (mAh)", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
        batcaplabel.place(relx=0.3, rely=0.46, anchor="center")
        batcapentry = Entry(dataframe, textvariable=self.batcap, font=("Arial", 12), width=8, relief="groove", bd=2)
        batcapentry.place(relx=0.5, rely=0.46, anchor="center")

         # Screen Size
        screensizelabel = Label(dataframe, text="Screen Size (inches)", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
        screensizelabel.place(relx=0.65, rely=0.46, anchor="center")
        screensizeentry = Entry(dataframe, textvariable=self.screensize, font=("Arial", 12), width=8, relief="groove", bd=2)
        screensizeentry.place(relx=0.8, rely=0.46, anchor="center")

         # Storage
        storagelabel = Label(dataframe, text="Storage (GB)", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
        storagelabel.place(relx=0.3, rely=0.56, anchor="center")
        storageentry = Entry(dataframe, textvariable=self.storage, font=("Arial", 12), width=8, relief="groove", bd=2)
        storageentry.place(relx=0.5, rely=0.56, anchor="center")

         # RAM
        ramlabel = Label(dataframe, text="RAM (GB)", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
        ramlabel.place(relx=0.65, rely=0.56, anchor="center")
        ramentry = Entry(dataframe, textvariable=self.ram, font=("Arial", 12), width=8, relief="groove", bd=2)
        ramentry.place(relx=0.8, rely=0.56, anchor="center")

         # Camera MP
        camlabel = Label(dataframe, text="Camera (MP)", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
        camlabel.place(relx=0.3, rely=0.66, anchor="center")
        camentry = Entry(dataframe, textvariable=self.cam, font=("Arial", 12), width=8, relief="groove", bd=2)
        camentry.place(relx=0.5, rely=0.66, anchor="center")

         # Release Year
        relyrlabel = Label(dataframe, text="Release Year", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
        relyrlabel.place(relx=0.65, rely=0.66, anchor="center")
        comyear = ttk.Combobox(dataframe, textvariable=self.relyr, state="readonly", font=("Arial", 12), width=10)
        comyear["values"] = (2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024)
        comyear.place(relx=0.8, rely=0.66, anchor="center")

        # Number of Days Used
        daysusedlabel = Label(dataframe, text="No. of Days Used", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
        daysusedlabel.place(relx=0.3, rely=0.76, anchor="center")
        daysusedentry = Entry(dataframe, textvariable=self.daysused, font=("Arial", 12), width=8, relief="groove", bd=2)
        daysusedentry.place(relx=0.5, rely=0.76, anchor="center")

        # Contact Number
        phonenum_label = Label(dataframe, text="Your Contact No.", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
        phonenum_label.place(relx=0.2, rely=0.95, anchor="center")
        phonenum_entry = Entry(dataframe, textvariable=self.phonenum, font=("Arial", 12), width=10, relief="groove", bd=2)
        phonenum_entry.place(relx=0.4, rely=0.95, anchor="center")

        # Upload Image Button
        addimglabel = Label(dataframe, text="Add Images", font=("Arial", 16, "bold"), bg="#34495e", fg="white")
        addimglabel.place(relx=0.3, rely=0.84, anchor="center")
        self.upload_btn = Button(dataframe, command=self.open_image, text="Upload Image", bg="#16a085", fg="white", font=("Arial", 12, "bold"), width=12, height=1)
        self.upload_btn.place(relx=0.5, rely=0.84, anchor="center")

         # Post Button
        postbtn = Button(dataframe, command=self.register, text="POST", bg="#e67e22", fg="white", font=("Arial", 14, "bold"), width=10, height=1)
        postbtn.place(relx=0.85, rely=0.96, anchor="center")

        self.create_circle_button(canvas, 1500, 50, 20, "brown", "A", 12) 



        

        # ---------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------

        #page 4 widgets
        
        # Navigation bar
        
      #   self.page4.navbar = Frame(self.page4, bg="grey", height=80)
      #   self.page4.navbar.pack(fill=X)
      #   can = Canvas(self.page4.navbar, width=50, height=50, bg="grey", highlightthickness=0)
      #   can.place(relx=0.88, rely=0.15)
      #   self.create_circle_button(can, 25, 25, 20, "brown", "A", 12)
        
        
      #   backbtn = Button(self.page4.navbar,text="<",command=self.go_back, bg="black", fg="white",font=("times new roman",25,"bold"), width=2,height=1, padx=2, pady=3)
      #   backbtn.pack(side=LEFT)
      #   title_label = Label(self.page4.navbar, text="TechKart", fg="white", bg="grey", font=('Arial', 32, 'bold', 'italic') , padx=20, pady=20)
      #   title_label.place(relx=0.05, rely=-0.1)
      #   # Search bar
      #   search_frame = Frame(self.page4.navbar, bg="white", width=500, height=90)
      #   # search_frame.pack(side=RIGHT, padx=20, pady=20)
      #   search_frame.place(relx=0.3, rely=0.2)
      #   self.entry = ttk.Combobox(search_frame,textvariable=self.searchbrand, width=38, font=('Arial', 16))
      #   self.entry["values"] = ("ALL BRANDS","Asus", "BlackBerry", "Gionee", "Google Pixel", "Honor", "HTC", "Huawei", "Infinix", "Intex", "iPhone", "Karbonn","Lava", "Lenovo", "LG", "Mi", "Micromax", "Motorola", "Nokia", "One Plus", "Oppo", "Realme", "Samsung", "Sony", "Techno", "Vivo")
      #   self.entry.insert(0, 'Search Brands')
      #   self.entry.bind('<FocusIn>', self.on_entry_click)
      #   self.entry.bind('<FocusOut>', self.on_focus_out)
      #   self.entry.pack(side=LEFT, padx=(0, 10))
      #   search_button = Button(search_frame, text="Search", command=self.search, font=('Arial', 14))
      #   search_button.pack(side=LEFT)

        

        
        
      #   canvas = Canvas(self.page4)
      #   canvas.pack(side=LEFT, fill=BOTH, expand=True)

      #   # Add a scrollbar to the canvas
      #   scrollbar = Scrollbar(self.page4, orient=VERTICAL, command=canvas.yview)
      #   scrollbar.pack(side=RIGHT, fill=Y)

      #   # Configure the canvas to use the scrollbar
      #   canvas.configure(yscrollcommand=scrollbar.set)
      #   canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

      #   # Create a frame inside the canvas to contain the information
      #   frame = Frame(canvas)
      #   canvas.create_window((0, 0), window=frame, anchor="nw")

        

      #   conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
      #   mycursor = conn.cursor()
      #   mycursor.execute("select *from products")
        
      #   row = mycursor.fetchall()
      #   self.create_page4_widgets(frame, row)
      #   c = 0
      #   r = 0
      #   for i in row:
      #      infoframe = Frame(frame, bg="light blue", height=350, width=350, bd=1, highlightbackground="black")
      #      infoframe.grid(row=r, column=c, padx=10, pady=10)
      #      adtitle = Label(infoframe, anchor="center", text=f"{i[7]}", font=("times new roman", 16, "bold", "italic"), bg="light blue", fg="black")
      #      adtitle.place(rely=0.12, relx=0.5, anchor="center")
      #      temp_image_path = f"temp_image_{i[0]}.png"  
      #      img = Image.open(temp_image_path)
      #      desired_width = 100  
      #      desired_height = 100 
      #      img = img.resize((desired_width, desired_height))
      #      photo = ImageTk.PhotoImage(img)
      #      self.img_label = Label(infoframe, image=photo)
      #      self.img_label.image = photo  
      #      self.img_label.place(relx=0.37, rely=0.2)
      #      pricelbl = Label(infoframe, anchor="center", text=f"₹{i[5]}/-",font=("times new roman", 16, "bold"), bg="light blue", fg="red" )
      #      pricelbl.place(relx=0.5, rely=0.6, anchor="center")
      #      adbrand = Label(infoframe, anchor="center", text=f"{i[3]}", font=("times new roman", 16, "bold"), bg="light blue", fg="black")
      #      adbrand.place(rely=0.68, relx=0.5, anchor="center")
      #      admodel = Label(infoframe, anchor="center", text=f"{i[4]}", font=("times new roman", 16, "bold"), bg="light blue", fg="black")
      #      admodel.place(rely=0.75, relx=0.5, anchor="center")
      #      shopbtn = Button(infoframe,command=lambda i=i: self.shop(i), text="SHOP NOW", bg="orange", fg="black",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
      #      shopbtn.place(relx=0.5, rely=0.9, anchor="center")

           
      #      c += 1

      #      if c == 4:
      #         c = 0
      #         r += 1

     
              
           

    def create_circle_button(self,canvas, x, y, radius, color, text, fontsize):
     button = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
     canvas.create_text(x, y, text=text, fill="white", font=("Helvetica", fontsize, "bold"))
     canvas.tag_bind(button, "<Button-1>",lambda event: self.show_page("page6"))


    def slidingimages(self, parent, images, interval=2000):
       self.parent = parent
       self.images = images
       self.interval = interval
       self.canvas = Canvas(parent, bg="white", highlightthickness=0)
       self.canvas.pack(fill="both", expand=True)
       self.image_objects = []
       self.image_index = 0
       self.load_images()
       self.animate()

    def load_images(self):
        for img_path in self.images:
            image = Image.open(img_path)
            # frame_width = self.parent.winfo_width()
            # frame_height = self.parent.winfo_height()
            # resized_image = image.resize((frame_width, frame_height), Image.LANCZOS)

            # photo = ImageTk.PhotoImage(resized_image)
            photo = ImageTk.PhotoImage(image)
            self.image_objects.append(photo)

    def animate(self):
        if self.image_index >= len(self.image_objects):
            self.image_index = 0
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_objects[self.image_index])
        self.image_index += 1
        self.parent.after(self.interval, self.animate)

    def showpage1(self):  
       #self.page1.pack(fill=BOTH, expand=True)
       self.show_page("page1")
         
    
    def show_page(self, page_name):
        # Hide the current page
        if self.current_page:
            self.page_stack.append(self.current_page)
            self.current_page.pack_forget()

        # Show the requested page
        if page_name == "page2":
            self.current_page = self.page2
        elif page_name == "page3":
            self.current_page = self.page3
        elif page_name == "page4":
            self.current_page = self.page4
        elif page_name == "page5":
            self.current_page = self.page5
        elif page_name == "page6":
           self.current_page = self.page6
        elif page_name == "page7":
           self.current_page = self.page7
        elif page_name == "page1":
           self.current_page = self.page1
        elif page_name == "homepage":
           self.current_page = self.homepage
           

        self.current_page.pack(fill=BOTH, expand=True)

    def login_logout(self):
       if self.islogin == 0:
          self.showpage1()
       else:
         #  self.page6.destroy()
         #  self.page7.destroy()
         #  self.page1.destroy()
          for widget in self.page6.winfo_children():
            widget.destroy()

          for widget in self.page7.winfo_children():
            widget.destroy()

          for widget in self.page4.winfo_children():
            widget.destroy()

          self.usermail.set("")
          self.usermail2.set("")
          self.userpassword.set("")
          self.userpassword2.set("")

          

          messagebox.showinfo("LOGGED OUT", "You have been Logged Out")
          self.islogin = 0
          

    def go_back(self):
        # Pop the top page from the stack and display it
        self.numcode = 0
        if self.page_stack:
            self.current_page.pack_forget()
            self.current_page = self.page_stack.pop()
            self.current_page.pack(fill=BOTH, expand=True)

    def loginfunction(self):
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
                self.islogin = 1
                # Page 6 widgets
                if res[5] is not None:
                   self.fname = res[5]
                else:
                   match = re.search(r"^[^@._]+",self. email)

                   if match:
                    self.fname = match.group()

                if res[6] is not None:
                   self.lname = res[6]
                else:
                   self.lname = ""

               #  canvas = Canvas(self.page6, width=self.page6.winfo_screenwidth(), height=self.page6.winfo_screenheight(), bg="white")
               #  canvas.pack(fill=BOTH, expand=True)
                self.feedrec(self.email)

                self.page6_widgets(self.email, res[8])

                #page 7 widgets
                self.page7_widgets(self.fname, self.lname, self.email)
                # ---------------------------------------------------------------------------------------------------
                messagebox.showinfo("Login", "Login Successful!")
                if self.numcode == 0:
                   self.show_page("page2")
                elif self.numcode == 1:
                   self.sellpage()
                else:
                   self.buypage()
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
                self.contact = None
                self.user_id = random.randint(1032222000, 1032223000)
                
                # Get current month and year
                self.current_month = datetime.datetime.now().strftime("%B")  # Full month name
                self.current_year = datetime.datetime.now().year
                self.fname = None
                self.lname = None
                self.totalsales = 0
                query = "insert into users values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                query2 = 'insert into useractivity values(%s, %s, %s, %s, %s, %s)'
                mycursor.execute(query, (self.user_id, self.email, password, self.current_month, self.current_year, self.fname, self.lname, self.contact, self.totalsales))
                mycursor.execute(query2, (self.user_id, self.email, None, None, None, 0))
                
                
                match = re.search(r"^[^@._]+",self. email)
                if match:
                    self.fname = match.group()
                self.lname = ""

                conn.commit()
                self.islogin = 1
                self.is_signup = 1
                # Page 6 widgets
               #  canvas = Canvas(self.page6, width=self.page6.winfo_screenwidth(), height=self.page6.winfo_screenheight(), bg="white")
               #  canvas.pack(fill=BOTH, expand=True)
                self.feedrec(self.email)
                self.page6_widgets(self.email, self.totalsales)
                # page 7 widgets
                self.page7_widgets(self.fname, self.lname, self.email)
                # ---------------------------------------------------------------------------------------------------
                messagebox.showinfo("Sign Up","Sign Up Successful!")
                # self.page2.lift()
                if self.numcode == 0:
                   self.show_page("page2")
                elif self.numcode == 1:
                   self.sellpage()
                else:
                   self.buypage()
               
            except IntegrityError:
                messagebox.showerror("Error", "User ID already exists. Please try again.")
               
            finally:
                conn.close()
                

    def sellpage(self):
        # self.page3.lift()
       self.show_page("page3")

    def become_a_seller(self):
       if self.islogin == 1:
          self.sellpage()
       else:
          msg = messagebox.askokcancel("Log In with Email", "Close deals from the comfort of your home!")
          if msg:
            self.numcode = 1
            self.showpage1()
          else:
            self.show_page("homepage")


    def become_a_buyer(self):
       if self.islogin == 1:
          self.buypage()
       else:
          msg = messagebox.askokcancel("Log In with Email", "Close deals from the comfort of your home!")
          if msg:
            self.numcode = 2
            self.showpage1()
          else:
            self.show_page("homepage")

    def register(self):
        if self.brand.get() == "" or self.model.get() == "" or self.phonenum.get() == "" or self.batcap.get() == 0 or self.screensize.get() == 0 or self.storage.get() == 0 or self.ram.get() == 0 or self.cam.get() == "":
            messagebox.showerror("Error","All fields compulsory")
        else:
         num1 = IntVar()
         num2 = IntVar()
         num3 = IntVar()
         num4 = IntVar()
         num5 = IntVar()

         num1, num2, num3, num4, num5 = extract_integers(self.cam.get())
         
         self.price = int(adjust_price(int(model.predict([[int(self.batcap.get()), float(self.screensize.get()), int(self.storage.get()), int(self.ram.get()), int(num1), int(num2), int(num3), int(num4), int(num5)]])[0]), int(self.relyr.get()), int(self.daysused.get())))
         reg = messagebox.askyesno("",f"Your product evaluated to INR {self.price}, Do you want to confirm registeration?")
         if reg > 0:
             pricereport(model, int(self.batcap.get()), float(self.screensize.get()), int(self.storage.get()), int(self.ram.get()), int(num1), int(num2), int(num3), int(num4), int(num5), int(self.relyr.get()), int(self.daysused.get()))
             try:
                 conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
                 mycursor = conn.cursor()
                  
                #  self.product_id = random.randint(1034444000, 1034448999)
                 self.adtitle = self.adtitle_entry.get("1.0", END)
               
                 self.descp = f"Battery Capacity:{self.batcap.get()} mAh Screen Size:{self.screensize.get()} inches \n Storage:{self.storage.get()} GB RAM:{self.ram.get()} GB Camera(MP):{self.cam.get()}"


                 image = self.img
                 if image:
                    with open(image, "rb") as file:
                        img_data = file.read()
                 else:
                    img_data = None  # Assign None if image is not selected

             
                 query = "insert into products values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                 phonenumber = self.phonenum.get()
                 mobilebrand = self.brand.get()
                 brandmodel = self.model.get()
                 mycursor.execute(query, (self.product_id, self.email, phonenumber, mobilebrand, brandmodel, self.price, img_data, self.adtitle, self.descp))
                 conn.commit()
                 messagebox.showinfo("","Product resgistered for sale!")
                 self.resetfields()
             except IntegrityError:
                messagebox.showerror("Error", "Product ID already exists. Please try again.")
               
             finally:
                conn.close()
         else:
            self.page3.lift()

    def buypage(self):
        self.show_page("page4")
        self.page4.pack(fill=BOTH, expand=True)
    #    self.page4.lift()

    
    
    def open_image(self):
      filepath = filedialog.askopenfilename(parent=self.page3, filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
      if filepath:
        # Open the image file
        image = Image.open(filepath)
        # Optionally, resize the image if necessary
        # image = image.resize((300, 300), Image.ANTIALIAS)  # Adjust size as needed
        
        # Save the image to a temporary file
        self.product_id = random.randint(1034444000, 1034448999)
        temp_filepath = f"temp_image_{self.product_id}.png"  
        image.save(temp_filepath)
        
        #messagebox.showinfo("Success", "Image upload successful!")
        self.upload_btn.config(text="Uploaded")
        # Return the file path to the temporary image file
        self.img = temp_filepath

      
    

    def on_entry_click(self,event):
      if self.entry.get() == 'Search Brands':
         self.entry.delete(0, END)
         self.entry.config(fg='black')

    def on_focus_out(self,event):
       if self.entry.get() == '':
          self.entry.insert(0, 'Search Brands')
          self.entry.config(fg='grey')


    def create_page4_widgets(self, frame, data):
      c = 0
      r = 0
      for i in data:
        infoframe = Frame(frame, bg="light blue", height=350, width=350, bd=1, highlightbackground="black")
        infoframe.grid(row=r, column=c, padx=10, pady=10)
        adtitle = Label(infoframe, anchor="center", text=f"{i[7]}", font=("times new roman", 16, "bold", "italic"), bg="light blue", fg="black")
        adtitle.place(rely=0.12, relx=0.5, anchor="center")
        temp_image_path = f"temp_image_{i[0]}.png"
        img = Image.open(temp_image_path)
        desired_width = 100
        desired_height = 100
        img = img.resize((desired_width, desired_height))
        photo = ImageTk.PhotoImage(img)
        self.img_label = Label(infoframe, image=photo)
        self.img_label.image = photo
        self.img_label.place(relx=0.37, rely=0.2)
        pricelbl = Label(infoframe, anchor="center", text=f"₹{i[5]}/-",font=("times new roman", 16, "bold"), bg="light blue", fg="red" )
        pricelbl.place(relx=0.5, rely=0.6, anchor="center")
        adbrand = Label(infoframe, anchor="center", text=f"{i[3]}", font=("times new roman", 16, "bold"), bg="light blue", fg="black")
        adbrand.place(rely=0.68, relx=0.5, anchor="center")
        admodel = Label(infoframe, anchor="center", text=f"{i[4]}", font=("times new roman", 16, "bold"), bg="light blue", fg="black")
        admodel.place(rely=0.75, relx=0.5, anchor="center")
        shopbtn = Button(infoframe,command=lambda i=i: self.shop(i), text="SHOP NOW", bg="orange", fg="black",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
        shopbtn.place(relx=0.5, rely=0.9, anchor="center")

        c += 1

        if c == 4:
            c = 0
            r += 1



    def search(self):
      for widget in self.page4.winfo_children():
        if widget != self.page4.navbar:
         widget.destroy()

      canvas = Canvas(self.page4)
      canvas.pack(side=LEFT, fill=BOTH, expand=True)

      # Add a scrollbar to the canvas
      scrollbar = Scrollbar(self.page4, orient=VERTICAL, command=canvas.yview)
      scrollbar.pack(side=RIGHT, fill=Y)

      # Configure the canvas to use the scrollbar
      canvas.configure(yscrollcommand=scrollbar.set)
      canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

      frame = Frame(canvas)
      canvas.create_window((0, 0), window=frame, anchor="nw")

      # Here, repack the scrollbar onto the canvas
      scrollbar.config(command=canvas.yview)  # Update command of the scrollbar
      canvas.config(yscrollcommand=scrollbar.set)

      conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
      mycursor = conn.cursor()

      if self.searchbrand.get() == "ALL BRANDS":
        mycursor.execute("select *from products")
      else:
       mycursor.execute(f"select *from products where brand='{self.searchbrand.get()}' ")
       m, p = model_price(self.searchbrand.get())
       self.latestproduct(self.searchbrand.get(), m, p)
      row = mycursor.fetchall()
      
      self.create_page4_widgets(frame, row)

    def showpage7(self):
       self.show_page("page7")      

    def page6_widgets(self, email, ts):
       conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
       mycursor = conn.cursor()
       query = "select *from users where email = %s"
       mycursor.execute(query, (email,))
       res2 = mycursor.fetchone()

       canvas = Canvas(self.page6, width=self.page6.winfo_screenwidth(), height=self.page6.winfo_screenheight(), bg="white")
       canvas.pack(fill=BOTH, expand=True)
       

       self.create_circle_button(canvas, 1250, 200, 60, "brown", "A", 40)
    
       namelbl = Label(canvas, text=f"{self.fname} {self.lname}", bg="white", fg="black",font=("times new roman", 35, "bold"))
       namelbl.place(relx=0.7, rely=0.35)
       fromlbl = Label(canvas, text=f"Member since {res2[3]} {res2[4]}", bg="white", fg="black",font=("times new roman", 18, "bold"))
       fromlbl.place(relx=0.701, rely=0.42)
       editbtn = Button(canvas, command=self.showpage7, text="🖊️Edit Profile", bg="#085c5d", fg="white",font=("times new roman",16,"bold"), width=26, height=1, padx=2, pady=6)
       editbtn.place(relx=0.82, rely=0.56, anchor="center")

       if ts == 0:
          prolbl = Label(canvas, text="Your perfect deal is \n just around the corner! \n Keep your hopes high \n and your listings fresh.", bg="white", fg="black",font=("Georgia", 25, "bold", "italic"))
          prolbl.place(relx=0.24, rely=0.4)
          startsellbtn = Button(canvas, command=self.sellpage, text="Start Selling", bg="black", fg="white",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
          startsellbtn.place(relx=0.35, rely=0.65, anchor="center")
       else:
          prolbl = Label(canvas, text=f"Congradulations on {ts} \n successfull sales! 🎉🎈 \n Continue your journey with us!", bg="white", fg="purple",font=("Georgia", 25, "bold", "italic"))
          prolbl.place(relx=0.24, rely=0.4)
          startsellbtn = Button(canvas, command=self.sellpage, text="Start Selling", bg="black", fg="white",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
          startsellbtn.place(relx=0.4, rely=0.65, anchor="center")

       

                                                

       backbtn = Button(self.page6,text="<",command=self.go_back, bg="black", fg="white",font=("times new roman",25,"bold"), width=1,height=1, padx=2, pady=6)
       backbtn.place(relx=0.07, rely=0.35)
    
    def page7_widgets(self, fn, ln, mail):
        conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
        mycursor = conn.cursor()
        query = "select *from users where email=%s"
        mycursor.execute(query, (mail,))
        res = mycursor.fetchone()
        
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.contactnum = StringVar()
        self.gmail = StringVar()
        dataframe = Frame(self.page7, relief=RIDGE, bg="white")
        dataframe.place(relx=0.5, rely=0.47, anchor="center", width=900, height=750)

        edtttlabel = Label(dataframe, anchor="center", text="EDIT PROFILE", font=("times new roman", 42, "bold"), bg="white", fg="black")
        edtttlabel.pack(side=TOP, fill=X)

        can = Canvas(dataframe, width=1000, height=160, bg="white", highlightthickness=0)
        can.place(relx=0.4, rely=0.16)
        self.create_circle_button(can, 70, 70, 60, "brown", "A", 40)

        pplabel = Label(dataframe,  text="Profile Picture", font=("times new roman", 16), bg="white", fg="black")
        pplabel.place(relx=0.4, rely=0.34)

        fnlabel = Label(dataframe,  text="First Name", font=("times new roman", 18, "bold"), bg="white", fg="black")
        fnlabel.place(relx=0.15, rely=0.4)
        fnentry = Entry(dataframe, textvariable=self.firstname, font=("times new roman", 13, "bold"), width=25, bd=3)
        fnentry.place(relx=0.15, rely=0.45)
        fnentry.insert(0, f"{fn}")

        lnlabel = Label(dataframe,  text="Last Name", font=("times new roman", 18, "bold"), bg="white", fg="black")
        lnlabel.place(relx=0.6, rely=0.4)
        lnentry = Entry(dataframe, textvariable=self.lastname,  font=("times new roman", 13, "bold"), width=25, bd=3)
        lnentry.place(relx=0.6, rely=0.45)
        lnentry.insert(0, f"{ln}")

        abtlabel = Label(dataframe,  text="About me(optional)", font=("times new roman", 12, "bold"), bg="white", fg="black")
        abtlabel.place(relx=0.15, rely=0.52)
        abttext = Text(dataframe, font=("times new roman", 13, "bold"), width=58, height=3, bd=3)
        abttext.place(relx=0.45, rely=0.6, anchor="center")

        conlabel = Label(dataframe,  text="Contact Information", font=("times new roman", 14, "bold"), bg="white", fg="black")
        conlabel.place(relx=0.15, rely=0.72)
        phoneentry = Entry(dataframe, textvariable=self.contactnum,   font=("times new roman", 13, "bold"), width=25, bd=3)
        phoneentry.place(relx=0.15, rely=0.8)
        if res[7] is None:
         phoneentry.insert(0, "+91 | ")
        else:
           phoneentry.insert(0, f"{res[7]}")

        mailentry = Entry(dataframe,textvariable=self.gmail,   font=("times new roman", 13, "bold"), width=25, bd=3)
        mailentry.place(relx=0.15, rely=0.86)
        mailentry.insert(0, f"{mail}")

        savebtn = Button(dataframe, command=lambda: self.savechanges(self.gmail.get()), text="Save Changes", bg="black", fg="white",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
        savebtn.place(relx=0.8, rely=0.9, anchor="center")

        backbtn = Button(self.page7,text="<",command=self.go_back, bg="black", fg="white",font=("times new roman",25,"bold"), width=2,height=1, padx=2, pady=6)
        backbtn.place(relx=0.1, rely=0.35)

        conn.close()

    def savechanges(self, mail):
       conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
       mycursor = conn.cursor()
       query = "UPDATE users SET fname=%s, lname=%s, contact=%s WHERE email=%s"
       mycursor.execute(query, (self.firstname.get(), self.lastname.get(), self.contactnum.get(), mail))
       conn.commit()
       messagebox.showinfo("","Changes saved successfully!")
       conn.close()

    def page5widgets(self,i):
        backbtn = Button(self.page5,text="<",command=self.go_back, bg="black", fg="white",font=("times new roman",25,"bold"), width=2,height=1, padx=2, pady=3)
        backbtn.pack(side=LEFT)
        payframe = Frame(self.page5, relief=RIDGE, bg="grey")
        payframe.place(relx=0.5, rely=0.5, anchor="center", width=950, height=750)

        paylabel = Label(payframe, anchor="center", text=f"{i[3]} {i[4]}", font=("Roboto", 45, "bold"), bg="grey", fg="black")
        paylabel.pack(side=TOP, fill=X)
        
        temp_image_path = f"temp_image_{i[0]}.png"
        img = Image.open(temp_image_path)
        desired_width = 240
        desired_height = 240
        img = img.resize((desired_width, desired_height))
        photo = ImageTk.PhotoImage(img)
        self.img_label = Label(payframe, image=photo)
        self.img_label.image = photo
        self.img_label.place(relx=0.38, rely=0.18)

        pricelabel = Label(payframe, anchor="center", text=f"₹{i[5]} /-", font=("times new roman", 30, "bold"), bg="grey", fg="black")
        pricelabel.place(relx=0.45, rely=0.52)

        dlabel = Label(payframe,  text=f"{i[8]}", font=("times new roman", 18, "bold", "italic"), bg="grey", fg="black", wraplength=900, bd=1, relief="solid")
        dlabel.place(relx=0.06, rely=0.62)

        conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
        mycursor = conn.cursor()
        query = "select *from users where email=%s"
        mycursor.execute(query, (i[1],))
        res = mycursor.fetchone()
        if res[5] == None:
           match = re.search(r"^[^@._]+",i[1])
           if match:
                payee = match.group()
                payee2 = ""
        else:
           payee = res[5]
           payee2 = res[6]

        dlabel = Label(payframe,  text=f"Pay ₹{i[5]}/- to {payee} {payee2}", font=("Helvetica", 21), bg="grey")
        dlabel.place(relx=0.12, rely=0.85)



        paybtn = Button(payframe, command=lambda: self.payment(i), text=f"PAY ₹{i[5]}/-", bg="blue", fg="white",font=("times new roman",12,"bold"), width=12, height=1, padx=2, pady=6)
        paybtn.place(relx=0.8, rely=0.9, anchor="center")
       

        

    def shop(self, i):
       #sp = messagebox.askyesno(f"{i[3]} {i[4]}", f"Pay {i[5]}?")
       self.latestproduct(i[3], i[4], i[5])
       self.page5widgets(i)
       self.show_page("page5")

    def payment(self,i):
     sp = messagebox.askyesno(f"{i[3]} {i[4]}", f"Pay INR {i[5]}?")
     if sp > 0:
        bnd = i[3]
        mdl = i[4]
        conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
        mycursor = conn.cursor()
        mycursor2 = conn.cursor()
        query = "delete from products where product_id=%s"
        query2 = "select *from users where email=%s"
        mycursor.execute(query, (i[0],))
        mycursor2.execute(query2,(i[1], ))
        res = mycursor2.fetchone()
        ns = res[8] + 1
        q3 = "update users set totalsales = %s where email = %s"
        mycursor2.execute(q3,(ns,i[1]))
        conn.commit()
        messagebox.showinfo("Congradulations!", f"Your Order of {bnd} {mdl} confirmed")
        conn.close()

    def latestproduct(self, b, m, p):
       conn = mysql.connector.connect(host="localhost", username="root", password="addysql@13", database="pythonproject")
       mycursor = conn.cursor()

       if self.is_signup == 0:
          query = 'update useractivity set brand=%s, model=%s, price=%s, search_hist=%s where email=%s'
          mycursor.execute(query, (b, m, p, 1, self.usermail.get()))
       else:
          query = 'update useractivity set brand=%s, model=%s, price=%s, search_hist=%s where email=%s'
          mycursor.execute(query, (b, m, p, 1, self.usermail2.get()))


       conn.commit()
       conn.close()

    def feedrec(self,mail):
        self.page4.navbar = Frame(self.page4, bg="grey", height=80)
        self.page4.navbar.pack(fill=X)
        can = Canvas(self.page4.navbar, width=50, height=50, bg="grey", highlightthickness=0)
        can.place(relx=0.88, rely=0.15)
        self.create_circle_button(can, 25, 25, 20, "brown", "A", 12)
        
        
        backbtn = Button(self.page4.navbar,text="<",command=self.go_back, bg="black", fg="white",font=("times new roman",25,"bold"), width=2,height=1, padx=2, pady=3)
        backbtn.pack(side=LEFT)
        title_label = Label(self.page4.navbar, text="TechKart", fg="white", bg="grey", font=('Arial', 32, 'bold', 'italic') , padx=20, pady=20)
        title_label.place(relx=0.05, rely=-0.1)
        # Search bar
        search_frame = Frame(self.page4.navbar, bg="white", width=500, height=90)
        # search_frame.pack(side=RIGHT, padx=20, pady=20)
        search_frame.place(relx=0.3, rely=0.2)
        self.entry = ttk.Combobox(search_frame,textvariable=self.searchbrand, width=38, font=('Arial', 16))
        self.entry["values"] = ("ALL BRANDS","Asus", "BlackBerry", "Gionee", "Google Pixel", "Honor", "HTC", "Huawei", "Infinix", "Intex", "iPhone", "Karbonn","Lava", "Lenovo", "LG", "Mi", "Micromax", "Motorola", "Nokia", "One Plus", "Oppo", "Realme", "Samsung", "Sony", "Techno", "Vivo")
        self.entry.insert(0, 'Search Brands')
        self.entry.bind('<FocusIn>', self.on_entry_click)
        self.entry.bind('<FocusOut>', self.on_focus_out)
        self.entry.pack(side=LEFT, padx=(0, 10))
        search_button = Button(search_frame, text="Search", command=self.search, font=('Arial', 14))
        search_button.pack(side=LEFT)

        canvas = Canvas(self.page4)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(self.page4, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to contain the information
        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        row = rec(mail)
        self.create_page4_widgets(frame, row)

    def resetfields(self):
       self.brand.set("")
       self.model.set("")
       self.adtitle_entry.delete('1.0', END) 
       self.batcap.set(0)
       self.screensize.set(0)
       self.storage.set(0)
       self.ram.set(0)
       self.cam.set("")
       self.relyr.set(0)
       self.daysused.set(0)
       self.phonenum.set("")
       self.upload_btn.config(text="Upload Image")
          


        
    
       

root = Tk()
obj = Cart(root)
root.mainloop() 



    
