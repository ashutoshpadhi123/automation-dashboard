# 🖥️ Automation Dashboard

A simple **Flask + SQLite + D3.js** dashboard for visualizing UI and API automation metrics.  
Data is imported from an Excel file (`AutomationData.xlsx`) containing **two sheets**:  
- **UI Automation**
- **API Automation**

## 📌 Features
- Pulls data from SQLite instead of a static CSV
- Displays interactive D3.js bar charts for UI & API metrics
- Shows total UI and API Automation counts separately

## UI Automation Data
- Product name and test suite types
- Manual, automated, and ready-for-automation counts
- Execution times and 2025 targets
- Automation coverage percentages

## API Automation Data
- Application names and test counts
- Current automation status
- 2025 targets and assigned developers
- Progress tracking (Complete/In Progress/Pending)

---

## 📂 Project Structure
automation-dashboard/
├── app.py # Flask server
├── import_excel_to_db.py # Imports Excel into SQLite
├── AutomationData.xlsx # Source data (2 sheets)
├── data.db # Generated SQLite DB
├── static/
│ └── index.html # Dashboard UI (D3.js charts)
├── requirements.txt # Python dependencies
├── Procfile # For Render deployment
└── README.md

---

## ⚙️ Local Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ashutoshpadhi123/automation-dashboard.git
cd automation-dashboard
```

### 2️⃣ Create Virtual Environment & Install Dependencies
On Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
On Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Import Excel into SQLite
```bash
python import_excel_to_db.py
```
This will generate data.db with two tables: ui_automation and api_automation


### 4️⃣ Run the Flask App
```bash
python app.py
```

### **Visit**: localhost:5000 to view the dashboard on your device.

### **Note** : To update the data, the data in the file AutomationData.xlsx needs to be changed. Do the following:
#### 1️⃣ Save the file
#### 2️⃣ Exit the venv by ctrl+C
#### 3️⃣ Repeat step 2, 3, and 4 from the local setup.
#### 4️⃣ **Visit**: localhost:5000 to view the dashboard with updated data.
