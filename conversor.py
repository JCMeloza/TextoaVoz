'''
Este programa extraera el texto de una url dada para luego convertir ese texto a un fichero mp3
'''
import nltk
from newspaper import Article
from gtts import gTTS

#descargar recursos necesarios para nltk
nltk.download('punkt')
nltk.download('punkt_tab')

#creamos una variable tipo string donde almazenamos la url que vamos a utilizar.
url=str(input("Introduce la url del texto que vamos a pasar a mp3:"))

# Extraer y procesar el artículo con newspaper3k y nltk
article=Article(url)
article.download()
article.parse()

#dividimos el texto en oraciones con nltk
oraciones=nltk.sent_tokenize(article.text)
text=article.text

#unimos las oraciones en un texto limpio
texto= " ".join(oraciones)

#convertimos el texto en un archivo mp3 con gtts
tts=gTTS(texto, lang='es')
tts.save("noticia_n.mp3")

print("El artículo ha sido convertido a voz y guardado.")


