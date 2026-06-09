import pandas as pd
from pathlib import Path
from joblib import dump
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "dataset" / "orbiteye_climate_data.csv"
MODEL_PATH = ROOT / "models" / "risk_model.pkl"
ENCODER_PATH = ROOT / "models" / "risk_encoder.pkl"

FEATURES = [
    "chuva_mm", "umidade", "temperatura", "vento_kmh",
    "nivel_rio_m", "indice_vegetacao", "historico_ocorrencias",
]

def main():
    df = pd.read_csv(DATASET)
    x = df[FEATURES]

    encoder = LabelEncoder()
    y = encoder.fit_transform(df["risco"])

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=220,
        max_depth=9,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Acuracia do modelo: {accuracy:.2%}")
    print(classification_report(y_test, predictions, target_names=encoder.classes_))

    dump(model, MODEL_PATH)
    dump(encoder, ENCODER_PATH)

    print(f"Modelo salvo em: {MODEL_PATH}")
    print(f"Encoder salvo em: {ENCODER_PATH}")

if __name__ == "__main__":
    main()
