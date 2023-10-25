import streamlit as st
import pandas as pd
import streamlit.components.v1 as c
import streamlit as st
from streamlit_folium import folium_static
import folium
import variables as v
from PIL import Image

# Ass visual files

backgroundColor = "#F0F0F0"
st.set_page_config(page_title="EDA: Alquileres residenciales vs alquileres turísticos ",
                   page_icon="favicon.ico")


st.title("Estudio del alquiler residencial en Madrid e impacto de las viviendas vacacionales")

# Using object notation
selection = st.sidebar.selectbox(
    "Indice:",
    ("Portada","Introducción", "Análisis", "Mapas", "Conclusiones")
)

if selection == "Portada":

    firts_co, left_co, cent_co, right_co, last_co = st.columns(5)
    img_port = Image.open(v.URL_IMG_PORT)
    img_port2 = Image.open(v.URL_IMG_PORT2)

    with firts_co:
        st.image(img_port, width=450, )
    with right_co:
        st.markdown("<h1 style='text-align: center; color: white;'>VS</h1>", unsafe_allow_html=True)
    with last_co:
        st.image(img_port2, width=400, )

    st.write("## Hipotesis iniciales:") 
    st.write("- Un breve estudio sobre el alquiler residencial en Madrid y contrastandolo con datos de la paginas idealista con datos actuales.")
    st.write("""
        - Comparar estos análisis con los alquileres de viviendas vacacionales.
        """)
    
elif selection == "Introducción":
    img_com = Image.open(v.URL_IMG_COM_MAD)
    img_ide = Image.open(v.URL_IMG_IDEALISTA)

    st.write("\n")
    st.write("\n")
    st.write("\n")

    first_co, last_co = st.columns(2)
    with first_co:
        st.image(img_com, width=100, )
        st.write("\n")
        st.write("\n")
        st.image(img_ide, width=200, )

    with last_co:
        st.write("¿La Comunidad de Madrid debería regular las viviendas vacacionales?")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("¿De donde hemoas sacado nuestros datos para el estudio? \n Los datos de Idealista los hemos adquirido median webscraping con: \n - Selenium \n - Beatiful Soup")
elif selection == "Análisis":
    container_1 = st.container()
    with container_1:
        df_idealista = pd.read_csv("../data/rentaMadrid2023Idealista.csv", sep=";")
        with st.expander("Tabla Idealista"):
            st.write("Aqui os vamos a mostrar una parte de los datos que hemos podido adquirir de la web de Idealista")
            st.write(df_idealista.head(10))
        with st.expander("Primeros Análisis"):
            container_1_1 = st.container()
            with container_1_1:
                col1, col2 = st.columns(2)
                with col1:
                    st.write(df_idealista.describe())
                with col2:
                    df_mode = df_idealista.loc[:,"Price":"Room"].mode().T
                    df_mode.rename(columns={0: "Mode"}, inplace=True)
                    st.write(df_mode)
                st.write("\n")
            container_1_2 = st.container()
            with container_1_2:
                img_analy1 = Image.open(v.URL_IMG_DENS_MAD)
                st.image(img_analy1)
                col1, col2 = st.columns(2)
                with col1:
                    st.write(" - Precio medio: 2133.81 € \n - m² medio: 114 \n ")
                with col2:
                    st.write(" - Precio más repetido: 1500€ \n - m² más repetido: 60")
            container_1_3 = st.container()
            with container_1_3:
                st.write("\n")
                img_analy2 = Image.open(v.URL_IMG_BOX_VIO_MAD)
                st.image(img_analy2)
                st.write("\n")
                st.write("Podemos apreciar el aumento de las viviendas de 60m²")
                img_analy3 = Image.open(v.URL_IMG_EV_TAM_MAD)
                st.image(img_analy3)
        with st.expander("Analisis multivariable:"):
            file = open(v.URL_HTML_PLOTLY_VAR_MAD, "r")
            c.html(file.read(), height=500)
            df_idealista[["Price", "m2", "Floor"]].corr()

            st.write(" Podemos apreciar que cuanto mayor son los m² mayor es el precio y aunmenta el numero de habitaciones pero el numero del piso no tiene relación alguna.")
            st.write("Vamos a ver las correlaciones entre estas variables:")
            img_corr = Image.open(v.URL_IMG_CORR_MAD)
            st.image(img_corr)
            st.write("- Correlaciones positivas elevadas: Precio/m², m²/Room")
            file = open(v.URL_HTML_CORR_MAD, "r")
            c.html(file.read(), height=500)

