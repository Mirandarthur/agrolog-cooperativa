import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração da página executiva
st.set_page_config(page_title="AgroLog AI - Cooperativa", layout="wide")
st.title("🚜 AgroLog AI - Painel de Decisão Logística (Soja)")

# 2. Carregar a base sanitizada gerada
df = pd.read_csv("base_logistica_cooperativa_sanitizada.csv")

# 3. Métricas de Topo (KPIs)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Custo Médio R$/Ton", f"R$ {df['R$_Ton'].mean():.2f}")
col2.metric("Média Consumo Frota", f"{df['Media_km_l'].mean():.2f} km/L")
col3.metric("Total Viagens", len(df))
col4.metric("Tempo Médio Fila", f"{df['Tempo_Espera_Fila_h'].mean():.1f} h")

# 4. Gráficos Interativos
st.subheader("Custo por Tonelada por Rota e Tipo de Frota")
fig = px.bar(df, x="Rota", y="R$_Ton", color="Tipo_Frota", barmode="group")
st.plotly_chart(fig, use_container_width=True)

# 5. Módulo do Agente de IA (Simulado ou via API)
st.subheader("🤖 Recomendação do Agente de Alocação de Frota")
st.info(
    "**Análise Prescritiva da IA:** Identificamos que a Frota Própria na rota *Porto de Paranaguá* "
    "está enfrentando uma média de 12.4h de fila de tombador. **Ação recomendada:** Realoque 5 veículos "
    "próprios para a rota *Terminal Mairinque* e cubra o excedente do Porto via Frota Dedicada."
)