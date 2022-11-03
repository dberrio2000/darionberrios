from tkinter import *
import requests
import json

class Pokemon:

    def __init__(self, attack, name, pokedex_num, type_1, type_2 = "none"): #definition
        self.attack = attack
        self.name = name
        self.pokedex_num = pokedex_num
        self.type_1 = type_1
        self.type_2 = type_2

    def __str__(self): #str method to print pokemon object
        return "Attack: {}\nName: {}\nPokeDex Number: {}\nType 1: {}\nType 2: {}\n"\
               .format(self.attack, self.name, self.pokedex_num, self.type_1,\
                       self.type_2)
class PokeDex:
    
    def __init__(self):
        self.window = Tk()
        self.nameentry_label = Label(text = "Enter the name of the Pokemon.")
        self.nameentry_label.pack()
        self.nameentry = Entry()
        self.nameentry.pack()
        self.retrieve_button = Button(text = "Retrieve data")
        self.retrieve_button.bind("<Button-1>", self.clickhandler) #function is called when button is clicked
        self.retrieve_button.pack()
        self.results_label = Label(text = "Results: ") #come back and add code to
                                                      #display results.
        self.results_label.pack()

        self.window.mainloop()

    def clickhandler(self, e):
        user_input = self.nameentry.get()
        self.search(user_input) 
    
    def search(self, name):
        poke_request = requests.get("https://pokeapi.co/api/v2/pokemon/")
        poke_json = poke_request.text
        search_data = json.loads(poke_json)
        for i in search_data["results"]:
            if name.lower() == (i["name"]):
                print ("----------------")
                print ("Pokemon Found!")
                print ("----------------")
                self.results_label["text"] = "Results: " + i["name"]
                pokemon_page = requests.get(i["url"])
                stats_json = pokemon_page.text
                stats_data = json.loads(stats_json)
                for s in stats_data["stats"]:
                    if s["stat"]["name"] == "attack":
                        pokemon = Pokemon(attack = (s["base_stat"]),\
                                          name = stats_data["name"],\
                                          pokedex_num = stats_data["id"],\
                                          type_1 = stats_data["types"][0]\
                                          ["type"]["name"])
                        if len(stats_data["types"]) > 1:
                            pokemon.type_2 = stats_data["types"][1]\
                                             ["type"]["name"]
                        print (pokemon)
                        print ("----------------")
        
PokeDex()
