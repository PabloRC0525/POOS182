from tkinter import *
from tkinter import ttk
import tkinter as tk
from Alm_Clase import *
from tkinter import messagebox

controlador = Alm_clase()

def ejecutaInsert():
    controlador.registro(Nombre.get(),PR.get(),Clasif.get(),Marca.get(),vacio)
    
        
def ejecutaconsulta():
    # Obtiene los usuarios de la base de datos
    rUsu= controlador.consulta()
    # Borra los datos existentes en la tabla
    tabla0.delete(*tabla0.get_children())
    # Inserta los nuevos datos en la tabla
    for usu in rUsu:
        tabla0.insert('', 'end', text=usu[0], values=(usu[1], usu[2], usu[3], usu[4]))
        
def ejecutaACT(varNomAE, varPAE, varClasAE, varMcAE):
    controlador.actualizar(varAct.get(),varNomAE.get(), varPAE.get(), varClasAE.get(), varMcAE.get())
    
def ejecutadelete():
    controlador.eliminar(varElim.get())        
    
        
def clas():
    rsUsu= controlador.prom()
    for usu in rsUsu:
            cadena= str(usu[0])
    if(rsUsu): 
            textBus.config(state='normal')  # Configuración del estado del widget Text
            textBus.delete(1.0, 'end')  # Limpia el contenido del widget Text
            textBus.insert('end', cadena)  # Inserta la cadena en el widget Text
            textBus.config(state='disabled')  # Restaura el estado del widget Text a 'disabled'
    rUsu = controlador.clas()
    tabla.delete(*tabla.get_children())
    for usu in rUsu:
        tabla.insert('', 'end', text=usu[0], values=(usu[1], usu[2]))
    rUsu = controlador.mc()
    tabla1.delete(*tabla1.get_children())
    for usu in rUsu:
        tabla1.insert('', 'end', text=usu[0], values=(usu[1], usu[2], usu[3]))

ventana = Tk()
ventana.title("Almacen_Beb")
ventana.geometry("800x400")

panel = ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)
pestaña5 = ttk.Frame(panel)


#Alta de bebida
titulo = Label(pestaña1,text="Alta de bebidas",fg="blue",font=("Modern",18)).pack()

Nom = Label(pestaña1, text="Nombre:")
Nom.pack()
Nombre = ttk.Entry(pestaña1,width= 30)
Nombre.pack()
    

Pr = Label(pestaña1, text="Ingrese Precio:")
Pr.pack()
PR = ttk.Entry(pestaña1,width= 30)
PR.pack()

Clas = ttk.Label(pestaña1, text="Ingrese Clasificacion: ")
Clas.pack()
opciones = ["Agua", "Bebida_Azucarada", "Bebida_Energetica"]
Clasif = ttk.Combobox(pestaña1, values=opciones, width=30)
Clasif.pack()

Mc = ttk.Label(pestaña1, text="Ingrese Marca: ")
Mc.pack()
opciones2 = ["Pepsi", "Coca-cola", "Monster", "Red_Bull"]
Marca = ttk.Combobox(pestaña1, values=opciones2, width=30)
Marca.pack()

BotonRegistrar = Button(pestaña1,text="Registrar",bg="#255748",fg="white",command=ejecutaInsert)
BotonRegistrar.pack()

#Baja de bebida
titulo3 = Label(pestaña2,text="Eliminar Usuario:",fg ="red",font=("Modern",18))
titulo3.pack()

varElim = tk.StringVar()
lblidE = Label(pestaña2,text="Identificador de bebida:")
lblidE.pack()
txtidE = Entry(pestaña2,textvariable=varElim)
txtidE.pack()

btnElimina = Button(pestaña2,text="Eliminar bebida", command=ejecutadelete)
btnElimina.pack()

mensajeAE = tk.StringVar()
lblMensajeAE = Label(pestaña2, textvariable=mensajeAE)
lblMensajeAE.pack()

#Actualizar
     
titulo3 = Label(pestaña3,text="Actualizar Bebida:",fg ="green",font=("Modern",18))
titulo3.pack()

varAct = tk.StringVar()
lblidA = Label(pestaña3,text="Identificador de bebida:")
lblidA.pack()
txtidA = Entry(pestaña3,textvariable=varAct)
txtidA.pack()

