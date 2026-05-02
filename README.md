# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos

## Descripción
Sistema de gestión de tareas con autenticación de usuarios, desarrollado con Flask y SQLite.

## Requisitos
- Python 3.x
- Flask
- bcrypt
- requests

## Instalación
1. Cloná el repositorio o descargá los archivos.
2. Abrí una terminal en la carpeta del proyecto.
3. Instalá las dependencias:
```bash
python -m pip install flask bcrypt requests
```

## Cómo ejecutar

### 1. Iniciar el servidor
```bash
python servidor.py
```
El servidor quedará corriendo en `http://127.0.0.1:5000`

### 2. Iniciar el cliente
Abrí una terminal nueva y ejecutá:
```bash
python cliente.py
```

## Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | /registro | Registra un nuevo usuario |
| POST | /login | Inicia sesión |
| GET | /tareas | Muestra página de bienvenida |

## Pruebas con Thunder Client

### Registro
- **Método:** POST
- **URL:** `http://127.0.0.1:5000/registro`
- **Body:**
```json
{
    "usuario": "juan",
    "contraseña": "1234"
}
```

### Login
- **Método:** POST
- **URL:** `http://127.0.0.1:5000/login`
- **Body:**
```json
{
    "usuario": "juan",
    "contraseña": "1234"
}
```

### Tareas
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tareas`

## Tecnologías utilizadas
- **Flask** — framework para la API REST
- **SQLite** — base de datos local
- **bcrypt** — hasheo de contraseñas
- **requests** — cliente HTTP en consola

## Capturas de pantalla de las pruebas realizadas

### Registro
![Registro](capturas/registro.png)

### Login
![Login](capturas/login.png)

### Tareas
![Tareas](capturas/tareas.png)

### Cliente
![Cliente](capturas/cliente.png)

## Respuestas Conceptuales

### ¿Por qué hashear contraseñas?
Hashear contraseñas es fundamental para proteger los datos de los usuarios. 
Si la base de datos es comprometida por un atacante, las contraseñas hasheadas 
no pueden ser leídas en texto plano. bcrypt agrega además un "salt" aleatorio 
a cada contraseña, lo que hace que dos contraseñas iguales tengan hashes diferentes.

### Ventajas de usar SQLite en este proyecto
- **Simple:** No requiere instalar un servidor de base de datos separado.
- **Portable:** La base de datos es un único archivo (tareas.db) fácil de mover o compartir.
- **Integrado en Python:** No necesita instalación extra, viene incluido con Python.
- **Suficiente para proyectos chicos:** Para una aplicación de este tipo, SQLite 
es más que suficiente sin necesidad de usar bases de datos más complejas como MySQL o PostgreSQL.
