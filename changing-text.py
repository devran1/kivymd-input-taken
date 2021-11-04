#!/usr/bin/env python3


# importing all necessary modules
# like MDApp, MDLabel Screen, MDTextField
# and MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton

from kivy.lang import Builder

KV = '''
MDScreen:

    
    MDLabel:
        id:label_id
        text: 'update this at on enter'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        halign: 'center'
        

    MDRectangleFlatButton:
        id:btn      
        text:"Submit"      
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.btnfunc()
        
'''



class Demo(MDApp):

    def build(self):        
        return Builder.load_string(KV)
    
    def btnfunc(self):
        
        print("button is pressed!!")

        written=open("page.txt","r")
        a=written.readlines()
 
        self.root.ids["label_id"].text=str(a)
        
        
   
if __name__ == "__main__":
    Demo().run()
