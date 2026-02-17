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
- 🎨 **Custom Aliases:** Allow users to define custom short codes (e.g., `mysite.com/sale`) *(Optional)*.
- ⏳ **Expiration:** Set time-to-live (TTL) for temporary links *(Optional)*.
- 🛡️ **Rate Limiting:** Prevent abuse of the API.
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
│   ├── config/         # Database and environment configuration
│   ├── controllers/    # Request handlers (logic for endpoints)
│   ├── models/         # Database schemas (Mongoose/SQL models)
│   ├── routes/         # API route definitions
│   ├── services/       # Business logic (hashing, validation)
│   └── utils/          # Helper functions (error handling, validation)
├── tests/              # Unit and integration tests
├── .env                # Environment variables
├── package.json        # Dependencies and scripts (or requirements.txt)
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
   git clone [https://github.com/yourusername/url-shortener.git](https://github.com/yourusername/url-shortener.git)
   cd url-shortener
   ```

2. **Install dependencies**
   ```bash
   # For Node.js
   npm install

   # For Python
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the root directory using `.env.template`

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
PORT=5000
DATABASE_URL=mongodb://localhost:27017/urlshortener
BASE_URL=http://localhost:5000
REDIS_URL=redis://localhost:6379  # Optional
JWT_SECRET=your_super_secret_key # Optional (if using Auth)
```

---

## 📡 API Endpoints

### 1. Shorten a URL
**POST** `/api/url/shorten`

**Body:**
```json
{
  "longUrl": "[https://www.very-long-website.com/content/article/123](https://www.very-long-website.com/content/article/123)",
  "customCode": "my-article"
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
- Redirects to the original `longUrl`.

### 3. Get URL Stats (Optional)
**GET** `/api/url/stats/:code`

**Response:**
```json
{
  "urlCode": "my-article",
  "clicks": 42,
  "lastClicked": "2023-10-27T10:00:00Z"
}
```

---

## 🗺️ Roadmap

- [ ] Add User Authentication (OAuth/JWT)
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

Distributed under the MIT License. See `LICENSE` for more information.