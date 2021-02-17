import Tkinter as tk
from Tkinter import *

class Binario:
   peso = None

   def __init__(self):
        self.peso = None

   #Funcion para generar tablas dependiendo del numero de variables que se van a usar
   
   def calcular(self, restri, vari, ttablas, ttablasa, marc1):
      listacon = []
      listautil = []
      var = int(vari)
      restr = int(restri)
      #Listas de restricciones y variables
      for i in range(var):
         listacon.append(int (ttablas['tabla'+str(i+1)].get()))
      for i in range(var):
         listautil.append(int (ttablasa['tablaa'+str(i+1)].get()))
      
      print(listacon)
      print(listautil)
      print(var)
      print(restr)

      
      K = [[0 for x in range(restr + 1)] for x in range(var + 1)]
      #Tabla de abajo hacia arriba
      for i in range(var + 1):
         for w in range(restr + 1):
            if i == 0 or w == 0:
               K[i][w] = 0
            elif listacon[i-1] <= w:
               K[i][w] = max(listautil[i-1] + K[i-1][w-listacon[i-1]], K[i-1][w])
            else:
               K[i][w] = K[i-1][w]
       # Devuelve el valor máximo de beneficio que puede almacenar la bolsa
      
      print(var)
      result1= tk.StringVar()

      Titulo1 = tk.Label(marc1, text="         Valor Z           ", bg="yellow").grid(row=11,column=0)

      etiqueta1=tk.Label(marc1, textvariable = result1)
      etiqueta1.grid(row=12, column=0)

      # Muestra el valor en pantalla

      result1.set(K[var][restr])
      print(var)
      
   # Funcion definida para ingresar los valores de restricciones y variables
   
   def ingresar_variables(self, nodos, nodo, marc):
      tablas = dict()
      tablasa = dict()
      Titulo3 = tk.Label(marc, text="         Ingresar  condicion        ", bg="yellow").grid(row=8,column=0)
      Titulo4 = tk.Label(marc, text="          Ingresar  utilidad        ", bg="yellow").grid(row=9,column=0)
      restriccion = int(nodos)
      variable = int(nodo)
      # Se generan los espacios para ingresar condiciones
      for i in range(variable):
         tablas['tabla'+str(i+1)] = Entry(marc)
         tablas['tabla'+str(i+1)].pack()
         tablas['tabla'+str(i+1)].grid(row=8,column=i+1)
         print(variable)
      # Se generan los espacios para ingresar utilidades
      for i in range(variable):
         tablasa['tablaa'+str(i+1)] = Entry(marc)
         tablasa['tablaa'+str(i+1)].pack()
         tablasa['tablaa'+str(i+1)].grid(row=9,column=i+1)
         print(variable)
      Texto112 = tk.Label(marc, text="___________________________________________________").grid(row=10,column=0)
      # Se llama pasan las varibles para realizar los calculos en la funcion
      btnInsertarVar = Button(marc,text='Ingresar', command=lambda: binario.calcular(restriccion, variable, tablas, tablasa ,marc)).grid(row=10,column=1,sticky=tk.W,pady=4)
      
   # Funcion donde se define la interfaz grafica 
   def iniciar(self):
      marco=tk.Tk()
      marco.title("Binario")
      marco.geometry("1400x600")
      marco.configure(background="#000000")

      # Espacio para ingresar la restriccion
      
      Titulo1 = tk.Label(marco, text="         Ingresar restriccion           ", bg="yellow").grid(row=0,column=0)
      Texto1 = tk.Label(marco, text="Numero").grid(row=1,column=0)
      e1 = Entry(marco)
      e1.pack()
      e1.grid(row=2,column=0)

      # Espacio para ingresar el numero de varibles a utilizar

      Titulo2 = tk.Label(marco, text="    Ingresar numero de variables    ", bg="yellow").grid(row=4,column=0)
      Texto2 = tk.Label(marco, text="Numero").grid(row=5,column=0)
      e2 = Entry(marco)
      e2.pack()
      e2.grid(row=6,column=0)

      # Se generan los espacios para ingresar los datos necesarios para que el programa funcione
   
      Texto111 = tk.Label(marco, text="___________________________________________________").grid(row=7,column=0)
      btnInsertar = Button(marco,text='Ingresar', command=lambda: binario.ingresar_variables(e1.get(),e2.get(),marco)).grid(row=7,column=1,sticky=tk.W,pady=4)
      
      marco.mainloop()


binario = Binario()
binario.iniciar()
