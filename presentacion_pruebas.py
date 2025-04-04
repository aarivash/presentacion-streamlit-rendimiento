import streamlit as st
import base64
import plotly.express as px
import pandas as pd
import os

from df2 import df2

st.set_page_config(page_title="AVATTAR - Pruebas de Rendimiento", layout="wide")

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

st.title("AVATTAR - 🚀Pruebas de Rendimiento")

tabs = st.tabs([
    "Introducción",
    "Tipos de Pruebas",
    "Herramientas",
    "Metodología",
    "Indicadores (KPIs)",
    "Ejemplos Visuales",
    "Buenas Prácticas",
    #"Conclusión",
    #"Trivia"
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
    st.header("🧩 Metodología: ¿Cómo se hacen las pruebas de rendimiento?")

    st.markdown("A continuación te explicamos, paso a paso, cómo se preparan y ejecutan este tipo de pruebas. Ideal para quienes recién comienzan en este mundo. 👇")

    col1, col2 = st.columns([2, 1])  # Izquierda info - Derecha imagen

    with col1:
        pasos = [
            {
                "icon": "📝",
                "titulo": "Recolección de requerimientos",
                "desc": "Es clave entender qué se quiere medir, cuál es el objetivo de negocio, cuántos usuarios se esperan y qué áreas del sistema son críticas."
            },
            {
                "icon": "🧠",
                "titulo": "Diseño de escenarios",
                "desc": "Se definen las rutas de navegación de los usuarios, qué acciones van a simular y cómo será la distribución de la carga (por ejemplo: login, compra, descarga)."
            },
            {
                "icon": "🔧",
                "titulo": "Preparación del entorno",
                "desc": "El entorno de pruebas debe ser lo más parecido posible al entorno real. Esto incluye bases de datos, servicios, redes, etc."
            },
            {
                "icon": "🚀",
                "titulo": "Ejecución controlada",
                "desc": "Se lanza la prueba con herramientas como JMeter o K6, monitoreando su comportamiento en tiempo real."
            },
            {
                "icon": "📊",
                "titulo": "Análisis de resultados",
                "desc": "Se recopilan métricas como tiempo de respuesta, errores, uso de CPU/RAM y se buscan cuellos de botella o comportamientos anómalos."
            },
            {
                "icon": "📘",
                "titulo": "Informe y recomendaciones",
                "desc": "Se entrega un reporte claro y visual que resume los hallazgos, riesgos detectados y propuestas de mejora."
            }
        ]

        for paso in pasos:
            st.markdown(f"""
            <div style='padding:15px; border:1px solid #e0e0e0; border-radius:10px; margin-bottom:15px; background-color:#f9f9f9'>
                <h4>{paso["icon"]} {paso["titulo"]}</h4>
                <p>{paso["desc"]}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style='margin-top: 25px; padding: 15px; background-color: #f0f2f6; border-left: 5px solid #2196F3; border-radius: 5px'>
            <b>🎯 Tip importante:</b><br>
            Involucra al equipo de desarrollo, QA y operaciones desde el inicio del proceso. Cuanto más colaborativo sea el enfoque, mejores serán los resultados.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("images/Diagrama_Rendi.png", caption="Diagrama de flujo metodológico", use_container_width=True)


with tabs[4]:
    st.header("📊 Indicadores Clave de Rendimiento (KPIs)")

    st.markdown("""
    Los KPIs son métricas que nos ayudan a entender cómo se comporta un sistema bajo carga.
    Aquí te mostramos los más importantes y cómo interpretarlos. 👇
    """)

    # Primera fila: indicadores y gráfico 1
    col1, col2 = st.columns([2, 1.2])

    with col1:
        kpis = [
            {
                "icon": "⏱️",
                "titulo": "Tiempo de respuesta",
                "desc": "Mide cuánto tarda el sistema en responder a una solicitud. Ej: si un login tarda más de 3 segundos, puede ser molesto para el usuario.(Experiencia de Usuario)"
            },
            {
                "icon": "🚨",
                "titulo": "Tasa de error",
                "desc": "Porcentaje de transacciones fallidas. Ej: si 100 usuarios hacen clic en 'comprar' y 5 reciben error, la tasa es 5%."
            },
            {
                "icon": "⚙️",
                "titulo": "Throughput (Transacciones por segundo) *",
                "desc": "Cantidad de operaciones que puede manejar el sistema por segundo. Ej: 1200 transacciones por minuto indica buena capacidad."
            },
            {
                "icon": "🔋",
                "titulo": "Uso de CPU / RAM",
                "desc": "Nos dice si el sistema está usando más recursos de los que debería. Ej: una app que usa 95% de RAM puede colapsar rápido."
            },
            {
                "icon": "💣",
                "titulo": "Tiempo hasta caída",
                "desc": "Cuánto tiempo resiste el sistema con carga antes de volverse inestable. Ej: si al cabo de 40 minutos deja de responder, algo no está bien."
            }
        ]

        for kpi in kpis:
            st.markdown(f"""
            <div style='padding:15px; border:1px solid #e0e0e0; border-radius:10px; margin-bottom:15px; background-color:#fafafa'>
                <h4>{kpi["icon"]} {kpi["titulo"]}</h4>
                <p>{kpi["desc"]}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style='margin-top: 20px; padding: 15px; background-color: #f0f2f6; border-left: 5px solid #FF9800; border-radius: 5px'>
            <b>💡 Consejo:</b><br>
            Compara estos valores contra un punto de referencia o benchmark. No todos los sistemas tienen el mismo estándar de tiempo de respuesta.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### 📈 Ejemplo: Carga vs Tiempo de Respuesta")

        df = pd.DataFrame({
            "Usuarios simultáneos": [50, 100, 200, 400, 600],
            "Tiempo de respuesta (ms)": [300, 500, 900, 1500, 2500]
        })

        fig = px.line(df, x="Usuarios simultáneos", y="Tiempo de respuesta (ms)",
                    markers=True, title="Impacto de la carga en el tiempo de respuesta")

        st.plotly_chart(fig, use_container_width=True)
        
        fig2 = px.line(df2, x="Usuarios", y="Throughput (tps)",
                    title="❌ Throughput que no escala con la carga",
                    markers=True)
        st.plotly_chart(fig2, use_container_width=True)    
        
        with st.expander("❗ Ejemplo visual de Throughput deficiente"):
            st.markdown("""
            Imagina una tienda online que realiza pruebas de carga.

            - En condiciones ideales, debería procesar 20 transacciones por segundo con 200 usuarios conectados.
            - Pero en esta prueba, aunque aumentan los usuarios... las transacciones no aumentan 🧨

            Esto significa que el sistema **ya está saturado** o tiene cuellos de botella. 👎
            """)    

            # Segunda fila: nuevo gráfico a la derecha del ejemplo negativo
            col3, col4 = st.columns([2, 1.2])
    
            st.markdown("""
            👉 Como ves en el gráfico, después de cierto punto el sistema **deja de escalar**.  
            Esta es una clara señal de que **hay un límite técnico** que debe analizarse antes de ir a producción.
            """)

    with col3:
            st.markdown("""
            👉 Como ves en el gráfico, después de cierto punto el sistema **deja de escalar**.  
            Esta es una clara señal de que **hay un límite técnico** que debe analizarse antes de ir a producción.
            """)

with tabs[5]:
    st.header("🖼️ Ejemplos Visuales de Pruebas de Rendimiento")

    # Bloque 1: Dashboard de monitoreo en tiempo real
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("images/dashboard_jmeter.png", use_container_width=True)
    with col2:
        st.markdown("""
📊 **Dashboard de Monitoreo en Tiempo Real**

Este tipo de dashboards permiten observar, en tiempo real:

- 📈 Comportamiento de usuarios virtuales
- 🧠 Saturación del sistema
- 🚨 Alertas de errores
- 💡 Uso de recursos del servidor

👉 Generalmente integrados con herramientas como **Grafana**, **Prometheus**, **OctoPerf**, o **New Relic**.
        """)

    # Bloque 2: Gráfico de carga vs tiempo de respuesta
    col3, col4 = st.columns([1, 2])
    with col3:
        st.image("images/grafico_carga_tiempo_respuesta.png", use_container_width=True)
    with col4:
        st.markdown("""
📈 **Curva de carga vs tiempo de respuesta**

Este tipo de gráfico es útil para:

- Identificar puntos donde el sistema comienza a saturarse
- Detectar incrementos súbitos en el tiempo de respuesta
- Observar el rendimiento en función del tráfico de usuarios

🎯 Ayuda a validar que el sistema puede mantener la calidad bajo distintas condiciones.
        """)

    # Bloque 3: Errores detectados durante la prueba
    col5, col6 = st.columns([1, 2])
    with col5:
        st.image("images/Errores.png", use_container_width=True)
    with col6:
        st.markdown("""
🚨 **Errores frecuentes detectados en pruebas**

Durante las pruebas de carga, se pueden detectar errores como:

- ❌ **HTTP 500**: fallos internos del servidor
- 🚫 **HTTP 403 / 503**: rechazos por exceso de tráfico o caídas de servicio
- 🕒 **Timeouts**: operaciones que no responden dentro del tiempo esperado

🔍 Estos errores son señales de que el sistema necesita ajustes antes de ir a producción.
        """)


with tabs[6]:
    #st.header("✅ Buenas Prácticas en Pruebas de Rendimiento")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("images/Buenas_practicas_2.png", use_container_width=True)

    with col2:
        st.markdown("""
        ### 🧰 Prácticas esenciales para obtener buenos resultados

        <div style='padding:15px; border:1px solid #d0d0d0; border-radius:10px; background-color:#f9f9f9'>

        - 🧪 Probar en entornos lo más similares a producción  
        - 🕵️‍♂️ Aislar variables externas como caché, antivirus, redes compartidas  
        - 🧾 Documentar cada configuración (versiones, datos, scripts)  
        - 📈 Incluir pruebas de rendimiento en cada ciclo de desarrollo  
        - 🚀 Ejecutar pruebas antes y después de cambios importantes  
        - 🧠 Interpretar métricas, no solo mirar gráficas  
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        ### 🤖 Automatización y control

        <div style='padding:15px; border:1px solid #e0e0e0; border-radius:10px; background-color:#f5f5f5'>

        - 🔁 Versiona tus scripts de carga (usa Git o similar)  
        - ⚙️ Integra con CI/CD (Jenkins, GitLab, etc.)  
        - 📥 Almacena resultados por fecha para análisis histórico  
        - 📤 Genera reportes automáticos (HTML, CSV, JSON)

        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style='margin-top:25px; padding:20px; background-color: #f0f8ff; border-left: 5px solid #4CAF50; border-radius: 8px'>
    💡 <b>Consejo experto:</b><br>
    No esperes a que algo falle para medir. ¡Haz de las pruebas de rendimiento una práctica continua!  
    Así evitarás sorpresas desagradables en producción. 😎
    </div>
    """, unsafe_allow_html=True)


#with tabs[7]:
    #st.header("📌 Conclusión")
    #with st.container():
        #col1, col2 = st.columns([1, 2])
        #with col1:
            #st.image("images/conclusion.png", use_container_width=True)
        #with col2:
            #st.markdown("""
#💬 Las pruebas de rendimiento no son opcionales:

#- 🧠 Aportan inteligencia operacional
#- 📈 Mejoran experiencia usuario
#- 🚀 Ayudan a escalar con seguridad
#- 📉 Previenen fallos catastróficos
#            """)

#with tabs[8]:
    #st.header("🎯 Trivia Interactiva")
    #respuesta = st.radio("¿Qué tipo de prueba se usa para validar estabilidad prolongada bajo carga?", [
        #"Prueba de carga",
        #"Prueba de volumen",
        #"Prueba de estrés",
        #"Prueba de resistencia (Soak)"
    #])
    #if respuesta == "Prueba de resistencia (Soak)":
        #st.success("¡Correcto! 🎯")
    #else:
        #st.error("No es esa. ¡Sigue probando!")
