from tkinter import *

import tkintermapview


cinemainc:list=[]
cinema:list=[]
client:list=[]
worker:list=[]
temporary:list=[]
temporary2:list=[]
temporary3:list=[]

#pracownicy kina, użytkownicy kina, kina sieci
class workers():
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
         import requests
         from bs4 import BeautifulSoup
         url = f"https://pl.wikipedia.org/wiki/{self.location}"
         response = requests.get(url).text
         response_html = BeautifulSoup(response, "html.parser")
         longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
         latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
         print(longitude)
         print(latitude)
         return [latitude, longitude]

#sieci kin
class cinemas:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]



def add_cinemainc():
    nazwa = entry_name.get()
    cinemainc.append(nazwa)

    entry_name.delete(0, END)
    entry_location2.delete(0, END)
    entry_location.delete(0, END)

    entry_name.focus()

    show_cinemainc()

def show_cinemainc():
    listbox_lista_sieci.delete(0,END)
    for idx,user in enumerate(cinemainc):
        listbox_lista_sieci.insert(idx,f'{idx+1}. {user}')


def remove_cinemainc():
    i=listbox_lista_sieci.index(ACTIVE)
    cinemainc.pop(i)
    show_cinemainc()

def edit_cinemainc():
    i=listbox_lista_sieci.index(ACTIVE)
    name=cinemainc[i]

    entry_name.insert(0,name)

    button_dodaj_siec.config(text='zapisz',command=lambda: update_cinemainc(i))

def update_cinemainc(i):
    new_name=entry_name.get()

    cinemainc[i]=new_name


    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_siec.config(text='Dodaj obiekt',command=add_cinema)
    show_cinemainc()

def show_cinemain_details():


    i=listbox_lista_sieci.index(ACTIVE)
    n=cinemainc[i]


    for idx,kino in enumerate(cinema):
        if n!=cinema[idx].location2:
            cinema[idx].marker.delete()
            cinema.pop(idx)
            temporary.append(kino)

    for idx,val in enumerate(client):
        client[idx].marker.delete()

    for idx,val in enumerate(worker):
        worker[idx].marker.delete()

    listbox_lista_client.delete(0, END)
    listbox_lista_obiektow_worker.delete(0, END)
    show_cinema()








def add_cinema():
    name=entry_name.get()
    loc=entry_location.get()
    inc=entry_location2.get()

    user= workers(name=name, location=loc, location2=inc)
    cinema.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_cinema()




def show_cinema():
    listbox_lista_obiketow.delete(0,END)
    for idx,user in enumerate(cinema):
        listbox_lista_obiketow.insert(idx,f'{idx+1}. {user.name}')


def remove_cinema():
    i=listbox_lista_obiketow.index(ACTIVE)
    cinema[i].marker.delete()
    cinema.pop(i)
    show_cinema()

def edit_cinema():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=cinema[i].name
    location=cinema[i].location
    loc2=cinema[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,loc2)

    button_dodaj_placowke.config(text='zapisz',command=lambda: update_cinema(i))

