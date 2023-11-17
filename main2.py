from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

def multiplicar(a,b):
    resultado=a*b
    return resultado
def dividir(a,b):
    resultado=a/b
    return resultado
def sumar(a,b):
    resultado=a+b
    return resultado
def restar(a,b):
    resultado=a-b
    return resultado
def correr():
    MyApp().run()
class MainApp(App):
    def build(self):
        layout1 = BoxLayout(orientation='vertical', padding=40)
        button45 = Button(text='Multiplicar', on_press=self.togo)
        layout1.add_widget(button45)
        
           
        return layout1
    
    def togo(self,instance):
            correr()
    
    
    

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40)
        
        self.input_text1 = TextInput(hint_text='Ingresa dato', multiline=False)
        self.input_text2 = TextInput(hint_text='Ingresa dato', multiline=False)
        self.output_label = Label(text='Texto de salida')
        
        button1 = Button(text='Multiplicar', on_press=self.paramultiplicar)
        button2 = Button(text='Dividir', on_press=self.paradividir)
        button3 = Button(text='Sumar', on_press=self.parasumar)
        button4 = Button(text='Restar', on_press=self.pararestar)
        button5 = Button(text='Limpiar', on_press=self.limpiar)
        button6 = Button(text='XD', on_press=self.XD)
        
        layout.add_widget(self.input_text1)
        layout.add_widget(self.input_text2)
        layout.add_widget(self.output_label)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)
        layout.add_widget(button6)
        
        layout2 = BoxLayout(orientation='vertical', padding=40)
        boton55 = Button(text='Limpiar')
        layout2.add_widget(boton55)
        
        
        
        return layout
    
    def paramultiplicar(self, instance):
        text1 = self.input_text1.text
        text2 = self.input_text2.text
        resultado=multiplicar(int(text1),int(text2))
        self.output_label.text = str(resultado)
        
    def paradividir(self, instance):
        text1 = self.input_text1.text
        text2 = self.input_text2.text
        resultado=dividir(int(text1),int(text2))
        self.output_label.text = str(round(resultado,4))
        
    def parasumar(self, instance):
        text1 = self.input_text1.text
        text2 = self.input_text2.text
        resultado=sumar(int(text1),int(text2))
        self.output_label.text = str(round(resultado,4))
        
    def pararestar(self, instance):
        text1 = self.input_text1.text
        text2 = self.input_text2.text
        resultado=restar(int(text1),int(text2))
        self.output_label.text = str(round(resultado,4))
        
    def limpiar(self, instance):
        self.output_label.text = 'Inserte nuevo dato'  
        self.input_text1.text= 'Ingrese dato'
        self.input_text2.text= 'Ingrese dato'
        
    def XD(self,instance):
        self.output_label.text = 'buenas'    
        

if __name__ == '__main__':
    MainApp().run()