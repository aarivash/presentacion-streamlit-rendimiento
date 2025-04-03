import streamlit as st
import base64
import plotly.express as px
import pandas as pd
import os

st.set_page_config(page_title="Presentación - Pruebas de Rendimiento", layout="wide")

# --- Utilidades visuales ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def set_background(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Fondo y logos ---
#set_background("images/Fondo_present_streamlit.png")
logo_top_b64 = get_base64_image("images/logo1_avtr.png")
logo_bottom_b64 = get_base64_image("images/logo2_avtr.png")

st.markdown(f"""
    <style>
    .logo-top-right {{
        position: fixed;
        top: 50px;
        right: 25px;
        width: 180px;
        z-index: 100;
    }}
    .logo-bottom-right {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 100px;
        z-index: 100;
    }}
    </style>
    <img src="data:image/png;base64,{logo_top_b64}" class="logo-top-right">
    <img src="data:image/png;base64,{logo_bottom_b64}" class="logo-bottom-right">
""", unsafe_allow_html=True)

st.title("🚀 Presentación Interactiva: Pruebas de Rendimiento")

tabs = st.tabs([
    "Introducción",
    "Tipos de Pruebas",
    "Herramientas",
    "Metodología",
    "Indicadores (KPIs)",
    "Ejemplos Visuales",
    "Buenas Prácticas",
    "Conclusión",
    "Trivia"
])

with tabs[0]:
    st.header("🔍 ¿Qué son las pruebas de rendimiento?")
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("images/intro.png", use_container_width=True)
        with col2:
            st.markdown("""
**Objetivos de las pruebas:**

- 🔍 Detectar cuellos de botella
- 🧱 Validar la estabilidad del sistema
- ⏱️ Asegurar tiempos de respuesta aceptables
- 📊 Optimizar el uso de recursos
- 🌐 Mejorar la experiencia de usuario
            """)
    with st.container():
        st.markdown("""
**¿Por qué son importantes?**

- 🚨 Evitan incidentes en producción
- 📈 Aumentan la confianza del cliente
- 💡 Revelan oportunidades de mejora continua
        """)

with tabs[1]:
    st.header("🧪 Tipos de Pruebas de Rendimiento")
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("images/tipos.png", use_container_width=True)
        with col2:
            st.markdown("""
- 📦 **Carga:** evaluar comportamiento con usuarios esperados
- 🔥 **Estrés:** observar fallos al sobrecargar el sistema
- 🧠 **Volumen:** procesar grandes volúmenes de datos
- 🕒 **Soak (resistencia):** estabilidad durante horas o días
- 📈 **Escalabilidad:** medir rendimiento al aumentar infraestructura
            """)
    with st.container():
        st.markdown("""
**¿Cuándo aplicar cada una?**

- 🧪 Carga: antes de lanzamientos
- 🧪 Estrés: en ambientes críticos
- 🧪 Soak: en sistemas 24/7
- 🧪 Escalabilidad: al migrar o aumentar usuarios
        """)

with tabs[2]:
    st.header("⚙️ Herramientas más utilizadas")
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("images/herramientas.png", use_container_width=True)
        with col2:
            st.markdown("""
- 🐘 **JMeter:** protocolo HTTP, FTP, JDBC
- 💻 **k6:** moderno, basado en JavaScript
- ☁️ **OctoPerf:** UI gráfica amigable y en la nube
- 🏢 **LoadRunner:** robusto, usado en grandes corporativos
            """)
    with st.container():
        with st.expander("🔍 Ver ejemplo de JMeter"):
            st.image("https://jmeter.apache.org/images/screenshots/jmeter_graphs.png")
        with st.expander("🔍 Ver ejemplo de k6"):
            st.image("https://k6.io/images/illustrations/k6-dashboard.png")

with tabs[3]:
    st.header("🧩 Metodología aplicada")
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("images/metodologia.png", use_container_width=True)
        with col2:
            st.markdown("""
1. 📝 Recolección de requerimientos
2. 🧠 Diseño de escenarios
3. 🔧 Preparación del entorno
4. 🏃‍♂️ Ejecución con monitoreo
5. 📉 Análisis con KPIs
6. 📘 Informe final con recomendaciones
            """)
    with st.container():
        st.markdown("""
**Herramientas complementarias:**
- 📊 Grafana
- 📡 Prometheus
- 🔍 New Relic
        """)

with tabs[4]:
    st.header("📊 Indicadores Clave (KPIs)")
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("images/kpis.png", use_container_width=True)
        with col2:
            st.markdown("""
- ⏱️ Tiempo de respuesta promedio y percentiles
- 🚨 Tasa de errores
- ⚙️ Throughput (transacciones por segundo)
- 🔋 Uso de CPU / RAM / disco
- 💣 Tiempo hasta caída o recuperación
            """)
    df = pd.DataFrame({
        "Usuarios": [100, 200, 400, 600, 800],
        "Tiempo de respuesta (ms)": [250, 400, 800, 1600, 2200]
    })
    fig = px.line(df, x="Usuarios", y="Tiempo de respuesta (ms)", markers=True, title="Escalado de carga")
    st.plotly_chart(fig, use_container_width=True)

with tabs[5]:
    st.header("🖼️ Ejemplos Visuales")
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("images/ejemplo_kpi.png", use_container_width=True)
        with col2:
            st.markdown("""
📈 Dashboard con tiempos de respuesta, errores y throughput.

✅ Ideal para monitoreo en tiempo real y post-ejecución.
            """)

with tabs[6]:
    st.header("✅ Buenas Prácticas")
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("images/buenas_practicas.png", use_container_width=True)
        with col2:
            st.markdown("""
- 🔬 Probar en ambientes realistas
- 📅 Incluir pruebas en cada sprint
- 💾 Versionar scripts y datos
- 🤖 Automatizar ejecuciones
- 🧠 Documentar todo: desde resultados hasta conclusiones
            """)

with tabs[7]:
    st.header("📌 Conclusión")
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("images/conclusion.png", use_container_width=True)
        with col2:
            st.markdown("""
💬 Las pruebas de rendimiento no son opcionales:

- 🧠 Aportan inteligencia operacional
- 📈 Mejoran experiencia usuario
- 🚀 Ayudan a escalar con seguridad
- 📉 Previenen fallos catastróficos
            """)

with tabs[8]:
    st.header("🎯 Trivia Interactiva")
    respuesta = st.radio("¿Qué tipo de prueba se usa para validar estabilidad prolongada bajo carga?", [
        "Prueba de carga",
        "Prueba de volumen",
        "Prueba de estrés",
        "Prueba de resistencia (Soak)"
    ])
    if respuesta == "Prueba de resistencia (Soak)":
        st.success("¡Correcto! 🎯")
    else:
        st.error("No es esa. ¡Sigue probando!")
