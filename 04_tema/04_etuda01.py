from kivy.app import App
from kivy.uix.button import Button

class MojaApp(App):
    def build(self) -> Button:
        tlacidlo = Button(text="Klikni ma")
        tlacidlo.bind(on_press=self.klik)   # keď sa stlačí, zavolaj funkciu self.klik
        return tlacidlo

    def klik(self, instancia):
        print("Niekto ma klikol!")

MojaApp().run()