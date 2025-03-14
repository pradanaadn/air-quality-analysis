import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    layout="wide",
    page_title="Air Quality Analysis",
    page_icon="🌍",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Air Quality Analysis Dashboard"
    }
)

@st.cache_data
def load_markdown_description(md_file_path):
    """Load and return content from a markdown file"""
    try:
        with open(md_file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Description not available."
@st.cache_data
def load_plotly_html(html_file_path):
    with open(html_file_path, 'r') as f:
        html_content = f.read()
    
    components.html(html_content, height=800, width=1000)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown("<h1 style='text-align: center;'>Air Quality Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>by: Putu Gede Pradana Adnyana</h4>", unsafe_allow_html=True)
    
    
    plot_options = {
        "Correlation Matrix (Wind Direction)": {
            "plot": "dashboard/asset/correlation_matrix_wd.html",
            "description": "dashboard/asset/corelation_matrix_wd.md"
        },
        "Correlation Matrix (Season)": {
            "plot": "dashboard/asset/correlation_matrix_musim.html",
            "description": "dashboard/asset/correlation_matrix_musim.md"
        },
        "Air Quality PM2.5": {
            "plot": "dashboard/asset/air_quality_pm25_metric.html",
            "description": "dashboard/asset/air_quality_pm25.md"
        }
    }
    
    selected_plot = st.selectbox("Select a plot to display:", list(plot_options.keys()))
    
    st.markdown(f"### {selected_plot}")
    description = load_markdown_description(plot_options[selected_plot]["description"])
    st.markdown(description)
    if selected_plot == "Air Quality PM2.5":
        selected_metric = st.selectbox("Select a metric to display:", ['mean', 'median', 'min', 'max'])
        load_plotly_html(plot_options[selected_plot]["plot"].replace("metric", selected_metric))

    else:
        load_plotly_html(plot_options[selected_plot]["plot"])