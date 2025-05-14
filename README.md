# Economics_News_AI_Agent

El objetivo de este proyecto fue crear un agente de IA para realizar un reporte económico diario. Para ello realiza web scraping de páginas de noticias económicas y resume las noticias más importantes en bullet. Además, también realiza web scraping de algunas páginas de internet para obtener datos de variables financieras, graficarlas y analizarlas para incluirlas en el reporte.

Estructura del repositorio

economic_report/
├── main.ipynb                      # Flujo general: scraping → análisis → PDF
├── .env                            # Clave API OpenAI
├── requirements.txt                # Dependencias del proyecto
│
├── data/
│   ├── fx_data.csv                 # Datos de tipos de cambio
│   ├── crude_prices.csv            # Precios de petróleo
│   └── rates_data.csv              # Tasas de interés
│
├── assets/
│   ├── divisas.png                 # Gráfica de variación de divisas
│   ├── curva_mexico.png            # Curva de rendimientos México
│   ├── petroleo.png                # Gráfica de precios de petróleo
│
├── news_scraper.py                 # Extrae noticias desde Yahoo y Investing
├── market_scraper.py              # Extrae datos financieros con yfinance
├── analysis_agent.py              # Usa OpenAI para resumir y analizar
└── reporte.py                     # Define el diseño y genera el PDF final
