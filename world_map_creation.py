from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv


lats, longs, places = [], [], []
# input desired coordinates
my_coords = [43.653225,-79.3832]

with open('raw_1AB_map - Sheet1.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')
    for data in reader:
        lats.append(float(data['Latitude']))
        longs.append(float(data['Longitude']))
        places.append(data['Place of Birth'])

# How much to zoom from coordinates (in degrees)
zoom_scale = 1

plt.figure(figsize=(12,6))


m = Basemap(projection='robin',lon_0=0,resolution='c')

m.drawcoastlines()
m.fillcontinents(color='lime',lake_color='aqua')

# draw parallels and meridians.
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,360.,60.))
m.drawmapboundary(fill_color='aqua')

x,y = m(longs,lats)
m.plot(x,y,'r*',markersize=8)

#provides title for map
plt.title("Birthplaces of BME Students")
plt.show()
