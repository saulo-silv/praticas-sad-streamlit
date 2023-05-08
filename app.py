import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fonte de Dados
# https://www.kaggle.com/datasets/whenamancodes/student-performance

st.set_page_config(page_title="Dashboard - Student Dataset", page_icon=":books:")

st.sidebar.title("Configurações de Exibição")

st.title("Análise de Dados do Dataset de Estudantes")

st.sidebar.subheader("Selecione o que deseja exibir")
show_dataset = st.sidebar.checkbox("Dados do Dataset")
show_dataset_description = st.sidebar.checkbox("Descrição do Dataset")

graph1_type = st.sidebar.selectbox("Gráfico 1: Selecione o tipo de gráfico", ("Barra", "Pizza", "Dispersão", "Histograma", "Boxplot"))

media = sum(dados) / len(dados)

st.line_chart(pd.Series(dados).rolling(window=3).mean())
st.write(f"Média: {media}")

