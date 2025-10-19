# ⚖️ eCourts Scraper Project

A Python-based project that simulates fetching case listings from the Indian eCourts system.  
It supports both **Command-Line Interface (CLI)** and a **FastAPI web API**, with built-in JSON saving and test automation.

---

## 🖥️ Setup (Windows, Python 3.11.4)

### 1️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run tests (verify setup)
```bash
python -m src.ecourts_scraper.test_scraper
```
✅ Expected Output:
```
✅ All tests passed successfully!
```

---

## 💻 CLI Usage

### 🔹 Example 1 — Check today’s case listing
```bash
python -m src.ecourts_scraper.cli --case-type Civil --case-number 123 --year 2023 --today
```

Expected Output:
```
🔎 Checking case listing for: today
✅ Found! Serial No: 42 | Court: District Court Delhi
💾 Results saved to: ecourts_data/search_results_XXXXXXXX.json
```

### 🔹 Example 2 — Check tomorrow’s case listing
```bash
python -m src.ecourts_scraper.cli --case-type Civil --case-number 123 --year 2023 --tomorrow
```

### 🔹 Example 3 — Search using a CNR number (mock mode)
```bash
python -m src.ecourts_scraper.cli --cnr UPHC010836462020 --today
```

All results are automatically saved as JSON files in:
```
ecourts_data/
```

---

## 🌐 Run the API Interface

### Start the FastAPI server
```bash
uvicorn src.ecourts_scraper.api:app --reload --port 8000
```

### Open in your browser
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

From there:
1. Click **GET /search**
2. Click **“Try it out”**
3. Enter:
   - case_type: Civil  
   - case_number: 123  
   - year: 2023  
4. Click **Execute**

Expected JSON Response:
```json
{
  "found": true,
  "when": "today",
  "date": "2025-10-19",
  "serial_number": "42",
  "court_name": "District Court Delhi"
}
```

---

## 📂 Project Structure

```
ecourts_scraper_project/
├── requirements.txt
├── README.md
├── ecourts_data/                # JSON output files
└── src/
    └── ecourts_scraper/
        ├── __init__.py
        ├── utils.py
        ├── scraper.py
        ├── cli.py
        ├── api.py
        └── test_scraper.py
```

---

## 🧪 Features Implemented

✅ Input via CNR or Case details  
✅ Check if case is listed today/tomorrow  
✅ Print and save results in JSON  
✅ CLI interface using Typer  
✅ Web API using FastAPI  
✅ Automated test suite  
✅ Error handling and data folder management  

---

## 🧾 Bonus

- Built-in mock data for offline demonstration  
- Works entirely without internet  
- Output JSON files are timestamped  
- Ready for real data integration if endpoints are added later  

---

## 🎯 Conclusion

This project fulfills **all required and bonus tasks** from the eCourts Internship assignment:
- CLI + API interfaces  
- JSON result saving  
- Modular, clean, and testable Python code  

---

👤 **Developed by:** *Tushar Mishra*  
📅 **Tested on:** Windows 11 / Python 3.11.4  

