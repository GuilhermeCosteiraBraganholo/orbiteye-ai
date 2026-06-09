from pathlib import Path
import sys
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from predict_risk import predict_risk
from generative_alert import gerar_alerta

st.set_page_config(page_title="OrbitEye", page_icon="🛰️", layout="wide")

st.markdown("""
<style>
    .main-title { font-size: 42px; font-weight: 800; margin-bottom: 0px; }
    .subtitle { font-size: 18px; color: #AAB2C0; margin-top: 0px; margin-bottom: 24px; }
    .risk-card { padding: 18px; border-radius: 12px; font-size: 22px; font-weight: 700; text-align: center; margin-top: 12px; }
    .risk-baixo { background-color: #0f5132; color: white; }
    .risk-medio { background-color: #664d03; color: white; }
    .risk-alto { background-color: #984c0c; color: white; }
    .risk-critico { background-color: #842029; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🛰️ OrbitEye</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Plataforma inteligente de monitoramento climático com Machine Learning, dados ambientais e indicadores orbitais.</div>',
    unsafe_allow_html=True
)

dataset_path = ROOT / "dataset" / "orbiteye_climate_data.csv"
df = pd.read_csv(dataset_path)

st.subheader("Visão geral do monitoramento")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Regiões monitoradas", df["regiao"].nunique())
col2.metric("Leituras processadas", len(df))
col3.metric("Alertas alto/crítico", len(df[df["risco"].isin(["ALTO", "CRITICO"])]))
col4.metric("Modelo IA", "Random Forest")

st.info(
    "O índice de vegetação representa uma leitura derivada de sensoriamento remoto, "
    "usada aqui como indicador orbital para complementar a análise climática."
)

risk_order = ["BAIXO", "MEDIO", "ALTO", "CRITICO"]
risk_counts = df["risco"].value_counts().reindex(risk_order).fillna(0).reset_index()
risk_counts.columns = ["risco", "quantidade"]

fig = px.bar(risk_counts, x="risco", y="quantidade", title="Distribuição dos níveis de risco no dataset", text="quantidade")
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Simular nova previsão")

col_a, col_b = st.columns(2)
with col_a:
    regiao = st.selectbox("Região monitorada", sorted(df["regiao"].unique()))
    chuva_mm = st.slider("Chuva acumulada (mm)", 0.0, 180.0, 150.0)
    umidade = st.slider("Umidade (%)", 0.0, 100.0, 95.0)
    temperatura = st.slider("Temperatura (°C)", 0.0, 45.0, 26.0)
with col_b:
    vento_kmh = st.slider("Velocidade do vento (km/h)", 0.0, 100.0, 70.0)
    nivel_rio_m = st.slider("Nível do rio (m)", 0.0, 8.0, 6.5)
    indice_vegetacao = st.slider("Índice de vegetação/satélite", 0.0, 1.0, 0.10)
    historico_ocorrencias = st.slider("Ocorrências históricas na região", 0, 15, 12)

dados = {
    "chuva_mm": chuva_mm,
    "umidade": umidade,
    "temperatura": temperatura,
    "vento_kmh": vento_kmh,
    "nivel_rio_m": nivel_rio_m,
    "indice_vegetacao": indice_vegetacao,
    "historico_ocorrencias": historico_ocorrencias,
}

if st.button("Analisar risco", type="primary"):
    resultado = predict_risk(dados)
    risco = resultado["risco"]
    confianca = resultado["confianca"]

    risk_class = {"BAIXO": "risk-baixo", "MEDIO": "risk-medio", "ALTO": "risk-alto", "CRITICO": "risk-critico"}.get(risco, "risk-medio")
    st.markdown(f'<div class="risk-card {risk_class}">Risco previsto: {risco} | Confiança: {confianca}%</div>', unsafe_allow_html=True)

    alerta = gerar_alerta(regiao, risco, confianca, dados)
    st.warning(alerta)

    c1, c2, c3 = st.columns(3)
    c1.metric("Chuva analisada", f"{chuva_mm} mm")
    c2.metric("Nível do rio", f"{nivel_rio_m} m")
    c3.metric("Histórico local", historico_ocorrencias)

    st.subheader("Dados enviados para análise")
    st.json(dados)

st.divider()
st.subheader("Amostra do dataset")
st.dataframe(df.head(25), use_container_width=True)
st.caption("OrbitEye AI | Global Solution FIAP | Análise preditiva de risco climático")
