
# Nova Financial Analytics – Week 1  
**Predicting Stock Price Movements Using News Sentiment**


## Project Overview
This project, developed for **Nova Financial Solutions**, enhances financial forecasting by integrating **qualitative news sentiment** with **quantitative stock market data**. The core objective is to determine if the sentiment of financial news headlines (Positive, Negative, Neutral) can serve as a predictive signal for daily stock price movements.  

By leveraging **Natural Language Processing (NLP)**, **technical indicators**, and **statistical correlation analysis**, this work moves beyond traditional charting methods and provides actionable, sentiment-driven investment strategies.

---

## Repository Structure
```
nova-financial-analytics-week1/
├── .github/             # CI/CD workflows (unit tests, automation)
├── data/                # Raw and processed datasets (excluded via .gitignore)
├── notebooks/           # Jupyter notebooks for analysis
│   ├── EDA.ipynb                # Exploratory Data Analysis (news dataset)
│   ├── Technical_Analysis.ipynb # Stock indicators & visualization
│   └── Sentiment_Correlation.ipynb # NLP sentiment scoring & correlation
├── src/                 # Reusable Python modules
│   ├── __init__.py
│   ├── loader.py        # Data ingestion and cleaning utilities
│   ├── analysis.py      # Technical indicators & financial metrics
│   └── plotting.py      # Custom visualization functions
├── tests/               # Unit tests for reproducibility
├── .gitignore           # Ignore venv, data dumps, etc.
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Installation & Setup
1. **Clone the Repository**
```bash
git clone https://github.com/abenezer4/nova-financial-analytics-week1.git
cd nova-financial-analytics-week1
```

2. **Create a Virtual Environment**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

>  **Note for Windows Users:** If you encounter errors installing TA-Lib, use:  
```bash
conda install -c conda-forge ta-lib
```

---

##  Key Analysis Modules

### 1. Exploratory Data Analysis (EDA)
**Goal:** Understand the characteristics of the financial news dataset.  
**Findings:**  
- Headlines are concise (50–80 chars).  
- Publisher bias: Benzinga dominates (>70%).  
- Timestamp anomaly (“Midnight Spike”) → required daily aggregation.  
**Visuals:** Histogram of headline lengths, publisher pie chart, publication frequency plot.

---

### 2. Quantitative Analysis
**Goal:** Compute technical indicators to contextualize price movements.  
**Tools:** TA-Lib, PyNance, pandas.  
**Metrics:**  
- SMA (20 & 50-day) → trend identification.  
- RSI → overbought/oversold signals.  
- MACD → momentum tracking.  
- Volatility & Sharpe ratio → risk-adjusted returns.  
**Visuals:** SMA overlays, RSI plot, MACD chart.

---

### 3. Sentiment & Correlation Analysis
**Goal:** Correlate headline sentiment with stock returns.  
**Method:**  
- TextBlob polarity and VADER compound scores applied to headlines.  
- Daily sentiment aggregated per ticker.  
- Daily returns computed from closing prices.  
- Correlations (Pearson, Spearman, Kendall) calculated globally and per ticker.  

**Findings:**  
- Global correlation: weak positive (~0.16 Pearson).  
- NVDA shows strongest positive correlation (VADER Pearson 0.52, Spearman 0.80).  
- GOOG shows weak negative correlation.  
- AAPL & AMZN show extreme values due to anomalies.  
**Visuals:** Scatter plots (TextBlob & VADER vs returns), Pearson heatmap, per-ticker bar chart.

---

##  Results Summary
- Sentiment exhibits weak but notable alignment with daily returns.  
- VADER consistently outperforms TextBlob in predictive strength.  
- NVDA demonstrates the most promising sentiment-return relationship.  
- Correlation is noisy, consistent with financial market complexity.  

---

##  Limitations & Future Work
- Correlation ≠ causation; sentiment may align but not drive returns.  
- Data sparsity and publisher bias distort results.  
- Outliers inflate correlation values.  

**Future Improvements:**  
- Use **FinBERT** for domain-specific sentiment scoring.  
- Expand dataset to include intraday news and price movements.  
- Weight sentiment by publisher credibility.  

---

## Usage
Run the analysis notebooks:  
```bash
jupyter notebook
```
- Open `EDA.ipynb` for news insights.  
- Open `Technical_Analysis.ipynb` for stock indicators.  
- Open `Sentiment_Correlation.ipynb` for sentiment-return correlation.  

---


