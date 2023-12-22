import tkinter as tk
from tkinter import Tk, messagebox, ttk



contactos = []




def agregar_contacto():
   nombre= caja_nombre.get()
   telefono= caja_numero.get()
   if nombre and telefono:
       contacto={"nombre":nombre,"telefono":telefono}
       contactos.append(contactos)
       treeview.insert("", tk.END,text=nombre, values=(telefono))





def eliminar_contacto():
   seleccion= treeview.selection()
   try:
       if seleccion :
           confirmar = messagebox.askyesno("Alerta", "¿estas seguro que deseas eliminar este contacto?")
       for item in seleccion:
               treeview.delete(item)
       else:
          messagebox.showwarning("Ningun contacto ah sido seleccionado", "selecciona un contacto")
   except:
       messagebox.showwarning("Error", "Ocurrio un error al eliminar ese contacto")


ventana = tk.Tk()
ventana.title("gestor de contactos")   


treeview = ttk.Treeview(ventana, columns=('tel'))
treeview.heading("#0", text="Nombre")
treeview.heading("tel", text="Telefono")
treeview.pack()

etiqueta_nombre=tk.Label(text="Nombre")
etiqueta_nombre.pack()
caja_nombre = tk.Entry(ventana, font=("Arial", 12))
caja_nombre.pack(pady=5)

etiqueta_numero=tk.Label(text="Numero")
etiqueta_numero.pack()
caja_numero = tk.Entry(ventana, font=("Arial", 12))
caja_numero.pack(pady=5)


boton_agregar = tk.Button(ventana, text="Agregar Contacto", command=agregar_contacto, bg="#A5F2F3")
boton_agregar.pack(side=tk.LEFT, padx=5)
boton_eliminar = tk.Button(ventana, text="Eliminar Contacto", command=eliminar_contacto, bg="#ff6565")
boton_eliminar.pack(side=tk.LEFT, padx=5)


ventana.mainloop() 
