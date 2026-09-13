import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Configuração da Página
st.set_page_config(
    page_title="AgroLog AI | Control Tower - Cooper Tradição",
    page_icon="🚜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilização CSS Enterprise Dark
st.markdown("""
<style>
    .stApp { background-color: #0B0F17; }
    
    .metric-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 18px 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }
    .metric-label { color: #94A3B8; font-size: 0.82rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
    .metric-value { color: #F8FAFC; font-size: 1.7rem; font-weight: 700; margin-top: 4px; }
    .metric-sub-green { color: #10B981; font-size: 0.8rem; font-weight: 600; }
    .metric-sub-red { color: #EF4444; font-size: 0.8rem; font-weight: 600; }
    
    .ai-agent-card {
        background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%);
        border: 1px solid #4338CA;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .agent-badge {
        background-color: #4F46E5; color: white; padding: 4px 12px;
        border-radius: 20px; font-size: 0.75rem; font-weight: bold; text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# 3. Carga e Cache de Dados
@st.cache_data
def load_data():
    return pd.read_csv("base_logistica_cooperativa_completa.csv")

try:
    df_raw = load_data()

    # 4. Sidebar - Filtros Multivariados
    st.sidebar.image("https://img.icons8.com/color/96/semi-truck.png", width=65)
    st.sidebar.title("Filtros Operacionais")
    st.sidebar.caption("Safra Soja 2026 • Cooper Tradição")

    tipo_frota = st.sidebar.multiselect(
        "Modalidade de Frota:",
        options=df_raw["Tipo_Frota"].unique(),
        default=df_raw["Tipo_Frota"].unique()
    )

    rotas_sel = st.sidebar.multiselect(
        "Corredores Logísticos:",
        options=df_raw["Rota"].unique(),
        default=df_raw["Rota"].unique()
    )

    status_sel = st.sidebar.multiselect(
        "Status da Entrega:",
        options=df_raw["Status_Entrega"].unique(),
        default=df_raw["Status_Entrega"].unique()
    )

    df = df_raw[
        (df_raw["Tipo_Frota"].isin(tipo_frota)) &
        (df_raw["Rota"].isin(rotas_sel)) &
        (df_raw["Status_Entrega"].isin(status_sel))
    ]

    # 5. Header Executivo
    col_h1, col_h2 = st.columns([3, 1])
    with col_h1:
        st.title("🚜 AgroLog AI — Control Tower & Torre de Decisão")
        st.caption("Plataforma Prescritiva de Inteligência em Transportes | Escoamento Agro")
    with col_h2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<span style='background-color:#065F46; color:#D1FAE5; padding:8px 16px; border-radius:20px; font-weight:bold;'>🟢 Operação Ativa: 256 Veículos</span>", unsafe_allow_html=True)

    st.markdown("---")

    # 6. Painel Financeiro e Operacional de Topo (KPIs)
    k1, k2, k3, k4, k5 = st.columns(5)
    
    rec_total = df["Receita_Faturada_R$"].sum() if not df.empty else 0
    custo_total = df["Custo_Total_Viagem_R$"].sum() if not df.empty else 0
    margem_total = df["Margem_Lucro_R$"].sum() if not df.empty else 0
    pct_margem = (margem_total / rec_total * 100) if rec_total > 0 else 0
    vol_total = df["Carga_Toneladas"].sum() if not df.empty else 0
    media_fila_porto = df["Fila_Porto_Tombador_h"].mean() if not df.empty else 0

    with k1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Faturamento Bruto</div>
                <div class="metric-value">R$ {rec_total/1e6:.2f}M</div>
                <div class="metric-sub-green">▲ Volume: {vol_total:,.0f} t</div>
            </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Custo Operacional</div>
                <div class="metric-value">R$ {custo_total/1e6:.2f}M</div>
                <div class="metric-sub-red">Diesel + Pedágio + Manut.</div>
            </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Margem Líquida</div>
                <div class="metric-value">R$ {margem_total/1e6:.2f}M</div>
                <div class="metric-sub-green">Margem: {pct_margem:.1f}%</div>
            </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Média Fila Porto</div>
                <div class="metric-value">{media_fila_porto:.1f}h</div>
                <div class="metric-sub-red">Gargalo em Paranaguá</div>
            </div>
        """, unsafe_allow_html=True)

    with k5:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Score Telemetria</div>
                <div class="metric-value">{df['Score_Telemetria'].mean():.0f}/100</div>
                <div class="metric-sub-green">Segurança & Condução</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 7. Central de Agentes Especialistas em IA
    st.markdown("### 🤖 Central Prescritiva dos Agentes Virtuais")
    
    tab_agent1, tab_agent2, tab_agent3 = st.tabs([
        "🎯 Agente Alocador de Frota",
        "💸 Agente de Arbitragem Financeira",
        "🌱 Agente de Eficiência & ESG"
    ])

    with tab_agent1:
        st.markdown("""
            <div class="ai-agent-card">
                <span class="agent-badge">Agente 1 • Otimizador de Ativos</span>
                <h4 style="color:#E0E7FF; margin-top:10px;">Recomendação: Deslocamento de Frota Própria</h4>
                <p style="color:#C7D2FE;">
                    A <strong>Frota Própria (46 veículos)</strong> está acumulando uma média de <strong>14.2h em fila de tombador no Porto de Paranaguá</strong>, onde o custo fixo de espera corrói a margem. 
                    <br><strong>Decisão Sugerida:</strong> Migre 12 veículos próprios para o corredor <em>Silo Pato Branco ➔ Indústria Esmagadora (PR)</em> (ciclo rápido de 140km) e cubra o excedente do Porto via <strong>Frota Dedicada (210 terceiros)</strong>, reduzindo o custo total por tonelada em <strong>R$ 11,30/t</strong>.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with tab_agent2:
        st.markdown("""
            <div class="ai-agent-card">
                <span class="agent-badge">Agente 2 • Monitor de Frete e Margem</span>
                <h4 style="color:#E0E7FF; margin-top:10px;">Oportunidade: Rota Arco Norte via Itaqui</h4>
                <p style="color:#C7D2FE;">
                    O custo logístico total via <strong>Porto de Itaqui (MA)</strong> apresenta uma margem líquida de <strong>38,4%</strong> contra apenas <strong>26,1%</strong> no escoamento via Paranaguá, devido ao menor impacto de pedágios por tonelada. 
                    <br><strong>Decisão Sugerida:</strong> Direcionar 15% do volume de grãos do Noroeste para o Arco Norte durante a janela das próximas duas semanas.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with tab_agent3:
        st.markdown("""
            <div class="ai-agent-card">
                <span class="agent-badge">Agente 3 • Telemetria e Descarbonização</span>
                <h4 style="color:#E0E7FF; margin-top:10px;">Alerta: Desperdício em Marcha Lenta</h4>
                <p style="color:#C7D2FE;">
                    Identificados 18 motoristas com score de telemetria abaixo de 70 pontos e consumo médio de <strong>1,62 km/L</strong>. O tempo excessivo de motor ligado nos pátios gerou um consumo desnecessário de <strong>4.200 Litros de Diesel</strong> este mês.
                    <br><strong>Decisão Sugerida:</strong> Aplicar o protocolo de desligamento automático nos pátios para reduzir 11,2 toneladas de emissões de CO₂.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # 8. Visões Analíticas Profundas
    v_tab1, v_tab2, v_tab3, v_tab4 = st.tabs([
        "💰 DRE Financeiro por Corredor",
        "⏱️ Gargalos de Tempo & Filas",
        "🚚 Análise de Frota & Motoristas",
        "📄 Relatório de Dados Brutos"
    ])

    with v_tab1:
        st.subheader("Análise de Receita, Custo e Margem por Rota")
        df_fin = df.groupby("Rota", as_index=False)[["Receita_Faturada_R$", "Custo_Total_Viagem_R$", "Margem_Lucro_R$"]].sum()
        
        fig_fin = go.Figure()
        fig_fin.add_trace(go.Bar(x=df_fin["Rota"], y=df_fin["Receita_Faturada_R$"], name="Receita Bruta", marker_color="#3B82F6"))
        fig_fin.add_trace(go.Bar(x=df_fin["Rota"], y=df_fin["Custo_Total_Viagem_R$"], name="Custo Operacional", marker_color="#EF4444"))
        fig_fin.add_trace(go.Bar(x=df_fin["Rota"], y=df_fin["Margem_Lucro_R$"], name="Margem Líquida", marker_color="#10B981"))
        
        fig_fin.update_layout(
            barmode="group", template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            height=400, xaxis=dict(showgrid=False)
        )
        st.plotly_chart(fig_fin, use_container_width=True)

    with v_tab2:
        st.subheader("Composição do Tempo Total de Ciclo (Horas Rodando vs. Filas)")
        df_tempo = df.groupby("Rota", as_index=False)[["Tempo_Rodando_h", "Fila_Silo_h", "Fila_Porto_Tombador_h"]].mean()
        
        fig_time = px.bar(
            df_tempo, x="Rota", y=["Tempo_Rodando_h", "Fila_Silo_h", "Fila_Porto_Tombador_h"],
            title="Distribuição do Tempo de Viagem (Horas)",
            labels={"value": "Horas", "variable": "Etapa do Ciclo"},
            color_discrete_sequence=["#10B981", "#F59E0B", "#EF4444"]
        )
        fig_time.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=400)
        st.plotly_chart(fig_time, use_container_width=True)

    with v_tab3:
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.subheader("Média de Consumo (km/L) por Tipo de Frota")
            fig_kml = px.box(df, x="Tipo_Frota", y="Media_Consumo_km_l", color="Tipo_Frota", color_discrete_map={"Própria": "#10B981", "Dedicada": "#6366F1"})
            fig_kml.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=350)
            st.plotly_chart(fig_kml, use_container_width=True)
            
        with col_f2:
            st.subheader("Distribuição do Status das Entregas")
            fig_status = px.pie(df, names="Status_Entrega", hole=0.4, color_discrete_sequence=px.colors.qualitative.Set2)
            fig_status.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=350)
            st.plotly_chart(fig_status, use_container_width=True)

    with v_tab4:
        st.subheader("Explorador de Dados Operacionais e Rastreabilidade")
        st.dataframe(
            df[[
                "ID_Viagem", "Data", "Tipo_Frota", "Placa_Veiculo", "Motorista", "Rota", 
                "Carga_Toneladas", "Receita_Faturada_R$", "Custo_Total_Viagem_R$", 
                "Margem_Lucro_R$", "Tempo_Total_Ciclo_h", "Score_Telemetria", "Status_Entrega"
            ]],
            use_container_width=True,
            height=400
        )

    # Rodapé Executivo
    st.markdown("---")
    st.caption("© 2026 AgroLog AI Control Tower • Preparado para Cooper Tradição • Responsável Técnico: Miranda")

except Exception as e:
    st.error(f"Erro no carregamento do painel executivo: {e}")
    st.warning("Verifique se o arquivo 'base_logistica_cooperativa_completa.csv' foi adicionado ao GitHub.")
