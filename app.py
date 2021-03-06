import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
from folium.plugins import BeautifyIcon

# set app layout
st.set_page_config(layout = 'wide')

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

hide_streamlit_style = """
<style>
.css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 0rem;
                }
</style>
"""
st.markdown(hide_streamlit_style,  unsafe_allow_html=True)
title= '8. Tübinger Kulturnacht, 7. Mai 2022'
st.header(title)
st.write("[kulturnacht-tuebingen.de](https://www.kulturnacht-tuebingen.de/)")

# read data
data = pd.read_csv('Data/orts.csv',encoding='cp1252')

#create map
m = folium.Map(location=[48.51982477582212, 9.05509538690078], zoom_start=15)
tooltip = "Klicken Sie hier für Informationen"
iframe_start = folium.IFrame("""<b>18:00 Marktplatz</b><br> Startschuss  der Kulturnacht
<br><a href=https://www.kulturnacht-tuebingen.de/partys/location/location_id/8349 target="_blank">siehe Veranstaltungen</a>""")
popup_start = folium.Popup(iframe_start, min_width=200, max_width=200, min_height=130, max_height=130)


for i in range(len(data)):
    location = [data['Latitude'][i], data['Longitude'][i]]
    # set starting location
    if data['Ort'][i] == 'Marktplatz Tübingen':
        icon_start = BeautifyIcon(icon='map-pin',
                             inner_icon_style='color:#ff7442;font-size:25px;', 
                             background_color='transparent',border_color='transparent')
        marker = folium.Marker(
        location=location,
        icon = icon_start, 
        popup = popup_start,tooltip=tooltip).add_to(m)
    # set other locations
    else:
        iframe_reg = folium.IFrame("""<b>{}</b><br> <a href={} target="_blank">siehe Veranstaltungen</a>""".format(data['Ort'][i], data['Link'][i]))
        popup_reg = folium.Popup(iframe_reg, min_width=190, max_width=190, min_height=130, max_height=130)
        # star marker
        icon_star = BeautifyIcon(icon='map-pin',
                             inner_icon_style='color:#1bbbe9;font-size:25px;', 
                             background_color='transparent',border_color='transparent')
        marker = folium.Marker(
        location=location, icon=icon_star,
        popup = popup_reg, tooltip=tooltip).add_to(m)
        
folium.TileLayer('stamentoner').add_to(m)
#m.get_root().html.add_child(folium.Element(title_html))

folium_static(m,  width=1400, height=550)



