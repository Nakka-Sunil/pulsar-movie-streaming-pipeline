# 🎬 Movie Streaming Pipeline with Apache Pulsar

## 📌 Overview
This project implements a **real-time, event-driven movie streaming pipeline** using **Apache Pulsar**. Movie data is produced as events, consumed by multiple services, stored in a database, and processed for notifications. The system is designed with **fault tolerance**, **Dead Letter Queue (DLQ)** handling, and **decoupled consumers**, closely resembling real-world streaming architectures.

---

## 🏗️ Architecture

**Flow:**
```
Producer → Pulsar Topic → Consumers
                     ├── DB Consumer (Store movies)
                     ├── Email Notification Consumer
                     └── Dead Letter Queue (DLQ)
```

- Valid movie records are persisted into the database
- Failed records are routed to DLQ
- Successful events trigger email notifications

---

## 🚀 Key Features

- Real-time event streaming using **Apache Pulsar**
- Database persistence with primary key validation
- Dead Letter Queue (DLQ) for failed messages
- Email notification service
- Shared consumer subscriptions
- Explicit message acknowledgment & negative acknowledgment handling
- Graceful exception and shutdown handling

---

## 🛠️ Tech Stack

- **Apache Pulsar** – Messaging & streaming
- **Python** – Producer & consumer services
- **MySQL / SQL Database** – Movie data storage
- **JSON** – Message format
- **SMTP / Email Service** – Notifications
- **Docker (optional)** – Local Pulsar setup

---

## 📂 Project Structure

```
Movie_Streaming/
│
├── producer/
│   └── movie_producer.py
│
├── consumers/
│   ├── db_consumer.py
│   ├── email_consumer.py
│   └── dlq_consumer.py
│
├── mailing_service/
│   └── send_mail_serv.py
│
├── db_config/
│   └── db_connection.py
│
├── requirements.txt
└── README.md
```

---
### 3️⃣ Configure Database

Update `db_connection.py` with your database credentials:

```python
host = "localhost"
user = "root"
password = "password"
database = "movies"
```

---

### 4️⃣ Run Consumers

**Database Consumer**
```bash
python db_consumer.py
```

**Email Consumer**
```bash
python email_consumer.py
```

**DLQ Consumer**
```bash
python dlq_consumer.py
```

---

### 5️⃣ Run Producer
```bash
python movie_producer.py
```

---

## ❌ Failure Handling (DLQ Logic)

- Messages failing DB insertion (e.g., duplicate primary key)
- Messages explicitly `negative_acknowledged`
- Unhandled exceptions during processing

➡️ These messages are automatically routed to the **Dead Letter Queue**

---

## 📧 Email Notification Logic

- Email is triggered only after successful message consumption
- Uses a decoupled Pulsar consumer
- Ensures notifications are not sent for failed records

---

## 🧪 Test Scenarios

- Database connection failure → Message retried / DLQ
- KeyboardInterrupt → Graceful shutdown
- Consumer crash → Message re-delivery

---

## 📈 Learning Outcomes

- Apache Pulsar internals
- Message acknowledgment strategies
- DLQ design patterns
- Event-driven microservices
- Real-time data processing

---

## 🔮 Future Enhancements

- Retry topic before DLQ
- Schema Registry (Avro/JSON Schema)
- Monitoring with Pulsar Manager
- Streamlit dashboard for monitoring
- Partitioned topics for scalability

---

## 👤 Author

**Sunil Nakka**  
Software Engineer | Data & Streaming Enthusiast



