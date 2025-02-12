import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de renda",
     page_icon="https://cdn-icons-png.flaticon.com/512/3594/3594449.png",
     layout="centered",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv(r"C:\Users\vitor\Desktop\EBAC\atividades\M16\original (1)\projeto 2\input\previsao_de_renda.csv")

#plots
fig, ax = plt.subplots(8,1,figsize=(20,20))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Entendimento dos dados - Univariada')
plt.clf()
var = 'renda'
sns.displot(renda, x=var, bins = 20, height=4, aspect=2)
sns.despine()
#plt.xticks(rotation=45)
st.pyplot(plt)

plt.clf()
var = 'educacao'
sns.displot(renda, x=var, bins = 20, height=5, aspect=2)
plt.xticks(rotation=20)
sns.despine()
st.pyplot(plt)

plt.clf()
var = 'estado_civil'
sns.displot(renda, x=var, bins = 20, height=5, aspect=2)
#plt.xticks(rotation=90)
sns.despine()
st.pyplot(plt)

plt.clf()
var = 'tipo_renda'
sns.displot(renda, x=var, bins = 20, height=5, aspect=2)
#plt.xticks(rotation=90)
sns.despine()
st.pyplot(plt)

plt.clf()
var = 'idade'
sns.displot(renda, x=var, bins = 20, height=5, aspect=2)
#plt.xticks(rotation=90)
sns.despine()
st.pyplot(plt)

st.write('## Gráficos bivariada')

fig, ax = plt.subplots(1, 1, figsize=(10, 6)) 
sns.barplot(x='posse_de_imovel', y='renda', data=renda, ax=ax) 
#plt.xticks(rotation=90) 
sns.despine() 
st.pyplot(fig) 

fig, ax = plt.subplots(1, 1, figsize=(10, 6)) 
sns.barplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax) 
#plt.xticks(rotation=90) 
sns.despine() 
st.pyplot(fig) 

fig, ax = plt.subplots(1, 1, figsize=(10, 6)) 
sns.barplot(x='qtd_filhos', y='renda', data=renda, ax=ax) 
#plt.xticks(rotation=90) 
sns.despine() 
st.pyplot(fig) 

fig, ax = plt.subplots(1, 1, figsize=(10, 6)) 
sns.barplot(x='tipo_renda', y='renda', data=renda, ax=ax) 
#plt.xticks(rotation=90) 
sns.despine() 
st.pyplot(fig) 

fig, ax = plt.subplots(1, 1, figsize=(10, 6)) 
sns.barplot(x='educacao', y='renda', data=renda, ax=ax) 
plt.xticks(rotation=30) 
sns.despine() 
st.pyplot(fig) 

fig, ax = plt.subplots(1, 1, figsize=(10, 6)) 
sns.barplot(x='estado_civil', y='renda', data=renda, ax=ax) 
#plt.xticks(rotation=45) 
sns.despine() 
st.pyplot(fig) 

fig, ax = plt.subplots(1, 1, figsize=(10, 6)) 
sns.barplot(x='tipo_residencia', y='renda', data=renda, ax=ax) 
#plt.xticks(rotation=90) 
sns.despine()





