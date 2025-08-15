import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.uix.behaviors import ButtonBehavior

class imgbtn(ButtonBehavior, Image):
   def __init__(self, **kwargs):
      super(imgbtn, self).__init__(**kwargs)
   def on_press(self):
      GuiLayouts.l1.text=self.source

class GuiLayouts(App):
    

    def build(self):

        self.window= FloatLayout()
        self.window.cols= 1
        self.window.size = (1440, 1024)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        #LabelBase.register(name='HeadingFont' , fn_regular='Jaini-Regular.tff')

        self.topLabel = Label(
            text='Enemy Tracker',
            #font_name='HeadingFont' ,
            pos= (0 , 240),
            font_size = 96
        )
        self.window.add_widget(self.topLabel)

        self.window.add_widget(
           Image(
              source='assets/divider.gif' ,
              pos = (0, 170)
           )
        )

        self.window.add_widget(
            imgbtn(
                  source='assets/createmonsterbutton.png',
                  pos = (-200,85)
      )
        )
        return self.window