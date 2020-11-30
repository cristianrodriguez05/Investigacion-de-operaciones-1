import Tkinter as tk
from Tkinter import *

class Binario:
   peso = None

   def __init__(self):
        self.peso = None
   
   def calcular(self, var, ttablas, ttablasa, marc1):
      print(ttablas)
      K = [[0 for x in range(W + 1)] for x in range(n + 1)]
      #Tabla de abajo hacia arriba
      for i in range(n + 1):
         for w in range(W + 1):
            if i == 0 or w == 0:
               K[i][w] = 0
            elif wt[i-1] <= w:
               K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
               K[i][w] = K[i-1][w]
       # Devuelve el valor máximo de beneficio que puede almacenar la bolsa
      return K[n][W]
   #Main

   def ingresar_variables(self, nodo, marc):
      tablas = dict()
      tablasa = dict()
      Titulo3 = tk.Label(marc, text="         Ingresar  condicion        ", bg="yellow").grid(row=8,column=0)
      Titulo4 = tk.Label(marc, text="          Ingresar  utilidad        ", bg="yellow").grid(row=9,column=0)
      variable = int(nodo)
      for i in range(variable):
         tablas['tabla'+str(i+1)] = Entry(marc)
         tablas['tabla'+str(i+1)].pack()
         tablas['tabla'+str(i+1)].grid(row=8,column=i+1)
         print(variable)
      for i in range(variable):
         tablasa['tablaa'+str(i+1)] = Entry(marc)
         tablasa['tablaa'+str(i+1)].pack()
         tablasa['tablaa'+str(i+1)].grid(row=9,column=i+1)
         print(variable)
      Texto112 = tk.Label(marc, text="___________________________________________________").grid(row=10,column=0)
      btnInsertarVar = Button(marc,text='Ingresar', command=lambda: binario.calcular(variable, tablas, tablasa ,marc)).grid(row=10,column=1,sticky=tk.W,pady=4)

      
   def iniciar(self):
      marco=tk.Tk()
      marco.title("Binario")
      marco.geometry("1400x600")
      marco.configure(background="#f2f2d4")


      Titulo1 = tk.Label(marco, text="         Ingresar restriccion           ", bg="yellow").grid(row=0,column=0)
      Texto1 = tk.Label(marco, text="Numero").grid(row=1,column=0)
      e1 = Entry(marco)
      e1.pack()
      e1.grid(row=2,column=0)

      Titulo2 = tk.Label(marco, text="    Ingresar numero de variables    ", bg="yellow").grid(row=4,column=0)
      Texto2 = tk.Label(marco, text="Numero").grid(row=5,column=0)
      e2 = Entry(marco)
      e2.pack()
      e2.grid(row=6,column=0)

      Texto111 = tk.Label(marco, text="___________________________________________________").grid(row=7,column=0)
      btnInsertar = Button(marco,text='Ingresar', command=lambda: binario.ingresar_variables(e2.get(),marco)).grid(row=7,column=1,sticky=tk.W,pady=4)
      
      marco.mainloop()


binario = Binario()
binario.iniciar()

#val = [100,60,70,15,9]
wt = [42,23,21,15,7]
W = 60
n = len(val)
