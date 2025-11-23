# nova-financial-analytics-week1
Predicting Price Moves with News Sentiment
Project Overview
This project, developed for Nova Financial Solutions, aims to enhance financial forecasting by integrating qualitative news sentiment with quantitative stock market data. The core objective is to determine if the sentiment of financial news headlines (Positive, Negative, Neutral) can serve as a predictive signal for daily stock price movements.

By leveraging Natural Language Processing (NLP) and statistical correlation, this analysis seeks to move beyond traditional technical indicators and provide actionable, sentiment-driven investment strategies.

Repository Structure
The project follows a modular data science structure to ensure reproducibility and scalability.

Plaintext

nova-financial-analytics/
├── .github/
│   └── workflows/       # CI/CD pipelines (e.g., unit tests)
├── data/                # Raw and processed datasets (excluded from git)
├── notebooks/           # Jupyter notebooks for analysis
│   ├── EDA.ipynb        # Exploratory Data Analysis (News data)
│   ├── Technical_Analysis.ipynb # Stock Indicators & Visualization
│   └── Sentiment_Analysis.ipynb # NLP & Correlation (In Progress)
├── src/                 # Reusable Python modules
│   ├── __init__.py
│   ├── loader.py        # Data ingestion and cleaning utilities
│   ├── analysis.py      # Financial metrics & indicators logic
│   └── plotting.py      # Custom visualization functions
├── tests/               # Unit tests for src modules
├── .gitignore           # Files to ignore (e.g., venv, data)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
Installation & Setup
To run this project locally, follow these steps:

1. Clone the Repository
Bash

git clone https://github.com/YOUR_USERNAME/nova-financial-analytics.git
cd nova-financial-analytics
2. Create a Virtual Environment
Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
Note for Windows Users: If you encounter errors installing TA-Lib, download the pre-built binary from Christoph Gohlke's library or execute:

Bash

conda install -c conda-forge ta-lib
Key Analysis Modules
1. Exploratory Data Analysis (EDA)
Goal: Understand the characteristics of the financial news dataset.

Key Findings:

Headline Length: Headlines are concise (50-80 chars), optimized for rapid trader consumption.

Publisher Bias: A small number of publishers (e.g., Benzinga) dominate the news volume.

Data Anomaly: A "Midnight Spike" in timestamps was discovered, necessitating a shift to Daily Aggregation for correlation analysis.

2. Quantitative Analysis
Goal: Compute technical indicators to contextualize price movements.

Tools Used: YFinance for data, TA-Lib for indicators, PyNance for metrics.

Metrics Calculated:

SMA (Simple Moving Average): For trend identification (20-day & 50-day).

RSI (Relative Strength Index): To spot overbought/oversold conditions.

MACD: To track market momentum.

Volatility & Sharpe Ratio: To assess risk-adjusted returns.

3. Sentiment Analysis (Upcoming)
Goal: Correlate headline polarity with stock returns.

Method: TextBlob will score headlines (-1 to +1). We will then calculate the Pearson correlation between the Daily Sentiment Score and the Daily Stock Return.

Usage
Running the Analysis
The core analysis is contained in the notebooks/ folder. To launch the environment:

Bash

jupyter notebook
Open EDA.ipynb for news data insights.

Open Technical_Analysis.ipynb for stock charts and metrics.

Using the Source Modules
You can import the custom modules in your own scripts:

Python

from src.loader import load_news_data
from src.analysis import apply_technical_indicators

# Load and process data
df = load_news_data('data/raw_news.csv')
df_indicators = apply_technical_indicators(stock_data)
Contributing
Fork the repository.

Create a feature branch (git checkout -b feature/YourFeature).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a Pull Request.