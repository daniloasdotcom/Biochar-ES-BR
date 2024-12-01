import streamlit as st

# Function to display carbon amounts as squares with percentage
def display_carbon_squares(dose, carbon_levels):
    biochars = ['CH350ºC', 'CH600ºC', 'EB350ºC', 'EB600ºC']
    carbon_values = [int(dose * level) for level in carbon_levels]  # Convert values to integers
    percentages = [round((value / 2000000) * 100, 2) for value in carbon_values]  # Calculate percentage

    st.write("### Carbon Added to Soil (kg)")
    col1, col2, col3, col4 = st.columns(4)

    for idx, (biochar, carbon_value, percentage) in enumerate(zip(biochars, carbon_values, percentages)):
        with [col1, col2, col3, col4][idx]:
            st.markdown(f"""
                <div style="
                    border: 2px solid #3498DB;
                    border-radius: 10px;
                    background-color: #ECF0F1;
                    padding: 20px;
                    text-align: center;
                ">
                    <h5 style="margin: 0; color: #333333; font-size: 12px;">{biochar}</h5>
                    <p style="font-size: 24px; font-weight: bold; color: #2ECC71; margin-top: 10px;">{carbon_value} kg</p>
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                <div style="
                    border: 2px solid #E67E22;
                    border-radius: 10px;
                    background-color: #FDEBD0;
                    padding: 10px;
                    text-align: center;
                    margin-top: 10px;
                ">
                    <h5 style="margin: 0; color: #333333; font-size: 12px;">% of carbon on soil from biochar</h5>
                    <p style="font-size: 20px; font-weight: bold; color: #D35400; margin-top: 5px;">{percentage}%</p>
                </div>
            """, unsafe_allow_html=True)

    return percentages  # Return percentages


# Function to display the carbon dashboard
def carbon_dashboard():
    st.markdown("""
        <style>
        .slider-label {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: -20px;
        }
        .justified-text {
            text-align: justify;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("Back to Blog"):
        st.session_state['page'] = 'blog'

    st.title("Carbon Addition to Soil by Biochar Application")

    st.write("""
        <p class="justified-text">Soil organic matter is a highly heterogeneous component composed of microorganisms, roots, macro and mesofauna, organic residues, organic molecules of different types, and charred organic matter. An essential element of this organic matter is carbon, which, due to its chemical characteristics, forms the structural base of the molecules that make up soil organic matter.</p>
    """, unsafe_allow_html=True)

    st.write("""
        <p class="justified-text">Since carbon is the main component of organic molecules, its quantity is often used to quantify soil organic matter. Moreover, measuring the organic carbon present in the soil allows estimation of how much carbon a given area stores, an important indicator for carbon sequestration strategies and carbon stock.</p>
    """, unsafe_allow_html=True)

    st.write("""
        <p class="justified-text">Additionally, in tropical climate soils, such as Latosols and Argisols predominant in Brazil, organic carbon levels are generally below 5 dag/dm³ (5%). Increasing or even maintaining these levels is desirable, considering the multiple benefits organic matter provides for soil fertility, structure, and productivity. However, the rapid organic matter cycle in tropical climates makes this increase a challenge.</p>
    """, unsafe_allow_html=True)

    st.write("""
        <p class="justified-text">In this context, biochars derived from plant biomass can contribute, at least by adding organic carbon. With high organic carbon content (generally above 50% by mass) and a longer residence time in the soil (compared to raw biomass), applying these materials tends to increase the total organic carbon content of the soil. However, the amount of carbon added depends on both the carbon content of the biochar and the dose applied. Use our dashboard below and see a hypothetical effect of % carbon addition in the soil based on biochar doses.</p>
    """, unsafe_allow_html=True)

    carbon_levels = [598.7, 766.6, 549.9, 650.5]

    st.markdown('<p class="slider-label">Select the amount of biochar (t)</p>', unsafe_allow_html=True)
    dose = st.slider('', 0, 50, 1, format="%d t")

    percentages = display_carbon_squares(dose, carbon_levels)

    # Get the percentage for coffee husk at 350ºC
    coffee_husk_350_percentage = percentages[0]  # Assuming it's the first item in the list

    st.write("""
        <p class="justified-text">The presented percentages show the increase in soil carbon content due to biochar application. For the calculations, the following assumptions were considered:</p>
        <ul class="justified-text">
            <li>Calculation based on mass/mass.</li>
            <li>Soil bulk density: 1 kg/dm³.</li>
            <li>Soil layer depth: 20 cm.</li>
            <li>Total area: 1 hectare (10,000 m²).</li>
            <li>Assuming total area application.</li>
            <li>And the carbon contents shown in the table below</li>
        </ul>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .center-table {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .table-caption {
            text-align: center;
            font-style: italic;
            margin-top: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Render table and caption
    st.markdown("""
        <div class="center-table">
            <table border="1" style="border-collapse: collapse; text-align: center;">
                <thead>
                    <tr>
                        <th>Biochar</th>
                        <th>Temperature</th>
                        <th>C Content (kg/t)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Coffee Husk</td>
                        <td>350ºC</td>
                        <td>598.7</td>
                    </tr>
                    <tr>
                        <td>Coffee Husk</td>
                        <td>600ºC</td>
                        <td>766.6</td>
                    </tr>
                    <tr>
                        <td>Eucalyptus Bark</td>
                        <td>350ºC</td>
                        <td>549.9</td>
                    </tr>
                    <tr>
                        <td>Eucalyptus Bark</td>
                        <td>600ºC</td>
                        <td>650.5</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p class="table-caption">Source: The author</p>
    """, unsafe_allow_html=True)

    st.write(f"""                       
        <p  class ="justified-text" > These assumptions provide an estimate of the proportion of carbon added to the soil with the biochar application.</p>
    """, unsafe_allow_html=True)

    st.write(f"""
        <p class="justified-text">With a selected dose of <strong>{dose} tons</strong>, biochars (in the case of coffee husk produced at 350ºC) can increase soil carbon content by <strong>{coffee_husk_350_percentage}%</strong>.</p>
    """, unsafe_allow_html=True)

    st.write("""
        <p class="justified-text">To promote a sustainable increase in organic carbon, it is necessary to use recalcitrant sources, that is, those that resist decomposition and remain in the soil longer. Biochar presents this characteristic, especially when produced from biomass with a high lignin content or subjected to higher temperatures during its production. The higher the production temperature and the lignin content of the biomass, the more recalcitrant the biochar, prolonging its permanence in the soil.</p>
    """, unsafe_allow_html=True)
