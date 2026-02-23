# 🔗 URL Shortener

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg) ![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)

A lightweight and scalable **URL Shortener** service that converts long URLs into short, shareable links and redirects users to the original destination efficiently. Designed with performance and scalability in mind.

---

## 📑 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [API Endpoints](#-api-endpoints)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📌 Features

- 🔗 **Shorten URLs:** Convert long URLs into compact, unique codes.
- 🚀 **Fast Redirection:** High-performance redirection to the original destination.
- 📊 **Analytics:** Track click counts, referrers, and timestamps *(Optional)*.
- ⏳ **Expiration:** Set time-to-live (TTL) for temporary links *(Optional)*.
- 🐳 **Docker Support:** Containerized for easy deployment.

---

## 🏗️ Tech Stack

- **Backend:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Authentication:** JWT

---

## 📂 Project Structure

```text
url-shortener/
├── app/
│   ├── api/            # API route definitions
│   ├── core/           # Settings and security
│   ├── db/             # Sessions and configurations
│   ├── models/         # Database schemas (Postgresql models)
│   ├── schemas/        # object representation pydantic models
│   ├── services/       # Business logic (hashing, validation)
│   └── tasks/          # Async tasks
├── .env                # Environment variables
├── .env.template       # Environment variables template
├── requirements.txt    # Dependencies and scripts (or requirements.txt)
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites
- [Python](https://www.python.org/) (v3.9+)
- [PostgreSQL](https://www.postgresql.org/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vineet8800/url-shortener.git
   cd url-shortener
   ```

2. **Install dependencies**
   ```bash
   # For Python
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the root directory using `.env.template` and add required configuration 


4. **Run the application**
   ```bash
   # For Python
   uvicorn main:app --reload
   ```

The server should now be running on your configured port.

---

## 🔑 Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

```properties
DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/url_shortener
BASE_URL=http://localhost:8000
SECRET_KEY=19f2c7e3a4b8d6c3f0de5a1b9d2c7f3e3a6d3b0c1e9f3a2b4c6de33f1a3cb7d
REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/1
```

---

## 📡 API Endpoints

### 1. Shorten a URL
**POST** `/shorten`

**Body:**
```json
{
  "original_url": "https://www.very-long-website.com/content/article/123",
  "expires_at": "2026-02-23T06:07:12.047Z"
}
```

**Response:**
```json
{
  "urlCode": "my-article"
}
```

### 2. Redirect
**GET** `/:code`
- Redirects to the original `original_url`.

### 3. Get URL Stats for current user
**GET** `/urls`

**Response:**
```json
[{
  "short_code": "my-article",
  "long_url": "https://www.very-long-website.com/content/article/123",
  "clicks": 42,
  "expiration": "2023-10-27T10:00:00Z"
}]
```

---

## 🗺️ Roadmap

- [ ] Implement QR Code generation for links
- [ ] Create a frontend dashboard (React)
- [ ] Add unit tests

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License.