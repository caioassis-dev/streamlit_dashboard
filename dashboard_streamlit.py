import streamlit  as st
import pandas as pd
import plotly.express as px
import pdb

st.set_page_config(layout="wide")

st.title("Análise de Preços de Combustíveis")

df = pd.read_csv("precosCombustiveis.csv", sep=";",decimal=",")

df['Data da Coleta'] = pd.to_datetime(df['Data da Coleta'], format="%d/%m/%Y").dt.date

st.sidebar.title("Selecione o mês desejado")
df = df.sort_values('Data da Coleta')
df['Month'] = df['Data da Coleta'].apply(lambda x: str(x.year) + '-' + str(x.month))
month = st.sidebar.selectbox("Ano - Mês", df['Month'].unique())

df_filtered = df[df['Month'] == month]

col1, col2 = st.columns(2)
col3,col4,col5= st.columns(3)


fig_date = px.bar(df_filtered, x='Produto', y='Valor de Venda', color='Bandeira',title="Preço combustivel mês",color_discrete_sequence=['blue', 'green', 'red','purple', 'orange', 'pink','black'])
col1.plotly_chart(fig_date,use_container_width=True)

nome_revendas = px.bar(df_filtered, color='Estado - Sigla', x='Bandeira',title="Revendas por região",color_discrete_sequence=['lightblue', 'green', 'red','purple', 'darkorange', 'pink','black','yellow','white','darkblue'])
col2.plotly_chart(nome_revendas,use_container_width=True)

media_combustivel = px.pie(df_filtered, values='Quantidade compra', names='Produto', title="Quantidade L por mes todas revendedoras",color='Produto', color_discrete_sequence=['blue', 'green', 'red','purple', 'orange', 'pink','black'])
col3.plotly_chart(media_combustivel,use_container_width=True)

litros_revenda = px.bar(df_filtered, y='Quantidade compra', x='Bandeira', title="Quantidade L por bandeira", color='Bandeira',color_discrete_sequence=['blue', 'green', 'red','purple', 'orange', 'pink','black'])
col4.plotly_chart(litros_revenda,use_container_width=True)

media_notas = df_filtered.groupby('Bandeira')['Nota atendimento'].mean().reset_index()
media_notas_revenda = px.bar(media_notas, y='Nota atendimento', x='Bandeira', title="Média de notas de avaliação avaliação", color='Bandeira',color_discrete_sequence=['blue', 'yellow', 'purple','red', 'orange', 'pink','black'])
col5.plotly_chart(media_notas_revenda,use_container_width=True)

st.markdown(" \n")

st.markdown("###### desenvolvido por: Caio Assis ")
