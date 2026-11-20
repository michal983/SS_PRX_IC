from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class mojaApka(App):
    def build(self):
        plocha = BoxLayout(orientation = "vertical")

        self.pocet_klikov = 0
        self.popisok = Label(text = "zatial nic" + str(self.pocet_klikov) + "kliknutí")
        plocha.add_widget(self.popisok)

        tlacidlo = Button(text = "klikni ma")
        tlacidlo.bind(on_press = self.klik)
        plocha.add_widget(tlacidlo)

        return plocha

    def klik(self,kto_zavolal):
        self.pocet_klikov += 1
        self.popisok.text = f"Michal,klikol si {self.pocet_klikov}"


mojaApka().run()