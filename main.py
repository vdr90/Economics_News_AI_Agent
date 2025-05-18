#!/usr/bin/env python
# coding: utf-8

# # Proyecto Final Building AI Agents
# ## Extractor y Analizador de Datos Web
# ### Valeria Durán Rubio 124273

# In[1]:


import os
import nbformat
import time
from nbclient import NotebookClient
from datetime import datetime

root_path = "/Users/valduran/github/Economics_News_AI_Agent/src"
os.chdir(root_path)

src_path = "./"

# Orden de ejecución
notebooks = [
    "market_scraper.ipynb",
    "news_scraper.ipynb",
    "data_updater.ipynb",
    "analysis_agent.ipynb",
    "market_visualizer.ipynb",
    "pdf_generator.ipynb"
]

# Crear carpeta de logs si no existe
log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"log_{datetime.today().strftime('%d%m%y')}.txt")

import time
from nbclient import NotebookClient
import nbformat

# Ejecutar notebooks uno por uno
for nb_file in notebooks:
    nb_path = os.path.join(src_path, nb_file)
    print(f"\n🚀 Ejecutando: {nb_file}...")

    try:
        with open(nb_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        client = NotebookClient(
            nb,
            timeout=600,
            kernel_name="python3",  # Nombre de tu entorno
            allow_errors=False
        )
        client.execute()  # Ejecuta todas las celdas correctamente

        # Guardar el notebook ejecutado (opcional)
        with open(nb_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)

        print(f"✅ Finalizado: {nb_file}")

        # Pausa antes del siguiente notebook
        time.sleep(2)

    except Exception as e:
        error_msg = f"\n❌ Error ejecutando {nb_file}:\n{str(e)}\n"
        print(error_msg)

        # Registrar error en archivo de log
        with open(log_file, "a", encoding="utf-8") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{timestamp}] {error_msg}")

        #break



