import streamlit  as st
import pandas as pd
import plotly.express as px
import pdb

st.set_page_config(layout="wide")

df = pd.read_csv("precosCombustiveis.csv", sep=";",decimal=",")

df['Data da Coleta'] = pd.to_datetime(df['Data da Coleta'], format="%d/%m/%Y").dt.date

st.sidebar.title("Selecione o mês desejado")
df = df.sort_values('Data da Coleta')
df['Month'] = df['Data da Coleta'].apply(lambda x: str(x.year) + '-' + str(x.month))
month = st.sidebar.selectbox("Ano - Mês", df['Month'].unique())

df_filtered = df[df['Month'] == month]


st.title("Análise de Preços de Combustíveis")

imagem_path = "./kisspng-gasoline-petroleum-fuel-dispenser-filling-station-fuel-5ac010c23b9727.2370270715225366422441.png"
largura_desejada = 120  # Defina a largura desejada em pixels
st.image(imagem_path, use_column_width=False, width=largura_desejada)


col4, col5 = st.columns(2)
col6,col7,col8= st.columns(3)

fig_date = px.bar(df_filtered, x='Produto', y='Valor de Venda', color='Bandeira',title="Preço combustivel no mês",color_discrete_sequence=['blue', 'green', 'red','purple', 'orange', 'pink','black'])
col4.plotly_chart(fig_date,use_container_width=True)

nome_revendas = px.bar(df_filtered, color='Estado - Sigla', x='Bandeira',title="Revendas por região",color_discrete_sequence=['lightblue', 'green', 'red','purple', 'darkorange', 'pink','black','yellow','white','darkblue'])
col5.plotly_chart(nome_revendas,use_container_width=True)

media_combustivel = px.pie(df_filtered, values='Quantidade compra', names='Produto', title="Quantidade L por mês de todas revendedoras",color='Produto', color_discrete_sequence=['blue', 'green', 'red','purple', 'orange', 'pink','black'])
col6.plotly_chart(media_combustivel,use_container_width=True)

litros_revenda = px.bar(df_filtered, y='Quantidade compra', x='Bandeira', title="Quantidade L por bandeira no mês", color='Bandeira',color_discrete_sequence=['blue', 'green', 'red','purple', 'orange', 'pink','black'])
col7.plotly_chart(litros_revenda,use_container_width=True)

media_notas = df_filtered.groupby('Bandeira')['Nota atendimento'].mean().reset_index()
media_notas_revenda = px.bar(media_notas, y='Nota atendimento', x='Bandeira', title="Média avaliações dos clientes", color='Bandeira',color_discrete_sequence=['blue', 'yellow', 'purple','red', 'orange', 'pink','black'])
col8.plotly_chart(media_notas_revenda,use_container_width=True)

st.markdown(" \n")
st.markdown(" \n")

st.markdown("###### dados retirados do site: https://basedosdados.org/dataset/6ea3e28a-42be-401a-a066-ad87ca931e69 ")
st.markdown(" \n")

st.markdown("###### desenvolvido por: Caio Assis ")
