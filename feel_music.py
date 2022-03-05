
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from pytube import YouTube
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import os, sys


KV = """
MyBL:
        orientation: "vertical"
        size_hint:(0.95, 0.95)
        pos_hint:{"center_x": 0.5, "center_y": 0.5}
        hello_lable: hello
        
        
        Label:
                font_size:"20sp"
                text: root.data_label
                
        TextInput:
                id:Inp
                multiline: False
                padding_y: (5,5)
                padding_x: (5,5)
                size_hint:(1,0.3)
                on_text: app.process()
                background_color: [99/255.0, 97/255.0, 97/255.0, 1]
                
                foreground_color: [87/255.0, 16/255.0, 16/255.0, 1]
                
                
                

        Button:
                text: "Download"
                bold: True
                background_color:'#571010'
                size_hint:(1,0.4)
                background_down: '#808080'
                
                on_press: root.callback()
                
        Label:
                font_size:"15sp"
                size_hint:(1,0.1)
                id: hello
                

"""
Window.clearcolor = (73/255.0, 72/255.0, 74/255.0, 1)
class MyBL(BoxLayout):
    data_label = StringProperty("Введи ссылку на видео YouTube")
    hello_lable = ObjectProperty()
    
    #db = ObjectProperty()
    def callback(self):
        print("Out")
        try:
            yt_obj = YouTube(text)

            yt_obj.streams.get_audio_only().download(output_path= 'Внутренний общий накопитель\Music', filename=f'{yt_obj.title}.mp3')
            
            print('Video Downloaded Successfully')
            
            
        except Exception as e:
            print(e)
        self.hello_lable.text = 'Video Downloaded Successfully'

class MyApp(App):
    running = True
    def process(self):
        global text
        text = self.root.ids.Inp.text
        return text
    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False

MyApp().run()