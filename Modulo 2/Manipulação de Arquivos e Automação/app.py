from datetime import datetime

import  streamlit as st

st.sidebar.title("locadora de carros")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/743/743922.png")
carro = st.selectbox("Selecione o carro que deseja alugar", ["gol", "uno", "hb20", "onix"])
st.sidebar.image(f"{carro}.png", width=900)

dias = st.slider("Selecione a quantidade de dias que deseja alugar o carro", 1, 30)
valores_diarios = {"gol": 100, "uno": 80, "hb20": 120, "onix": 150}
st.sidebar.write(f"O preço diário do {carro} é de R$ {valores_diarios[carro]:.2f}")
st.button("Alugar")
st.write(f"Você selecionou o {carro} por {dias} dias. O valor total é de R$ {valores_diarios[carro] * dias:.2f}")

data_retirada = st.date_input("Selecione a data de retirada do carro",datetime.now())
data_devolucao = st.date_input("Selecione a data de devolução do carro",data_retirada)


if st.button("Calcular valor total"):
    dias = (data_devolucao - data_retirada).days
    if dias < 1:
        st.error("A data de devolução deve ser posterior à data de retirada.")
    else:
        valor_total = valores_diarios[carro] * dias
        st.write(f"O valor total para alugar o {carro} por {dias} dias é de R$ {valor_total:.2f}")

if st.button("alugar"):
    st.success(f"Parabéns! Você alugou o {carro} por {dias} dias. O valor total é de R$ {valores_diarios[carro] * dias:.2f}")   