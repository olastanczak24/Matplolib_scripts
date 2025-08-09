import matplotlib.pyplot as plt

CTA = ("Catania (CTA)", -2.2, 0.0)
NAP = ("Napoli",        2.0, 0.0)

fig, ax = plt.subplots(figsize=(10, 6))

# Punkty
ax.scatter([CTA[1], NAP[1]], [CTA[2], NAP[2]], s=[200, 180])

# Etykiety
ax.text(CTA[1], CTA[2] + 0.18, CTA[0], ha="center")
ax.text(NAP[1], NAP[2] + 0.16, NAP[0], ha="center")

# Ustawienia osi
ax.set_aspect("equal")
ax.set_xlim(-4.2, 3.4)
ax.set_ylim(-2.2, 2.2)
ax.axis("off")

plt.show()

