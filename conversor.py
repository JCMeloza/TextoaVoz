'''
Este programa extraera el texto de una url dada para luego convertir ese texto a un fichero mp3
'''
import nltk
from newspaper import Article
from gtts import gTTS
#import nltk.downloader
#descargar recursos necesarios para nltk
nltk.download('punkt')

#creamos una variable tipo string donde almazenamos la url que vamos a utilizar.
url=str(input("Introduce la url del texto que vamos a pasar a mp3:"))
article=Article(url)
article.download()
article.parse()
texto=article.text
tts=gTTS(texto, lang='es')
tts.save("noticia.mp3")


