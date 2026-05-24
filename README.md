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

Automated pipeline defined in `.github/workflows/ci.yml`, triggered on every push to `main`.

### Pipeline Steps

| Step | Description | Status |
|------|-------------|--------|
| Set up job | Prepare runner environment | ✅ |
| Checkout Code | Pull latest source code | ✅ |
| Set up Python 3.9 | Install Python environment | ✅ |
| Install Dependencies | `pip install -r requirements.txt` | ✅ |
| Run Tests with pytest | Execute all 6 unit tests | ✅ |
| Deploy message | Trigger Render deployment | ✅ |

### Pipeline Result

![alt text](<images/Screenshot 2026-05-12 at 8.22.18 PM.png>)

**build-test-deploy** — succeeded in 17s ✅

---

## Local App Running

![alt text](<images/Screenshot 2026-05-12 at 8.12.09 PM.png>)
```
* Serving Flask app 'app'
* Running on http://127.0.0.1:5001
```

---

## Live App
![alt text](<images/Screenshot 2026-05-12 at 1.26.41 PM.png>)
![alt text](<images/Screenshot 2026-05-12 at 8.12.52 PM.png>)
The application is deployed on Render and accessible at:
**[https://02230288-dso101-a4.onrender.com](https://02230288-dso101-a4.onrender.com)**

---

## Dependencies

```
flask==3.0.3
pytest==8.2.2
gunicorn==22.0.0
```
---
## Challenges Faced

**Port Conflict on macOS**
The most immediate challenge was that Flask's default port 5000 was already occupied by macOS AirPlay Receiver. This prevented the app from starting. The issue was resolved by disabling AirPlay Receiver in System Settings and running the app on port 5001 instead.

**Dependency Conflicts During Installation**
When installing packages via `pip install -r requirements.txt`, several warnings appeared about conflicting versions — particularly with Spyder's pyqt5 requirement and the black formatter version. While these did not break the project, they required careful reading to confirm the core packages (Flask, pytest, gunicorn) installed correctly.

**Setting Up the GitHub Actions Workflow**
The `.github/workflows/ci.yml` file was not pushed automatically with the initial commit, causing the Actions tab to show the default "Get started" page instead of the pipeline. This was resolved by manually creating the workflow file directly through the GitHub web editor.

**Understanding the CI/CD Flow**
Connecting all the pieces — local development, GitHub version control, automated testing in Actions, and deployment on Render — required understanding how each tool interacts. Configuring the Render deploy hook as a GitHub secret to trigger automatic deployment was a new concept that took time to set up correctly.

---
## Conclusion

This assignment successfully demonstrated the implementation of a full CI/CD pipeline from development to deployment. A Flask API was built with three functional endpoints, six unit tests were written and verified using pytest with all passing, and a GitHub Actions workflow was configured to automatically run the pipeline on every push to the main branch. The application was deployed to Render with auto-deployment triggered via a webhook secret.

The project provided practical insight into how real-world software teams automate their development workflows. By integrating testing directly into the pipeline, bugs can be caught before they reach production, and deployment becomes a reliable, repeatable process rather than a manual task. Overall, the assignment reinforced the value of DevOps practices in building maintainable and reliable software systems.
