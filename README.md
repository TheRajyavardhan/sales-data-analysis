# Sales Data Analysis

A Python application for analyzing sales data with data loading, cleaning, and visualization features.

## Features

- Load data from CSV files
- View and explore dataset information
- Clean and preprocess data
- Calculate sales metrics (total, by month, by category, etc.)
- Analyze customer and product performance
- Export results

## Folder Structure

```
sales-data-analysis/
├── data/
│   ├── raw/          # Original CSV files
│   └── processed/    # Cleaned data
├── src/
│   ├── main.py       # Main menu and entry point
│   ├── load_data.py  # Data loading functions
│   └── analysis.py   # Data analysis functions
└── outputs/          # Analysis results
```

## Requirements

- Python 3.x
- pandas

## Usage

Run the main program:

```bash
python src/main.py
```

Follow the menu to load and analyze your sales data.

## Default Data Path

`data/raw/sales.csv`
