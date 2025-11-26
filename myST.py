
import streamlit as st
import streamlit.components.v1 as components
import xml.etree.ElementTree as ET

def parse_svg_width(root):
    w = root.get('width')
    if w:
        w = w.strip()
        if w.endswith('px'):
            w = w[:-2]
        # falls Prozent o.ä. vorkommt, geben wir None zurück
        try:
            return int(float(w))
        except Exception:
            return None
        
def parse_svg_height(root):
    h = root.get('height')
    if h:
        h = h.strip()
        if h.endswith('px'):
            h = h[:-2]
        # falls Prozent o.ä. vorkommt, geben wir None zurück
        try:
            return int(float(h))
        except Exception:
            return None


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
with st.container(width=768, horizontal_alignment="left", vertical_alignment="top", gap="small"):
    st.image("degree distribution cumulative.svg")
    st.write("Fig. xx: *Degree distribution*")

# Davidis
#with st.container(width=2400, horizontal_alignment="left", vertical_alignment="top", gap="small"):
    #width_01 = st.slider("",1000,2400,1600, key="s01")

# SVG-Datei einlesen
with open("USPresInaugAddr_0.16.svg", "r", encoding="utf-8") as f:
    svg_content = f.read()
# SVG parsen, um die Breite zu extrahieren
root = ET.fromstring(svg_content)
svg_width  = parse_svg_width(root)
svg_height = parse_svg_height(root)
# Anzeige anpassen
scale_factor = svg_width//1600 if svg_width > 1600 else 1
width_xx = st.slider("",1000,2400,1600, key="xx")
inner_inline = f"<div style=\"width: {width_xx}px; height: {width_xx}px; \"><div style=\"width: 100%; height: 100%; display: flex; justify-content: left; align-items: center;\">{svg_content}</div></div>"
components.html(inner_inline, height=width_xx, width=width_xx)
#st.write("Fig. xx: *Ingredient graph for Davidis recipes*")

# Ottolenghi
with st.container(width=2400, horizontal_alignment="left", vertical_alignment="top", gap="small"):
    width_02 = st.slider("",1000,2400,1600, key="s02")
    st.image("YO_fullGraph.svg", width=width_02)
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
#    st.image("YO_Gemüse_only.svg", width=width_02)
#    st.write("Fig. xx: *Vegetables in the Ottolenghi graph*")