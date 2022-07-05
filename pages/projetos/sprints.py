import streamlit as st
import matplotlib.pyplot as plt
import datetime

def sprints():

    st.date_input("Today is", datetime.datetime.now())

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Monitoramento do Progresso das Atividades da " \
             "Sprint</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    time = ["04/07", "05/07", "06/07", "07/07", "08/07",
            "11/07", "12/07", "13/07", "14/07", "15/07"]
    progress_desired = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    real_progress =    [0, 0, 0, 0, 0, 0, 0, 0, 0,  0]

    fig02 = plt.figure(figsize=(10, 5))

    plt.plot(time, progress_desired, marker='o', label="Planejado")
    plt.plot(time, real_progress, marker='o', label="Entregue")
    plt.title('Gráfico de Progresso das Atividades da Sprint')
    plt.xlabel('Tempo')
    plt.ylabel('Progresso')
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()

    st.pyplot(fig02)

    st.markdown("""
        # Product backlog
        """)

    col1, col2 = st.columns([1, 1])

    with col1.expander("Prioridades"):
        st.markdown("""
        # Prioridades
        - Alocar as reuniões da sprint
        - Realizar o treinamento em agregados e ADA
        - Avaliar e organizar os dados da Duda e do Mateus
        - Solicitar a agenda deles para o período entre 18 e 29 de julho
        
        """)

    with col2.expander("Demais"):
        st.markdown("""
        - Criar uma lista de eventos de divulgação dos nossos trabalhos
        
        """)

    st.markdown("""
                # To do
    """)

    with st.expander("Day 04/07 - Segunda-feira - Em Progresso"):
        st.markdown("""
        
        - Agendar para sábado a medição das plantas na área experimental
        - ~~Solicitar o podão à professsora e agendar para sabádo a coletar foliar~~
        - Agendar para sexta-feria o uso da estufa para secagem do material
        - Agendar para domingo/segunda-feira que vem a digestão
        - Verificar solução nitroperclórica
        - ~~Iniciar a masseração do solo do 4º ano (NT e COT)~~
        
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico
            
        """)
    with st.expander("Day 05/07 - Terça-feira"):
        st.markdown("""    

        - Testar o aparelho de Nitrogênio Total
        - Avaliar o extrator de Richards e a Mudança de posição dele
        - Bem como planejar as determinações de CC e PMP
        - Iniciar a separação do agregados (atrás da quadra)
        
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 06/07 - Quarta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 07/07 - Quinta-feira"):
        st.markdown("""    

        - Planejar a digestão foliar e as determinações para o Aurélio
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 08/07 - Sexta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 11/07 - Segunda-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 12/07 - Terça-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 13/07 - Quarta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 14/07 - Quinta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 15/07 - Sexta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """, unsafe_allow_html=True)