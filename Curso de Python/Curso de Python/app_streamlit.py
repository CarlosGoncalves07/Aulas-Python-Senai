#import streamlit as st

#st.title("Calculadora Simples🧮")
# Botão do Windows + . abre icones
#ctrl + aspas"Abre o terminal > No terminal > pip install streamlit > python -m streamlit run .\app_streamlit.py
#Local URL: http://localhost:8501
  #Network URL: http://10.107.148.106:8501
# st.subheader("Feito com Streamlit😎")

# valor1 = st.number_input("Digite o primeiro valor",0)
# valor2 = st.number_input("Digite o segundo valor",0)

# opcao = st.selectbox(
#     "Qual operação deseja realizar?", 
#     ("Soma", "Subtração", "Multiplicação", "Divisão"))
# if st.button("Calcular"):
#     if opcao == "Soma":
#         st.success(f"{valor1+valor2}")
#     if opcao == "Subtração": st.button("Calcular")
#     st.success(f"{valor1-valor2}")
#     if opcao == "SMultiplicação": st.button("Calcular")
#     st.success(f"{valor1*valor2}")
#     if opcao == "Vidisão": st.button("Calcular")
#     st.success(f"{valor1/valor2}")
import streamlit as st


st.title("Calculadora Simples 🧮")
st.subheader("Feito com Streamlit ❤️")


# st.markdown(body="<h1 font-family='comic-sans'> Teste </h1>",unsafe_allow_html=True)

# ctrl + ; para comentar varias linhas


valor1 = st.number_input("Digite o primeiro valor",0)
valor2 = st.number_input("Digite o segundo valor",0)


opcao = st.selectbox(
    "Qual operação deseja realizar?",
    ("Soma", "Subtração", "Multiplicação", "Divisão"))




if st.button("Calcular"):
    try:
        if opcao == "Soma":
            st.success(f"{valor1 + valor2}")
        elif opcao == "Subtração":
            st.success(f"{valor1 - valor2}")
        elif opcao == "Multiplicação":
            st.success(f"{valor1 * valor2}")
        elif opcao == "Divisão":
            st.success(f"{valor1 / valor2}")
        else:
            st.error("Opção inválida.")
    except:
        st.error("Ocorreu um erro.")