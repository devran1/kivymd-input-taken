#!/usr/bin/env python3


# importing all necessary modules
# like MDApp, MDLabel Screen, MDTextField
# and MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
 
# creating Demo Class(base class)
class Demo(MDApp):
    #global nam #when you call global you can call from other function (use self)
    #nam=input("input :")
    def build(self):
        screen = Screen()
        global name
        #name=input("Enter:") 
        #real_name += name
        
        # defining label with all the parameters
        l = MDLabel(text="HI PEOPLE!", halign='center',
                    theme_text_color="Custom",
                    text_color=(0.5, 0, 0.5, 1),
                    font_style='Caption')
         
        # defining Text field with all the parameters
        name = MDTextField(text="name", pos_hint={'center_x': 0.8, 'center_y': 0.8},size_hint_x=None, width=100)
        print(name.text)
        
        btn1 = MDRectangleFlatButton(text="Submit", pos_hint={'center_x': 0.8, 'center_y': 0.9},on_release=self.btnfunc1)
        if btn1 is True:
            print("hey")
         
        # defining Button with all the parameters
        btn = MDRectangleFlatButton(text="Submit", pos_hint={'center_x': 0.5, 'center_y': 0.3},on_release=self.btnfunc)
       
        # adding widgets to screen
        screen.add_widget(name)
        screen.add_widget(btn)
        screen.add_widget(btn1)
        screen.add_widget(l)
        # returning the screen
        return screen
 
    # defining a btnfun() for the button to
    # call when clicked on it
    def btnfunc(self, obj):
        print("button is pressed!!")
 
    def btnfunc1(self, obj):

       print(name.text)
        
        
        #print("pressed")
        #yield name

        #print(name)	 	
 
    pass

if __name__ == "__main__":
    Demo().run()
