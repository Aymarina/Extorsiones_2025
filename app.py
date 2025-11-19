import streamlit as st
import pandas as pd
import plotly.express as px
# Cargar el dataset desde la carpeta data
df = pd.read_csv("data/Extorsiones-2025.csv")

# Mostrar las primeras filas en la consola (opcional)
print(df.head())
