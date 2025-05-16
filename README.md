# 🧠 Economics News AI Agent

Este proyecto construye un **agente de IA** que genera un reporte económico diario con:

- 📰 Extracción automática de noticias económicas de Yahoo Finance
- 📊 Datos financieros (divisas, petróleo, tasas de interés, oro e índices accionarios)
- 🤖 Resumen automatizado con IA (OpenAI)
- 📄 Reporte final en PDF con texto y gráficas

---

## 📂 Estructura del repositorio

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
│   ├── crude_prices_orig.csv       # Versión original antes de procesar
│   ├── fx_data.csv                 # Tipos de cambio
│   ├── rates_data.csv              # Tasa de interés de EE.UU.
│   ├── noticias_yahoo.json         # Noticias scrapeadas sin procesar
│   ├── scraped_data.json           # Último snapshot de variables de mercado
│   ├── scraped_data_140525.json    # Snapshot del 14 de mayo de 2025
│   └── scraped_data_150525.json    # Snapshot del 15 de mayo de 2025
│
├── src/                            # Código fuente principal
│   ├── main.ipynb                  # Notebook principal para correr el flujo completo
│   ├── news_scraper.ipynb          # Scrapea noticias desde Yahoo Finance
│   ├── market_scraper.ipynb        # Scrapea tasas, precios e índices
│   ├── data_updater.ipynb          # Actualiza y combina datos diarios en los CSV
│   ├── analysis_agent.ipynb        # Analiza y resume datos del mercado con OpenAI
│   ├── market_visualizer.ipynb     # Genera y guarda visualizaciones de datos
│   └── reporte.ipynb               # Compone el reporte final con texto e imágenes
│
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

1. Ejecuta `main.ipynb`
2. El notebook hará scraping, analizará con IA y generará un PDF listo para enviar
3. Revisa tu carpeta: `reporte_economico.pdf`

---

## 📌 Futuras mejoras

- Envío automático por correo
- Soporte multilingüe (inglés/español)
- Visualización interactiva en Streamlit o Dash

---
