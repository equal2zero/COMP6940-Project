import pandas as pd
import numpy as np
#import folium
#from folium import plugins
#import rioxarray as rxr
#import earthpy as et
#import earthpy.spatial as es
from tkinter import *
import tkintermapview

root = Tk()
root.geometry("900x700")

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)
map_widget.pack()

df = pd.read_csv("tnt2021.csv")

# Create a column with lat and long tuple
df["lat_long"] = list(zip(df.latitude, df.longitude))

#Trinidad
map_widget.set_position(10.42, -61.22)

map_widget.set_zoom(10)
lat = list(df["latitude"])
long = list(df["longitude"])

for la, lo in zip(lat, long):
    map_widget.set_marker(la,lo)

    #fires.add_child(folium.Marker(location = location, popup = str("fire"),icon=folium.Icon(color="red")))

root.title("2021 Fires in Trinidad")

root.mainloop()




