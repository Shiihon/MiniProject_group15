import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Wine Quality Explorer", layout="wide")

## Select the page
page = st.sidebar.radio("Pages", ["Wine Quality Analysis", "Wine Quality Info"])

# A page for our plot, diagrams and other things we analyzed
if page == "Wine Quality Analysis":
    ## Title
    st.title("Wine Quality Exploratory Data Analysis",)

    ## Sidebar for selecting a dataset
    st.sidebar.header("Wine Filter")
    dataset_choice = st.sidebar.selectbox("Select Wine Type", ["Red Wine", "White Wine", "Red & White Wine"])

    ## Display dynamic subheader that's beneath the title based on selected dataset
    if dataset_choice == "Red Wine":
        st.subheader("Exploring Wine Quality: Red Wines")
    elif dataset_choice == "White Wine":
        st.subheader("Exploring Wine Quality: White Wines")
    else:
        st.subheader("Exploring Wine Quality: Red vs. White Wines")

    ## Function for loading the chosen dataset
    def load_data(dataset_name):
        if dataset_name == "Red Wine":
            return pd.read_csv('../red_wine_cleaned.csv')
        elif dataset_name == "White Wine":
            return pd.read_csv('../white_wine_cleaned.csv')
        else:
            df_all = pd.read_csv('../red_white_wine_cleaned.csv')
            # Remove the auto generated index column
            df_all = df_all.drop(columns=['Unnamed: 0'])
            return df_all

    ## Display some data from the chosen dataset
    chosen_df = load_data(dataset_choice)
    st.markdown(f"**Loaded {len(chosen_df)} samples from the {dataset_choice} dataset**")
    st.write("Here are 5 random samples from the overall dataset:")
    st.dataframe(chosen_df.sample(5))

    ## Descriptive Stats
    st.subheader("Descriptive Statistics")
    st.write("""
        Descriptive statistics such as mean, median, standard deviation, and quartiles will help us understand the distribution and central tendency of the wine attributes. 
        This is used as a starting point to analyze patterns and identify any noteworthy trends in the wine dataset.
        """)
    st.write(chosen_df.describe())

    ## Organize sections in tabs
    tab1, tab2, tab3 = st.tabs(["Feature Distribution", "2D Scatter Plot" ,"3D Scatter Plot"])
    with tab1:
        ## Distribution & Boxplot
        st.subheader("Feature Distribution")
        st.markdown("#### Visualizing Feature Distribution & Spread")
        st.write("""
            The distribution plot shows the frequency of different values for each selected feature, helping us to understand the shape and spread of the data.
            By examining the histogram along with the Kernel Density Estimation (KDE) curve, we can get a clearer idea of whether a feature follows a normal distribution, is skewed, or has multiple modes.
            On the other hand, the boxplot provides a summary of the data's spread and highlights potential outliers, the median, and the interquartile range (IQR).
            These plots are crucial for identifying patterns, outliers, or potential transformations needed for further analysis.
            """)
        # creates dropdown to be able to select a specific feature (column) from the dataset
        col_to_plot = st.selectbox("Select feature for distribution plot:", chosen_df.columns[:-1])

        st.markdown("##### Histogram")
        st.write("""
                Looking through all the histograms it is clear that almost all the shapes do not have the characteristics of a normal distribution.
                Almost all of them are right-skewed with long tails extending to unusually high values compared to where most of the data is gathered.
                The only histogram with a normal-like distribution is the one for "ph". 
                The only other histogram that stands out is the one for "quality" which have an almost symmetric multimodal distribution.
                """)
        # creates a new figure for plotting
        fig1, ax1 = plt.subplots()
        # creates a histogram with kde curve, drawn on specified axes
        sns.histplot(chosen_df[col_to_plot], kde=True, ax=ax1, color="#007eba")
        # displays the plotted figure
        st.pyplot(fig1, use_container_width=True)

        st.markdown("##### Boxplot")
        # creates a new figure for plotting
        fig2, ax2 = plt.subplots()
        # creates a boxplot wit wine type on the x-axis and the chosen feature (column) on y-axis
        # choose a predefined color palette 
        sns.boxplot(data=chosen_df, x="wine_type", y=col_to_plot, color="#68ab7d")
        # displays the plotted figure
        st.pyplot(fig2, use_container_width=True)
    with tab2:
        ## 2D Plot
        st.subheader("2D Scatter Plot")
        st.write("This 2D scatter plot visualizes the relationship between two selected variables, colored by the quality of the wine.")
        # creates dropdown to be able to select a specific feature (column) on the x-axis
        # removed the last two columns quality and wine type
        col1 = st.selectbox("X-axis:", chosen_df.columns[:-2], index=0)
        # creates dropdown to be able to select a specific feature (column) on the y-axis
        # removed the last two columns quality and wine type
        col2 = st.selectbox("Y-axis:", chosen_df.columns[:-2], index=1)
        # creates a scatter plot figure for chosen features on x- and y-axis
        fig3 = px.scatter(chosen_df, x=col1, y=col2, color="quality", title=f"{col1} vs {col2} (colored by quality)", color_continuous_scale="Plasma")
        # displays the plotted figure
        st.plotly_chart(fig3, use_container_width=True)
    with tab3:
        ## 3D Plot
        st.subheader("3D Scatter Plot")
        st.write("This 3D scatter plot allows you to visually analyze patterns and clusters across multiple variables, helping to identify which features might influence quality the most.")
        # creates dropdown menus for selecting columns for the x-,y- and z-axis
        x_3d = st.selectbox("3D X-axis:", chosen_df.columns[:-2], key="x3d")
        y_3d = st.selectbox("3D Y-axis:", chosen_df.columns[:-2], key="y3d")
        z_3d = st.selectbox("3D Z-axis:", chosen_df.columns[:-2], key="z3d")
        # creates a 3D scatter plot figure mapped to the above selection
        fig4 = px.scatter_3d(chosen_df, x=x_3d, y=y_3d, z=z_3d, color="quality", title="3D Feature Scatter", color_continuous_scale="Viridis")
        # displays the plotted figure
        st.plotly_chart(fig4, use_container_width=True)

    # Correlation Heatmap
    if st.checkbox("Show Correlation Heatmap"):
        st.subheader("Correlation Heatmap")
        if dataset_choice == "Red Wine":
            st.write("""
                The correlation heatmap for the red wine dataset reveals how different chemical properties relate to wine quality. 
                Notably, alcohol content shows a moderate positive correlation with quality, suggesting that higher alcohol levels may be associated with better-rated red wines. 
                Conversely, volatile acidity and density exhibit negative correlations with quality, implying that higher levels of these characteristics may be linked to lower quality. 
                Overall, the heatmap helps identify which variables might play a more influential role in determining red wine quality, providing a foundation for deeper statistical or predictive modeling.
                """)
        elif dataset_choice == "White Wine":
            st.write("""
                In the white wine dataset, the heatmap similarly highlights key relationships. 
                Alcohol again shows a relatively strong positive correlation with quality, indicating consistency across wine types. 
                Density and residual sugar tend to correlate negatively or very weakly with quality, suggesting they may not positively influence perceived quality. 
                Interestingly, white wine tends to show slightly different correlation strengths compared to red wine, which may reflect differences in production or chemical profiles. 
                These insights guide feature selection for modeling wine quality.
                """)
        else:
            st.write("""
                When both red and white wine data are combined, the heatmap provides an overview of general patterns across all wine types. 
                While alcohol remains a key feature positively correlated with quality, the correlations of other variables are somewhat diluted due to differences between red and white wine profiles.
                """)
            chosen_df['wine_type_white'] = chosen_df['wine_type'].map({'red': 0, 'white': 1})

        # Select only numeric columns
        numeric_df = chosen_df.select_dtypes(include=['number'])
        corr = numeric_df.corr()
        fig5, ax5 = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax5)
        st.pyplot(fig5)

