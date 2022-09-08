import streamlit as st
import pandas as pd
import os

# Quitar headers y mas
st.set_page_config(page_title='TIX')#, page_icon = favicon)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Seleccionar Eventos
evento = st.sidebar.selectbox(label='Seleccionar evento', options=os.listdir('./data/'))
df = pd.read_csv(f'./data/{evento}', index_col='Codigo')

# App
st.title('Buscar registro')
codigo = st.text_input(label='', placeholder='Ingresar numero')
if st.button(label='Buscar') or codigo:
    c1, c2 = st.columns(2)
    try:
        ser = df.loc[codigo]
        if ser['Entro'] == True:
            c1.markdown('### Ya esta adentro')
            c2.image(image='./assets/caution.png', width=200)

        else:
            df.loc[codigo, 'Entro'] = True

            c1.markdown(f'### *Nombre:* {ser["Nombre"]}')
            c1.markdown(f'### *Cedula:* {ser["Cedula"]}')
            c2.image(image='./assets/aprobado.png', width=200)

    except:
        c1.markdown('### No se encontro')
        c2.image(image='./assets/fallado.png', width=200)

    df.to_csv(f'./data/{evento}')

    st.markdown('#### Los registros que faltan')
    st.write(df[df['Entro'].isnull()][['Nombre','Cedula']])

