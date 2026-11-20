from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class mojaApka(App):
    def build(self):
        plocha = BoxLayout(orientation = "vertical")

        cast_in_out = BoxLayout()
        self.input = TextInput(hint = "Zadaj cm")
        self.output = Label(text = " ")
        cast_in_out.add_widget(self.input)
        cast_in_out.add_widget(self.output)