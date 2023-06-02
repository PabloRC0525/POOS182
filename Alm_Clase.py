from tkinter import *
from tkinter import messagebox
import sqlite3
class Alm_clase:
    def __init__(self):
        pass

    def conexionDB (self):
        try:
            conexion = sqlite3.connect("C:/Users/pabiq/Documents/GitHub/POOS182/Base.db")
            print("Conectado a la DB")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    def registro(self,Nombre,Precio,Clasificacion,Marca,vacio):
        conx = self.conexionDB()
        if Nombre==vacio or Precio==vacio or Clasificacion==vacio or Marca==vacio:
            messagebox.showerror("Error","Se deben llenar todos los datos")
            conx.close()
        else:
            cursor = conx.cursor()
            datos = (Nombre,Precio,Clasificacion,Marca)
            sqlInsert = "insert into AlmacenBebidas(Nombre,Precio,Clasificacion,Marca) values (?,?,?,?)"
            cursor.execute(sqlInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Correcto","Sus datos se han registrado correctamente")
                
    def consulta(self):
        #1. realizar conexion DB
        conx = self.conexionDB()
        try:
            #4. Preparamos lo necesario
            cursor=conx.cursor()
            sqlselect= "select * from AlmacenBebidas"
            #5. Ejecutamos y cerramos conexion
            cursor.execute(sqlselect)
            RSUsuarios = cursor.fetchall()
            conx.close()
            return RSUsuarios
                
        except sqlite3.OperationalError:
            print("Error de consulta")
            
    def actualizar(self, id,nom,pr,clas,mc):
        conx = self.conexionDB()
        # 2. Validar vacios
        if(id==""):
            messagebox.showwarning("Error","Ingresa un ID")
        else:
            if nom == "" or clas == "" or mc == ""or pr == "":
                messagebox.showwarning("Aguas!!", "Formulario incompleto")
                conx.close()
            else:
                try:
                    cursor = conx.cursor()
                    cursor.execute("SELECT * FROM AlmacenBebidas WHERE id=" + id)
                    if cursor.fetchone() is None:
                        messagebox.showerror("Error", "El ID no existe")
                    else:
                        datos = ( nom,pr,clas,mc, id)
                        sqlUpdate = "UPDATE AlmacenBebidas SET Nombre=?, Precio=?, Clasificacion=?, Marca=? WHERE id=?"
                        cursor.execute(sqlUpdate, datos)
                        conx.commit()
                        conx.close()
                        messagebox.showinfo("Exito", "Bebida actualizada exitosamente")
                except sqlite3.OperationalError:
                    print("Error de actualización")
    
    def eliminar(self, id):
        conx = self.conexionDB()
        # 2. Validar vacios
        if(id==""):
            messagebox.showwarning("Error","Ingresa un ID")
        else:
            try:
                cursor = conx.cursor()
                cursor.execute("SELECT * FROM AlmacenBebidas WHERE id=" + id)
                if cursor.fetchone() is None:
                    messagebox.showerror("Error", "El ID no existe")
                else:
                    sqldelete = "DELETE FROM AlmacenBebidas WHERE id=?"
                    cursor.execute(sqldelete, id)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Exito", "Bebida eliminada exitosamente")
            except sqlite3.OperationalError:
                    print("Error al eliminar")
    def prom(self):
        conx = self.conexionDB()
        try:
            cursor=conx.cursor()
            sqlselect= "select avg(Precio) as precio_promedio from AlmacenBebidas"
            cursor.execute(sqlselect)
            RSUsuarios = cursor.fetchall()
            conx.close()
            return RSUsuarios
        except sqlite3.OperationalError:
            print("Error")