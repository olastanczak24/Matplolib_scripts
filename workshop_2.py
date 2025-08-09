import geopandas as gpd
import matplotlib.pyplot as plt

# Pobierz granice Włoch z GADM 4.1 (poziom 1 = regiony)
URL = "zip+https://geodata.ucdavis.edu/gadm/gadm4.1/shp/gadm41_ITA_shp.zip"
LAYER = "gadm41_ITA_1"

regions = gpd.read_file(URL, layer=LAYER)

subset = regions[regions["NAME_1"].isin(["Sicilia", "Campania"])]

CTA = ("Catania (CTA)", 15.087, 37.502)
NAP = ("Napoli",        14.268, 40.851)

fig, ax = plt.subplots(figsize=(8, 8))

ax.set_facecolor("#cfe1f4")

regions.plot(ax=ax, facecolor="#f2f2f2", edgecolor="#cccccc", linewidth=0.5, zorder=0)

subset.plot(ax=ax, edgecolor="black")


for (name, lon, lat), size, dy in [(CTA, 200, 0.18), (NAP, 180, 0.18)]:
    ax.scatter(lon, lat, s=size, color="red")
    ax.text(lon, lat + dy, name, ha="center", va="bottom")

ax.set_aspect("equal")
ax.set_axis_off()
plt.title("Catania i Napoli na tle regionów")
plt.savefig("sicilia_napoli_geopandas.png", dpi=300, bbox_inches="tight")
plt.show()
