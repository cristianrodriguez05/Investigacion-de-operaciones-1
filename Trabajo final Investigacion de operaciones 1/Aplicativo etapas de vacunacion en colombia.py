import Tkinter as tk
from Tkinter import *
import Tkinter 
import tkMessageBox
#libreria usada Tkinter

class Binario:
   vacuna = None

   def __init__(self):
        self.vacuna = None

        
   #funcion para mostrar resultado en pantalla
   def resultadofinal(self, nombre, valor):
      
      etapa = "-----------------------"
      mensaje = "------------------------"
      fecha = "-------------------------"
      #seleccion del mensaje a mostrar deacuerdo a los datos obtenidos deacuerdo al maximo valor de beneficio y bnjo la restriccion
      if valor > 100000:
         etapa= "Etapa I"
         mensaje= "Talento humano en salud en primera línea, personal de apoyo asistencial,personal de servicios generales y administrativos, adultos mayores de 80 años."
         fecha = "20 de Febrero de 2021"
      elif valor > 10000:
         etapa= "Etapa II"
         mensaje= "Talento humano en salud que no está en primera línea, adultos entre los 60 y 79 años."
         fecha = "Por definir"
      elif valor > 1000:
         etapa= "Etapa III"
         mensaje= "Profesores, personal de Fuerzas Militares y Policía, población de 16 a 59 años con comorbilidades."
         fecha = "Por definir"
      elif valor > 100:
         etapa= "Etapa IV"
         mensaje= "Personal de instituciones de prevencion del riesgo, cuidadores institucionales y poblaciones con menor riesgo de transmisión."
         fecha = "Por definir"
      elif valor > 10:
         etapa= "Etapa V"
         mensaje= "Personas entre los 15 y 59 años sin comorbilidades"
         fecha = "Por definir"
      else:
         etapa = "Fila de espera"
         mensaje = "Las personas segun cambios en los parametros establecidos para personas menores de 16 años y mujeres en estado de gestacion"
         fecha = "Por definir"
      # se muestra el resultado con los datos ingresados y se da una respuesta de la vacunacion
      tkMessageBox.showinfo('Resultado aplicativo de vacunacion',"Usted  " + nombre + "\n\n"  + "Pertenece a la  "+ etapa + "\n\n" + "En esta etapa las vacunas seran destinadas a:" + "\n\n" + mensaje+ "\n\n"+ "Fecha para inicio de vacunacion de la etapa:" + "\n\n" + fecha)



   
   def calcular(self, nombre,saludp,saluds,enfermedadd,edadd,institutoo, marc1):

      #variable con los valores de los datos de la funcion anterior
      valor=saludp+saluds+enfermedadd+edadd+institutoo
      listacon = []
      listautil = []
      var = 1
      restr = 300000 
      listacon.append(valor)
      listautil.append(valor) 
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
       # Devuelve el valor máximo de beneficio que puede conseguirse
       
      resultado= K[var][restr]
      print("         El Valor Z es igual a:         ")
      print(resultado)
      # se envai el valor de resultado a la funcion resultadofinal para mostrar los resultados correspondientes
      binario.resultadofinal(nombre,resultado)
      
   #funcion para unificar datos en variables unicas
   def ingresar_variables(self, nombre, edad1, salud1,enf1, enf2,enf3,enf4,enf5,enf6,enf7,enf8,enf9,enf10,instituto,marc):
      
      saludpri = IntVar()
      saludseg = IntVar()
      enfermedad = IntVar()
      edadval = IntVar()
      institutoval = IntVar()
      edad = int(edad1)
      salud = int(salud1)
      enfermedad = 0

      #variable unica edad
      if edad >= 80:
         edadval = 100000
      elif edad >= 60:
         edadval = 10000
      elif edad >= 16:
         edadval = 10
      else:
         edadval = 1

      #variables unicas saludseg y saludpri, derivadas de la varible salud
      if salud != 9 and salud !=10:
         saludpri = 100000
         saludseg = 1
      elif salud == 9:
         saludseg = 10000
         saludpri = 1
      else:
         saludseg = 1
         saludpri = 1
         
      #variable unica enfermedad
      if enf1 == True:
         enfermedad = enfermedad + 1000
      if enf2 == True:
         enfermedad = enfermedad + 1000
      if enf3 == True:
         enfermedad = enfermedad + 1000
      if enf4 == True:
         enfermedad = enfermedad + 1000
      if enf5 == True:
         enfermedad = enfermedad + 1000
      if enf6 == True:
         enfermedad = enfermedad + 1000
      if enf7 == True:
         enfermedad = enfermedad + 1000
      if enf8 == True:
         enfermedad = enfermedad + 1000
      if enf9 == True:
         enfermedad = enfermedad + 1000
      if enf10 == True:
         enfermedad = enfermedad + 1000

      #variable unica instituto
      if instituto == 1 or instituto == 2 or instituto == 3 or instituto == 4 or instituto == 8:
         institutoval = 1000
      elif instituto == 5 or instituto == 6 or instituto == 7 or instituto == 9:
         institutoval = 100
      else:
         institutoval = 1

      #se envian a la funcion calcular los datos agrupados en las variables unicas
      binario.calcular(nombre,saludpri,saludseg,enfermedad,edadval,institutoval,marc)

   # Funcion donde se define la interfaz grafica  
   def iniciar(self):

      marco=tk.Tk()
      marco.title("Aplicativo de Vacunacion")
      marco.geometry("810x750")
      marco.configure(background="#000000")

      # Encabezado del aplicativo 
      Encabezado1 = tk.Label(marco, text="         Aplicativo para las etapas de vacunación en Colombia          ", bg="OliveDrab3",font=(None, 20)).grid(row=0,column=0,columnspan=5)
      Bar1 = tk.Label(marco, text="___________________________________________________", bg="black",fg="black").grid(row=1,column=0,columnspan=5)
      Encabezado2 = tk.Label(marco, text=" Por favor diligencie los siguientes campos para poder conocer la etapa ", bg="grey").grid(row=2,column=0,columnspan=5)
      Encabezado3 = tk.Label(marco, text=" en la que va a recibir la vacuna contra el COVID-19 ", bg="grey").grid(row=3,column=0,columnspan=5)
      Barra1 = tk.Label(marco, text="________________________________________________________________________________________________________________", bg="black",fg="grey").grid(row=4,column=0,columnspan=5)
      
      # Espacio para ingresar el nombre
      Titulo1 = tk.Label(marco, text="         1.      Ingrese su nombre completo          ", bg="DarkOliveGreen1").grid(row=5,column=0,columnspan=5)
      e1 = Entry(marco)
      e1.pack()
      e1.grid(row=7,column=0,columnspan=5,padx=10,ipadx=200)
      Barra2 = tk.Label(marco, text="________________________________________________________________________________________________________________", bg="black",fg="grey").grid(row=8,column=0,columnspan=5)


      # Espacio para ingresar la edad
      Titulo2 = tk.Label(marco, text="    2.	Ingrese su edad    ", bg="DarkOliveGreen1").grid(row=9,column=0,columnspan=5)
      Texto1 = tk.Label(marco, text="En numeros", bg="grey").grid(row=10,column=0,columnspan=5)
      e2 = Entry(marco)
      e2.pack()
      e2.grid(row=12,column=0,columnspan=5)


      # primera pregunta de respuesta unica
      Barra3 = tk.Label(marco, text="________________________________________________________________________________________________________________", bg="black",fg="grey").grid(row=13,column=0,columnspan=5)
      Titulo3 = tk.Label(marco, text="    3.	¿Trabaja usted en algun servicio del sector salud?   ", bg="DarkOliveGreen1").grid(row=14,column=0,columnspan=5)
      Texto2 = tk.Label(marco, text="Seleccione una de las opciones", bg="grey").grid(row=15,column=0,columnspan=5)
      Bar4 = tk.Label(marco, text="___________________________________________________", bg="black",fg="black").grid(row=16,column=0,columnspan=5)
      seleccion = IntVar()
      # opciones de respuesta para la pregunta
      Op1 = Radiobutton(marco,text='UCI', value=1, variable=seleccion)
      Op2 = Radiobutton(marco,text='Urgencias', value=2, variable=seleccion)
      Op3 = Radiobutton(marco,text='Hospitalizacion', value=3, variable=seleccion)
      Op4 = Radiobutton(marco,text='Laboratorio clinico', value=4, variable=seleccion)
      Op5 = Radiobutton(marco,text='Radiologia', value=5, variable=seleccion)
      Op6 = Radiobutton(marco,text='Terapia respiratoria', value=6, variable=seleccion)
      Op7 = Radiobutton(marco,text='Transporte asistencial', value=7, variable=seleccion)
      Op8 = Radiobutton(marco,text='Medicina legal', value=8, variable=seleccion)
      Op9 = Radiobutton(marco,text='Otros', value=9, variable=seleccion)
      Op10 = Radiobutton(marco,text='Ninguno', value=10, variable=seleccion)
      Op1.grid(row=17,column=0)
      Op2.grid(row=17,column=1)
      Op3.grid(row=17,column=2)
      Op4.grid(row=17,column=3)
      Op5.grid(row=17,column=4)
      Op6.grid(row=18,column=0)
      Op7.grid(row=18,column=1)
      Op8.grid(row=18,column=2)
      Op9.grid(row=18,column=3)
      Op10.grid(row=18,column=4)

      # primera pregunta de respuesta multiple
      Barra3 = tk.Label(marco, text="________________________________________________________________________________________________________________", bg="black",fg="grey").grid(row=19,column=0,columnspan=5)
      Titulo4 = tk.Label(marco, text="    4.	¿Presenta usted alguna de las siguientes condiciones?   ", bg="DarkOliveGreen1").grid(row=20,column=0,columnspan=5)
      Bar5 = tk.Label(marco, text="___________________________________________________", bg="black",fg="black").grid(row=21,column=0,columnspan=5)
      # opciones de respuesta para la pregunta
      Con1 = BooleanVar()
      Con2 = BooleanVar()
      Con3 = BooleanVar()
      Con4 = BooleanVar()
      Con5 = BooleanVar()
      Con6 = BooleanVar()
      Con7 = BooleanVar()
      Con8 = BooleanVar()
      Con9 = BooleanVar()
      Con10 = BooleanVar()
      Chck1 = tk.Checkbutton(marco, text='Hipertension', var=Con1)
      Chck2 = tk.Checkbutton(marco, text='Diabetes', var=Con2)
      Chck3 = tk.Checkbutton(marco, text='insuficiencia renal', var=Con3)
      Chck4 = tk.Checkbutton(marco, text='VIH', var=Con4)
      Chck5 = tk.Checkbutton(marco, text='Cancer', var=Con5)
      Chck6 = tk.Checkbutton(marco, text='Tuberculosis', var=Con6)
      Chck7 = tk.Checkbutton(marco, text='EPOC', var=Con7)
      Chck8 = tk.Checkbutton(marco, text='ASMA', var=Con8)
      Chck9 = tk.Checkbutton(marco, text='Obesidad', var=Con9)
      Chck10 = tk.Checkbutton(marco, text='Trasplante de organo vital', var=Con10)
      Chck1.grid(column=0, row=22)
      Chck2.grid(column=1, row=22)
      Chck3.grid(column=2, row=22)
      Chck4.grid(column=3, row=22)
      Chck5.grid(column=4, row=22)
      Chck6.grid(column=0, row=23)
      Chck7.grid(column=1, row=23)
      Chck8.grid(column=2, row=23)
      Chck9.grid(column=3, row=23)
      Chck10.grid(column=4, row=23)

      # segunda pregunta de respuesta unica
      Barra4 = tk.Label(marco, text="________________________________________________________________________________________________________________", bg="black",fg="grey").grid(row=24,column=0,columnspan=5)
      Titulo5= tk.Label(marco, text="    5.       ¿Pertenece usted a alguna de las siguientes instituciones?   ", bg="DarkOliveGreen1").grid(row=25,column=0,columnspan=5)
      Texto2 = tk.Label(marco, text="Seleccione una de las opciones", bg="grey").grid(row=26,column=0,columnspan=5)
      Bar6 = tk.Label(marco, text="___________________________________________________", bg="black",fg="black").grid(row=27,column=0,columnspan=5)
      seleccion2 = IntVar()
      # opciones de respuesta para la pregunta
      Opc1 = Radiobutton(marco,text='Sector educativo', value=1, variable=seleccion2)
      Opc2 = Radiobutton(marco,text='Fuerzas militares', value=2, variable=seleccion2)
      Opc3 = Radiobutton(marco,text='Policia nacional', value=3, variable=seleccion2)
      Opc4 = Radiobutton(marco,text='Fiscalia', value=4, variable=seleccion2)
      Opc5 = Radiobutton(marco,text='Bomberos', value=5, variable=seleccion2)
      Opc6 = Radiobutton(marco,text='Cruz roja', value=6, variable=seleccion2)
      Opc7 = Radiobutton(marco,text='Defensa civil', value=7, variable=seleccion2)
      Opc8 = Radiobutton(marco,text='Funerarias', value=8, variable=seleccion2)
      Opc9 = Radiobutton(marco,text='Sector aereo', value=9, variable=seleccion2)
      Opc10 = Radiobutton(marco,text='Ninguno', value=10, variable=seleccion2)
      Opc1.grid(row=28,column=0)
      Opc2.grid(row=28,column=1)
      Opc3.grid(row=28,column=2)
      Opc4.grid(row=28,column=3)
      Opc5.grid(row=28,column=4)
      Opc6.grid(row=29,column=0)
      Opc7.grid(row=29,column=1)
      Opc8.grid(row=29,column=2)
      Opc9.grid(row=29,column=3)
      Opc10.grid(row=29,column=4)


      #boton para ingresar los datos
      Barra5 = tk.Label(marco, text="________________________________________________________________________________________________________________", bg="black",fg="grey").grid(row=30,column=0,columnspan=5)
      Bar1 = tk.Label(marco, text="___________________________________________________", bg="black",fg="black").grid(row=31,column=0,columnspan=5)
      btnInsertar = Button(marco,text='Ingresar Datos', command=lambda: binario.ingresar_variables(e1.get(),e2.get(),seleccion.get(),Con1.get(),Con2.get(),Con3.get(),Con4.get(),Con5.get(),Con6.get(),Con7.get(),Con8.get(),Con9.get(),Con10.get(),seleccion2.get(),marco),borderwidth=7,bg="OliveDrab3",width=100, anchor="n").grid(row=32,column=0,columnspan=5,pady=4)
      
      marco.mainloop()


binario = Binario()
binario.iniciar()
