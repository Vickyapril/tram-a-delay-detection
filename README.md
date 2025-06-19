# 🚦 Real-Time Delay Detection for Bordeaux's Tram A using Kafka, Flink & Airflow

This project is a real-time data pipeline that detects delays on Bordeaux's TRAM A at the Peychotte stop. The system leverages open GTFS-RT data and uses technologies such as Kafka, PySpark, Apache Flink, and Apache Airflow to stream, process, and alert based on tram delays.

## 📌 Motivation

While existing applications like TBM provide tram tracking, this project showcases how you can independently build a real-time alerting system using open data and modern streaming tools—ideal for learning or demonstrating data engineering skills.

---

## ⚙️ Architecture Overview
![Architecture](https://github.com/Vickyapril/tram-a-delay-detection/blob/main/screenshots/Architecture%20(1).png)

## 🔧 Technologies Used

- 🟧 Apache Kafka — Real-time messaging
- 💡 Apache Flink SQL — Real-time stream processing
- 🧠 PySpark — Static GTFS data analysis (for stop ID lookup)
- 📩 Email Alerts — Send alerts when delays > 3 minutes
- ⏱ Apache Airflow — Pipeline orchestration

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/vickyapril/tram-a-delay-detection.git
```


### 2. Install Requirements
```bash
pip install -r requirements.txt
```


### 3. Start Kafka & Flink
Ensure Zookeeper, Kafka, and Flink are running.

### 4. Run Airflow
```bash
airflow standalone
```
Trigger the DAG real_time_tram_a_delay from the UI.


### 📬 Sample Email Alert
![Email-Alert](https://github.com/Vickyapril/tram-a-delay-detection/blob/main/screenshots/email-alert.png)

### 🧪 Testing Locally
You can simulate delays manually by modifying the transformer output or waiting until the early morning schedules (e.g., 5:30 AM) to test real GTFS-RT delays.


### 📚 Medium Article

You can read the detailed walk-through here:  
👉 [Real-Time Delay Detection for Bordeaux's Tram A using Kafka, Flink & Airflow](https://medium.com/@vickyapril/real-time-delay-detection-for-bordeauxs-tram-a-using-kafka-flink-airflow-33018d625c08)


