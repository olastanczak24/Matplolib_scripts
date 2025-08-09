import geopandas as gpd
import matplotlib.pyplot as plt

URL = "zip+https://geodata.ucdavis.edu/gadm/gadm4.1/shp/gadm41_ITA_shp.zip"
LAYER = "gadm41_ITA_1" 
regions = gpd.read_file(URL, layer=LAYER)
sicily = regions[regions["NAME_1"].str.contains("Sicil", case=False, na=False)]

fig, ax = plt.subplots(figsize=(8, 8))

sicily.plot(ax=ax, color="darkblue")


fig.savefig("sicilia.png", dpi=300, bbox_inches='tight')