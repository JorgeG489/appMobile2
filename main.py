from flet import *
import threading  # Usaremos threading para manejar el tiempo de espera

def main(page: Page):
    global login_container  # Hacemos global para poder usarlo en otras funciones

    # Crear los TextField y el botón dentro de la función main
    text_field_username = TextField(
        label="Nombre de usuario",
        width=300,
        bgcolor="white",
        border_color="black",
        border_radius=5,
        color="black"
    )

    text_field_password = TextField(
        label="Contraseña",
        width=300,
        password=True,
        bgcolor="white",
        border_color="black",
        border_radius=5,
    )

    # Crear el contenedor global para la página de inicio de sesión y el contenido principal
    login_container = Container(
        width=400,
        height=300,
        margin=20,
        padding=20,
        bgcolor="#6F78F2",
        border_radius=15,
        alignment=alignment.center,
        animate=animation.Animation(duration=1000, curve="easeInOut"),  # Animación agregada
        content=Column(
            controls=[
                Text("Iniciar sesión", size=24, weight="bold", color="white"),
                text_field_username,
                text_field_password,
                ElevatedButton(
                    text="Iniciar sesión",
                    on_click=lambda e: on_login_click(e, text_field_username, text_field_password, page),
                    bgcolor="#4C5BCA",
                    color="white",
                ),
            ],
            spacing=15
        )
    )

    # Agregar el contenedor a la página
    page.add(login_container)

def on_login_click(e, text_field_username, text_field_password, page):
    # Obtener el valor de los campos de texto
    user_input = text_field_username.value
    password_input = text_field_password.value
    
    # Verificar las credenciales
    if user_input == "admin" and password_input == "admin":
        # Reemplazar el contenido del contenedor con la página principal y animar su expansión
        show_main_page(page)
    else:
        # Mostrar mensaje de error
        page.add(Text("Credenciales incorrectas", color="red"))

def show_main_page(page: Page):
    global login_container  # Hacemos global para poder usarlo en otras funciones
    
    # Actualizar el contenido del contenedor
    login_container.content = Column(
        controls=[
            # Contenedor para el texto principal
            Container(
                content=Column(
                    controls=[
                        Text("Bienvenido a la página principal", size=24, weight="bold", color="white"),
                        ElevatedButton(
                            text="Cerrar sesión",
                            on_click=lambda e: on_logout_click(page),
                            bgcolor="#f44336",
                            color="white",
                        ),
                    ],
                    spacing=15
                ),
                alignment=alignment.top_center,
                padding=20
            ),
            # Contenedor para los íconos en la parte inferior
            Container(
                content=Row(
                    controls=[
                        IconButton(icon=icons.HOME, on_click=lambda e: print("Casa")),
                        IconButton(icon=icons.SEARCH, on_click=lambda e: print("Buscar")),
                        IconButton(icon=icons.MENU, on_click=lambda e: print("Menú")),
                    ],
                    spacing=20,
                    alignment="center"
                ),
                alignment=alignment.bottom_center,
                padding=20,
                expand=True  # Para empujar este contenedor al fondo
            )
        ],
        spacing=0,  # No hay espacio entre los contenedores
        alignment=alignment.center  # Centra el contenido verticalmente
    )

    # Animar el contenedor para que se expanda
    login_container.width = 600
    login_container.height = 400
    
    # Refrescar la página para mostrar el nuevo contenido con la animación
    page.update()

def on_logout_click(page: Page):
    global login_container  # Hacemos global para poder usarlo en otras funciones

    # Animar el contenedor para hacerlo pequeño primero
    login_container.width = 400
    login_container.height = 300

    # Actualizar la página para mostrar la animación de hacerse pequeño
    page.update()

    # Esperar que la animación de reducción termine (0.8 segundos) y luego mostrar el login
    threading.Timer(0.8, lambda: show_login_page(page)).start()

def show_login_page(page: Page):
    global login_container  # Hacemos global para poder usarlo en otras funciones
    
    # Actualizar el contenido del contenedor con el formulario de inicio de sesión
    text_field_username = TextField(
        label="Nombre de usuario",
        width=300,
        bgcolor="white",
        border_color="black",
        border_radius=5,
        color="black"
    )

    text_field_password = TextField(
        label="Contraseña",
        width=300,
        password=True,
        bgcolor="white",
        border_color="black",
        border_radius=5,
    )

    login_container.content = Column(
        controls=[
            Text("Iniciar sesión", size=24, weight="bold", color="white"),
            text_field_username,
            text_field_password,
            ElevatedButton(
                text="Iniciar sesión",
                on_click=lambda e: on_login_click(e, text_field_username, text_field_password, page),
                bgcolor="#4C5BCA",
                color="white",
            ),
        ],
        spacing=15
    )
    
    # Actualizar la página para mostrar el nuevo contenido (formulario de inicio de sesión)
    page.update()

# Inicia la aplicación
app(target=main, view=AppView.FLET_APP)
