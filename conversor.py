'''
Este programa extraera el texto de una url dada para luego convertir ese texto a un fichero mp3
'''
import nltk
from newspaper import Article
from gtts import gTTS
import streamlit as st
import time


#funcion para extraer el texto de una url, devuelve el texto extraido
def extraer_texto_url(url):
    
    #descargar recursos necesarios para nltk
    nltk.download('punkt')
    nltk.download('punkt_tab')
    
    # Extraer y procesar el artículo con newspaper3k y nltk
    article=Article(url)
    article.download()
    article.parse()
    noticia= article.text
    
    #dividimos el texto en oraciones con nltk
    oraciones=nltk.sent_tokenize(article.text)
    text=article.text

    #unimos las oraciones en un texto limpio
    texto= " ".join(oraciones)
    return texto

#funcion para convertir el texto en audio y guardarlo en un archivo mp3
def convertir_audio(texto,idioma):
    
    #convertimos el texto en un archivo mp3 con gtts
    tts=gTTS(texto, lang=idioma)
    st.info("Guardando el archivo mp3 .....espere")
    #guardar el archivo mp3
    tts.save("noticia.mp3")
    
    #mostramos mensaje de éxito
    st.success("¡Conversión completada!")


#definimos las diferentes paginas para navegar
def page_1():
   
    st.subheader("🗞️ Extraer audio de una noticia")

    

    with st.form("Introduce la url"):
        url = st.text_input("URL", value="", key="url_text")
        submit_url=st.form_submit_button("Enviar")
        
        if submit_url:
            
            texto= extraer_texto_url(url)
            convertir_audio(texto,"es")

def page_2():
    st.subheader("✍️ Escribe un texto para obtener su audio")

    with st.form("Introduce un texto"):
        texto = st.text_area("Introduce un texto", value="", key="texto_text")
        submit_texto=st.form_submit_button("Enviar")
        
        if submit_texto:
            
            #texto= extraer_texto_url(url)
            convertir_audio(texto,"es")


#creamos las categorias en el Sidebar
pg= st.navigation(
    {
        "Noticia": [
            st.Page(page_1,title="Obtener audio de noticia ", icon="📰"),
        ],
        "Texto": [
            st.Page(page_2, title="Obtener audio de texto", icon="✒️")
        ]
    }
)
#iniciamos la paginacion
pg.run()




