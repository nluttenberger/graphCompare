
import streamlit as st
import base64

# page
st.set_page_config(page_title="On comparing graphs")
st.set_page_config(layout="wide")


with st.container(width=1024, horizontal_alignment="left", vertical_alignment="top", gap="small"):
# title
    st.write("##### Norbert Luttenberger")
    st.write("<h3>Culinary Evolution:<br>A Graph-Based Method for Comparing Ingredient Compositions<br>in Historic and Modern Recipes. A case study.</h3>",
    unsafe_allow_html=True)
# intro text
    st.write("#### Intro")
    st.write("The culinary preferences of humans are subject to significant transformation over time. "\
             "These shifts are driven by various factors, including the availability of novel ingredients, " \
             "medical findings regarding food tolerability and healthy living, an increasing desire for " \
             "social distinction, the public presence of charismatic chefs or cookbook authors, " \
             "or mere fashion trends." \
    )       
    st.write("If we wish to gain a deeper understanding of how nutrition has evolved, " \
             "and if we assume that culinary preferences are reflected in the "\
             "popular cookbooks of their respective eras, " \
             "then a detailed comparison of these books is warranted. " \
             "The key question is: How can an entire cookbook be made \"visible\" for total comparison? " \
             "That is, how do we move beyond comparing selected recipes to analyzing entire volumes? " \
             "We opted for a graph-based model where recipes are represented as graphs." \
             "The nodes of the graph represent the recipes\'s ingredients, and the edges connect ingredients that appear together in a given recipe. " \
             "Built upon a foundation of well-established graph theory, graph-based models leverage numerous robust tools—encompassing both graph computation and graphical display—and offer straightforward interpretability."
    )
    st.write("This website focuses on detailing the design of this graph-based method and its necessary extensions to make it suitable for comparing different cookbooks—specifically, books from distinct historical periods. The accompanying case study serves a dual purpose: it both illustrates our methodological approach and provides initial insight into the culinary differences between two influential German cookbooks: \"*Kochbuch für die gewöhnliche und feinere Küche*\" by Henriette Davidis (1801–1876) and \"*Flavour: Mehr Gemüse, mehr Geschmack*\" by Yotam Ottolenghi (1968–)." \
    )
    st.write("We proceed as follows: ")

# concept
with st.container(width=1024, horizontal_alignment="left", vertical_alignment="top", gap="small"):
    st.write("#### Concept"
    )
    st.write("The conceptual ideas behind the method outlined here are outlined in the following."
    )
    st.write("###### Graph construction"
    )
    st.write("###### Editorial guidelines for recipes"
    )

# degree distribution
with st.container(width=1200, horizontal_alignment="left", vertical_alignment="top", gap="small"):
    st.image("degree distribution cumulative.svg")
    st.write("Fig. xx: *Degree distribution*")

# Davidis
with st.container(width=2400, horizontal_alignment="left", vertical_alignment="top", gap="small"):
    width_01 = st.slider("",1000,2400,1600, key="s01")
    st.image("HD_fullGraph.svg", width=width_01)
    st.write("Fig. xx: *Ingredient graph for Davidis recipes*")

# Ottolenghi
with st.container(width=2400, horizontal_alignment="left", vertical_alignment="top", gap="small"):
    width_02 = st.slider("",1000,2400,1600, key="s02")
    st.image("OL_fullGraph.svg", width=width_02)
    st.write("Fig. xx: *Ingredient graph for Ottolenghi recipes*")

# Davidis vegetables only 
#with st.container(width=2400, horizontal_alignment="left", vertical_alignment="top", gap="small"):
#    width_02 = st.slider("",1000,2400,1600, key="s02")
#    st.image("HD_Gemüse.svg", width=width_02)
#    st.write("Fig. xx: *Vegetables in the Davidis graph*")

# Davidis nutmeg
#with st.container(width=2400, horizontal_alignment="left", vertical_alignment="top", gap="small"):
#    width_03 = st.slider("",1000,2400,1600, key="s03")
#    st.image("HD_Muskat.svg", width=width_03)
#    st.write("Fig. xx: *Nutmeg in the Davidis graph*")

# Ottolenghi vegetables only
#with st.container(width=2400, horizontal_alignment="left", vertical_alignment="top", gap="small"):
#    width_02 = st.slider("",1000,2400,1600,key="s02")
#    st.image("Ottolenghi_Gemüse_only.svg", width=width_02)
#    st.write("Fig. xx: *Vegetables in the Ottolenghi graph*")