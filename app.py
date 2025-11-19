import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Extorsiones 2025", layout="wide")
st.title("📊 Análisis de Extorsiones en Colombia 2025")


COLORS = ["#780000", "#C1121F", "#FDF0D5", "#003049", "#669BBC"]


csv_path = r"C:\Users\angie\Desktop\Extorsiones_2025\data\Extorsiones-2025.csv"


if not os.path.exists(csv_path):
    st.error(f"Archivo CSV no encontrado en {csv_path}")
    st.stop()


df = pd.read_csv(csv_path)


for c in ["DEPARTAMENTO", "MUNICIPIO"]:
    if c in df.columns:
        df[c] = df[c].astype(str).str.title()


c1, c2 = st.columns(2)

with c1:
    st.subheader("Top 5 Departamentos")
    if "DEPARTAMENTO" in df.columns and "CANTIDAD" in df.columns:
        top5_dep = df.groupby("DEPARTAMENTO")["CANTIDAD"].sum().nlargest(5).reset_index()
        fig = px.pie(top5_dep, names="DEPARTAMENTO", values="CANTIDAD",
                     color="DEPARTAMENTO", color_discrete_sequence=COLORS, hole=0.3)
        fig.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Top 5 Municipios")
    if "MUNICIPIO" in df.columns and "CANTIDAD" in df.columns:
        top5_muni = df.groupby("MUNICIPIO")["CANTIDAD"].sum().nlargest(5).reset_index()
        fig = px.pie(top5_muni, names="MUNICIPIO", values="CANTIDAD",
                     color="MUNICIPIO", color_discrete_sequence=COLORS, hole=0.3)
        fig.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig, use_container_width=True)

st.header("Casos por departamento")
if "DEPARTAMENTO" in df.columns and "CANTIDAD" in df.columns:
    data_dep = df.groupby("DEPARTAMENTO")["CANTIDAD"].sum().reset_index().sort_values("CANTIDAD", ascending=False)
    fig = px.bar(data_dep, x="DEPARTAMENTO", y="CANTIDAD", text="CANTIDAD",
                 color="DEPARTAMENTO", color_discrete_sequence=COLORS)
    fig.update_layout(xaxis={"categoryorder": "total descending"}, showlegend=False)
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

st.header("30 municipios con mayor cantidad de casos")
if "MUNICIPIO" in df.columns and "CANTIDAD" in df.columns:
    top30 = df.groupby("MUNICIPIO")["CANTIDAD"].sum().nlargest(30).reset_index()
    fig = px.scatter(top30, x="MUNICIPIO", y="CANTIDAD", size="CANTIDAD",
                     color="CANTIDAD", color_continuous_scale=COLORS, size_max=60,
                     hover_name="MUNICIPIO")
    fig.update_traces(marker=dict(opacity=0.85, line=dict(width=1, color="#003049")))
    fig.update_layout(xaxis=dict(tickangle=-45, showgrid=False), yaxis_title="Cantidad de casos")
    st.plotly_chart(fig, use_container_width=True)
