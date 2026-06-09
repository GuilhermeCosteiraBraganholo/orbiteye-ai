#  OrbitEye AI

## Global Solution 2026/1 – FIAP

### Integrantes

* Guilherme Costeira Braganholo
* Julio Cesar Dias Vilella
* Gabriel Nakamura Ogata



---

# VIDEO
https://youtu.be/fGpEC8Og0mU

#  Visão Geral

O OrbitEye AI é uma plataforma inteligente desenvolvida para apoiar o monitoramento climático e a prevenção de desastres naturais.

A solução utiliza conceitos de Inteligência Artificial, Machine Learning, análise de dados ambientais e indicadores derivados de sensoriamento remoto para identificar regiões com potencial risco de enchentes, alagamentos e eventos climáticos extremos.

O objetivo é transformar dados em informações úteis para auxiliar a população, órgãos públicos e equipes de resposta na tomada de decisão preventiva.

---

#  Problema

Eventos climáticos extremos têm se tornado cada vez mais frequentes em diversas regiões do Brasil.

Enchentes, deslizamentos, tempestades e alagamentos causam prejuízos econômicos, impactos ambientais e colocam vidas em risco.

Embora existam diversos dados disponíveis, muitas vezes essas informações não são processadas de forma rápida e acessível para apoiar ações preventivas.

---

#  Solução Proposta

O OrbitEye AI foi desenvolvido para realizar a análise de indicadores ambientais e classificar automaticamente o nível de risco climático de uma determinada região.

A plataforma recebe informações relacionadas a:

* Chuva acumulada
* Umidade do ar
* Temperatura
* Velocidade do vento
* Nível do rio
* Índice de vegetação
* Histórico de ocorrências

Com base nesses dados, um modelo de Machine Learning realiza a classificação do risco em quatro categorias:

* Baixo
* Médio
* Alto
* Crítico

Após a classificação, o sistema gera automaticamente um alerta em linguagem simples para facilitar a comunicação com a população.

---

#  Relação com a Economia Espacial

O OrbitEye está alinhado ao tema da Global Solution ao utilizar conceitos relacionados à observação da Terra por satélites.

Indicadores derivados de sensoriamento remoto podem ser utilizados para complementar análises ambientais e climáticas, permitindo uma visão mais ampla das condições de determinada região.

A proposta demonstra como tecnologias associadas ao setor espacial podem gerar benefícios diretos para a sociedade, contribuindo para a prevenção de desastres naturais.

---

#  Machine Learning

O sistema utiliza o algoritmo Random Forest para classificação de risco climático.

As etapas realizadas foram:

1. Coleta dos dados
2. Tratamento dos dados
3. Treinamento do modelo
4. Geração das previsões
5. Apresentação dos resultados

O modelo foi treinado utilizando um conjunto de dados contendo informações climáticas simuladas baseadas em cenários reais.

---

#  Dashboard

O dashboard foi desenvolvido utilizando Streamlit.

Funcionalidades disponíveis:

* Visualização de métricas
* Distribuição dos níveis de risco
* Simulação de cenários climáticos
* Classificação automática do risco
* Exibição da confiança da previsão
* Geração de alertas

---

#  Tecnologias Utilizadas

* Python
* Pandas
* Scikit-Learn
* Streamlit
* Plotly
* Joblib
* OpenAI API (Opcional)

---

#  Arquitetura da Solução

Dados Climáticos e Ambientais

↓

Tratamento dos Dados

↓

Modelo de Machine Learning

↓

Classificação do Risco

↓

Dashboard OrbitEye

↓

Geração de Alertas

↓

População e Defesa Civil

---

#  Benefícios

* Apoio à prevenção de desastres naturais
* Melhor interpretação de dados climáticos
* Comunicação simplificada para a população
* Apoio à tomada de decisão
* Aplicação prática de Inteligência Artificial

---

# ▶ Como Executar

Instalação das dependências:

```bash
py -3.12 -m pip install -r requirements.txt
```

Treinamento do modelo:

```bash
py -3.12 src\train_model.py
```

Execução do dashboard:

```bash
py -3.12 -m streamlit run src\app.py
```

---

# 📽️ Demonstração

Durante a demonstração da solução são apresentados:

* Treinamento do modelo
* Dashboard interativo
* Simulação de cenários climáticos
* Classificação automática do risco
* Geração de alertas

---

# 📚
O OrbitEye AI demonstra como Inteligência Artificial, análise de dados e conceitos relacionados à observação da Terra podem ser utilizados para apoiar ações preventivas e reduzir impactos causados por eventos climáticos extremos.

A solução evidencia a aplicação prática de tecnologias modernas para resolver problemas reais da sociedade.
