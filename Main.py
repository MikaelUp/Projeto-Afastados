import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage, IntVar, Checkbutton
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
import os


# Criar a janela e o tema gráfico
interface = ttk.Window(title="Afastamento", themename="darkly")
interface.geometry("850x620")

# Tirando a opção de redimensionar a janela
interface.resizable(False, False)








interface.mainloop()