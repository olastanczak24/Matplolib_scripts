import matplotlib.pyplot as plt

CTA = ("Catania (CTA)", -2.2, 0.0)
NAP = ("Napoli (NAP)", 2.0, 0.0)

def circle_points(cx, cy, r, n):
    pts = []
    n = max(1, n)
    for i in range(n):
        theta = 2 * math.pi * i / n
        pts.append((cx + r * math.cos(theta), cy + r * math.sin(theta)))
    return pts

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot([CTA[1], NAP[1]], [CTA[2], NAP[2]])

#names

plt.show()