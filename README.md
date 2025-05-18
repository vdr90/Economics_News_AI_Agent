# 🧠 Economics News AI Agent

Este proyecto construye un **agente de IA** que genera un reporte económico diario con:

- 📰 Extracción automática de noticias económicas de Yahoo Finance e Investing.com
- 📊 Extracción automática de datos financieros (divisas, petróleo, tasas de interés, oro e índices accionarios) de distintos sitios
- 🤖 Resumen y análisis automatizado con IA (OpenAI)
- 📊 Generación de gráficas
- 📄 Reporte final en PDF con texto y gráficas

---

## 📂 Estructura del repositorio

![arq_scraper1](https://github.com/user-attachments/assets/ce9c6476-fde9-487a-8916-eafe9ae67e28)


```plaintext
Economics_News_AI_Agent/
├── assets/                         # Contiene imágenes de gráficas generadas para el reporte
│   ├── crudo.png
│   ├── niveles_indices.png
│   ├── niveles_indices_colores.png
│   ├── tasa_10y.png
│   ├── tipo_cambio.png
│   └── variacion_indices.png
│
├── data/                           # Archivos de datos de entrada/salida
│   ├── bullets_mercado.txt         # Bullets generados por el agente sobre el mercado
│   ├── bullets_noticias.txt        # Bullets traducidos y resumidos de noticias
│   ├── crude_prices.csv            # Precios del petróleo procesados
│   ├── fx_data.csv                 # Tipos de cambio
│   ├── rates_data.csv              # Tasa de interés de EE.UU.
│   ├── noticias_yahoo.json         # Noticias scrapeadas sin procesar
│   ├── scraped_data.json           # Último snapshot de variables de mercado
│   └── scraped_data_ddmmyy.json    # Snapshot de un día específico
│
├── src/                            # Código fuente principal
│   ├── news_scraper.ipynb          # Scrapea noticias desde Yahoo Finance
│   ├── market_scraper.ipynb        # Scrapea tasas, precios e índices
│   ├── data_updater.ipynb          # Actualiza y combina datos diarios en los CSV
│   ├── analysis_agent.ipynb        # Analiza y resume datos del mercado con OpenAI
│   ├── market_visualizer.ipynb     # Genera y guarda visualizaciones de datos
│   └── reporte.ipynb               # Compone el reporte final con texto e imágenes
│
├── logs/                           # Registros de la ejecución
│
├── ppt/                            # Presentación en PowerPoint
│   ├── Economic_report.pptx        # Reporte generado automáticamente en PDF
│   ├── imágenes/                   # Carpeta con imágenes utilizadas en el ppt
│   └── arq_scraper.png             # Imagen de la arquitectura del proyecto
│
├── main.py                         # Notebook principal para correr el flujo completo
├── run_report.sh                   # Script que automatiza la ejecución completa
├── requirements.txt                # Lista de dependencias para reproducir el entorno
├── README.md                       # Descripción del proyecto
└── .env                            # Variables de entorno (API keys, etc.)
```

---

## 🚀 Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

Configura tu API Key de OpenAI en el archivo `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🛠️ Cómo usar

1. Ejecuta `main.py`
2. El notebook hará scraping, analizará con IA y generará un PDF listo para enviar
3. Revisa tu carpeta: `economic_report_dd-mm-yyyy.pdf`

---

## 📌 Futuras mejoras

- Envío automático por correo
- Soporte multilingüe (inglés/español)
- Visualización interactiva en Streamlit o Dash

---
