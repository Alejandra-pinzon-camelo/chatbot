import tkinter as tk
from tkinter import scrolledtext
import spacy

# Cargar modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")


# Procesamiento del Lenguaje

def procesar_texto(oracion):
    doc = nlp(oracion)
    return {
        "tokens": [token.text for token in doc],
        "lematizacion": [(token.text, token.lemma_) for token in doc],
        "pos_tagging": [(token.text, token.pos_) for token in doc]
    }

def chatbot_respuesta(oracion):
    analisis = procesar_texto(oracion)

    if "comprar" in oracion.lower():
        return "🛒 Claro, tenemos ofertas increíbles. ¿Quieres juegos de PC, Xbox o PlayStation?"
    elif "xbox" in oracion.lower():
        return "🎮 Xbox: Tenemos *Halo Infinite* y *Forza Horizon 5* en promoción."
    elif "play" in oracion.lower() or "ps5" in oracion.lower():
        return "🕹️ PlayStation: ¡Tenemos *God of War Ragnarök* y *Spider-Man 2*! 🔥"
    elif "pc" in oracion.lower():
        return "💻 En PC puedes encontrar *Minecraft*, *Valorant* y *The Witcher 3*."
    elif "precio" in oracion.lower():
        return "💰 Los precios varían, pero tenemos descuentos de hasta el 40% esta semana."
    else:
        return f"Procesé tu mensaje y encontré:\nTokens: {analisis['tokens']}\nLemas: {analisis['lematizacion']}\nPOS: {analisis['pos_tagging']}"

# ------------------------------
# Interfaz gráfica con Tkinter
# ------------------------------
def enviar():
    mensaje = entrada.get()
    if mensaje.strip() == "":
        return
    
    # Mostrar mensaje del usuario
    chatbox.insert(tk.END, "🧑 Tú: " + mensaje + "\n", "user")
    
    # Obtener respuesta del bot
    respuesta = chatbot_respuesta(mensaje)
    chatbox.insert(tk.END, "🤖 Bot: " + respuesta + "\n\n", "bot")
    
    entrada.delete(0, tk.END)
    chatbox.yview(tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("🕹️ Tienda Gamer - Chatbot 🎮")
ventana.geometry("650x550")
ventana.config(bg="#0d1117")

# Título llamativo
titulo = tk.Label(
    ventana, 
    text="💥 Bienvenido a la Tienda Gamer 🎮💥", 
    font=("Consolas", 16, "bold"), 
    bg="#0d1117", fg="#00ffcc"
)
titulo.pack(pady=10)

# Caja de chat
chatbox = scrolledtext.ScrolledText(
    ventana, wrap=tk.WORD, width=70, height=20, 
    bg="#161b22", fg="white", font=("Consolas", 11), insertbackground="white"
)
chatbox.pack(pady=10)

# Estilos de texto
chatbox.tag_config("user", foreground="#58a6ff", font=("Consolas", 11, "bold"))
chatbox.tag_config("bot", foreground="#00ff88", font=("Consolas", 11))

# Marco para entrada y botón
frame = tk.Frame(ventana, bg="#0d1117")
frame.pack(pady=10)

# Entrada de texto
entrada = tk.Entry(frame, width=40, font=("Consolas", 12), bg="#21262d", fg="white", insertbackground="white")
entrada.pack(side=tk.LEFT, padx=10)

# Botón enviar
boton = tk.Button(
    frame, text="Enviar", command=enviar, 
    bg="#ff4b5c", fg="white", font=("Consolas", 12, "bold"), width=10
)
boton.pack(side=tk.LEFT)

# Mensaje inicial del bot
chatbox.insert(tk.END, "🤖 Bot: ¡Hola gamer! Bienvenido a la Tienda de Videojuegos 🎮\nEscríbeme si quieres ver precios, ofertas o juegos disponibles.\n\n", "bot")

ventana.mainloop()
