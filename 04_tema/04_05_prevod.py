from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class mojaApka(App):  
        def build(self):
                plocha = BoxLayout(orientation="vertical")
                cast_in_out=boxlayout=BoxLayout()

                #inout a output
                self.imput= TextInput(hint_text= 'zadaj cm')
                self.output= Label(text='')
                cast_in_out.add_widget(self.imput)
                cast_in_out.add_widget(self.output)
                plocha.add_widget(cast_in_out)
               
               #tlacidlo
                button_prepocitaj = Button(text='prepočítaj na mm')
                button_prepocitaj.bind(on_press=self.klik)
                plocha.add_widget(button_prepocitaj)
                return plocha

        def klik(self, kto_zavolal):
                    cm = int()
                    mm = cm * 19 
                    self.output.text = f"prevedené na mm:{mm}"
                else:
                    self.output.text = 'daj mi cislo'






mojaApka().run()