# Another page for wine quality info
if page == "Wine Quality Info":
    ## Title
    st.title(" What Affects Wine Quality?",)

    st.write("""
        Wine quality is influenced by a combination of factors that go beyond just chemical measurements. These include:

        - **Terroir**: The unique combination of soil, climate, and topography of a vineyard. Terroir significantly impacts the flavor and aroma of the wine. For example, wines from cooler climates tend to have higher acidity and lighter body, while those from warmer regions are fuller-bodied and fruit-forward. [Source: Wikifarmer](https://wikifarmer.com/en/factors-influencing-wine-characteristics/)

        - **Grape Variety**: Different grape varieties have distinct flavor profiles. For instance, Cabernet Sauvignon is known for its bold flavors, while Chardonnay offers a more subtle taste. [Source: Wikifarmer](https://wikifarmer.com/en/factors-influencing-wine-characteristics/)

        - **Winemaking Techniques**: Methods such as fermentation, maceration, and aging processes influence the final taste of the wine. Techniques like cold soaking can result in wines with softer, more rounded tannins. [Source: Vinfolio Blog](https://blog.vinfolio.com/2018/09/14/factors-affecting-wine-quality-how-winemaking-techniques-influence-a-vintage/)

        - **Climate and Weather**: The climate of the vineyard location affects grape ripening and flavor development. Regions with consistent sunlight and moderate temperatures often produce high-quality wines. [Source: Château Berne](https://chateauberne-vin.com/en-ch/blogs/news/facteurs-influencent-qualite-vin)

        Understanding these factors can help you appreciate the complexities behind each bottle of wine.
    """)

     ## Organize sections in tabs
    tab1, tab2 = st.tabs(["Educational Videos", "Articles"])
    with tab1:
        st.subheader("A Beginner's Guide To Wine")
        st.video("https://www.youtube.com/watch?v=SYQk0wj0hE0")

        st.subheader("Every Wine Explained")
        st.video("https://www.youtube.com/watch?v=dY_zzPxBxFA")
    with tab2:
        st.subheader("Learn More About Wine Quality")
        st.markdown("""
        Here are some useful articles and resources to learn more about what affects wine quality:

        - [Factors Influencing Wine Characteristics (Wikifarmer)](https://wikifarmer.com/en/factors-influencing-wine-characteristics/)
        - [Wine Quality and Winemaking Techniques (Vinfolio)](https://blog.vinfolio.com/2018/09/14/factors-affecting-wine-quality-how-winemaking-techniques-influence-a-vintage/)
        - [The Science Behind Great Wine (Wine Folly)](https://winefolly.com/deep-dive/the-science-behind-great-wine/)
        - [Terroir (Wikipedia)](https://en.wikipedia.org/wiki/Terroir)
        - [Unveiling the Secrets to Wine Quality: Key Factors and Their Effects (Bm wineguide)](https://bmwineguide.co.uk/unveiling-the-secrets-to-wine-quality-key-factors-and-their-effects/)
        - [Global warming and wine quality: are we close to the tipping point? (Oeno one)](https://oeno-one.eu/article/view/4774)
    
        """)

