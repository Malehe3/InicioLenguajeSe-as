import streamlit as st

# Título
st.title("Lenguaje de Señas Colombiano")

# Eslogan
st.header("Aprende Lenguaje de Señas Colombiano: Rompiendo Barreras, Construyendo Puentes")

# Introducción y Reflexión
st.write("""
## Introducción

Bienvenido a nuestra aplicación de aprendizaje del Lenguaje de Señas Colombiano (LSC). En Colombia, el lenguaje de señas es una herramienta vital para la comunicación inclusiva. Esta aplicación tiene como objetivo facilitar el aprendizaje de LSC, permitiendo a más personas comunicarse efectivamente con la comunidad sorda.

## Reflexión

Aprender LSC no solo es adquirir una nueva habilidad, sino también es un acto de inclusión y respeto hacia las personas sordas. Es una manera de construir una sociedad más equitativa y comprensiva.
""")

# Importancia
st.write("""
## ¿Por qué es importante aprender LSC?

El Lenguaje de Señas Colombiano es la lengua materna de muchas personas sordas en nuestro país. Aprender LSC es crucial porque:

- Promueve la inclusión y la comunicación efectiva.
- Fortalece las relaciones personales y profesionales.
- Ayuda a derribar barreras de comunicación y a crear una sociedad más justa.
""")

# Propósito y Recorrido del Aprendizaje
st.write("""
## Propósito de esta Aplicación y Recorrido de Aprendizaje

El propósito de esta aplicación es proporcionar una plataforma accesible y amigable para aprender LSC de manera estructurada y eficiente. A través de nuestros módulos, aprenderás:

1. **Lo Básico: El Abecedario y Tu Señal de Identificación**:
   - Comenzarás con lo más esencial, el abecedario. Aprenderás a deletrear tu nombre y a crear tu propia seña de identificación.

2. **Señas Comunes y Expresiones Cotidianas**:
   - A continuación, te enseñaremos señas comunes utilizadas en el día a día, como saludos, despedidas y frases básicas.

3. **Frases Complejas y Conversaciones**:
   - Una vez que domines las señas básicas, avanzarás a construir frases más complejas y participar en conversaciones sencillas.

4. **Temas Específicos y Vocabulario Avanzado**:
   - Finalmente, te adentrarás en temas específicos como salud, educación, y trabajo, ampliando tu vocabulario y comprensión del LSC.
""")

# Video
st.write("""
## Video de Introducción

Para comenzar, mira este video que te dará una visión general del Lenguaje de Señas Colombiano y te motivará en tu proceso de aprendizaje.
""")

# Incrustar un video (por ejemplo, un video de YouTube)
video_url = "https://www.youtube.com/watch?v=tJz9iwuU6aY"  # Reemplaza con la URL de tu video
st.video(video_url)
