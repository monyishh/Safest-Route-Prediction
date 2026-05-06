# 🛣️ Safest Route Prediction System

A full‑stack geospatial application that predicts the **safest travel route** between two locations using **real road networks** and **crime‑aware risk analysis**, instead of relying only on the shortest path.

This project integrates **OpenStreetMap routing (OSRM)**, **machine‑learning–based hotspot detection**, and an **interactive map visualization** to recommend safer travel routes.

---

## ✨ Features

* 🔍 **Crime Hotspot Detection** using DBSCAN clustering
* 🛣️ **Real‑world routing** via OpenStreetMap + OSRM
* ⏱️ **Time‑based risk scoring** (higher risk at night)
* ⚖️ **Multi‑route safety comparison**
* 🌍 **Interactive map visualization** with Leaflet.js
* ⚡ **FastAPI backend** with Swagger documentation

---

## 🧠 System Overview

**Input**:

* Source location (latitude, longitude)
* Destination location (latitude, longitude)
* Time of travel (hour)

**Output**:

* Safety score for each available route
* Safest route recommendation
* Visualized route on an interactive map

---

## 🏗️ Architecture

```
Frontend (Leaflet Map)
        ↓
FastAPI Backend
        ↓
OSRM (Real Road Routes)
        ↓
Crime Hotspot Analysis (DBSCAN)
        ↓
Route Safety Scoring
```

---

## 🧰 Tech Stack

### Backend

* Python
* FastAPI
* scikit‑learn
* Pandas, NumPy
* OSRM (OpenStreetMap Routing)

### Frontend

* HTML
* JavaScript
* Leaflet.js
* OpenStreetMap Tiles

---

## 📁 Project Structure

```
Safe_Route/
├── backend/
│   ├── main.py            # FastAPI entry point
│   ├── osrm.py            # Real route generation
│   ├── clustering.py      # Crime hotspot detection
│   ├── safety_score.py    # Route safety scoring logic
│   └── requirements.txt
│
├── frontend/
│   └── index.html         # Leaflet map UI
│
├── data/
│   └── crimes.csv         # Crime dataset
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <repo-url>
cd Safe_Route
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### 4️⃣ Run Backend + Frontend Together

```bash
cd backend
python -m uvicorn main:app --reload
```

Open the app in your browser at:

```
http://127.0.0.1:8000
```

The backend now serves the frontend automatically, so you do not need to open `frontend/index.html` separately.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Usage

### Endpoint

```
POST /predict-safe-route
```

### Request Body

```json
{
  "source": { "lat": 17.3850, "lng": 78.4867 },
  "destination": { "lat": 17.3900, "lng": 78.4900 },
  "hour": 22
}
```

### Response (Example)

```json
{
  "scores": {
    "route_1": 1.5
  },
  "safest_route": "route_1",
  "routes": {
    "route_1": [[17.3848,78.4866],[17.3898,78.4899]]
  }
}
```

---

## 🗺️ Frontend Visualization

* Open `frontend/index.html` in a browser
* Safest route is highlighted in **green**
* Alternate routes (if available) appear in red
* Click routes to view safety scores

---

## 📌 Key Learnings

* Real‑world route generation using OSRM
* Geospatial clustering with DBSCAN
* Backend–frontend integration
* Practical use of machine learning for decision support


---

## 🚀 Future Enhancements (Optional)

* Crime heatmap overlay
* ML classification (Safe / Moderate / Unsafe)
* Shortest vs Safest route toggle
* Deployment on cloud

---

## 👤 Author

**Manish Kumar**

---

⭐ If you find this project useful, feel free to star the repository!
