import tkinter as tk
root = tk.Tk()
root.title("DAVIER NC - OK")
root.geometry("400x200")
tk.Label(root, text="¡El EXE ya funciona!").pack(pady=40)
tk.Button(root, text="Cerrar", command=root.destroy).pack()
root.mainloop()
