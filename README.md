# 🚀 Smart Delivery Router: Cloud-Integrated Logistics Engine

A sophisticated urban routing system that calculates optimal delivery paths using **Dijkstra’s Shortest Path Algorithm** and synchronizes real-time logistics data to **Google Cloud (Firebase)**.

## 🌟 Overview
This project simulates a professional logistics environment where a delivery vehicle must navigate a complex urban graph. By implementing a priority-queue-based pathfinding engine, the system calculates the most time-efficient route and persists all delivery logs to a regional Google Cloud database in Singapore (**asia-southeast1**).



## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Algorithm:** Dijkstra’s Algorithm (Optimized with `heapq` / Min-Heap)
* **Cloud Infrastructure:** Google Firebase Realtime Database
* **Security:** IAM Service Account Key Management (Environment Protection)
* **Version Control:** Git/GitHub

## 📊 Urban Map Architecture
The system operates on a weighted undirected graph consisting of **12 key urban nodes**:
* **Logistics Hubs:** Warehouse, Metro Station, Airport, Tech Park
* **Commercial Zones:** Shopping Mall, Luxury Hotel
* **Residential Areas:** Residential Zone 1, Customer Home
* **Transit Points:** Point A, Point B, Point C

## 🚀 Key Engineering Features
- **Dynamic Pathfinding:** Implemented Dijkstra's Algorithm with a Time Complexity of $O(E \log V)$ using a Min-Heap for efficient neighbor exploration.
- **Cloud-Native Integration:** Real-time data persistence using the Firebase Admin SDK to log delivery routes, timestamps, and total weights.
- **Regional Optimization:** Configured for the `asia-southeast1` (Singapore) region to ensure low latency and high availability for users in India.
- **Security-First Design:** Implemented professional `.gitignore` patterns to prevent the leakage of sensitive Google Cloud JSON credentials.

## ⚙️ Setup & Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Srushti-Navale/Smart-Delivery-Router.git](https://github.com/Srushti-Navale/Smart-Delivery-Router.git)
2. Install dependencies :
   pip install firebase-admin
   
3. Configure Google Cloud Access:  -Obtain a serviceAccountKey.json from the Firebase Console (Project Settings > Service   Accounts).  -Place the key in the root directory.  -Update the DATABASE_URL in main.py with your unique Firebase endpoint.

4. Future Roadmap:  -Integration with Google Maps API for real-world coordinate mapping.  -Implementation of a Traffic Simulator to dynamically change edge weights (road congestion).  -Front-end visualization using Streamlit to display the delivery boy's path on an interactive map.

