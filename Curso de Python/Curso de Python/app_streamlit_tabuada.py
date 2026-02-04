import streamlit as st

st.title("Tabuada em Python 😎")

st.subheader("Feito com streamlit 🌍")

numero_tabuada = st.number_input("Digite o valor da tabuada",0)
inicio_tabuada = st.number_input("DIgite o início da Tabuada",0)
final_tabuada = st.number_input("DIgite o final da Tabuada",0)

opcao = st.selectbox(
    "Qual operação deseja realizar?", 
    ("Soma", "Subtração", "Multiplicação", "Divisão"))

if st.button("Mostrar Tabuada"):
    for multiplicador in range(inicio_tabuada, final_tabuada + 1):
        st.text(f"**{numero_tabuada}X{multiplicador}={numero_tabuada*multiplicador}**")