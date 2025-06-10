from tkinter import*

import tkintermapview

users:list=[]

class User:
    def __init__(self,name,surname,location,post):
        self.name=name
        self.surname=surname
        self.location=location
        self.post=post
        self.coordination=self.get_coordinates()
        self.markermap_widget.set_marker(self.coordinates[0])


    def get_coordinates(self) ->list:
        import requests
        from bs4 import BeautifulSoup
        url * https
        response = requests.get(url).text
        response_html = BeautifulSoup(response,"html.parser")
