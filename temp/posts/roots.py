import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Configurar a página
st.set_page_config(page_title="Simulação de Crescimento de Raízes", layout="centered")

# Título do aplicativo
st.title("Simulação de Crescimento de Raízes com Subramificações Hierárquicas")

# Instruções
st.markdown("""
Este aplicativo simula o crescimento de raízes de uma planta até que a raiz principal atinja 15 cm de profundidade.
As raízes crescem de forma gradual, com ramificações surgindo no ponto médio do crescimento e ramificações laterais
gerando suas próprias subramificações, que também crescem ao longo do tempo.
""")

# Função para expandir uma ramificação existente
def extend_branch(branch, angle, step_length=1):
    """
    Estende uma ramificação existente ao longo de um ângulo específico.
    """
    x_start, y_start = branch[-1]  # Ponto final atual da ramificação
    x_end = x_start + step_length * np.sin(np.radians(angle))
    y_end = y_start - step_length * np.cos(np.radians(angle))
    branch.append((x_end, y_end))

# Função para criar uma nova ramificação
def create_branch(start_point, angle, length=2):
    """
    Cria uma nova ramificação a partir de um ponto inicial.
    """
    x_start, y_start = start_point
    x_end = x_start + length * np.sin(np.radians(angle))
    y_end = y_start - length * np.cos(np.radians(angle))
    return [(x_start, y_start), (x_end, y_end)], angle

# Função para simular o crescimento das raízes
def simulate_root_growth():
    plot_placeholder = st.empty()  # Espaço reservado para o gráfico
    main_root = [(0, 0)]  # A raiz principal começa na superfície
    branches = []  # Lista de ramificações (cada uma com seus pontos e ângulo)
    subbranches = []  # Lista de subramificações geradas por ramificações
    ramification_points = []  # Pontos médios para futuras ramificações

    # Loop para crescimento da raiz principal e adição/expansão de ramificações
    for step in range(50):  # Número de lapsos (ajustável)
        if main_root[-1][1] <= -15:  # Parar quando atingir 15 cm de profundidade
            break

        if step % 2 == 0:
            # Crescimento da raiz principal
            last_point = main_root[-1]
            new_point = (last_point[0], last_point[1] - 1)  # Descer 1 cm
            main_root.append(new_point)

            # Adicionar ponto médio para futuras ramificações
            if len(main_root) > 2:
                midpoint_index = len(main_root) // 2
                ramification_points.append(main_root[midpoint_index])

        else:
            # Adicionar nova ramificação ou expandir as existentes
            if ramification_points:
                # Criar uma nova ramificação
                midpoint = ramification_points.pop(0)  # Pegar o próximo ponto médio
                angle = np.random.choice([-30, 30])  # Ângulo de ramificação
                branch, branch_angle = create_branch(midpoint, angle)
                branches.append((branch, branch_angle))

            # Expandir ramificações existentes
            for branch, branch_angle in branches:
                extend_branch(branch, branch_angle)

                # Adicionar subramificações às ramificações principais
                if len(branch) > 3 and np.random.random() < 0.3:  # 30% de chance de subramificar
                    midpoint = branch[len(branch) // 2]  # Escolher o ponto médio da ramificação
                    sub_angle = branch_angle + np.random.choice([-20, 20])  # Pequena variação do ângulo
                    subbranch, subbranch_angle = create_branch(midpoint, sub_angle)
                    subbranches.append((subbranch, subbranch_angle))

            # Expandir subramificações existentes
            for subbranch, subbranch_angle in subbranches:
                extend_branch(subbranch, subbranch_angle)

        # Atualizar o gráfico
        fig, ax = plt.subplots()
        ax.set_xlim(-20, 20)  # Ajustar para acomodar crescimento horizontal
        ax.set_ylim(-20, 0)
        ax.set_xlabel("Distância horizontal (cm)")
        ax.set_ylabel("Profundidade (cm)")
        ax.axhline(0, color='brown', linewidth=2, label="Superfície do Solo")

        # Desenhar a raiz principal
        main_root_x = [point[0] for point in main_root]
        main_root_y = [point[1] for point in main_root]
        ax.plot(main_root_x, main_root_y, color='green', linewidth=2, label="Raiz Principal")

        # Desenhar ramificações
        for branch, _ in branches:
            branch_x = [point[0] for point in branch]
            branch_y = [point[1] for point in branch]
            ax.plot(branch_x, branch_y, color='green', linestyle='--')

        # Desenhar subramificações
        for subbranch, _ in subbranches:
            subbranch_x = [point[0] for point in subbranch]
            subbranch_y = [point[1] for point in subbranch]
            ax.plot(subbranch_x, subbranch_y, color='blue', linestyle=':')

        ax.legend()

        # Renderizar o gráfico no Streamlit
        plot_placeholder.pyplot(fig)

        # Pausa para visualização
        time.sleep(0.5)

# Botão para iniciar a simulação
if st.button("Iniciar Simulação"):
    simulate_root_growth()
