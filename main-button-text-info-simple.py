#!/usr/bin/env python3


# importing all necessary modules
# like MDApp, MDLabel Screen, MDTextField
# and MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
 


class Demo(MDApp):
    
    def build(self):
        screen = Screen()
        global name
        
        name = MDTextField(text="name", pos_hint={'center_x': 0.8, 'center_y': 0.8},size_hint_x=None, width=100)
        
 
        btn1 = MDRectangleFlatButton(text="Submit", pos_hint={'center_x': 0.8, 'center_y': 0.9},on_release=self.btnfunc1)
      
        
       
        screen.add_widget(name)
      
        screen.add_widget(btn1)
 
        return screen

       
    def btnfunc1(self, obj):

       print(name.text)
            
    pass

if __name__ == "__main__":
    Demo().run()
