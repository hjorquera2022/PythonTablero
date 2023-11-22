import tkinter as tk
import chess

# Función para obtener el carácter Unicode de una pieza de ajedrez
def obtener_caracter_pieza(pieza):
    pieza_unicode = {
        chess.PAWN: "♙",
        chess.KNIGHT: "♘",
        chess.BISHOP: "♗",
        chess.ROOK: "♖",
        chess.QUEEN: "♕",
        chess.KING: "♔"
    }
    return pieza_unicode.get(pieza.symbol(), " ")

# Función para dibujar el tablero en la ventana
def dibujar_tablero():
    for i in range(8):
        for j in range(8):
            color = "white" if (i + j) % 2 == 0 else "black"
            etiqueta = tk.Label(ventana, text=obtener_caracter_pieza(tablero.piece_at(8 * i + j)), bg=color, fg="black", font=("Arial", 36))
            etiqueta.grid(row=i, column=j)

# Función para mover una pieza
def mover_pieza(origen, destino):
    movimiento = chess.Move.from_uci(origen + destino)
    if movimiento in tablero.legal_moves:
        tablero.push(movimiento)
        dibujar_tablero()

# Función para manejar el evento de mover una pieza
def mover_pieza_evento():
    origen = origen_entry.get()
    destino = destino_entry.get()
    mover_pieza(origen, destino)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ajedrez")

# Crear los campos de entrada y el botón para mover la pieza
origen_label = tk.Label(ventana, text="Origen:")
origen_label.grid(row=8, column=0)
origen_entry = tk.Entry(ventana)
origen_entry.grid(row=8, column=1)

destino_label = tk.Label(ventana, text="Destino:")
destino_label.grid(row=8, column=2)
destino_entry = tk.Entry(ventana)
destino_entry.grid(row=8, column=3)

mover_button = tk.Button(ventana, text="Mover", command=mover_pieza_evento)
mover_button.grid(row=8, column=4)

# Crear un objeto Board de chess
tablero = chess.Board()

# Dibujar el tablero inicial
dibujar_tablero()

# Iniciar el bucle principal de la ventana
ventana.mainloop()