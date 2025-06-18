# Real-Time Tram Delay Detection in Bordeaux

Modern cities rely heavily on real-time transit updates. Bordeaux's public transport system (TBM) already offers live information, but this project aims to build a lightweight, open-source version using free data and modern data engineering tools.

## Project Overview

In this project, we'll explore how to build a real-time data pipeline that detects tram delays at the **Peychotte** stop on **Tram A**, and sends alert emails when a tram is more than **3 minutes late**.

## Technologies Used

- **Apache Kafka** – for real-time data ingestion  
- **Apache Flink SQL** – for delay detection  
- **PySpark** – for schedule extraction  
- **Apache Airflow** – for orchestration  
- **Open Data from Bordeaux Métropole** – as the data source

## Architecture

![Real-Time Pipeline Architecture](tram-a-delay-detection/screenshots
/Architecture.jpeg)

---
