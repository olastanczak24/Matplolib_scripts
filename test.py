import folium

CTA = ("Catania", 37.5079, 15.0830)
NAP = ("Napoli", 40.8522, 14.2681)

m = folium.Map(
    location=(41.87, 12.56),
    zoom_start=6,
    tiles="OpenStreetMap"
)

folium.Marker(
    location=[CTA[1], CTA[2]],
    popup=CTA[0],
    tooltip=CTA[0],
    icon=folium.Icon(color="blue")
).add_to(m)

folium.Marker(
    location=[NAP[1], NAP[2]],
    popup=NAP[0],
    tooltip=NAP[0],
    icon=folium.Icon(color="green")
).add_to(m)

m.save("map.html")
