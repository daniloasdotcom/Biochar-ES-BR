import streamlit as st
import pandas as pd

# Load the dataset
def load_data():
    file_path = 'EMBRAPA_Job_Details_Extended.xlsx'  # Replace with actual file path
    data = pd.read_excel(file_path)
    return data

data = load_data()

# Streamlit app
def main():
    st.title("Filtro de Vagas - EMBRAPA")

    # Area filter on the main page
    area_options = data['Área'].dropna().unique()
    selected_area = st.selectbox("Selecione a Área", options=["Selecionar"] + list(area_options))

    if selected_area == "Selecionar":
        st.write("Por favor, selecione uma Área para visualizar as Subáreas.")
        return

    # Subarea buttons
    subarea_options = data[data['Área'] == selected_area]['Subárea'].dropna().unique()
    st.write("**Subáreas Disponíveis:**")
    selected_subarea = None

    cols = st.columns(4)  # Adjust the number of columns for layout
    for i, subarea in enumerate(subarea_options):
        col = cols[i % len(cols)]  # Cycle through columns
        if col.button(subarea):
            selected_subarea = subarea

    if not selected_subarea:
        st.write("Por favor, clique em uma Subárea para visualizar as informações.")
        return

    # Filter data based on selections
    filtered_data = data.copy()
    filtered_data = filtered_data[(filtered_data['Área'] == selected_area) & (filtered_data['Subárea'] == selected_subarea)]

    # Display results
    st.header("Resultados Filtrados")
    if filtered_data.empty:
        st.write("Nenhuma vaga encontrada para os filtros selecionados.")
    else:
        st.write(f"**Área:** {selected_area}")
        st.write(f"**Subárea:** {selected_subarea}")
        st.write("---")

        localidades_series = filtered_data['Localidade'].dropna().str.split(';')
        localidades = [loc.strip() for sublist in localidades_series for loc in sublist]
        localidades = list(set(localidades))  # Remove duplicates

        st.write("**Localidades:**")
        for localidade in localidades:
            st.write(f"- {localidade}")

        st.write("**Vagas:**")
        for _, vaga in filtered_data.iterrows():
            st.write(f"- Opção: {vaga['Opção nº']}")
            st.write(f"- AC: {vaga['AC']}")
            st.write(f"- PcD: {vaga['PcD']}")
            st.write(f"- PPP: {vaga['PPP']}")
            st.write(f"- Total de Vagas: {vaga['Total de Vagas']}")
            st.write("---")

        st.write("**Requisitos:**")
        for _, vaga in filtered_data.iterrows():
            st.write("**Mestrado em:**")
            for mestrado in vaga['Mestrado'].split(';'):
                st.write(f"- {mestrado.strip()}")

            st.write("**Graduação em:**")
            for graduacao in vaga['Graduação'].split(';'):
                st.write(f"- {graduacao.strip()}")

            st.write("**Descrição específica das atividade do cargo:**")
            st.write(f"<p style='text-align: justify;'>{vaga['Descrição específica das atividade do cargo'].capitalize()}</p>", unsafe_allow_html=True)
            st.write("---")

if __name__ == "__main__":
    main()