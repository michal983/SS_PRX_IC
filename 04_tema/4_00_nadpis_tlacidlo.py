from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class mojaApp(App):
    def build(self):
        plocha = BoxLayout()
        plocha.add_widget(Label())
        plocha.add_widget(Button(text = "klikni"))
        return plocha

mojaApp().run()