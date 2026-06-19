import streamlit as st
import json

# Carregando arquivo JSON
with open ("playlist.json","r",encoding="utf-8") as arquivo:
    dados = json.load(arquivo)



# ------------------------- SIDE BAR
st.sidebar.title("AOTY & SOTY PLAYLIST ❁")
st.sidebar.image("logo.png")

estilo = st.sidebar.selectbox("Escolha um estilo musical:", dados['estilos'].keys())
artista = st.sidebar.selectbox("Escolha um artista:", dados['estilos'][estilo]['Artistas'].keys())
# ------------------------- BODY
st.title(artista)

video, sobre = st.tabs(["Vídeo","Sobre"])

with video:
    st.video(dados['estilos'][estilo]['Artistas'][artista]['video'])

with sobre:
    nome_arquivo = dados['estilos'][estilo]['Artistas'][artista]['sobre']

    with open(nome_arquivo,'r',encoding='utf-8') as arquivo:
        texto = arquivo.read()

    st.markdown(texto)






