import requests

# Dirección base del servidor, siempre la misma mientras corre localmente
BASE_URL = "http://127.0.0.1:5000"

#REGISTRO DE USUARIOS
# Pide usuario y contraseña al usuario por consola.
# Envía los datos al endpoint /registro del servidor en formato JSON.
# Muestra el mensaje de éxito o error que responde el servidor.
def registrarse():
    print("\n--- REGISTRO ---")
    usuario = input("Ingresá tu usuario: ")
    contrasena = input("Ingresá tu contraseña: ")

    respuesta = requests.post(f"{BASE_URL}/registro", json={
        "usuario": usuario,
        "contraseña": contrasena
    })

    print(respuesta.json().get("mensaje") or respuesta.json().get("error"))

#LOGIN
# Envía las credenciales al endpoint /login.
# Si el servidor responde 200 (éxito), llama automáticamente a ver_tareas().
# Si las credenciales son incorrectas, muestra el mensaje de error.
def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    usuario = input("Ingresá tu usuario: ")
    contrasena = input("Ingresá tu contraseña: ")

    respuesta = requests.post(f"{BASE_URL}/login", json={
        "usuario": usuario,
        "contraseña": contrasena
    })

    if respuesta.status_code == 200:
        print(respuesta.json().get("mensaje"))
        ver_tareas()
    else:
        print(respuesta.json().get("error"))

#TAREAS
# Hace una petición GET al endpoint /tareas.
# Muestra en consola el HTML que devuelve el servidor.
def ver_tareas():
    print("\n--- TAREAS ---")
    respuesta = requests.get(f"{BASE_URL}/tareas")
    print("Página de bienvenida cargada correctamente.")
    print(respuesta.text)

#MENU PRINCIPAL
# Loop infinito que muestra las opciones disponibles.
# Llama a la función correspondiente según la opción elegida.
# Se cierra cuando el usuario elige la opción 3.
def menu():
    while True:
        print("\n=== SISTEMA DE TAREAS ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrarse()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida, intentá de nuevo.")

if __name__ == "__main__":
    menu()