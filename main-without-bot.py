#!/usr/bin/env python3

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton

from kivy.lang import Builder


###input is been read
KV = '''
MDScreen:

    MDTextField:
        id:name
        text: "name"
        pos_hint: {'center_x': 0.8, 'center_y': 0.8}
        size_hint_x: None
        width: 100

    
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
    
    def for_writing(self):
        #input
        names=self.root.ids["name"].text
        
        print(names)
        
    #    with open("page.txt","w") as thisW:
    #        thisW.write(str(names))



    def btnfunc(self):
       
        #names=self.root.ids["name"].text
        #print(names)
        
        #this_w=open("page.txt","w")
        #b=this_w.writelines(names)

        written=open("page.txt","r")
        a=written.readlines()
 

        ####write here
        self.root.ids["label_id"].text=str(a)
    
    
        
        
   
if __name__ == "__main__":
    Demo().run()
