from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MojaApp(App):
    def build(self) -> BoxLayout:
        koren = BoxLayout(orientation="vertical")
        koren.add_widget(Label(text="Zatiaľ nič"))
        koren.add_widget(Button(text="Klikni ma"))
        return koren

MojaApp().run()