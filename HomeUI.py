import tkinter as tk


def HomeUI():
    # Crear la ventana
    window = tk.Tk()
    window.geometry("500x600")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (500 / 2))
    y = int((screen_height / 2) - (600 / 2))
    window.geometry(f"500x600+{x}+{y}")
    window.title("Weasley & Weasley")

    # Establecer el color de fondo de la ventana
    window.configure(bg="#f6f6f5")

    # ZONA DE WIDGETS

    # Agregar la imagen del logo con un tamaño reducido
    imagen = tk.PhotoImage(file="Resources/logo_weasley.png").subsample(2)
    label_logo = tk.Label(window, image=imagen, bg="#f6f6f5")
    label_logo.pack(pady=20)

    # Agregar el título
    titulo = tk.Label(window, text="Weasley & Weasley", font=("Arial", 16, "bold"), bg="#f6f6f5")
    titulo.pack()

    # Agregar el slogan
    slogan = tk.Label(window, text="¡Artefactos mágicos del universo Harry Potter!", font=("Arial", 12), bg="#f6f6f5")
    slogan.pack()

    # Agregar el botón para iniciar sesión con un estilo llamativo y centrado
    btn_iniciar_sesion = tk.Button(window, text="Haz click aquí para iniciar sesión", bg="#d75f38", fg="white",
                                  font=("Arial", 12, "bold"))
    btn_iniciar_sesion.config(height=2, width=30)
    btn_iniciar_sesion.pack(pady=20)

    # Agregar el botón de inicio de sesión para el administrador en la esquina superior derecha
    btn_admin_login = tk.Button(window, text="🎩", name="btn_AdminLogin", bg="#442d81", fg="white",
                               font=("Arial", 12, "bold"))
    btn_admin_login.config(height=2, width=4)
    btn_admin_login.place(x=449, y=5)

    # Agregar el botón de inicio de sesión para el vendedor en la esquina superior derecha
    btn_vendedor_login = tk.Button(window, text="W", name="btn_VendedorLogin", bg="#34161a", fg="white",
                                   font=("Arial", 12, "bold"))
    btn_vendedor_login.config(height=2, width=4)
    btn_vendedor_login.place(x=449, y=58)

    # Función para la acción del clic en el enlace
    def iniciar_sesion_muggle():
        print("Acción de iniciar sesión para muggles")

    # Contenedor para los labels
    labels_frame = tk.Frame(window, bg="#f6f6f5")
    labels_frame.pack(pady=10)

    # Agregar el label para "¿Eres un muggle?" en letra negra
    label_muggle = tk.Label(labels_frame, text="¿Eres un Muggle?", font=("Arial", 12), bg="#f6f6f5", fg="black")
    label_muggle.pack(side=tk.LEFT)

    # Agregar el label con el enlace para iniciar sesión en azul y subrayado
    label_iniciar_sesion = tk.Label(labels_frame, text="Haz click aquí", font=("Arial", 12),
                                    bg="#f6f6f5", fg="blue", cursor="hand2")
    label_iniciar_sesion.pack(side=tk.LEFT)
    label_iniciar_sesion.bind("<Button-1>", lambda event: iniciar_sesion_muggle())

    # Iniciar el bucle principal de la ventana
    window.mainloop()


# Crear la ventana de inicio de sesión
HomeUI()
