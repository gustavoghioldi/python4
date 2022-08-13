from tkinter import END, BooleanVar, Button, Entry, IntVar, Listbox, Tk, messagebox, simpledialog , ttk, Label
from models.item import Item
from controllers.document_controller import DocumentController
items_list = list()

def print_items():
    DocumentController.print_document(items=items_list, address=e_address.get(), cuit=e_cuit.get())

def add_item():
    art = simpledialog.askstring("agregar", "articulos")
    q   = simpledialog.askfloat("agregar", "cantidad")
    items.insert(END, f"{q} - {art}")
    items_list.append(Item(q, art))

window = Tk()
window.geometry("600x900")
window.title("Sistema de Pedidos")

address = Label(window, text="Dirección")
address.place(x=50, y=50)
e_address = Entry(window)
e_address.place(x=200, y=50)


cuit = Label(window, text="CUIT")
cuit.place(x=50, y=100)
e_cuit = Entry(window)
e_cuit.place(x=200, y=100)


items = Listbox(window)

items.place(x=120, y=170)

b1 = Button(window, text="Agregar articulo", command=add_item)
b1.place(x=350, y=240)

b2 = Button(window, text="imprimir", command=print_items)
b2.place(x=350, y=290)



# messagebox.showinfo(title="soy un mensaje", message="bla bla bla")
# messagebox.showerror(message="ERROR!")
# messagebox.showwarning(message="Warning!")

# pregu = simpledialog.askstring(prompt="Di tu nombre", title="titulo")
# print(pregu)
# ask = messagebox.askquestion( message="si o no")
# print(ask)

window.mainloop()