Here’s a professional and informative **README.md** for your [brazil-price-tracker](https://github.com/Pitsch92/brazil-price-tracker) project.  
You can copy and paste this into your repository’s README.md file:

---

# 🇧🇷 Brazil Price Tracker

**Brazil Price Tracker** is a data analysis and dashboard project for tracking and visualizing iPhone 16 prices across major Brazilian retailers.  
It includes web scraping, data cleaning, and interactive dashboards for price monitoring and market analysis.

---

## 🚀 Features

- **Automated scraping** of iPhone 16 prices from major Brazilian e-commerce sites (Magazine Luiza, Americanas, Ponto Frio, Quero Quero)
- **Data cleaning and unification** from multiple sources and dates
- **Exploratory data analysis** in Jupyter notebooks
- **Interactive dashboards** (Dash and Streamlit) for:
  - Most/least expensive models
  - Average price by model
  - Price trends over time
  - Model listing frequency
  - Top 5 most expensive models per day
  - Price spread by storage size

---

## 🗂️ Project Structure

```
.
├── clean_price.py              # Price cleaning utility
├── scraper_selenium.py         # Selenium web scraper
├── scraper_selenium_v2.py      # Improved Selenium scraper
├── data_unification.ipynb      # Notebook for merging data
├── data_analysis.ipynb         # Exploratory data analysis
├── dashboard.py                # Streamlit dashboard
├── dash_dashboard.py           # Dash dashboard
├── full_table_2025-05-26.csv   # Unified dataset
├── iphone_16_*.csv             # Raw scraped data (by date/source)
└── ...
```

---

## 📊 Example Analyses

- **Most/Least Expensive Models:** Instantly see the price extremes.
- **Average Price by Model:** Compare typical prices across variants.
- **Price Trend Over Time:** Track how prices change for any model.
- **Model Frequency:** See which models are most frequently listed.
- **Top 5 Expensive Models Per Day:** Spot daily price leaders.
- **Price Spread by Storage:** Analyze how storage size affects price.

---

## 🛠️ How to Run

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Pitsch92/brazil-price-tracker.git
   cd brazil-price-tracker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install: `pandas`, `plotly`, `dash`, `streamlit`, `selenium`, `beautifulsoup4`, `chromedriver_autoinstaller`)*

3. **Run the Dash dashboard:**
   ```bash
   python dash_dashboard.py
   ```
   Open [http://localhost:8050](http://localhost:8050) in your browser.

4. **Or run the Streamlit dashboard:**
   ```bash
   streamlit run dashboard.py
   ```
   Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📦 Data Sources

- [Magazine Luiza](https://www.magazineluiza.com.br/)
- [Americanas](https://www.americanas.com.br/)
- [Ponto Frio](https://www.pontofrio.com.br/)
- [Quero Quero](https://www.queroquero.com.br/)

---

## 📝 License

This project is for educational and research purposes.  
Please respect the terms of service of the sites you scrape.

---

## 🙋‍♂️ Contributing

Pull requests and suggestions are welcome!  
Feel free to open issues for bugs, ideas, or questions.

---

## 📧 Contact

Created by [Pitsch92](https://github.com/Pitsch92)

---

**Happy price tracking! 📱🇧🇷**

---

Let me know if you want to add badges, screenshots, or any other info!

[1] https://github.com/Pitsch92/brazil-price-tracker
