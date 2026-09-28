# Insurance Premium Category Predictor

An end-to-end ML app that predicts a customer's **insurance premium category** from their profile. A trained scikit-learn model is served through a **FastAPI** backend, packaged with **Docker**, deployed on **AWS EC2**, and used by a **Streamlit** frontend.

## Architecture

```
Streamlit UI  ──HTTP POST /predict──▶  FastAPI (Docker container on AWS EC2)  ──▶  ML model (model.pkl)
(frontend.py)                           (app.py)                                     (model/predict.py)
```

## Tech Stack

Python · scikit-learn · FastAPI · Pydantic · Streamlit · Docker · Docker Hub · AWS EC2

## Project Structure

```
├── app.py                        # FastAPI app and /predict endpoint
├── frontend.py                   # Streamlit UI
├── model/
│   ├── model.pkl                 # Trained model
│   └── predict.py                # Loads the model and returns the prediction
├── schema/
│   ├── user_input.py             # Request validation (Pydantic)
│   └── prediction_response.py    # Response schema
├── config/
│   └── city_tier.py              # City tier mapping
├── Dockerfile
├── requirements.txt
└── .dockerignore / .gitignore
```

## API

**`POST /predict`**

Request:

```json
{
  "age": 30,
  "weight": 65.0,
  "height": 1.7,
  "income_lpa": 10.0,
  "smoker": true,
  "city": "Mumbai",
  "occupation": "retired"
}
```

Response:

```json
{
  "response": {
    "predicted_category": "...",
    "confidence": 0.0,
    "class_probabilities": { "...": 0.0 }
  }
}
```

Occupation options: `retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job`.

Interactive docs are available at `/docs` (Swagger UI).

## Run Locally

```bash
git clone https://github.com/harshrathi0010-web/Insurance_Premium_Predictor.git
cd Insurance_Premium_Predictor

python -m venv myenv
myenv\Scripts\activate            # Windows
pip install -r requirements.txt

uvicorn app:app --reload          # API on http://localhost:8000
```

In a second terminal, start the frontend:

```bash
pip install streamlit requests
streamlit run frontend.py         # UI on http://localhost:8501
```

Make sure `API_URL` in `frontend.py` points to the API:

```python
API_URL = "http://localhost:8000/predict"
```

## Run with Docker

```bash
docker build -t insurance-premium-api .
docker run -p 8000:8000 insurance-premium-api
```

Or pull the published image:

```bash
docker pull harshrathi10/insurance-premium-api:latest
docker run -d -p 8000:8000 harshrathi10/insurance-premium-api:latest
```

## Deploy on AWS EC2

1. Launch an Ubuntu EC2 instance and install Docker.
2. In the security group, allow inbound **TCP 8000** (and SSH on port 22).
3. Pull and run the image:
   ```bash
   docker pull harshrathi10/insurance-premium-api:latest
   docker run -d -p 8000:8000 harshrathi10/insurance-premium-api:latest
   ```
4. Open `http://<EC2-public-IP>:8000/docs` to verify.
5. Set `API_URL = "http://<EC2-public-IP>:8000/predict"` in `frontend.py` and run the Streamlit app.

> The public IP changes when an instance is stopped and started. Attach an Elastic IP if you need a fixed address.

## Author

**Harsh Rathi** · [GitHub](https://github.com/harshrathi0010-web)
