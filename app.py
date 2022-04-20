import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
from folium.plugins import BeautifyIcon

# set app layout
st.set_page_config(layout = 'wide')
title= '8. Tübinger Kulturnacht, 7. Mai 2022'
st.header(title)

# read data
data = pd.read_csv('Data/orts.csv',encoding='cp1252')



#create map
m = folium.Map(location=[48.520462436253766, 9.053572912482348], zoom_start=16)
tooltip = "Klicken Sie hier für Informationen"
iframe_start = folium.IFrame("""<b>18:00 Marktplatz</b><br> Startschuss  der 8. Tübinger Kulturnacht""")
popup_start = folium.Popup(iframe_start, min_width=300, max_width=300, min_height=75, max_height=75)


for i in range(len(data)):
    location = [data['Latitude'][i], data['Longitude'][i]]
    # set starting location
    if data['Ort'][i] == 'Marktplatz Tübingen':
        icon_start = BeautifyIcon(icon='circle',
                             inner_icon_style='color:#ff7442;font-size:25px;', 
                             background_color='transparent',border_color='transparent')
        marker = folium.Marker(
        location=location,
        icon = icon_start, 
        popup = popup_start,tooltip=tooltip).add_to(m)
    # set other locations
    else:
        iframe_reg = folium.IFrame("""<b>{}</b><br> <a href={} target="_blank">siehe Veranstaltungen</a>""".format(data['Ort'][i], data['Link'][i]))
        popup_reg = folium.Popup(iframe_reg, min_width=300, max_width=300, min_height=75, max_height=75)
        # star marker
        icon_star = BeautifyIcon(icon='star',
                             inner_icon_style='color:#fcff42;font-size:25px;', 
                             background_color='transparent',border_color='black')
        marker = folium.Marker(
        location=location, icon=icon_star,
        popup = popup_reg, tooltip=tooltip).add_to(m)
        
folium.TileLayer('stamentoner').add_to(m)
#m.get_root().html.add_child(folium.Element(title_html))

folium_static(m,  width=1300, height=600)
