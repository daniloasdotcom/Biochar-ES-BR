import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(page_title="Carbon", page_icon="🌍")

# Function to generate the K and K2O graph per ton of biochar
def plot_k_k2o_and_ca_levels(dose, k_levels, ca_levels):
    # Potassium Calculations
    k_per_b1 = dose * k_levels[0]  # For Coffee Husk Biochar 350º
    k_per_b2 = dose * k_levels[1]  # For Coffee Husk Biochar 600º
    k_per_b3 = dose * k_levels[2]  # For Eucalyptus Bark Biochar 350º
    k_per_b4 = dose * k_levels[3]  # For Eucalyptus Bark Biochar 600º

    # Conversion from K to K2O
    k2o_per_b1 = k_per_b1 * 1.205
    k2o_per_b2 = k_per_b2 * 1.205
    k2o_per_b3 = k_per_b3 * 1.205
    k2o_per_b4 = k_per_b4 * 1.205

    # Calcium Calculations
    ca_per_b1 = dose * ca_levels[0]  # For Coffee Husk Biochar 350º
    ca_per_b2 = dose * ca_levels[1]  # For Coffee Husk Biochar 600º
    ca_per_b3 = dose * ca_levels[2]  # For Eucalyptus Bark Biochar 350º
    ca_per_b4 = dose * ca_levels[3]  # For Eucalyptus Bark Biochar 600º

    biochars = ['CH350ºC', 'CH600ºC', 'EB350ºC', 'EB600ºC']
    values_k = [k_per_b1, k_per_b2, k_per_b3, k_per_b4]
    values_k2o = [k2o_per_b1, k2o_per_b2, k2o_per_b3, k2o_per_b4]
    values_ca = [ca_per_b1, ca_per_b2, ca_per_b3, ca_per_b4]

    background_color = "#F0F2F6"  # Application background color

    # K graph
    fig_k, ax_k = plt.subplots(figsize=(6, 4))
    fig_k.patch.set_facecolor(background_color)  # Set the background color of the graph
    ax_k.set_facecolor(background_color)  # Set the background color of the axis
    ax_k.bar(biochars, values_k, color='#3498DB', edgecolor='black', linewidth=1.2)
    ax_k.set_ylabel('Potassium (K) Quantity (kg)', fontsize=14, weight='bold', color='#333333')
    ax_k.set_xlabel('Type of Biochar', fontsize=14, weight='bold', color='#333333')
    ax_k.set_ylim(0, 3000)  # Fixed limit of 3000 for K
    ax_k.set_title('Potassium (K) Quantity\nDose: {} t of biochar'.format(dose), fontsize=16, weight='bold', color='#333333', pad=20)
    ax_k.spines['right'].set_visible(False)
    ax_k.spines['top'].set_visible(False)
    for i, v in enumerate(values_k):
        ax_k.text(i, v + 30, f'{v:.2f}', ha='center', fontsize=12, color='#555555')

    # K2O graph
    fig_k2o, ax_k2o = plt.subplots(figsize=(6, 4))
    fig_k2o.patch.set_facecolor(background_color)  # Set the background color of the graph
    ax_k2o.set_facecolor(background_color)  # Set the background color of the axis
    ax_k2o.bar(biochars, values_k2o, color='#1ABC9C', edgecolor='black', linewidth=1.2)
    ax_k2o.set_ylabel('K₂O Equivalent (kg)', fontsize=14, weight='bold', color='#333333')
    ax_k2o.set_xlabel('Type of Biochar', fontsize=14, weight='bold', color='#333333')
    ax_k2o.set_ylim(0, 4000)  # Fixed limit of 4000 for K2O
    ax_k2o.set_title('K₂O Equivalent\nDose: {} t of biochar'.format(dose), fontsize=16, weight='bold', color='#333333', pad=20)
    ax_k2o.spines['right'].set_visible(False)
    ax_k2o.spines['top'].set_visible(False)
    for i, v in enumerate(values_k2o):
        ax_k2o.text(i, v + 30, f'{v:.2f}', ha='center', fontsize=12, color='#555555')

    # Calcium graph
    fig_ca, ax_ca = plt.subplots(figsize=(6, 4))
    fig_ca.patch.set_facecolor(background_color)  # Set the background color of the graph
    ax_ca.set_facecolor(background_color)  # Set the background color of the axis
    ax_ca.bar(biochars, values_ca, color='#E74C3C', edgecolor='black', linewidth=1.2)
    ax_ca.set_ylabel('Calcium (Ca) Quantity (kg)', fontsize=14, weight='bold', color='#333333')
    ax_ca.set_xlabel('Type of Biochar', fontsize=14, weight='bold', color='#333333')
    ax_ca.set_ylim(0, 2000)  # Fixed limit of 2000 for Ca
    ax_ca.set_title('Calcium (Ca) Quantity\nDose: {} t of biochar'.format(dose), fontsize=16, weight='bold', color='#333333', pad=20)
    ax_ca.spines['right'].set_visible(False)
    ax_ca.spines['top'].set_visible(False)
    for i, v in enumerate(values_ca):
        ax_ca.text(i, v + 30, f'{v:.2f}', ha='center', fontsize=12, color='#555555')

    return fig_k, fig_k2o, fig_ca


