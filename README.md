# Detector de Phishing con Inteligencia Artificial  
### Examen #2 – Aplicaciones de la Inteligencia Artificial

---

## 👥 Integrantes del Proyecto
- Mathias José Calderón Vásquez
- Javier Viquez Barrientos

---

## 💡 Descripción de la Idea del Proyecto
El propósito de este proyecto es desarrollar un sistema capaz de detectar si el contenido de un correo electrónico corresponde a un intento de **phishing**.  
Para ello se implementó un modelo de Inteligencia Artificial utilizando técnicas de **Procesamiento de Lenguaje Natural (NLP)** y **Machine Learning**, todo integrado en una aplicación web construida con **Flask**.

El usuario ingresa el cuerpo textual de un correo electrónico y el sistema analiza su contenido para clasificarlo como:

- **Correo legítimo**, o  
- **Correo potencialmente malicioso (phishing)**.

El objetivo final es brindar una herramienta sencilla, intuitiva y funcional que permita al usuario evaluar mensajes sospechosos.

---

## 📚 Resumen Teórico

### 🧪 Tecnologías Utilizadas
- **Python 3.10+**
- **Flask** (framework web)
- **Scikit-learn** (modelo de Machine Learning)
- **NLTK** (procesamiento de texto)
- **CountVectorizer** (vectorización del contenido del correo)
- **Multinomial Naive Bayes** (modelo de clasificación)
- **HTML5, CSS3 y JS** para la interfaz web

---

### 🖥 Diseño del Sistema
El sistema está compuesto por tres partes principales:

1. **Front-end (Interfaz Web)**  
   - Formulario para que el usuario ingrese el contenido del correo.  
   - Botón para enviar el texto al servidor.  
   - Zona donde se muestra el resultado de análisis.

2. **Back-end (Servidor Flask)**  
   - Recibe el correo ingresado.
   - Preprocesa el texto (limpieza, tokenización, vectorización).
   - Carga el modelo previamente entrenado.
   - Clasifica el contenido como *phishing* o *no phishing*.
   - Devuelve la respuesta al usuario.

3. **Modelo de Machine Learning**  
   - Entrenado con un dataset real de correos legítimos y de phishing.
   - Utiliza un clasificador **MultinomialNB**, ideal para texto.
   - Procesa el texto a través de **CountVectorizer**.

---

### 📈 Avance del Proyecto
- ✔ Modelo entrenado y funcionando al 100%.  
- ✔ Interfaz web implementada.  
- ✔ Backend Flask conectado al modelo.  
- ✔ Clasificación en tiempo real a partir del cuerpo del correo.  
- ✔ Código limpio, modular y totalmente funcional.  

---

### ⚠️ Obstáculos Encontrados
- Diferencias entre versiones de `scikit-learn` al cargar el modelo pre-entrenado.  
- Ajustes necesarios para limpiar y procesar correctamente el texto.  
- Renderizado del template HTML en Flask (caché de templates).  
- Evitar subir librerías, entornos virtuales y archivos binarios al repositorio.

---

### 🧾 Conclusiones
El proyecto permitió aplicar conceptos de IA para resolver un problema real: identificar correos fraudulentos.  
Se logró integrar de manera exitosa:

- Técnicas de NLP  
- Modelos de Machine Learning  
- Construcción de interfaces  
- Desarrollo web con Flask  

El sistema final es simple, práctico y escalable, permitiendo futuras mejoras como detección basada en deep learning, análisis de URLs o verificación de headers.

---

## ▶️ Instrucciones para Ejecutar el Código

1- Crear y activar entonrno Virtual:

python -m venv venv
venv\Scripts\activate


2- instalar dependencias

pip install -r requirements.txt


3- Ejecutar la app

python app.py