elif selection == "Mapas":

    select_map = st.sidebar.selectbox(
        "Mapas:",
        ("Mapa Madrid",
         "Mapa delimitacion de los barrios de Madrid",
         "Mapa de las viviendas vacacionales",
         "Mapa de calor de las viviendas vacacionales",
         "Mapa de las viviendas de alquiler residencial",
         "Mapa de calor de las viviendas de alquiler residencial",
         "Mapa conjunto",
         "Mapa de la evolución de viviendas vacacionales en Madrid")
    )
    if select_map =="Mapa Madrid":
        map_mad = folium.Map(location=[40.4567, -3.6840], zoom_start=10)
        folium_static(map_mad)
    elif select_map == "Mapa delimitacion de los barrios de Madrid":
        file = open(v.URL_HTML_MAP_NEIGH_MAD, "r")
        c.html(file.read(), height=1000)
    elif select_map == "Mapa de las viviendas vacacionales":
        file = open(v.URL_HTML_MAP_HOL_MAD, "r")
        c.html(file.read(), height=1000)
    elif select_map == "Mapa de calor de las viviendas vacacionales":
        file = open(v.URL_HTML_MAP_HEAT_HOL_MAD, "r")
        c.html(file.read(), height=1000)
    elif select_map == "Mapa de las viviendas de alquiler residencial":
        file = open(v.URL_HTML_MAP_RES_MAD, "r")
        c.html(file.read(), height=1000)
    elif select_map == "Mapa de calor de las viviendas de alquiler residencial":
        file = open(v.URL_HTML_MAP_HEAT_RES_MAD, "r")
        c.html(file.read(), height=1000)
    elif select_map == "Mapa conjunto":
        file = open(v.URL_HTML_MAP_ALL, "r")
        c.html(file.read(), height=1000)
    elif select_map == "Mapa de la evolución de viviendas vacacionales en Madrid":
        file = open(v.URL_HTML_MAP_TIME_HOL_MAD, "r")
        c.html(file.read(), height=1000)

elif selection == "Conclusiones":

    st.write("Por último vamos a analizar la evolución del Alquiler en Madrid desde 2015 hasta 2018 para ver si este aumento de viviendas turísticas ha aumentado el alquiler residencial.")
    img_ev_alq = Image.open(v.URL_IMG_EV_RENT_MAD)
    st.image(img_ev_alq)
    st.write("Podemos sacar las siguientes conclusiones después de ver el anterior gráfico del INE:")
    st.write("""
- Tras el análisis de los alquileres de idealista en Madrid podemos asumir que el precio medio es de 1500€ por una media de 60m².
- Podemos observar que cada vez se alquilan pisos más pequeños en Madrid y cuanto más alejados estén del centro de Madrid, concretamente hacia el sur, podemos encontrar alquileres más bajos.
- En los análisis con los mapas observamos que la ha habido un gran aumento de vivienda vacacionales en los último 6 años y que se encuentran zonas centricas, haciendo que baje el número de alquileres residenciales en esas zonas.
- No puedo concluir con los datos obtenidos que el aumento de viviendas vacacionales este relacionado con el aumento de alquileres residenciales.
             """)
    st.write("## Siguientes pasos")
    st.write("""
Por último como no se ha podido confirmar la hipotesis podemos realizar un estudio más exhaustivo de la evolución de los alquileres de Madrid, también con más datos de alquileres en Madrid y analizar los datasets de las viviendas vacacionales para compararlo con los alquileres residenciales para ver si influye en el precio. Podremos realizar un estudio por barrios resiendciales y ver las características de las viviendas que más se alquilan y el motivo.

Una vez hecho podemos hacer un modelo predictivo para ver como pueden ir evolucionando los alquileres en Madrid y como puede llegar a aumentar las viviendas vacacionales a lo largo del tiempo, ya que hemos visto que en pocos años, el aumento ha sido enorme.
             """)
    st.write("# Muchas gracias a tod@s!")