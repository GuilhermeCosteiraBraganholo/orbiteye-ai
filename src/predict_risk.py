from pathlib import Path
from joblib import load
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "risk_model.pkl"
ENCODER_PATH = ROOT / "models" / "risk_encoder.pkl"

FEATURES = [
    "chuva_mm", "umidade", "temperatura", "vento_kmh",
    "nivel_rio_m", "indice_vegetacao", "historico_ocorrencias",
]

def predict_risk(data: dict) -> dict:
    model = load(MODEL_PATH)
    encoder = load(ENCODER_PATH)
    df = pd.DataFrame([data], columns=FEATURES)
    prediction = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]
    risk = encoder.inverse_transform([prediction])[0]
    confidence = float(max(probabilities))
    return {"risco": risk, "confianca": round(confidence * 100, 2)}
