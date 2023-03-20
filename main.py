import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

df = pd.read_csv("star_with_gravity.csv")
df.head()

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()
star_name = df["Star_name"].to_list()

mass.sort()
radius.sort()
gravity.sort()
dist.sort()
star_name.sort()

#plt.plot(radius,gravity)

plt.bar(star_name,mass)
plt.title("Star name vs Mass")
plt.xlabel("Star_name")
plt.ylabel("Mass")
plt.show()

plt.bar(star_name, radius)
plt.title("Star name vs Radius.")
plt.ylabel("Star_name")
plt.xlabel("Radius")
plt.show()

plt.bar(star_name, dist)
plt.title("Star name vs Distance")
plt.ylabel("Star_name")
plt.xlabel("Distance")
plt.show()

plt.bar(star_name, gravity)
plt.title("Star name vs Gravity")
plt.xlabel("Star_name")
plt.ylabel("Mass")
plt.show()