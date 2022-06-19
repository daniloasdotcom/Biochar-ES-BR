import streamlit as st
import matplotlib.pyplot as plt
import datetime
import calendar

def sprints():

    st.date_input("Today is", datetime.datetime.now())

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Monitoramento do Progresso das Atividades da " \
             "Sprint</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    year = 2022
    month = 6
    print(calendar.month(year, month))

    time = ["20/06", "21/06", "22/06", "23/06", "24/06",
            "27/06", "28/06", "29/06", "30/06", "01/06"]
    progress_desired = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    real_progress =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        - Coleta de folhas
        - Digestão foliar
        - Análises foliares
        - Medição das plantas
        - Masseração do solo para análise de COT e NT
        - Trabalhar no extrator de Richards
        - Criar uma lista de eventos de divulgação dos nossos trabalhos
        - Enviar para o Renato a proposta de trabalho para o próximo ciclo da iniciação
        - Aniversário do Ueslei
        - Alocar as reuniões da sprint
        - Atualizar as atividades e o gráfico
        """)

    with col2.expander("Demais"):
        st.markdown("""
        - Determinação da CC e PMP
        - Produção dos textos de PIIC
        - Avaliação dos dados da Duda
        - Determinação da estabilidade de agregados após 4 anos
        - Cachimbagem e extração para análise de H+Al (Preparar Fenolftaleina) 10-30 cm
        - Organizar os dados de Física do Solo da Duda
        - Enviar avaliação de desenpenho aos IC's
        - Preparar e enviar o cronograma para cada um dos IC's o periódo de 20 de junho a 01 de agosto
        - Alocar as atividades da sprint
        
        """)

    st.markdown("""
                # To do
    """)

    with st.expander("Day 20/06"):

        st.markdown("""    
            
        - Atualizar as atividades e o gráfico
            
        """)
    with st.expander("Day 21/06"):
        st.markdown("""    

        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 22/06"):
        st.markdown("""    

        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 23/06"):
        st.markdown("""    

        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 24/06"):
        st.markdown("""    

        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 27/06"):
        st.markdown("""    

        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 28/06"):
        st.markdown("""    

        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 29/06"):
        st.markdown("""    

        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 30/06"):
        st.markdown("""    

        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 01/07"):
        st.markdown("""    

        - Atualizar as atividades e o gráfico

        """, unsafe_allow_html=True)