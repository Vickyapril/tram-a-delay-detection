import smtplib
import json
from kafka import KafkaConsumer
from email.mime.text import MIMEText
from email.message import EmailMessage

# Kafka setup
consumer = KafkaConsumer(
    'tram_alerts',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("📬 Watching tram_alerts topic for delays at Peychotte...")

for message in consumer:
    alert = message.value
    print(f"🚨 Delay detected: {alert}")

    # Compose email
    body = f"""
    🚨 Delay Alert at Peychotte 🚨

    Trip ID: {alert['trip_id']}
    Route: {alert['route_id']}
    Stop ID: {alert['stop_id']}
    Arrival Delay: {alert['arrival_delay']} seconds
    Arrival Time (epoch): {alert['arrival_time']}

    Please check the live status.
    """

    msg = MIMEText(body)
    msg['Subject'] = "🚨 TRAM A Delay Detected at Peychotte"
    msg['From'] = "bodysoda2017@gmail.com"
    msg['To'] = "vicky.april02@gmail.com"

    # Send email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("bodysoda2017@gmail.com", "jkja joyp amah abmn")  # Use App Password!
        server.send_message(msg)
        server.quit()
        print("✅ Email alert sent!")
    except Exception as e:
        print("❌ Failed to send email:", e)
