import os
from tkinter import *
import os, json
from PIL import Image, ImageTk
import tkinter.font as TkFont
from classes.mail.e_mail import EmailClass
from classes.common import CommonFunctions

class myClass:

    def __init__(self):
        """ Main App Setup """

        self.ENTER_COLOUR = '#ADD8E6'
        self.DO_NOT_ENTER = '#E6ADAD'
        self.chatCounter = 0 # Need To Update
        self.CommonObj = CommonFunctions()
        self.PATH = self.CommonObj.get_path()
        # self.get_path() # Update Path To Correct

        self.win = Tk() # Creating a win
        self.win.geometry("480x320") # Setting Dimensions of R-Pi Screen
        self.win.configure(background=self.ENTER_COLOUR) # Setting Default Background Colour
        self.emailClient = EmailClass(self.PATH)

    def create_default_main_page_and_place(self): # Load_Default (Renamed)?

        # Create Enter Icon For Main Page
        image = ImageTk.PhotoImage(Image.open(self.PATH + "assets/images/ok.png")) # no
        self.lbl_enterIcon = Label(self.win, bg=self.ENTER_COLOUR)
        self.lbl_enterIcon.configure(image=image)
        self.lbl_enterIcon.image = image

        # Create Enter Text For Main Page
        i_font = TkFont.Font(family="Century",size=20,slant="italic")
        self.lbl_enterText = Label(self.win,text="You May Enter!", bg=self.ENTER_COLOUR, font=i_font)

        # Create Message Icon To Direct User To Message Page
        self.btn_messageIcon = Button(self.win, width=70,height=50, highlightthickness = 0, bd = 0)
        self.btn_messageIcon.config(bg=self.ENTER_COLOUR)
        image = ImageTk.PhotoImage(Image.open(self.PATH + "assets/images/message-icon.png"))
        self.btn_messageIcon.configure(image=image, command=self.change_screen) # command=self.change
        self.btn_messageIcon.image = image

        # Place / Pack Items Into Display Window
        self.lbl_enterIcon.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.lbl_enterText.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.btn_messageIcon.pack(side=TOP, anchor="e")


    def create_message_page_widgets(self):

        i_font = TkFont.Font(family="Century",size=10)
        self.button_frame = Frame(background=self.ENTER_COLOUR)
        self.x = Button(self.button_frame, text='Need Your Help, \n With My Computer!', padx=10, height=5, font=i_font)
        self.x.configure(command=lambda: self.sendEmail(0))
        self.y = Button(self.button_frame, text='Emergency SOS, \nUrgent', padx=10, height=5, font=i_font)
        self.y.configure(command=lambda: self.sendEmail(1))
        self.z = Button(self.button_frame, text='Can You \nFeed The Horses?', padx=10, height=5, font=i_font)
        self.z.configure(command=lambda: self.sendEmail(2))

    def sendEmail(self, messageCode):

        self.change_screen() # Return User To Main Screen.
        self.emailClient.send_email(messageCode)
        # self.sendEmail2('Test Message') # Testing


    def get_path(self):
        """ Returns Path for assets """

        self.PATH = '/home/pi/test-python/' # Setting Initial Path

        try:
            # If works running on linux env.
            os.uname()
        except:
            # Else running on local dev machine. i.e. windows
            self.PATH = ''
        finally:
            return self.PATH

    def change_screen(self):
        # (TO DO) - Also Need A Timeout to return to original screen.
        # Open Message Menu

        with open(self.PATH +"assets/config.json") as f:
            data = json.load(f)
            print(data)

        if data['ChatOpen'] == 1:
            # Hide Message Screen - Currently On Message Screen
            # MESSAGE_SCREEN_VISABLE = 0
            print("Reset")

            self.chatCounter = 0

            # Return To Default Settings
            # button2.pack(side=TOP, anchor="e")

            if data['InMeeting'] == 1:
                self.button_frame.configure(background='#ff3333')
            else:
                self.button_frame.configure(background=self.ENTER_COLOUR)

            self.button_frame.place_forget()
            self.x.grid_forget()
            self.y.grid_forget()
            self.z.grid_forget()

            # button_frame.grid_forget()

            image = ImageTk.PhotoImage(Image.open(self.PATH + "assets/images/message-icon.png"))
            self.btn_messageIcon.configure(image=image)
            self.btn_messageIcon.image = image

            self.lbl_enterIcon.place(relx=0.5, rely=0.4, anchor=CENTER)

            self.lbl_enterText.place(relx=0.5, rely=0.7, anchor=CENTER)

            data['ChatOpen'] = 0
            with open(self.PATH +"assets/config.json", 'w') as f:
                json.dump(data, f)
        else:
            # Show Message Screen
            # MESSAGE_SCREEN_VISABLE = 1

            self.chatCounter = 10

            data['ChatOpen'] = 1
            with open(self.PATH +"assets/config.json", 'w') as f:
                json.dump(data, f)

            # Hide buttons
            self.lbl_enterText.place_forget()
            self.lbl_enterIcon.place_forget()

            # Update Button 2 Image To Return Icon
            image = Image.open(self.PATH + "assets/images/no.png") # no - to do need return icon here
            resize_image2 = image.resize((50,50) , resample=3)
            img1 = ImageTk.PhotoImage(resize_image2)

            self.btn_messageIcon.configure(image=img1)
            self.btn_messageIcon.image = img1

            self.button_frame.place(relx=0.5, rely=0.5, anchor=CENTER) #.pack(side = 'center', fill = 'x')

            self.button_frame.columnconfigure(1, weight=1)
            self.x.grid(row=0, column=0, padx=6)
            self.y.grid(row=0, column=1, padx=6)
            self.z.grid(row=0, column=2, padx=6)

            self.button_frame.place(relx=0.5, rely=0.5, anchor=CENTER) #.pack(side = 'center', fill = 'x')


    def check_for_update_event_loop(self, name, CONFIG_FILE_LAST_UPDATED):
        """ # This function will be run every N milliseconds
        try to open the file and set the value of val to its contents
        """

        try:
            print(os.path.getmtime(self.PATH + 'assets/config.json'))
            print("Last Updated: " + str(CONFIG_FILE_LAST_UPDATED))

            print(self.chatCounter)

            if self.chatCounter > 0:
                print(self.chatCounter)
                if self.chatCounter == 1:
                    self.change_screen()
                self.chatCounter = self.chatCounter - 1


            if os.path.getmtime(self.PATH + 'assets/config.json') != CONFIG_FILE_LAST_UPDATED:
                CONFIG_FILE_LAST_UPDATED = os.path.getmtime(self.PATH + 'assets/config.json')
                # print("Update Found!")

                with open(name) as f:
                    data = json.load(f)
                    print(data)

                if int(data['InMeeting']) == 1:
                    # In Meeting = YES
                    print("UPDATE in Meeting")
                    self.lbl_enterText.configure(text='Do Not Enter!')
                    self.win.configure(background=self.DO_NOT_ENTER) # Repeating Code - Break Into Method Call
                    self.btn_messageIcon.configure(bg=self.DO_NOT_ENTER)
                    self.lbl_enterIcon.configure(bg=self.DO_NOT_ENTER)
                    self.lbl_enterText.configure(bg=self.DO_NOT_ENTER)

                    image = ImageTk.PhotoImage(Image.open(self.PATH + "assets/images/no.png")) # no
                    self.lbl_enterIcon.configure(image=image)
                    self.lbl_enterIcon.image = image
                    self.button_frame.configure(background=self.DO_NOT_ENTER)


                elif int(data['InMeeting']) == 3:
                    pass
                else:
                    # Not In Meeting = NO
                    self.lbl_enterText.configure(text='You May Enter!')
                    self.win.configure(background=self.ENTER_COLOUR)
                    # img = PhotoImage(file= path + "no.png") # message-icon.png
                    self.btn_messageIcon.configure(bg=self.ENTER_COLOUR)
                    self.lbl_enterIcon.configure(bg=self.ENTER_COLOUR)
                    self.lbl_enterText.configure(bg=self.ENTER_COLOUR)

                    image = ImageTk.PhotoImage(Image.open(self.PATH + "assets/images/ok.png")) # ok
                    self.lbl_enterIcon.configure(image=image)
                    self.lbl_enterIcon.image = image
                    self.button_frame.configure(background=self.ENTER_COLOUR)

        except IOError as e:
            print(e)
        else:
            # schedule the function to be run again after 1000 milliseconds
            self.win.after(1000,lambda: self.check_for_update_event_loop(name, CONFIG_FILE_LAST_UPDATED))