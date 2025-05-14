# 🧠 Economics News AI Agent

Este proyecto construye un **agente de IA** que genera un reporte económico diario con:

- 📰 Extracción automática de noticias económicas (Yahoo Finance, Investing.com)
- 📊 Datos financieros (divisas, petróleo, tasas de interés)
- 🤖 Resumen automatizado con IA (OpenAI)
- 📄 Reporte final en PDF con texto y gráficas

---

## 📂 Estructura del repositorio

```plaintext
economic_report/
├── main.ipynb                   # Flujo general: scraping → análisis → PDF
├── .env                         # Clave API OpenAI
├── requirements.txt             # Dependencias del proyecto
├── data/
│   ├── fx_data.csv              # Datos de tipos de cambio
│   ├── crude_prices.csv         # Precios de petróleo
│   └── rates_data.csv           # Tasas de interés
├── assets/
│   ├── divisas.png              # Gráfica de variación de divisas
│   ├── curva_mexico.png         # Curva de rendimientos México
│   └── petroleo.png             # Gráfica de precios de petróleo
├── news_scraper.py              # Extrae noticias desde Yahoo e Investing
├── market_scraper.py            # Extrae datos financieros con yfinance
├── analysis_agent.py            # Usa OpenAI para resumir y analizar
└── reporte.py                   # Define el diseño y genera el PDF final
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