varNomAE = tk.StringVar()
lblNomAE = Label(pestaña3,text="Nuevo nombre: ")
lblNomAE.pack()
txtNomAE = Entry(pestaña3,textvariable=varNomAE)
txtNomAE.pack()

varPAE = tk.StringVar()
lblPAE = Label(pestaña3,text="Nuevo precio: ")
lblPAE.pack()
txtPAE = Entry(pestaña3,textvariable=varPAE)
txtPAE.pack()

lblClasAE = ttk.Label(pestaña3, text="Ingrese nueva clasificacion: ")
lblClasAE.pack()
opciones = ["Agua", "Bebida_Azucarada", "Bebida_Energetica"]
txtClaAE = ttk.Combobox(pestaña3, values=opciones, width=30)
txtClaAE.pack()

varMcAE = ttk.Label(pestaña3, text="Ingrese nueva marca: ")
varMcAE.pack()
opciones2 = ["Pepsi", "Coca-cola", "Monster", "Red_Bull"]
txtMarAE = ttk.Combobox(pestaña3, values=opciones2, width=30)
txtMarAE.pack()

btnACT = Button(pestaña3,text="Actualizar bebida", command=lambda: ejecutaACT(varNomAE, varPAE, varClasAE, varMcAE))
btnACT.pack()


#Consultar bebidas
subUS= Label(pestaña4,text= "Bebidas:",fg="green",font=("Modern",15)).pack()
tabla0 = ttk.Treeview(pestaña4)
tabla0['columns'] = ('nombre','precio', 'clasificacion','marca')
tabla0.column('#0', width=50, minwidth=50)
tabla0.column('nombre', width=120, minwidth=120)
tabla0.column('precio', width=120, minwidth=120)
tabla0.column('clasificacion', width=150, minwidth=150)
tabla0.column('marca', width=150, minwidth=150)
tabla0.heading('#0', text='ID', anchor=tk.CENTER)
tabla0.heading('nombre', text='Nombre', anchor=tk.CENTER)
tabla0.heading('precio', text='Precio', anchor=tk.CENTER)
tabla0.heading('clasificacion', text='Clasificacion', anchor=tk.CENTER)
tabla0.heading('marca', text='Marca', anchor=tk.CENTER)
tabla0.pack() 

Consultar= Button(pestaña4,text="Consultar",command=ejecutaconsulta).pack()

#Calculos

tituloo = Label(pestaña5,text="Promedio Precios:",fg ="green",font=("Modern",18)).pack()

subBus= Label(pestaña5,text= "Promedio:",fg="blue",font=("Modern",15)).pack()
textBus = tk.Text(pestaña5, height=1, width=10)
textBus.pack() 

subUS= Label(pestaña5,text= "Clasificacion:",fg="green",font=("Modern",15)).pack()
tabla = ttk.Treeview(pestaña5,height=2)
tabla['columns'] = ('azucar', 'ener')
tabla.column('#0', width=120, minwidth=120)
tabla.column('azucar', width=120, minwidth=120)
tabla.column('ener', width=120, minwidth=120)
tabla.heading('#0', text='Agua', anchor=tk.CENTER)
tabla.heading('azucar', text='Azucaradas', anchor=tk.CENTER)
tabla.heading('ener', text='Energeticas', anchor=tk.CENTER)
tabla.pack() 

subS= Label(pestaña5,text= "Marca:",fg="green",font=("Modern",15)).pack()
tabla1 = ttk.Treeview(pestaña5,height=2)
tabla1['columns'] = ( 'cc', 'mt','rb')
tabla1.column('#0', width=120, minwidth=120)
tabla1.column('cc', width=120, minwidth=120)
tabla1.column('mt', width=120, minwidth=120)
tabla1.column('rb', width=120, minwidth=120)
tabla1.heading('#0', text='Pepsi', anchor=tk.CENTER)
tabla1.heading('cc', text='Coca-cola', anchor=tk.CENTER)
tabla1.heading('mt', text='Monster', anchor=tk.CENTER)
tabla1.heading('rb', text='Red Bull', anchor=tk.CENTER)
tabla1.pack() 

btnClas = Button(pestaña5,text="Consultar", command=clas)
btnClas.pack()
vacio =""

panel.add(pestaña1,text="Alta bebidas")
panel.add(pestaña2,text="Dar de baja")
panel.add(pestaña3,text="Actualizar")
panel.add(pestaña4,text="Consultar")
panel.add(pestaña5,text="Calculos")


ventana.mainloop()