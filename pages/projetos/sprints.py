import streamlit as st
import matplotlib.pyplot as plt
import datetime


def sprints():

    st.date_input("Today is", datetime.datetime.now())

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Monitoramento do Progresso das Atividades da " \
             "Sprint</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    time = ["02/06", "03/06", "04/06", "05/06", "06/06", "07/06", "08/06",
            "09/06", "10/06", "11/06", "12/06", "13/06", "14/06", "15/06"]
    progress_desired = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    real_progress =    [1, 1, 3, 3, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12]

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

    col1.markdown("""
    - Coleta de folhas
    - Digestão foliar
    - Análises foliares
    - Medição das plantas
    - Masseração do solo para análise de COT e NT
    """)

    col2.markdown("""
        - Determinação da CC e PMP
        - Produção dos textos de PIIC
        - Avaliação dos dados da Duda
        - Determinação da estabilidade de agregados após 4 anos
        """)


    
    st.markdown("""
    # To do
    
    ### Day 02/06 - Quinta-feira
    - ~~Planejar as atividades da sprint~~
    - ~~Solicitar aos IC's que envie uma previsão de disponibilidade para as próximas duas semanas~~
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 03/06 - Sexta-feira
    - ~~Aguardar a agenda de compromissos dos IC's~~
    - ~~Completar o plano da sprint~~
    - ~~Organizar todos os dados (Química e Física)~~
    - ~~Organizar amostras para iniciar a determinações química na semana que vem~~
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 04/06 - Sábado
    - ~~Enviar o cronograma de laboratório para os IC's~~
    - ~~Aguardar o parecer da Duda com relação ao cronograma de laboratório~~
    - ~~Aguardar o parecer do Aurélio com relação ao cronograma de laboratório~~
    - ~~Aguardar o parecer do Mateus com relação ao cronograma de laboratório~~
    - ~~Ajustar com as atividades da Maria Amélia~~
    - ~~Enviar o plano de trabalho para a Maria Amélia~~
    - ~~Retirar erlemeyers da estufa~~
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 05/06 - Domingo
    - ~~Aguardar o parecer do Ueslei com relação ao cronograma de laboratório~~
    - ~~Avaliar os dados já obtidos da coleta de 3 anos~~
    - ~~Planejar atividades necessárias para as amostras de 3 anos~~
    - ~~Atualizar as atividades e o gráfico~~
        
    ### Day 06/06 - Segunda-feira
    - ~~Organização do ambiente para as determinações da semana~~
    - ~~Cachimbagem e extração para análise de Ca, Mg e Al~~
    - ~~Enviar para os IC's o plano de trabalho da sprint~~
    - ~~Pedir para o Renato fazer a soliticação para a estufa de 105ºC~~
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 07/06 - Terça-feira
    - ~~Determinação de Al~~
    - ~~Agenda com o Carlos análise de Ca e Mg para 14/06~~
    - ~~Pipetagem de Ca e Mg~~
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 08/06 - Quarta-feira
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 09/06 - Quinta-feira
    - ~~Cachimbagem do pH do solo da coleta de 3 anos, agora com novos padrões~~
    - ~~Determinação do pH~~
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 10/06 - Sexta-feira
    - ~~Avaliar os cálculos realizados pelo Mateus com os dados de 4 anos~~
    - ~~Solicitar aos IC's o cronograma para o periódo de 20 de junho a 01 de agosto~~
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 11/06 - Sábado
    - ~~Descanso~~
     
    ### Day 12/06 - Domingo
    - ~~Descanso~~
    
    ### Day 13/06 - Segunda-feira
    - ~~Leitura de Ca e Mg com o Carlos~~
    - ~~Extração de K, Na e P~~
    - ~~Limpeza dos materiais~~
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 14/06 - Terça-feira
    - Trabalhar no extrator de Richards
    - Cachimbagem e extração para análise de H+Al (Preparar Fenolftaleina) 10-30 cm
    - Alocar as atividades da sprint
    - Alocar as reuniões da sprint
    - Trabalhar nos textos dos projetos
    - Envio do Cronograma solicitado aos IC's
    - Determinação de K, Na e P
    - Alocar as atividades da sprint
    - Atualizar as atividades e o gráfico
    
    ### Day 15/06 - Quarta-feira
    - Organizar os dados de Física do Solo da Duda
    - Criar uma lista de evetnos de divulgação
    - Enviar proposta de trabalho para o próximo ciclo da iniciação
    - Aniversário do Ueslei
    - Enviar avaliação de desenpenho aos IC's
    - Preparar e enviar o cronograma para cada um dos IC's o periódo de 20 de junho a 01 de agosto
    - Alocar as atividades da sprint
    - Atualizar as atividades e o gráfico
            
    """, unsafe_allow_html=True)