# Function to generate the 3D graph of planting hole volume
def plot_3d_volume(depth, width, length):
    background_color = "#F0F2F6"  # Application background color

    fig = plt.figure(figsize=(6, 6))
    fig.patch.set_facecolor(background_color)  # Set the background color of the figure
    ax = fig.add_subplot(111, projection='3d')

    # Set the position of the 3D bar
    x = [0]  # Initial X position
    y = [0]  # Initial Y position
    z = [0]  # Initial Z position
    dx = [width]  # Bar width
    dy = [length]  # Bar length
    dz = [depth]  # Bar height

    # Create the 3D bar with brown color
    ax.bar3d(x, y, z, dx, dy, dz, color='brown', alpha=0.7)

    # Set axis background to the same color as the background
    ax.set_facecolor(background_color)

    # Set axis labels with shorter labelpad to bring them closer
    ax.set_xlabel('Width (cm)', labelpad=5)
    ax.set_ylabel('Length (cm)', labelpad=5)
    ax.set_zlabel('Depth (cm)', labelpad=5)

    # Adjust plot margins to ensure labels are visible
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    ax.set_title('Planting Hole Volume', fontsize=14, weight='bold')

    return fig


# Function to generate the 3D graph of biochar volume with points
def plot_3d_biochar_with_points(depth, width, length, dose_per_hole):
    background_color = "#F0F2F6"  # Application background color

    fig = plt.figure(figsize=(6, 6))
    fig.patch.set_facecolor(background_color)  # Set the background color of the figure
    ax = fig.add_subplot(111, projection='3d')

    # Each black dot represents 1 gram of biochar with 2 cm³
    volume_per_point = 2  # cm³ per point
    num_points = int(dose_per_hole)  # Number of points (1 point = 1 gram of biochar)

    # Calculate the number of points based on the hole volume and the volume occupied by each point
    total_hole_volume_cm3 = depth * width * length  # Total volume in cm³
    points_per_hole = min(num_points, total_hole_volume_cm3 // volume_per_point)  # Limit to the hole volume

    # Uniformly distribute points within the hole
    x_points = np.random.uniform(0, width, int(points_per_hole))
    y_points = np.random.uniform(0, length, int(points_per_hole))
    z_points = np.random.uniform(0, depth, int(points_per_hole))

    # Increase point size to 50 and apply visible edges
    ax.scatter(x_points, y_points, z_points, color='black', edgecolors='white', s=50)  # s=50 increases point size

    # Set axis background to the same color as the background
    ax.set_facecolor(background_color)

    # Set axis labels with shorter labelpad to bring them closer
    ax.set_xlabel('Width (cm)', labelpad=5)
    ax.set_ylabel('Length (cm)', labelpad=5)
    ax.set_zlabel('Depth (cm)', labelpad=5)

    # Adjust plot margins to ensure labels are visible
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    ax.set_title(f'Distribution of Biochar\nin the Hole with {int(points_per_hole)}g of Biochar', fontsize=14, weight='bold')

    return fig


# Function for the potassium graph
def potassium_graph(): # Calls the function to configure the sidebar

    # Add custom CSS
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

    st.title("Coffee Husk Biochar: A Source of K")

    st.write("""
             <p class="justified-text">Biochars, when applied to soil, also carry essential nutrients for plant nutrition. \
             In general, the higher the ash content, the higher the amount of mineral nutrients present in biochars.</p>
        """, unsafe_allow_html=True)

    st.write("""
             <p class="justified-text">Furthermore, the raw material and the final production temperature of the biochars \
             are other key factors in defining the inorganic nutrient content present in them. We can observe this in the table below:</p>
            """, unsafe_allow_html=True)

    # Potassium and calcium levels data for biochars
    biochar_data = {
        "Biochar": ['Coffee Husk', 'Coffee Husk', 'Eucalyptus Bark', 'Eucalyptus Bark'],
        "Temperature": ['350ºC', '600ºC', '350ºC', '600ºC'],
        "K Content (kg/t)": [44.57, 56.57, 5.66, 7.01],
        "Ca Content (kg/t)": [16.70, 23.23, 26.36, 33.11]  # Adding calcium content
    }

    # Create dataframe
    df = pd.DataFrame(biochar_data)

    # Display the table centered with the defined CSS
    st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)

    st.write("""
        <p class="justified-text">It is clear that coffee husk biochars have a significant potassium content compared \
        to eucalyptus bark biochars. Eucalyptus bark, on the other hand, contains slightly more calcium \
        than coffee husk biochars. These differences in nutrient levels between the two materials are \
        related to biochemical aspects, which I explain in my blog post on biochemistry \
        <a href="https://bioquimicacomdanilo.com.br/2024/09/24/nutrientes-biocarvoes.html" target="_blank">here</a>.</p>
    """, unsafe_allow_html=True)

    st.write("""
                <p class="justified-text">Looking again at the table, we can also observe differences with temperature. Higher \
                temperatures concentrate more nutrients than lower temperatures. This phenomenon is related to \
                the loss of organic content and the preservation of inorganic content as production temperature increases. \
                We will discuss this in another post. Today, I would like to focus on the ability of coffee husk biochars \
                to carry a considerable amount of soluble K to the soil.</p>
               """, unsafe_allow_html=True)

    st.write("""
                <p class="justified-text">Our table shows that each ton of coffee husk biochar contains between 40 and 60 kg \
                of potassium. Consider that about 90%-95% of this content is water-soluble, therefore readily available for plant uptake.</p>
               """, unsafe_allow_html=True)

    st.write("""
                <p class="justified-text">Move the slider below the graphs to see how much K each ton of coffee husk biochar \
                carries. I have included a graph with equivalent values in K₂O for comparison, as potassium fertilizer recommendations \
                are expressed in K₂O.</p>
               """, unsafe_allow_html=True)

    # Display K, K2O, and Ca graphs in columns
    (col_k, col_k2o) = st.columns(2)

    # Use st.markdown to display a styled text above the slider
    st.markdown('<p class="slider-label">Select the amount of biochar (t)</p>', unsafe_allow_html=True)

    # Slider
    dose = st.slider('', 0, 50, 1, format="%d t")  # Keeping the text empty to avoid repetition
    k_levels = [44.57, 56.57, 5.66, 7.01]  # Corresponding to B1, B2, B3, B4 (Potassium)
    ca_levels = [16.70, 23.23, 26.36, 33.11]  # Corresponding to B1, B2, B3, B4 (Calcium)
    fig_k, fig_k2o, fig_ca = plot_k_k2o_and_ca_levels(dose, k_levels, ca_levels)

    # Display 2D graphs of K, K2O, and Ca in columns
    with col_k:
        st.pyplot(fig_k)
    with col_k2o:
        st.pyplot(fig_k2o)
    #with col_ca:
    #    st.pyplot(fig_ca)

    st.write("""
               <p class="justified-text">For some people, 1 ton of coffee husk biochar may seem like a large amount to transport and apply. \
               However, these values reduce since the producer will not apply it across the entire area. \
               Below, you can check how much biochar is needed for application in a planting hole, for example. \
               Feel free to change the values and dimensions of the hole and the equivalent biochar in the slider.</p>
           """, unsafe_allow_html=True)

    # Arrange input and output for the 3D graphs in three columns
    col_input, col_volume, col_biochar = st.columns(3)

    with col_input:
        # Input boxes for Depth, Width, and Length
        st.subheader("Planting Hole Dimensions")
        depth = st.number_input("Depth (cm)", min_value=1, value=40)
        width = st.number_input("Width (cm)", min_value=1, value=40)
        length = st.number_input("Length (cm)", min_value=1, value=40)

    # Calculate hole volume (D x W x L)
    hole_volume = (depth * width * length) / 1000  # Converted to dm³
    dose_per_hole = ((dose * hole_volume) / 2_000_000) * 1000000  # Converted to grams

    with col_volume:
        # Display 3D column graph of the hole volume
        fig_volume = plot_3d_volume(depth, width, length)
        st.pyplot(fig_volume)

        # Add centered text indicating the hole volume
        st.markdown(f"<div style='text-align: center;'><strong>Hole Volume:</strong> </div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center;'>{hole_volume:.2f} dm³</div>", unsafe_allow_html=True)

    with col_biochar:
        # Display 3D graph with black points representing biochar
        fig_biochar = plot_3d_biochar_with_points(depth, width, length, dose_per_hole)
        st.pyplot(fig_biochar)

        # Add centered text indicating the amount of biochar per hole
        st.markdown(f"<div style='text-align: center;'><strong>Amount of biochar per hole:</strong> {dose_per_hole:.2f} g</div>", unsafe_allow_html=True)

    st.write("""
               <p class="justified-text">For fertilization purposes, each ton of coffee husk biochar can add the equivalent of 50 to 70 kg/ha of K₂O. \
               For this, 32 grams per plant are required, mixed in a hole measuring 40 cm x 40 cm x 40 cm. \
               Of course, the amount of biochar should be multiplied by the number of plants per hectare to know the total biochar needed for each hectare.</p>
           """, unsafe_allow_html=True)

    st.write("""
                   <p class="justified-text">In conclusion, it is clear that coffee husk biochars can serve as a nutrient source, \
                   potentially replacing part of the potassium fertilization and other nutrients. \
                   Additionally, they serve as a relatively stable source of organic matter for the soil, \
                   contributing positively to other physical and biological attributes of agricultural interest.</p>
               """, unsafe_allow_html=True)

    st.write("""
                   <p class="justified-text">Finally, it is important to note that the beneficial effects vary significantly \
                   depending on the soil, the biochar, and the biochar dose, which we will discuss in a future post.</p>
               """, unsafe_allow_html=True)

# Run the display function
potassium_graph()
