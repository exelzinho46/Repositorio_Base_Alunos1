import requests
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Consulta de CEP",
    page_icon="📍",
    layout="wide"
)

st.title("📍 Consulta de CEP")


if "busca" not in st.session_state:
    st.session_state.busca = None


st.sidebar.title("Pesquisar CEP")
cep = st.sidebar.text_input(
    "Digite o CEP (somente números)",
    max_chars=8,
    placeholder="Ex: 01001000"
)


if st.sidebar.button("Pesquisar"):

    if len(cep) != 8 or not cep.isdigit():
        st.sidebar.error("Digite um CEP válido com 8 números.")
    else:

        resposta = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")

        if resposta.status_code == 200:

            busca = resposta.json()

            if "code" in busca:
                st.sidebar.error("CEP não encontrado.")
            else:
                st.session_state.busca = busca

        else:
            st.sidebar.error("Erro ao consultar a API.")


if st.session_state.busca is not None:

    busca = st.session_state.busca

    st.success("CEP encontrado com sucesso!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Informações")

        st.write(f"**CEP:** {busca['cep']}")
        st.write(f"**Endereço:** {busca['address']}")
        st.write(f"**Bairro:** {busca['district']}")
        st.write(f"**Cidade:** {busca['city']}")
        st.write(f"**Estado:** {busca['state']}")

    with col2:
        st.subheader("Localização")

        lat = float(busca["lat"])
        lng = float(busca["lng"])

        mapa = folium.Map(
            location=[lat, lng],
            zoom_start=16
        )

        folium.Marker(
            [lat, lng],
            tooltip=busca["address"],
            popup=f"{busca['address']} - {busca['city']}"
        ).add_to(mapa)

        st_folium(mapa, width=700, height=500)