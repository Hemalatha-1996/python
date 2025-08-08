# Flight Price Data Preprocessing 🛫📊

## Overview  
This project focuses on preprocessing flight price data to prepare it for analysis and predictive modeling.  
The dataset includes flight details such as journey date, departure and arrival times, number of stops, route, and price.

---

## Data Preprocessing Steps  
- Extracted journey date, month, and year from the `Date_of_Journey` column  
- Split departure and arrival times into separate hour and minute columns  
- Cleaned and converted `Total_Stops` from categorical to numerical values  
- Handled missing values and inconsistent data entries  
- Dropped unnecessary columns like `Route` to reduce noise  

---

## Tech Stack  
- Python 3  
- Libraries: Pandas, NumPy, Seaborn, Matplotlib, Openpyxl  

---

## Usage  
1. Install dependencies:  
```bash
pip install pandas numpy seaborn matplotlib openpyxl
