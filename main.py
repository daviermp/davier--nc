import tkinter as tk
from tkinter import ttk

class DavierNCApp:
    def __init__(self, root):
        root.title("DAVIER NC - Control Plasma CNC")
        root.geometry("1100x700")
        root.configure(bg="#0a1a1a")

        # HEADER
        header = tk.Frame(root, bg="#102828", height=80)
        header.pack(fill="x")
        
        tk.Label(header, text="DAVIER NC", font=("Arial Black", 22), 
                 bg="#102828", fg="white").pack(side="left", padx=20)
        tk.Label(header, text="Control Plasma CNC", font=("Arial", 12), 
                 bg="#102828", fg="#00ff99").pack(side="left")

        tk.Label(header, text="● CONECTADO", font=("Arial", 10, "bold"),
                 bg="#102828", fg="#00ff66").pack(side="right", padx=20)

        # MAIN
        main = tk.Frame(root, bg="#0a1a1a")
        main.pack(fill="both", expand=True, padx=15, pady=15)

        # Left - Config
        left = tk.LabelFrame(main, text=" CONFIGURACIÓN ", bg="#142828", 
                             fg="white", font=("Arial", 10, "bold"), padx=10, pady=10)
        left.pack(side="left", fill="y", padx=(0,10))

        tk.Label(left, text="Dimensiones Lámina (mm)", bg="#142828", fg="#88ffcc").pack(anchor="w", pady=5)
        
        row = tk.Frame(left, bg="#142828")
        row.pack(fill="x")
        tk.Label(row, text="Ancho:", bg="#142828", fg="white").pack(side="left")
        tk.Entry(row, width=8).pack(side="left", padx=5)
        tk.Label(row, text="Alto:", bg="#142828", fg="white").pack(side="left", padx=10)
        tk.Entry(row, width=8).pack(side="left")

        tk.Label(left, text="Material / Espesor", bg="#142828", fg="#88ffcc").pack(anchor="w", pady=(15,5))
        ttk.Combobox(left, values=["Acero 3mm", "Acero 6mm", "Inox 2mm"]).pack(fill="x")
        ttk.Combobox(left, values=["Lámina 1x2m", "Lámina 1.22x2.44m"]).pack(fill="x", pady=5)

        tk.Button(left, text="CARGAR DXF", bg="#00cc66", fg="white", 
                  font=("Arial", 10, "bold"), height=2).pack(fill="x", pady=15)
        tk.Button(left, text="GENERAR G-CODE", bg="#0099ff", fg="white",
                  font=("Arial", 10, "bold"), height=2).pack(fill="x")
        
        tk.Label(left, text="Costo estimado: $0", bg="#142828", fg="white", 
                 font=("Arial", 12, "bold")).pack(pady=20)

        # Center - Visor
        center = tk.LabelFrame(main, text=" VISOR DE CORTE ", bg="#000000", 
                               fg="#00ff99", font=("Arial", 10, "bold"))
        center.pack(side="left", fill="both", expand=True)

        canvas = tk.Canvas(center, bg="#0a0a0a", highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=5, pady=5)
        canvas.create_text(550, 300, text="Visor DXF / Plasma\nDAVIER NC", 
                           fill="#333", font=("Arial", 18), justify="center")

        # Right - Control
        right = tk.LabelFrame(main, text=" CONTROL ", bg="#142828", fg="white",
                              font=("Arial", 10, "bold"), padx=10, pady=10, width=200)
        right.pack(side="right", fill="y")
        right.pack_propagate(False)

        for txt in ["▶ INICIAR CORTE", "■ PAUSA", "■ DETENER", "⌂ ORIGEN"]:
            tk.Button(right, text=txt, bg="#333", fg="white").pack(fill="x", pady=4)

        tk.Label(right, text="Consola:", bg="#142828", fg="#88ffcc").pack(anchor="w", pady=(20,5))
        tk.Text(right, height=10, bg="black", fg="#00ff00").pack(fill="both", expand=True)

        tk.Label(root, text="DAVIER NC v1.0 | María la Baja - Bolívar", 
                 bg="#0a1a1a", fg="#666", font=("Arial", 8)).pack(side="bottom", pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = DavierNCApp(root)
    root.mainloop()
