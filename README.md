# LinkedIn Stealth Automation API

This project provides a FastAPI-based service for stealth automation on LinkedIn using `undetected-chromedriver` and `Selenium`. It supports session persistence and adapts to different UI variations on LinkedIn.

## 🚀 Features

- Stealth login to LinkedIn
- Persistent browser session across endpoints
- Connect to a LinkedIn profile
- Check connection status and send a message if connected
- Graceful session close

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/karishmasankar/linkedin-stealth-api
cd linkedin-stealth-api
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI app

```bash
uvicorn main:app --reload
```

Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API using Swagger UI.

---

## 📌 API Endpoints

### 1. `POST /login`

**Input:**

```json
{
  "username": "your_email",
  "password": "your_password"
}
```

Logs into LinkedIn with stealth browser and keeps session alive.

---

### 2. `POST /connect`

**Input:**

```json
{
  "profile_url": "https://www.linkedin.com/in/example"
}
```

Opens the given LinkedIn profile and sends a connection request.

---

### 3. `POST /check_connection` *(Optional if not implemented)*

**Input:**

```json
{
  "profile_url": "https://www.linkedin.com/in/example",
  "message": "Hi, great to connect!"
}
```

Checks if you're connected; if yes, sends a message.

---

### 4. `GET /close`

Closes the active browser session gracefully.

---

## 📦 Dependencies

* FastAPI
* Selenium
* undetected-chromedriver
* uvicorn

```


