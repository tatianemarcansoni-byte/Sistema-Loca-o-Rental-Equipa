#Passo a passo site
#Titulo - Sistema de Locações
#Secão Cadastrar locações
    #Campo Data
    #Campo Vendedor - Tatiane, Josir, Isaque
    #Campo Equipamento - 
    #Campo Quantidade
    #Campo Período
    #Campo Valor
    #Botão cadastrar locação
        #Quando eu clicar no botão tem que adicionar a venda na tabela e atualizar no dashboard

#Seção Locações cadastradas
    #Tabela com as locações cadastradas

#Seção dashboard
    #Card/metrica - Faturamento total
    #Grafico barra/coluna - venda por vendedor
    #Grafico de pizza - Venda por produto
import streamlit as st
import pandas as pd
import plotly.express as px

#Carregar a base de locações
Tabela_locações = pd.read_excel("vendas rental.xlsx")
Tabela_locações["Data"]= pd.to_datetime(Tabela_locações["Data"], errors="coerce")
#Titulo
st.write("# Rental Equipa")

#Seção cadastrar locações

st.sidebar.write("## Cadastrar Locações")
Data = st.sidebar.date_input("Data", max_value="today")
Vendedor = st.sidebar.selectbox("Vendedor", ["Josir", "Isaque", "Tatiane"])
Equipamento = st.sidebar.selectbox("Equipamento", ["Andaimes", "Betoneiras", "Escoras", "Aspirador", "Lavadora Automática", "Bomba submercivel", "Martelete rompedor", "Rodizio de andaime", "Sapata para andaime", "Plataforma para andaime", "Alisadora de concreto", "Compactador de solo", "Cortador de piso", "Guincho", "Pedestal", "Pas e disco flotação", "Disco de corte cortag", "Cruzetas"])
Quantidade = st.sidebar.number_input("Quantidade", step=1)
Periodo = st.sidebar.selectbox("Período", ["Diária", "Semanal", "Quinzenal", "Mensal"])
Valor = st.sidebar.number_input("Valor")
botão_cadastrar = st.sidebar.button ("Cadastrar")
#Logica de cadastro do botão
if botão_cadastrar:
    Nova_Locação = [Data, Vendedor, Equipamento, Quantidade, Periodo, Valor]
    Ultima_linha = len(Tabela_locações)
    Tabela_locações.loc[Ultima_linha]= Nova_Locação
    Tabela_locações.to_excel("vendas rental.xlsx", index=False)
    st.success("Locação Cadastrada!")

#Seção Locações cadastradas
st.write("## Locações Cadastradas")
Tabela_locações['Data'] = Tabela_locações['Data'].dt.date
st.dataframe(
    Tabela_locações,
    column_config={
        "Valor": st.column_config.NumberColumn(
            "Valor",
            format="R$ %,.2f",
        )
    }
)
#Seção Dashboard
st.write("## Dashboard")
#Card/metrica - Faturamento total
Faturamento= Tabela_locações["Valor"].sum()
#st.metric("Faturamento Total", f"R$ {Faturamento}")
# Formata o número para o padrão brasileiro (R$ 8.200,00)
faturamento_br = f"R$ {Faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Exibe na métrica
st.metric("Faturamento Total", faturamento_br)

    #Grafico barra/coluna - venda por vendedor
        #primeiro cria o Grafico
        #depois exibe o grafico
grafico1 = px.bar(Tabela_locações, x="Vendedor", y="Valor", color="Equipamento")
st.plotly_chart(grafico1)
    #Grafico de pizza - Venda por produto
grafico2 = px.pie(Tabela_locações, names="Equipamento", values="Valor", hole=0.5)
st.plotly_chart(grafico2)