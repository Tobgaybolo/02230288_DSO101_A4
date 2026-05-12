# CI/CD Pipeline Project

A Flask web application with a fully automated CI/CD pipeline using GitHub Actions and Render.

## Project Structure

```
project/
│── app.py                        # Flask backend application
│── test_app.py                   # Unit tests (pytest)
│── requirements.txt              # Python dependencies
│── render.yaml                   # Render deployment config
│── .gitignore
│── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions CI/CD pipeline
```

## API Endpoints

| Endpoint        | Method | Description              |
|----------------|--------|--------------------------|
| `/`            | GET    | Home – app status & info |
| `/health`      | GET    | Health check             |
| `/add/<a>/<b>` | GET    | Returns sum of a and b   |

## Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Run tests
pytest test_app.py -v
```

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
- [x] Documentation (this README).