def update_cinema(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_inc=entry_location2.get()

    cinema[i].name=new_name
    cinema[i].location=new_location
    cinema[i].location2=new_inc

    cinema[i].marker.delete()
    cinema[i].coordinates=cinema[i].get_coordinates()
    cinema[i].marker=map_widget.set_marker(cinema[i].coordinates[0],cinema[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_placowke.config(text='Dodaj obiekt',command=add_cinema)
    show_cinema()


def show_cinema_workers():


    i=listbox_lista_obiketow.index(ACTIVE)
    name=cinema[i].name
    location=cinema[i].location
    inc=cinema[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=inc)
    create_workers()

    map_widget.set_position(cinema[i].coordinates[0],cinema[i].coordinates[1])
    map_widget.set_zoom(10)

def show_cinema_clients():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=cinema[i].name
    location=cinema[i].location
    inc=cinema[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=inc)
    create_clients()

    map_widget.set_position(cinema[i].coordinates[0],cinema[i].coordinates[1])
    map_widget.set_zoom(10)






def add_client():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_pochodzenie=entry_location2.get()
    user= workers(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_pochodzenie)
    client.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_client()




def show_client():
    listbox_lista_client.delete(0,END)
    for idx,user in enumerate(client):
        listbox_lista_client.insert(idx,f'{idx+1}. {user.name}')

def remove_client():
    i=listbox_lista_client.index(ACTIVE)
    client[i].marker.delete()
    client.pop(i)
    show_client()

def edit_client():
    i=listbox_lista_client.index(ACTIVE)
    name=client[i].name
    location=client[i].location
    location2=client[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_client.config(text='Zapisz',command=lambda: update_client(i))

def update_client(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    client[i].name=new_name
    client[i].location=new_location
    client[i].location2=new_location2

    client[i].marker.delete()
    client[i].coordinates=client[i].get_coordinates()
    client[i].marker=map_widget.set_marker(client[i].coordinates[0],client[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_client.config(text='Dodaj obiekt',command=add_client)
    show_client()


def show_client_details():
    i=listbox_lista_client.index(ACTIVE)
    name=client[i].name
    location=client[i].location
    location2=client[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(client[i].coordinates[0],client[i].coordinates[1])
    map_widget.set_zoom(17)





def add_worker():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_pochodzenie=entry_location2.get()
    user= workers(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_pochodzenie)
    worker.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_worker()




def show_worker():
    listbox_lista_obiektow_worker.delete(0,END)
    for idx,user in enumerate(worker):
        listbox_lista_obiektow_worker.insert(idx,f'{idx+1}. {user.name}')


def remove_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    worker[i].marker.delete()
    worker.pop(i)
    show_worker()

def edit_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_worker.config(text='zapisz',command=lambda: update_worker(i))

def update_worker(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    worker[i].name=new_name
    worker[i].location=new_location
    worker[i].location2=new_location2

    worker[i].marker.delete()
    worker[i].coordinates=worker[i].get_coordinates()
    worker[i].marker=map_widget.set_marker(worker[i].coordinates[0],worker[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_worker.config(text='Dodaj obiekt',command=add_worker)
    show_cinema()


def show_worker_details():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(worker[i].coordinates[0],worker[i].coordinates[1])
    map_widget.set_zoom(17)



def create_clients():


    for idx,val in enumerate(worker):
        worker[idx].marker.delete()

    u=listbox_lista_obiketow.index(ACTIVE)
    d=cinema[u].name

    for idx,val in enumerate(client):
        client[idx].marker.delete()

        if client[idx].location2!=d:
            client.pop(idx)
            temporary2.append(val)


        else:
            client[idx].coordinates = client[idx].get_coordinates()
            client[idx].marker = map_widget.set_marker(client[idx].coordinates[0], client[idx].coordinates[1])

    show_client_temp()

def show_client_temp():
    listbox_lista_client.delete(0,END)
    listbox_lista_obiektow_worker.delete(0,END)
    for idx,val in enumerate(client):
        listbox_lista_client.insert(idx,f'{idx+1}.{val.name}')




def create_workers():

    for idx,val in enumerate(client):
        client[idx].marker.delete()

    u=listbox_lista_obiketow.index(ACTIVE)
    d=cinema[u].name

    for idx,val in enumerate(worker):

        worker[idx].marker.delete()

        if worker[idx].location2!=d:
            worker.pop(idx)
            temporary3.append(val)

        else :
            worker[idx].coordinates = worker[idx].get_coordinates()
            worker[idx].marker = map_widget.set_marker(worker[idx].coordinates[0], worker[idx].coordinates[1])

    show_worker_temp()


def show_worker_temp():
    listbox_lista_client.delete(0, END)
    listbox_lista_obiektow_worker.delete(0, END)
    for idx, val in enumerate(worker):
        listbox_lista_obiektow_worker.insert(idx, f'{idx + 1}.{val.name}')




def restore():

    for idx, val in enumerate(temporary):
        val=temporary[idx]
        cinema.append(val)

    for idx, val in enumerate(temporary2):
        val=temporary2[idx]
        client.append(val)

    for idx, val in enumerate(temporary3):
        val=temporary3[idx]
        worker.append(val)

    show_cinema()
    show_client()
    show_worker()

    for idx,val in enumerate(cinema):
        cinema[idx].marker.delete()
        cinema[idx].coordinates=cinema[idx].get_coordinates()
        cinema[idx].marker=map_widget.set_marker(cinema[idx].coordinates[0],cinema[idx].coordinates[1])

    for idx,val in enumerate(client):
        client[idx].marker.delete()
        client[idx].coordinates=client[idx].get_coordinates()
        client[idx].marker=map_widget.set_marker(client[idx].coordinates[0],client[idx].coordinates[1])

    for idx,val in enumerate(worker):
        worker[idx].marker.delete()
        worker[idx].coordinates=worker[idx].get_coordinates()
        worker[idx].marker=map_widget.set_marker(worker[idx].coordinates[0],worker[idx].coordinates[1])

    temporary.clear()
    temporary2.clear()
    temporary3.clear()





root = Tk()
root.geometry("1400x760")
root.title("Project POP AC")


ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0,columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_obiektow
#sieci kin
label_lista_sieci=Label(ramka_lista_obiektow, text="Lista sieci kin")
label_lista_sieci.grid(row=0, column=0,columnspan=2)
listbox_lista_sieci=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_sieci.grid(row=1, column=0, columnspan=3)
button_szczegoly_sieci=Button(ramka_lista_obiektow, text='Pokaż kina', command=show_cinemain_details)
button_szczegoly_sieci.grid(row=2, column=0)
button_usun_siec=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_cinemainc)
button_usun_siec.grid(row=2, column=1)
button_edytuj_siec=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_cinemainc)
button_edytuj_siec.grid(row=2, column=2)

#kina
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista kin")
label_lista_obiektow.grid(row=0, column=3,columnspan=2)
listbox_lista_obiketow=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiketow.grid(row=1, column=3, columnspan=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż klientów', command=show_cinema_clients)
button_pokaz_szczegoly_obiektu.grid(row=2, column=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż pracowników', command=show_cinema_workers)
button_pokaz_szczegoly_obiektu.grid(row=3, column=3)
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_cinema)
button_usun_obiekt.grid(row=2, column=4)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_cinema)
button_edytuj_obiekt.grid(row=2, column=5)

#klienci
label_lista_obiektow_client=Label(ramka_lista_obiektow, text="Lista klientów")
label_lista_obiektow_client.grid(row=0, column=6,columnspan=2)
listbox_lista_client=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_client.grid(row=1, column=6, columnspan=3)
button_pokaz_szczegoly_obiektu_client=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_client_details)
button_pokaz_szczegoly_obiektu_client.grid(row=2, column=6)
button_usun_obiekt_client=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_client)
button_usun_obiekt_client.grid(row=2, column=7)
button_edytuj_obiekt_client=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_client)
button_edytuj_obiekt_client.grid(row=2, column=8)

#pracownicy
label_lista_obiektow_worker=Label(ramka_lista_obiektow, text="Lista pracowników")
label_lista_obiektow_worker.grid(row=0, column=9,columnspan=2)
listbox_lista_obiektow_worker=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_worker.grid(row=1, column=9, columnspan=3)
button_pokaz_szczegoly_obiektu_worker=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_worker_details)
button_pokaz_szczegoly_obiektu_worker.grid(row=2, column=9)
button_usun_obiekt_worker=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_worker)
button_usun_obiekt_worker.grid(row=2, column=10)
button_edytuj_obiekt_worker=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_worker)
button_edytuj_obiekt_worker.grid(row=2, column=11)

# ramka_formularz
label_formularz=Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name=Label(ramka_formularz, text="Nazwa:")
label_name.grid(row=1, column=0, sticky=W)
label_location=Label(ramka_formularz, text="Miejscowość:")
label_location.grid(row=2, column=0,sticky=W)
label_location2=Label(ramka_formularz, text="Przypisanie:")
label_location2.grid(row=3, column=0,sticky=W)

entry_name=Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_location=Entry(ramka_formularz)
entry_location.grid(row=2, column=1)
entry_location2=Entry(ramka_formularz)
entry_location2.grid(row=3, column=1)


button_dodaj_siec=Button(ramka_formularz,text="Dodaj sieć", command=add_cinemainc)
button_dodaj_siec.grid(row=5, column=0, columnspan=2)

button_dodaj_placowke=Button(ramka_formularz, text='Dodaj placówkę',command=add_cinema)
button_dodaj_placowke.grid(row=6, column=0, columnspan=2)

button_dodaj_client=Button(ramka_formularz, text='Dodaj klienta',command=add_client)
button_dodaj_client.grid(row=7, column=0, columnspan=2)

button_dodaj_worker=Button(ramka_formularz, text='Dodaj pracownika',command=add_worker)
button_dodaj_worker.grid(row=8, column=0, columnspan=2)

button_odswiez=Button(ramka_formularz,text='Odśwież listę',command=restore)
button_odswiez.grid(row=9, column=0, columnspan=2)

# ramka_szczegoly_obiektow
label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="Szczegoly obiektu:")
label_szczegoly_obiektow.grid(row=1, column=0)
label_szczegoly_name=Label(ramka_szczegoly_obiektow, text="Nazwa:")
label_szczegoly_name.grid(row=1, column=1)
label_szczegoly_name_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_name_wartosc.grid(row=1, column=2)
label_szczegoly_location=Label(ramka_szczegoly_obiektow, text="Miejscowość:")
label_szczegoly_location.grid(row=1, column=3)
label_szczegoly_location_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location_wartosc.grid(row=1, column=4)
label_szczegoly_location2=Label(ramka_szczegoly_obiektow, text="Przypisanie:")
label_szczegoly_location2.grid(row=1, column=5)
label_szczegoly_location2_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location2_wartosc.grid(row=1, column=6)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)



root.mainloop()