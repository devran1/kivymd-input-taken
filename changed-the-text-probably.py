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
        id: label1
        text: "Hello, World!"
        halign: "center"

  

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
    


    #b=MDLabel.ids["label1"].text
    
   
        #screen = Screen()
        #global name,l,btn
            
        
        #name = MDTextField(text="name", pos_hint={'center_x': 0.8, 'center_y': 0.8},size_hint_x=None, width=100)
        
            
        #btn = MDRectangleFlatButton(text="Submit", pos_hint={'center_x': 0.5, 'center_y': 0.3},on_release=self.btnfunc)
        

        #written=open("page.txt","r")

        #a=written.readlines()

        #return screen

    def btnfunc(self):
        
        print("button is pressed!!")


        written=open("page.txt","r")

        a=written.readlines()

    #    self.ids["label_id"].text = a    
        self.root.ids["label_id"].text=str(a)
        
        #written=l.text
        #print(written)
       
    #    written=name.text
    #    print(written)

    #    report=open("page.txt","w")
    #    report.write(name.text)   
        
    #    if btn.on_release == self.btnfunc:

            #written=l.text

            #written=name.text

        #openit=open("page.txt","r")
        #this_text=openit.readlines()
        #for i in range(2):
        #l=MDLabel(text=name.text, halign='center',theme_text_color="Custom",text_color=(0.5, 0, 0.5, 1),font_style='Caption')
        
    #def update(self,obj):
    #    with open("page.txt","r") as file :
    #        f=file.read()   
    #        screen = Screen()
    #        l=MDLabel(text=str(f), halign='center',theme_text_color="Custom",text_color=(0.5, 0, 0.5, 1),font_style='Caption')
    #        screen.add_widget(l)

    #    return    

#    def forgot_password(self):
#        print(self.screen.get_screen('forgot_email').ids.forgot_email.text)

#class MenuScreen(MDApp):
    #pass
    #def on_enter(self): #ids ~name ?
    #    self.ids.label_id.text = "Label text Updated"    

if __name__ == "__main__":
    Demo().run()
