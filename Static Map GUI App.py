import requests
import json
import os
import urllib.request
import webbrowser
from PIL import ImageTk,Image
import random
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import *
import sys
from tkinter import messagebox


class App:
    def __init__(self):
        self.root = ThemedTk()
        self.root.title("Static Map App")
        self.WIDTH = 1600
        self.HEIGHT = 600
        self.size = 600
        self.root.geometry("1400x800")
        self.root.resizable(0, 0)
        ttk.Style().theme_use("black")
        ttk.Style().configure("TButton", font="OpenSans 13 bold", anchor="center", background="#47d1ff", foreground="white")
        ttk.Style().configure("TLabel")
        ttk.Style().configure("TEntry")
        ttk.Style().configure("TFrame", relief="ridge")
        self.frames()
        self.labels()
        self.entrys()
        self.buttons()
        self.mainloop()

    def frames(self):
        self.window_frame = ttk.Frame(self.root)
        self.window_frame.place(relheight=1, relwidth=1)
        self.info_frame = ttk.Frame(self.root)
        self.info_frame.place(relx=0.015, rely=0.025, relheight=0.95, relwidth=0.3)
        self.picture_frame = ttk.Frame(self.root)
        self.picture_frame.place(relx=0.4, rely=0.025, relheight=0.95, relwidth=0.583)

    def labels(self):
        self.key_label = ttk.Label(self.info_frame, text="API-Key :", font="OpenSans 13 bold")
        self.key_label.place(relx=0.01, rely=0.1)
        self.location_label = ttk.Label(self.info_frame, text="Location :", font="OpenSans 13 bold")
        self.location_label.place(relx=0.01, rely=0.17)
        self.zoom_label = ttk.Label(self.info_frame, text="Zoom Level of the Map :", font="OpenSans 13 bold")
        self.zoom_label.place(relx=0.01, rely=0.24)
        self.type_label = ttk.Label(self.info_frame, text="Type of base map :", font="OpenSans 13 bold")
        self.type_label.place(relx=0.01, rely=0.31)
        self.scale_label = ttk.Label(self.info_frame, text="Scalebar :", font="OpenSans 13 bold")
        self.scale_label.place(relx=0.01, rely=0.38)
        self.title_label = ttk.Label(self.info_frame, text="Static Map Search", font="OpenSans 15 bold", background="#47d1ff", relief="ridge", anchor="center")
        self.title_label.place(relx=0.01, rely=0.01, relheight=0.05, relwidth=0.97)

        self.location_pic_title = ttk.Label(self.picture_frame, text="Static Picture", font="OpenSans 15 bold", background="#47d1ff", relief="ridge", anchor="center")
        self.location_pic_title.place(relx=0.01, rely=0.01, relheight=0.05, relwidth=0.98)
        self.picture_label = ttk.Label(self.picture_frame, relief="ridge")
        self.picture_label.place(relx=0.01, rely=0.067, relheight=0.92, relwidth=0.98)

        self.title2_label = ttk.Label(self.info_frame, text="Static Route Search", font="OpenSans 15 bold", background="#47d1ff", relief="ridge", anchor="center")
        self.title2_label.place(relx=0.01, rely=0.45, relheight=0.05, relwidth=0.97)
        self.key2_label = ttk.Label(self.info_frame, text="API-Key :", font="OpenSans 13 bold")
        self.key2_label.place(relx=0.01, rely=0.54)
        self.location2_label = ttk.Label(self.info_frame, text="Start Location :", font="OpenSans 13 bold")
        self.location2_label.place(relx=0.01, rely=0.61)
        self.location3_label = ttk.Label(self.info_frame, text="End Location :", font="OpenSans 13 bold")
        self.location3_label.place(relx=0.01, rely=0.68)
        self.zoom2_label = ttk.Label(self.info_frame, text="Zoom Level of the Map :", font="OpenSans 13 bold")
        self.zoom2_label.place(relx=0.01, rely=0.75)
        self.type2_label = ttk.Label(self.info_frame, text="Type of base map :", font="OpenSans 13 bold")
        self.type2_label.place(relx=0.01, rely=0.82)
        self.scale2_label = ttk.Label(self.info_frame, text="Scalebar :", font="OpenSans 13 bold")
        self.scale2_label.place(relx=0.01, rely=0.89)

    def entrys(self):
        self.key_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.key_entry.place(relx=0.2, rely=0.1, relwidth=0.78)
        self.location_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.location_entry.place(relx=0.21, rely=0.17, relwidth=0.767)
        self.zoom_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.zoom_entry.place(relx=0.47, rely=0.24, relwidth=0.505)
        self.type_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.type_entry.place(relx=0.38, rely=0.31, relwidth=0.6)
        self.scalebar_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.scalebar_entry.place(relx=0.21, rely=0.38, relwidth=0.767)

        self.key2_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.key2_entry.place(relx=0.2, rely=0.54, relwidth=0.78)
        self.location2_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.location2_entry.place(relx=0.317, rely=0.61, relwidth=0.66)
        self.location3_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.location3_entry.place(relx=0.297, rely=0.68, relwidth=0.68)
        self.zoom2_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.zoom2_entry.place(relx=0.47, rely=0.75, relwidth=0.505)
        self.type2_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.type2_entry.place(relx=0.38, rely=0.82, relwidth=0.6)
        self.scalebar2_entry = ttk.Entry(self.info_frame, font="OpenSans 10 bold")
        self.scalebar2_entry.place(relx=0.21, rely=0.89, relwidth=0.767)

    def buttons(self):
        self.get_data = ttk.Button(self.info_frame, text="Get Location", command= lambda: self.get_location())
        self.get_data.place(relx=0.14, rely=0.94, relheight=0.05, relwidth=0.7)
        self.information_button = ttk.Button(self.root, text="Info", command= lambda: self.show_info())
        self.information_button.place(relx=0.322, rely=0.025, relwidth=0.07, relheight=0.2)
        self.About_button = ttk.Button(self.root, text="About")
        self.About_button.place(relx=0.322, rely=0.395, relwidth=0.07, relheight=0.2)
        self.Exit_button = ttk.Button(self.root, text="Exit", command= lambda: self.root.destroy())
        self.Exit_button.place(relx=0.322, rely=0.774, relwidth=0.07, relheight=0.2)

    def get_location(self):
        try:
            self.key = self.key_entry.get()
            self.location = self.location_entry.get()
            self.scalebar = self.scalebar_entry.get()
            self.zoom = self.zoom_entry.get()
            self.type = self.type_entry.get()
            self.informations = (self.key, self.location, self.scalebar, self.zoom, self.type)
            self.url = "https://www.mapquestapi.com/staticmap/v5/map?key=%s&center=%s&scalebar=%s&zoom=%s&type=%s&size=796,700" % (self.informations)
            #webbrowser.open_new_tab('%s' % self.url)
            self.request = requests.get(self.url)
            with open("static_map_pic.png", "wb") as f:
                f.write(self.request.content)
            self.image = ImageTk.PhotoImage(file="static_map_pic.png")
            self.location_pic_title.configure(text="Static Map Picture")
            self.picture_label.configure(image=self.image)
        except:
            self.key2 = self.key2_entry.get()
            self.location2 = self.location2_entry.get()
            self.location3 = self.location3_entry.get()
            self.scalebar2 = self.scalebar2_entry.get()
            self.zoom2 = self.zoom2_entry.get()
            self.type2 = self.type2_entry.get()
            self.informations2 = (self.key2, self.location2, self.location3, self.scalebar2, self.zoom2, self.type2)
            self.url2 = "https://www.mapquestapi.com/staticmap/v5/map?key=%s&start=%s&end=%s&scalebar=%s&zoom=%s&type=%s&size=796,700" % (self.informations2)
            # webbrowser.open_new_tab('%s' % self.url)
            self.request2 = requests.get(self.url2)
            with open("static_route_pic.png", "wb") as f:
                f.write(self.request2.content)
            self.image2 = ImageTk.PhotoImage(file="static_route_pic.png")
            self.location_pic_title.configure(text="Static Route Picture")
            self.picture_label.configure(image=self.image2)

    def show_info(self):
        messagebox.showinfo("Search input Guide", "###Static Map Search###\n"
                                                  "API-Key = Key\n"
                                                  "Example: developer.mapquest.com\n"
                                                  "Location: = Location\n"
                                                  "Example: Berlin\n"
                                                  "Zoom Level of the Map: 0-20\n"
                                                  "Example: 15\n"
                                                  "Type of base map = map, sat, hyb, light and dark\n"
                                                  "Example: hyb\n"
                                                  "Scalebar = true or false\n"
                                                  "Example: true\n"
                                                  "\n"
                                                  "###Static Route Search###\n"
                                                  "API-Key = Key\n"
                                                  "Example: developer.mapquest.com\n"
                                                  "Start Location = Start Location\n"
                                                  "Example: Hamburg\n"
                                                  "End Location = End Location\n"
                                                  "Example: Berlin\n"
                                                  "Zoom Level of the Map = 0-20\n"
                                                  "Example: 13\n"
                                                  "Type of base map = map, sat, hyb, light and dark\n"
                                                  "Example : map\n"
                                                  "Scalebar = true or false\n"
                                                  "Example: false\n")

    def mainloop(self):
        self.root.mainloop()
App()