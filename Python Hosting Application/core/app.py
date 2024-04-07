# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess
from threading import Thread
import os


class App(tk.Frame):
    
    
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.master.title("Python Hosting Application")
        self.master.geometry("1080x675")
        
        # VAR
        self.Showgui = IntVar()
        self.MainMenu = Menu(self)

        # Bouton pour exécuter la commande
        self.run_button = tk.Button(self, text="Lancer le serveur Minecraft", command=self.start_server)
        self.run_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Zone de texte pour afficher la sortie en temps réel
        self.output_text = tk.Text(self, wrap="word")
        self.output_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # CheckBox pour gui
        self.CheckBoxGui = tk.Checkbutton(self,text="Gui",variable=self.Showgui)
        self.CheckBoxGui.grid(row=1, column=1,padx=10, pady=10, sticky="w")
        

        self.vlist = ["fabric", "vanilla"]
        # Combobox pour le modloader
        self.loaderCombobox = ttk.Combobox(self, values=self.vlist, state="readonly")
        self.loaderCombobox.set("Pick a modloader")
        self.loaderCombobox.grid(row=2, column=1,padx=10, pady=10, sticky="w")

        self.vlist = ["1.20.4", "1.20.3", "1.20.2", "1.20.1", "1.20", "1.19.4", "1.19.3", "1.19.2", "1.19.1", "1.19", "1.18.2", "1.18.1", "1.18","1.17.1", "1.17", "1.16.5", "1.16.4", "1.16.3", "1.16.2", "1.16.1", "1.16"]
        # Combobox pour la version
        self.versionCombobox = ttk.Combobox(self, values=self.vlist, state="readonly")
        self.versionCombobox.set("Pick a version")
        self.versionCombobox.grid(row=3, column=1,padx=10, pady=10, sticky="w")
        
        

        
    def start_server(self):
        # Exécute la commande shell pour démarrer le serveur Minecraft
        if (self.loaderCombobox.get() == "vanilla"):
            command = f"cd \"{os.path.dirname(os.path.abspath(__file__))[:-5]}\\jar\\vanilla\" & java -Xmx2G -jar server.jar"
        else:
            command = f"cd \"D:\\VisualStudio Project\\Python Hosting Application\\Python Hosting Application\\jar\\fabric\\{self.versionCombobox.get()}\" & java -Xmx2G -jar server.jar"
        self.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        
        # Lance un thread pour lire la sortie de la commande en temps réel
        self.reader_thread = Thread(target=self.read_output)
        self.reader_thread.daemon = True
        self.reader_thread.start()
    
    def read_output(self):
        # Lit en continu la sortie de la commande
        for line in self.process.stdout:
            # Met à jour la zone de texte avec la sortie lue
            self.output_text.insert(tk.END, line)
            self.output_text.see(tk.END)

