# 📊 Sales Data Analysis

A Python-based command-line application designed to analyze sales data efficiently.
This project simulates a real-world data pipeline — from raw data ingestion to actionable business insights.

It is built with modular architecture, making it scalable, maintainable, and suitable for real-world use cases.

---

## 🚀 Features

* 📥 Load data from multiple CSV files
* 🔍 Explore dataset structure and quality
* 🧹 Clean and preprocess messy data
* 📈 Perform business analytics:

  * Total Revenue
  * Monthly Sales Trends
  * Top Products
  * Category-wise Performance
  * Region-wise Sales
  * Customer Analysis
* 🧮 Calculate Average Order Value (AOV)
* 🧪 Experiment with new logic in sandbox environment
* 📤 (Upcoming) Export analysis results

---

## 📂 Project Structure

```
sales-data-analysis/
├── .vscode/                 # VS Code settings (optional)
│
├── data/
│   ├── raw/                # Raw datasets (uncleaned)
│   │   ├── sales_1.csv
│   │   ├── sales_2.csv
│   │   ├── sales_3.csv
│   │   ├── sales_4.csv
│   │   └── sales_5.csv
│   │
│   └── processed/          # Cleaned datasets
│       └── clean_data_1.csv
│
├── experiments/            # Testing and experimental code
│   └── sandbox_logic.py
│
├── outputs/                # Final results (reports, exports)
│
├── src/                    # Core application code
│   ├── __pycache__/        # Auto-generated Python cache
│   ├── main.py             # Entry point (menu-driven system)
│   ├── load_data.py        # Data loading & validation
│   ├── analysis.py         # Data analysis & business logic
│   └── utility.py          # Helper functions
│
├── .gitignore              # Ignored files config
└── README.md               # Project documentation
```

---

## ⚙️ Requirements

* Python 3.x
* pandas

Install dependencies:

```bash
pip install pandas
```

---

## ▶️ How to Run

Run the application from the root directory:

```bash
python src/main.py
```

---

## 📌 Default Behavior

* If no file path is provided, the system loads:

```
data/raw/sales_1.csv
```

* Cleaned data is expected to be stored in:

```
data/processed/
```

---

## 🧠 Core Functional Flow

1. Load raw dataset
2. Inspect dataset structure
3. Clean and preprocess data
4. Perform analysis
5. Generate insights

---

## 📊 Available Analysis

* ✔ Total Sales
* ✔ Sales by Month
* ✔ Top Products
* ✔ Sales by Category
* ✔ Region-wise Sales
* ✔ Customer Analysis
* ✔ Average Order Value

---

## ⚠️ Current Limitations

* ❌ Export functionality not fully implemented (Menu Option 12)
* ❌ Best Sales Period analysis pending (Option 10)
* ❌ No visualization (charts/graphs) yet

---

## 🔮 Future Improvements

* 📊 Add data visualization using Matplotlib / Seaborn
* 📤 Export results to CSV/Excel
* 🖥️ Build GUI (Tkinter or Web App)
* 🤖 Integrate AI insights (optional advanced feature)

---

## 🧩 Design Principles

* **Modular Architecture** → Clear separation of concerns
* **Scalability** → Easy to extend with new features
* **Real-world Pipeline** → Raw → Processed → Output flow
* **Experimentation Friendly** → Dedicated sandbox environment

---

## 💡 Learning Outcomes

This project helps you understand:

* Data cleaning techniques
* Pandas-based analysis
* Structuring real-world Python projects
* Writing modular and maintainable code
* Translating business questions into data insights

---

## 🎯 Why This Project Matters

Businesses rely on sales data to make decisions.  
This project demonstrates how raw, unstructured data can be transformed into meaningful insights such as revenue trends, customer behavior, and product performance.

It reflects real-world data workflows used in analytics and data science roles.
