import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AgroLog AI - Cooperativa", layout="wide")

st.title("🚜 AgroLog AI - Painel de Decisão Logística (Soja)")
st.caption("Protótipo Executivo - Escoamento da Safra")

@st.cache_data
def load_data():
    return pd.read_csv("base_logistica_cooperativa_sanitizada.csv")

try:
    df = load_data()

    # Cards Executivos (KPIs)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Custo Médio R$/Ton", f"R$ {df['R$_Ton'].mean():.2f}")
    col2.metric("Média Consumo Frota", f"{df['Media_km_l'].mean():.2f} km/L")
    col3.metric("Total de Viagens", len(df))
    col4.metric("Tempo Médio Fila", f"{df['Tempo_Espera_Fila_h'].mean():.1f} h")

    st.divider()

    # Gráfico de Desempenho
    st.subheader("📊 Custo por Tonelada por Rota (Própria vs. Dedicada)")
    fig = px.bar(
        df,
        x="Rota",
        y="R$_Ton",
        color="Tipo_Frota",
        barmode="group",
        labels={"R$_Ton": "Custo R$/Ton", "Tipo_Frota": "Frota"}
    )
    st.plotly_chart(fig, use_container_width=True)

    # Bloco do Agente de IA
    st.subheader("🤖 Recomendação do Agente de Alocação de Frota")
    st.info(
        "**Análise Prescritiva da IA:** Identificamos que a **Frota Própria** na rota "
        "*Unidade Sudoeste -> Porto de Paranaguá* enfrenta média de **12.4h em fila de tombador**. "
        "\n\n**Ação recomendada:** Realoque 5 veículos próprios para a rota *Terminal Mairinque* "
        "e cubra o excedente de Paranaguá via Frota Dedicada (terceiros)."
    )

except Exception as e:
    st.error(f"Erro ao carregar a base de dados: {e}")
    st.warning("Certifique-se de que o arquivo 'base_logistica_cooperativa_sanitizada.csv' está salvo no mesmo repositório do GitHub.")
