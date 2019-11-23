
import pyodbc as p
import Data_Fetch as df

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

conn = p.connect('DSN=ORIGIN;Server=localhost;Database=DERECHOS;Trusted_Connection=yes;')
cursor = conn.cursor()



class MyGrid(Widget):

    ide = ObjectProperty(None)
    nombre = ObjectProperty(None)
    apellido = ObjectProperty(None)

    def insert(self):
        idgen = int(self.ide.text)
        nombre = self.nombre.text
        apellido = self.apellido.text

        print("Id: ", idgen, "\nnombre: ", nombre, "\napellido: " , apellido)
        cursor.execute("INSERT INTO DERECHOS.dbo.Generador VALUES('%d' , '%s' , '%s')" %(idgen,nombre,apellido))
        conn.commit()
        self.ide.text = ""
        self.nombre.text = ""
        self.apellido.text = ""

    def check(self):
        df.show()



class  MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()