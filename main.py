from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

# Include Kivy Design File
Builder.load_file('calc.kv')

# Window Resize
Window.size = (500,600)

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    
    # Button Press
    def button_press(self, button):
        prior = self.ids.calc_input.text

        if 'Error' in prior:
            prior = ''

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # Sign Button
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    # Equels Button
    def equels(self):
        prior = self.ids.calc_input.text

        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'Error'
        

    # Dot Button
    def dot(self):
        prior = self.ids.calc_input.text
        
        if '.' in prior:
            pass
        else:
            prior = f"{prior}."
            self.ids.calc_input.text = prior

    # Remove Button
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    # Pas_neg Button
    def pos_neg(self):
        prior = self.ids.calc_input.text

        if "-" in prior:
            self.ids.calc_input.text = f"{prior.replace('-','')}"
        else:
            self.ids.calc_input.text = f"-{prior}"


class CalculaterApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculaterApp().run()