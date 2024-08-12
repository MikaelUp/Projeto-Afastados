import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage, IntVar, Checkbutton
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
import os


# Criar a janela e o tema gráfico
interface = ttk.Window(title="Afastamento", themename="cosmo")
interface.geometry("850x620")

# Tirando a opção de redimensionar a janela
interface.resizable(False, False)


# Criando Frames
frame_logo = ttk.Frame(interface, width=850, height=52, bootstyle="primary")
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(interface, orient=HORIZONTAL).grid(row=1, column=0, ipadx=680, pady=0)



interface.mainloop()