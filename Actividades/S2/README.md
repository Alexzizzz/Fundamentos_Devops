# 🐳 Gestión de Imágenes Docker desde VS Code

## 📝 Descripción del Proyecto
Este repositorio contiene los apuntes y prácticas de nuestra sesión de hoy. El objetivo principal fue aprender a interactuar con **Docker** directamente desde **Visual Studio Code**, específicamente enfocándonos en cómo construir y subir (push) imágenes de contenedores sin necesidad de salir del editor.

## 🛠️ Herramientas y Tecnologías
* **Editor:** Visual Studio Code
* **Contenedores:** Docker Desktop
* **Extensiones de VS Code:** Docker / Dev Containers
* **Control de Versiones:** Git & GitHub

## 🚀 Lo que aprendimos hoy

Durante esta sesión cubrimos los siguientes puntos clave:

1. **Preparación del Entorno:** Configurar un archivo `Dockerfile` básico para definir nuestra imagen.
2. **Construcción (Build):** Aprendimos a crear la imagen de Docker utilizando la interfaz gráfica de VS Code y la terminal integrada.
3. **Subida de Imágenes (Push):** Vimos el proceso para etiquetar (tag) nuestra imagen y subirla a un registro de contenedores (como Docker Hub) directamente desde las herramientas de Visual Studio Code.
4. **Solución de problemas en la Terminal:** Manejo de rutas y correcta ejecución de comandos en el directorio del proyecto.

## 📋 Comandos Útiles de Repaso

Si necesitas recordar cómo hacer el proceso desde la terminal, aquí están los comandos básicos:

```bash
# 1. Construir la imagen desde el Dockerfile
docker build -t nombre-de-tu-imagen:etiqueta .

# 2. Etiquetar la imagen para el registro (ej. Docker Hub)
docker tag nombre-de-tu-imagen:etiqueta tu-usuario/nombre-de-tu-imagen:etiqueta

