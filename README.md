# CI/CD Pipeline with Testing & Deployment

## Aim

The aim of this assignment was to design and implement a complete CI/CD (Continuous Integration and Continuous Deployment) pipeline for a Flask web application. This involved building a functional backend API, writing automated unit tests using pytest, and configuring a GitHub Actions workflow to automatically build, test, and deploy the application to Render on every push to the main branch. The goal was to gain hands-on experience with modern DevOps practices and understand how automation reduces manual effort in software development and deployment.

---

## Overview
A Flask web application with a fully automated CI/CD pipeline built using GitHub Actions and deployed to Render. Every push to `main` automatically runs tests and triggers deployment.

---

## Project Structure

```
02230288_DSO101_A4/
│── app.py                        # Flask backend application
│── test_app.py                   # Unit tests (pytest)
│── requirements.txt              # Python dependencies
│── render.yaml                   # Render deployment configuration
│── .gitignore
│── README.md
│── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions CI/CD pipeline
```

---

## Application — API Endpoints

| Endpoint        | Method | Description                        |
|----------------|--------|------------------------------------|
| `/`            | GET    | Home — returns app status and info |
| `/health`      | GET    | Health check                       |
| `/add/<a>/<b>` | GET    | Returns the sum of a and b         |

**Sample response from `/`:**
```json
{"message": "CI/CD Pipeline App is Running!", "status": "success", "version": "1.0.0"}
```

---

## Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/Tobgaybolo/02230288_DSO101_A4.git
cd 02230288_DSO101_A4

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
# Visit http://127.0.0.1:5001/

# 4. Run tests
pytest test_app.py -v
```

---

## Unit Tests

Six tests written using **pytest** covering all endpoints and edge cases.

```python
def test_home():               # Basic assertion test (1+1==2)
def test_home_route():         # Home route returns HTTP 200
def test_home_route_json():    # Home route returns correct JSON
def test_health_route():       # Health endpoint returns "healthy"
def test_add_route():          # Add route returns correct sum
def test_add_zeros():          # Add route handles zeros correctly
```

### Test Output

![alt text](<images/Screenshot 2026-05-12 at 8.10.10 PM.png>)
```
platform darwin -- Python 3.11.5, pytest-8.2.2, pluggy-1.6.0
collected 6 items

test_app.py::test_home PASSED                  [ 16%]
test_app.py::test_home_route PASSED            [ 33%]
test_app.py::test_home_route_json PASSED       [ 50%]
test_app.py::test_health_route PASSED          [ 66%]
test_app.py::test_add_route PASSED             [ 83%]
test_app.py::test_add_zeros PASSED             [100%]

6 passed in 0.11s
```

---

## CI/CD Pipeline

The pipeline runs automatically on every push to `main`:

1. **Checkout** – pulls latest code
2. **Setup Python** – installs Python 3.9
3. **Cache** – speeds up future runs
4. **Install Dependencies** – `pip install -r requirements.txt`
5. **Run Tests** – `pytest test_app.py -v`
6. **Deploy to Render** – triggers auto-deploy via webhook

## Deployment (Render)

### Step-by-Step Setup

1. Go to [render.com](https://render.com) and sign up
2. Click **New → Web Service**
3. Connect your GitHub repo
4. Set these values:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Deploy**
6. Copy your **Deploy Hook URL** from Render dashboard
7. In GitHub → Settings → Secrets → Actions, add:
   - Name: `RENDER_DEPLOY_HOOK`
   - Value: (paste your Render deploy hook URL)

Now every push to `main` automatically tests and deploys your app!

## Test Output

```
test_app.py::test_home PASSED
test_app.py::test_home_route PASSED
test_app.py::test_home_route_json PASSED
test_app.py::test_health_route PASSED
test_app.py::test_add_route PASSED
test_app.py::test_add_zeros PASSED

6 passed in 0.42s
```

## Marking Criteria Checklist

- [x] Project structure (app.py, test_app.py, requirements.txt, ci.yml)
- [x] CI pipeline – build + test steps in GitHub Actions
- [x] Unit tests with pytest (6 tests)
- [x] Deployment automation via Render webhook
- [x] Documentation (this README)
