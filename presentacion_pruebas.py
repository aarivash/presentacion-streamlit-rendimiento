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

st.title("🚀Pruebas de Rendimiento (Performance Test)")

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

    col1, col2, col3 = st.columns([1, 1.5, 1.5])

    with col1:
        st.image("images/saturacion_prueba_ren.png", use_container_width=True)
        st.markdown("""
    **Resumen visual:**  
    Esta imagen representa un sistema sometido a carga creciente, donde se observan los efectos de la saturación si no se aplican pruebas adecuadas.
    """)

    with col2:
        st.markdown("""
        Las **pruebas de rendimiento** son un conjunto de técnicas que permiten evaluar cómo se comporta un sistema bajo distintas condiciones de carga.

        ### 🎯 ¿Para qué sirven?
        - 🔎 **Detectar cuellos de botella** antes de que impacten al usuario
        - 📊 **Medir tiempos de respuesta** frente a diferentes volúmenes de tráfico
        - 🔋 **Evaluar el uso de recursos** como CPU, memoria y red
        - 🧱 **Validar la estabilidad** en situaciones de carga prolongada

        ### 🧪 ¿Cuándo aplicarlas?
        - Antes de un **lanzamiento importante**
        - Tras una **migración o cambio de arquitectura**
        - Para soportar campañas con **alto tráfico**
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='padding:15px; border:2px solid #e0e0e0; border-radius:10px; background:#f9f9f9'>
        <b>📌 ¿Sabías que...?</b><br><br>
        Más del <b>70% de los fallos en producción</b> se deben a la falta de pruebas de rendimiento adecuadas. <br><br>
        <i>Una prueba a tiempo puede ahorrar miles de dólares en incidentes.</i>
        </div>
        
        <div style='margin-top: 10px; padding: 10px; background-color: #f0f2f6; border-left: 5px solid #4CAF50; border-radius: 5px'>
        <b>✅ Recuerda:</b> <br>
        Una aplicación rápida no solo es eficiente, también es sinónimo de calidad percibida.
        </div>
        
        """, unsafe_allow_html=True)
        
        
with tabs[1]:
    st.header("🧪 Tipos de Pruebas de Rendimiento")

        # Tarjetas tipo resumen
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="border:1px solid #ddd; border-radius:10px; padding:15px; background:#fafafa">
        <h4>📦 Prueba de Carga</h4>
        - 📊 Evalúa rendimiento bajo condiciones esperadas  
        - ⏱️ 30 min – 2 hrs  
        - 📅 Antes de producción
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="border:1px solid #ddd; border-radius:10px; padding:15px; background:#fafafa">
        <h4>🔥 Prueba de Estrés</h4>
        - ✴️ Empuja el sistema al límite  
        - ⏱️ 30 min – 1 hr  
        - 🛠️ Infraestructura crítica
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="border:1px solid #ddd; border-radius:10px; padding:15px; background:#fafafa">
        <h4>🧠 Prueba de Volumen</h4>
        - 📄 Datos masivos o ETL(Transf.Datos)  
        - ⏱️ 1 – 4 hrs  
        - ⚙️ Procesos batch
        </div>
        """, unsafe_allow_html=True)

        # Gráfico comparativo
    st.markdown("#### 📊 Comparativa de Tipos de Prueba (Duración vs Frecuencia)")
    df = pd.DataFrame({
        "Tipo": ["Carga", "Estrés", "Volumen", "Resistencia (Soak)", "Escalabilidad"],
        "Duración (hrs)": [2, 1, 4, 12, 2],
        "Frecuencia": [5, 3, 2, 1, 2]
    })
    fig = px.bar(df.melt(id_vars=["Tipo"], var_name="Métrica", value_name="Valor"),
                 x="Valor", y="Tipo", color="Métrica", barmode="group",
                 orientation="h", height=400)
    st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("""
        <div style="border:1px solid #ddd; border-radius:10px; padding:15px; background:#fafafa">
        <h4>⏲️ Resistencia (Soak)</h4>
        - ⌛ Carga sostenida  
        - ⏱️ 6 – 12 hrs  
        - 🧩 Sistemas 24/7
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="border:1px solid #ddd; border-radius:10px; padding:15px; background:#fafafa">
        <h4>📈 Escalabilidad</h4>
        - 🔼 Agregar CPU, RAM  
        - ⏱️ 1 – 2 hrs  
        - ☁️ Cloud o microservicios
        </div>
        """, unsafe_allow_html=True)


with tabs[2]:  # ← pestaña Herramientas
    st.header("🛠️ Herramientas Populares para Pruebas de Rendimiento")

    col1, col2 = st.columns([1, 1.6])

    with col1:
        st.image("images/comparativa_herra.png", caption="Comparativa visual", use_container_width=True)

    with col2:
        st.subheader("📚 Explora las herramientas disponibles")
        st.caption("Haz clic sobre cada bloque para ver más detalles.")

        with st.expander("🧪 Apache JMeter", expanded=True):
            st.markdown("""
            **🔎 Descripción:**  
            JMeter es una herramienta open-source desarrollada por Apache para pruebas de carga y rendimiento.

            **⚙️ Protocolos soportados:**  
            HTTP, HTTPS, FTP, JDBC, SOAP, REST, JMS, SMTP, TCP y más.

            **💰 Licencia:**  
            Gratuita, licencia Apache 2.0.

            **✅ Ideal para:**  
            - Proyectos con bajo presupuesto  
            - Automatización vía CI/CD  
            - Usuarios con conocimientos técnicos

            [🌐 Sitio oficial JMeter](https://jmeter.apache.org/)
            """)

        with st.expander("⚙️ k6 (Grafana)"):
            st.markdown("""
            **🔎 Descripción:**  
            k6 es una moderna herramienta de línea de comandos para pruebas de carga, escrita en Go, con scripting en JavaScript.

            **⚙️ Protocolos soportados:**  
            HTTP, WebSockets, gRPC (experimental).

            **💰 Licencia:**  
            Gratuita (MIT) con versión de pago en la nube.

            **✅ Ideal para:**  
            - Integración en pipelines DevOps  
            - Pruebas como código  
            - Equipos modernos

            [🌐 Sitio oficial k6](https://k6.io/)
            """)

        with st.expander("🌐 OctoPerf"):
            st.markdown("""
            **🔎 Descripción:**  
            OctoPerf es una plataforma SaaS para pruebas de carga con una interfaz amigable basada en JMeter.

            **⚙️ Protocolos soportados:**  
            HTTP, REST, WebSockets, SQL, SAP, etc.

            **💰 Licencia:**  
            Comercial, con versión gratuita limitada.

            **✅ Ideal para:**  
            - Empresas que prefieren no instalar nada  
            - Visualizaciones e informes potentes  
            - Trabajo colaborativo y generación rápida

            [🌐 Sitio oficial OctoPerf](https://octoperf.com/)
            """)

        with st.expander("🏢 LoadRunner"):
            st.markdown("""
            **🔎 Descripción:**  
            LoadRunner es una herramienta empresarial para pruebas de carga con soporte avanzado de protocolos.

            **⚙️ Protocolos soportados:**  
            HTTP, SAP, Citrix, Oracle, Siebel, etc. (más de 50)

            **💰 Licencia:**  
            Comercial (de pago), incluye versión trial.

            **✅ Ideal para:**  
            - Grandes organizaciones  
            - Integraciones complejas  
            - Soporte técnico robusto

            [🌐 Sitio oficial LoadRunner](https://www.microfocus.com/en-us/products/loadrunner-professional/overview)
            """)

    
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
