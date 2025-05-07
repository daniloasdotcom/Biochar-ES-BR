import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    file_path = "data/cinzas.xlsx"
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        st.error("The file 'cinzas.xlsx' was not found in the project directory.")
        return None


def show_explanatory_text01():
    explanatory_text = """
    <div style="text-align: justify;">
    The pyrolysis temperature and the type of biomass feedstock are critical factors in determining the properties of biochars. These factors influence nutrient content and availability, the amount of functional groups, the degree of recalcitrance, and the alkalinity of the final biochar.
    <br><br>
    Alkalinity is essential for using biochar as a soil amendment because it directly affects its ability to neutralize soil acidity, creating a more favorable environment for crop growth. Additionally, alkalinity is associated with the cation exchange capacity, which is key to retaining and making nutrients available to plants. Thus, the selection of a biochar should consider its potential to influence soil pH for proper agronomic use.
    <br><br>
    According to Fidel et al. (2017), the sources of alkalinity in biochars fall into four main categories: low-acidity organic functional groups, soluble organic compounds, carbonates, and other inorganic alkalis. The latter two are often associated with the ash content in biochar.
    <br><br>
    It would seem logical that higher ash content would result in higher alkalinity. However, this is not always the case.
    <br>
    <br>
    </div>
    """
    st.markdown(explanatory_text, unsafe_allow_html=True)


def show_explanatory_text02():
    explanatory_text = """
    <div style="text-align: justify;">
    When examining the graph above, we see that even highly lignified materials (labeled as crop residues), which typically contain lower ash content (points clustered toward the left), display wide pH variability (ranging from 4 to 10). This suggests that ash content alone is not a reliable predictor of biochar alkalinity.
    <br>
    </div>
    """
    st.markdown(explanatory_text, unsafe_allow_html=True)


def show_explanatory_text03():
    explanatory_text = """
    <div style="text-align: justify;">
    This variability is likely due to the specific chemical species formed during pyrolysis, which ultimately define the alkaline character of the biochar.
    <br>
    </div>
    """
    st.markdown(explanatory_text, unsafe_allow_html=True)


def plot_graph(df, x_col, y_col, title, x_label, y_label, selected_option, color_map):
    plt.style.use("seaborn-v0_8-poster")
    fig, ax = plt.subplots(figsize=(8, 6))

    if selected_option == "Full dataset":
        for classification, group_data in df.groupby("Classificacao"):
            ax.scatter(
                group_data[x_col],
                group_data[y_col],
                label=classification,
                color=color_map.get(classification, "gray"),
                alpha=0.8,
                s=100
            )
    else:
        group_data = df[df["Classificacao"] == selected_option]
        ax.scatter(
            group_data[x_col],
            group_data[y_col],
            label=selected_option,
            color=color_map.get(selected_option, "gray"),
            alpha=0.8,
            s=100
        )

    ax.set_title(title, fontsize=18, fontweight="bold")
    ax.set_xlabel(x_label, fontsize=14)
    ax.set_ylabel(y_label, fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.legend(title="Classification", fontsize=12, title_fontsize=14, loc='lower right')
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.text(
        1.05, 0.5,
        "Source: UCD BIOCHAR DATABASE, 2024",
        transform=ax.transAxes,
        fontsize=10,
        color="gray",
        ha="left",
        va="center",
        rotation=90
    )

    return fig


def main():
    st.title("pH vs Ash Content in Biochars")

    show_explanatory_text01()

    df_cinzas = load_data()

    if df_cinzas is not None:
        options = ["Full dataset", "Organic Waste", "Crop Residues", "Woody Biomass"]
        color_map = {
            "Organic Waste": "#1f77b4",
            "Crop Residues": "#ff7f0e",
            "Woody Biomass": "#2ca02c"
        }

        layout = st.columns([4, 7])
        with layout[0]:
            selected_option = st.radio("Select classification:", options, index=0, key="ash_ph")
        with layout[1]:
            fig = plot_graph(df_cinzas, "Cinzas", "pH", "Ash vs pH", "Ash Content (%)", "pH", selected_option, color_map)
            st.pyplot(fig)

        with st.expander("💡 Why categorize by feedstock lignification level?"):
            st.markdown("""
            <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
            This classification assumes that the more resistant the organic matter to oxidation, the less ash it produces during pyrolysis. This graph allows us to observe such trends more clearly.
            </div>
            """, unsafe_allow_html=True)

    show_explanatory_text02()
    st.markdown("<br>", unsafe_allow_html=True)
    show_explanatory_text03()
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: left;">
    <strong>References</strong>: <br>
    Fidel, R.B., Laird, D.A., Thompson, M.L., & Lawrinenko, M. (2017). Characterization and quantification of biochar alkalinity. 
    <em>Chemosphere, 167</em>, 367-373. Available at: <a href="https://doi.org/10.1016/j.chemosphere.2016.09.151" target="_blank">https://doi.org/10.1016/j.chemosphere.2016.09.151</a>.<br>
    UCD BIOCHAR DATABASE. Biochar Database. University of California, Davis, 2024. Available at: <a href="https://biochar.ucdavis.edu" target="_blank">https://biochar.ucdavis.edu</a>. Accessed on: Dec 4, 2024.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
