# tram-a-delay-detection
 Real-time delay detection for Bordeaux’s Tram A using Kafka, Flink SQL, PySpark &amp; Airflow
 Modern cities rely heavily on real-time transit updates. Bordeaux's public transport (TBM) already offers live information, but this project aims to build a lightweight, open-source version using free data and modern data engineering tools.
In this post, we'll explore how to build a real-time pipeline that detects tram delays at Peychotte stop on Tram A, and sends alert emails when a tram is more than 3 minutes late.
We'll use:
Apache Kafka for real-time data ingestion
Apache Flink SQL for delay detection
PySpark for schedule extraction
Airflow for orchestration
Open data from Bordeaux Métropole
