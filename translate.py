import tkinter as tk
from tkinter import filedialog
import pysrt
from deep_translator import GoogleTranslator

def traducir_texto(texto, destino):
    translator = GoogleTranslator(source='auto', target=destino)
    traduccion = translator.translate(texto)
    return traduccion

def traducir_archivo_srt(ruta_archivo, nombre_archivo, destino):
    # Carga el archivo SRT
    subtitulos = pysrt.open(ruta_archivo)

    # Traduce cada línea de subtítulo
    for subtitulo in subtitulos:
        texto_ingles = subtitulo.text
        texto_traducido = traducir_texto(texto_ingles, destino)
        subtitulo.text = texto_traducido

    # Guarda los subtítulos traducidos en un nuevo archivo SRT
    ruta_salida = ruta_archivo.replace('.srt', f'_traducido_{nombre_archivo}.srt')
    subtitulos.save(ruta_salida, encoding='utf-8')

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[('Archivos SRT', '*.srt')])
    ruta_archivo_entry.delete(0, tk.END)
    ruta_archivo_entry.insert(0, archivo)

def traducir_archivo():
    ruta_archivo = ruta_archivo_entry.get()
    nombre_archivo = nombre_archivo_entry.get()
    idioma_destino = idioma_destino_entry.get()
    traducir_archivo_srt(ruta_archivo, nombre_archivo, idioma_destino)
    tk.messagebox.showinfo("Traducción completada", "El archivo SRT ha sido traducido con éxito.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title('Traductor de Archivo SRT')
ventana.geometry('400x250')

# Etiqueta y campo de entrada para la ruta del archivo SRT
ruta_archivo_label = tk.Label(ventana, text='Ruta del archivo SRT:')
ruta_archivo_label.pack()

ruta_archivo_entry = tk.Entry(ventana, width=40)
ruta_archivo_entry.pack()

examinar_button = tk.Button(ventana, text='Examinar', command=seleccionar_archivo)
examinar_button.pack()

# Etiqueta y campo de entrada para el nombre del archivo destino
nombre_archivo_label = tk.Label(ventana, text='Nombre del archivo destino:')
nombre_archivo_label.pack()

nombre_archivo_entry = tk.Entry(ventana, width=30)
nombre_archivo_entry.pack()

# Etiqueta y campo de entrada para el idioma destino
idioma_destino_label = tk.Label(ventana, text='Idioma destino:')
idioma_destino_label.pack()

idioma_destino_entry = tk.Entry(ventana, width=20)
idioma_destino_entry.pack()

# Botón para iniciar la traducción
traducir_button = tk.Button(ventana, text='Traducir', command=traducir_archivo)
traducir_button.pack()

# Iniciar bucle principal de la GUI
ventana.mainloop()
