import os
from dotenv import load_dotenv

load_dotenv()

def gerar_alerta(regiao: str, risco: str, confianca: float, dados: dict) -> str:
    chuva = dados["chuva_mm"]
    nivel = dados["nivel_rio_m"]
    vento = dados["vento_kmh"]

    orientacoes = {
        "BAIXO": "A situação está controlada, mas o monitoramento deve continuar.",
        "MEDIO": "Evite áreas de alagamento e acompanhe os canais oficiais.",
        "ALTO": "Redobre a atenção, evite deslocamentos desnecessários e mantenha documentos em local seguro.",
        "CRITICO": "Procure uma área segura imediatamente e siga as orientações da Defesa Civil."
    }

    fallback = (
        f"Atenção: a região {regiao} apresenta risco {risco} de ocorrência climática. "
        f"O OrbitEye analisou {chuva} mm de chuva, nível do rio em {nivel} m e ventos de {vento} km/h. "
        f"{orientacoes.get(risco, 'Acompanhe os canais oficiais e mantenha atenção aos alertas.')}"
    )

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return fallback

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        prompt = f"""
        Crie um alerta curto, natural e objetivo para moradores.
        Região: {regiao}
        Risco: {risco}
        Confiança da previsão: {confianca}%
        Dados: chuva {chuva} mm, rio {nivel} m, vento {vento} km/h.
        Evite linguagem técnica. Use tom de Defesa Civil.
        """
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você escreve alertas públicos de Defesa Civil de forma clara, segura e objetiva."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.35,
            max_tokens=120,
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return fallback
