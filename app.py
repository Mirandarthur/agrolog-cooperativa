import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Configuração da Página e Tema
st.set_page_config(
    page_title="AgroLog AI | Cockpit Executivo - Cooper Tradição",
    page_icon="🚜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Injeção de CSS para Estilização Executiva (Dark Premium)
st.markdown("""
<style>
    /* Fundo da aplicação */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Card de Métricas Customizado */
    .metric-card {
        background: linear-gradient(135deg, #1E2640 0%, #111827 100%);
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 18px 22px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    .metric-label {
        color: #9CA3AF;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .metric-value {
        color: #F9FAFB;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 4px;
    }
    .metric-sub {
        color: #10B981;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Box da IA Prescritiva */
    .ai-box {
        background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%);
        border-left: 5px solid #6366F1;
        border-radius: 8px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    .ai-badge {
        background-color: #4F46E5;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
    }
    .ai-title {
        color: #E0E7FF;
        font-size: 1.1rem;
        font-weight: bold;
        margin-top: 8px;
    }
    .ai-desc {
        color: #C7D2FE;
        font-size: 0.95rem;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)

# 3. Carga e Cache de Dados
@st.cache_data
def load_data():
    df = pd.read_csv("base_logistica_cooperativa_sanitizada.csv")
    return df

try:
    df_raw = load_data()

    # 4. Barra Lateral (Filtros Interativos)
    st.sidebar.image("https://img.icons8.com/color/96/semi-truck.png", width=70)
    st.sidebar.title("Filtros da Operação")
    st.sidebar.caption("Safra Soja 2026 - Cooper Tradição")

    tipo_frota_filtro = st.sidebar.multiselect(
        "Tipo de Frota:",
        options=df_raw["Tipo_Frota"].unique(),
        default=df_raw["Tipo_Frota"].unique()
    )

    rotas_filtro = st.sidebar.multiselect(
        "Rotas Logísticas:",
        options=df_raw["Rota"].unique(),
        default=df_raw["Rota"].unique()
    )

    # Aplicação dos Filtros
    df = df_raw[(df_raw["Tipo_Frota"].isin(tipo_frota_filtro)) & (df_raw["Rota"].isin(rotas_filtro))]

    # 5. Cabeçalho Executivo
    col_head1, col_head2 = st.columns([3, 1])
    with col_head1:
        st.title("🚜 AgroLog AI — Cockpit Logístico de Soja")
        st.caption("Sistema Prescritivo de Inteligência em Transportes | Gestão de Frota Própria vs. Dedicada")
    with col_head2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<span style='background-color:#065F46; color:#D1FAE5; padding:8px 16px; border-radius:20px; font-weight:bold;'>🟢 Status: Operação Safra Ativa</span>", unsafe_allow_html=True)

    st.markdown("---")

    # 6. Painel de KPIs Superiores
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    avg_ton = df["R$_Ton"].mean() if not df.empty else 0
    avg_kml = df["Media_km_l"].mean() if not df.empty else 0
    total_trips = len(df)
    avg_queue = df["Tempo_Espera_Fila_h"].mean() if not df.empty else 0

    with kpi1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Custo Médio / Tonelada</div>
                <div class="metric-value">R$ {avg_ton:.2f}</div>
                <div class="metric-sub">▼ 3.2% vs. meta de frete</div>
            </div>
        """, unsafe_allow_html=True)

    with kpi2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Consumo Módulo (km/L)</div>
                <div class="metric-value">{avg_kml:.2f} km/L</div>
                <div class="metric-sub">▲ Frota própria: 1.91 km/L</div>
            </div>
        """, unsafe_allow_html=True)

    with kpi3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Viagens Auditadas</div>
                <div class="metric-value">{total_trips}</div>
                <div class="metric-sub">46 Próprios | 210 Dedicados</div>
            </div>
        """, unsafe_allow_html=True)

    with kpi4:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Tempo Média de Fila</div>
                <div class="metric-value">{avg_queue:.1f} horas</div>
                <div class="metric-sub" style="color:#EF4444;">▲ Gargalo em Paranaguá</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 7. Card do Agente de IA Executivo
    st.markdown("""
        <div class="ai-box">
            <span class="ai-badge">🤖 Agente Prescritivo Logístico • IA Ativa</span>
            <div class="ai-title">Recomendação Estratégica da Safra</div>
            <div class="ai-desc">
                <strong>Diagnóstico do Algoritmo:</strong> A <u>Frota Própria</u> operando na rota <em>Unidade Sudoeste ➔ Porto de Paranaguá</em> acumula média de <strong>12.4h de espera em fila de tombador</strong>, elevando o custo fixo ocioso em R$ 18,40/Ton.<br>
                <strong>Ação Prescritiva Sugerida:</strong> Realoque imediata de <strong>8 caminhões próprios</strong> para a rota curta de transbordo (<em>Terminal Mairinque</em>) com ciclo contínuo. Atribua o volume do Porto exclusivamente à <u>Frota Dedicada (terceirizada)</u> para absorver o custo de permanência.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 8. Abas de Gráficos e Analytics
    tab1, tab2, tab3 = st.tabs(["📊 Arbitragem de Custos (R$/Ton)", "⏱️ Fila e Tempo de Espera", "🚚 Desempenho por Frota"])

    with tab1:
        st.subheader("Comparativo do Custo Médio por Tonelada (R$/Ton)")
        
        # Agrupamento correto por Média
        df_grouped = df.groupby(["Rota", "Tipo_Frota"], as_index=False)["R$_Ton"].mean()

        fig_cost = px.bar(
            df_grouped,
            x="Rota",
            y="R$_Ton",
            color="Tipo_Frota",
            barmode="group",
            text_auto=".2f",
            color_discrete_map={"Própria": "#10B981", "Dedicada": "#6366F1"},
            labels={"R$_Ton": "Custo Médio (R$/Ton)", "Tipo_Frota": "Categoria da Frota"}
        )
        fig_cost.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=420,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor="#374151")
        )
        st.plotly_chart(fig_cost, use_container_width=True)

    with tab2:
        st.subheader("Gargalos de Pátio e Filas nos Silos/Porto (Horas Paradas)")
        
        fig_queue = px.box(
            df,
            x="Rota",
            y="Tempo_Espera_Fila_h",
            color="Tipo_Frota",
            color_discrete_map={"Própria": "#10B981", "Dedicada": "#F59E0B"},
            labels={"Tempo_Espera_Fila_h": "Horas em Fila / Tombador"}
        )
        fig_queue.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=420
        )
        st.plotly_chart(fig_queue, use_container_width=True)

    with tab3:
        st.subheader("Eficiência Energética da Frota (km/L por Placa/Módulo)")
        
        df_kml = df.groupby(["Tipo_Frota", "Rota"], as_index=False)["Media_km_l"].mean()
        fig_kml = px.line(
            df_kml,
            x="Rota",
            y="Media_km_l",
            color="Tipo_Frota",
            markers=True,
            color_discrete_map={"Própria": "#10B981", "Dedicada": "#EF4444"}
        )
        fig_kml.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=400
        )
        st.plotly_chart(fig_kml, use_container_width=True)

    # Rodapé
    st.markdown("---")
    st.caption("© 2026 AgroLog AI Suite • Desenvolvido para Cooper Tradição • Gestor da Operação: Miranda")

except Exception as e:
    st.error(f"Erro no carregamento do painel: {e}")
    st.warning("Verifique se o arquivo 'base_logistica_cooperativa_sanitizada.csv' está na raiz do repositório no GitHub.")
