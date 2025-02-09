import streamlit as st
import pandas as pd
import plotly.express as px

df_car = pd.read_csv('vehicles.csv') # leitura do conjunto de dados de veículos

st.header('US Vehicle Data')

#Criando a caixa de seleção
opt1_hist = st.checkbox('Create a histogram')
opt2_scat = st.checkbox('Create a scatter chart')

if opt1_hist: # caso esta opção seja selecionada
    #informando ao usuário o tipo de gráfico e a informação que será apresentada
    st.write('The histogram presents a count of vehicles with similar mileage')

    #criação do gráfico histograma
    hist_chart = px.histogram(df_car, x='odometer')

    #apresentando o gráfico para o usuário
    st.plotly_chart(hist_chart, use_container_width=True)

if opt2_scat: # caso esta opção seja selecionada
    #informando ao usuário o tipo de gráfico e a informação que será apresentada
    st.write('The scatter chart presents the ratio between model year and mileage')

    #criação do gráfico de dispersão
    scat_chart = px.scatter(df_car, x='model_year', y='odometer')

    #apresentando o gráfico para o usuário
    st.plotly_chart(scat_chart)

