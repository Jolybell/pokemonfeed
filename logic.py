from random import randint
import requests
import datetime
class Pokemon:
    pokemons = {}

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(50,80)
        self.strength = randint (1,30)
        self.manna = randint (10,50)
        self.last_feed_time = datetime.datetime.now() 
        Pokemon.pokemons[pokemon_trainer] = self
    
    

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            images=[]
            images.append(data['sprites']['back_default'])
            images.append(data['sprites']['back_shiny'])
            images.append(data['sprites']['front_shiny'])
            images.append(data['sprites']['front_default'])
            return images
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}, Хп твоего покемона: {self.hp}, Сила твоего покемона: {self.strength}, Манна твоего покемона: {self.manna}, Класс твоего покемона: Обычный" 
        

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    # Метод класса для атаки
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.datetime.now()  
        delta_time = datetime.timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"
        
    def attack(self,enemy):
        enemy.hp -= self.strength
        if enemy.hp <0:
        
            return f"{enemy.pokemon_trainer} проиграл, {self.pokemon_trainer} выиграл"
        else: 
            return f"{enemy.pokemon_trainer} имеет {enemy.hp} хп, {self.pokemon_trainer} имеет {self.hp} хп"
class Wizard(Pokemon):
    def info(self):
        return f"Имя твоего покеомона: {self.name}, Хп твоего покемона: {self.hp}, Сила твоего покемона: {self.strength}, Манна твоего покемона: {self.manna}, Класс твоего покемона: Маг" 
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.datetime.now()  
        delta_time = datetime.timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase + self.manna
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"
    pass
class Fighter(Pokemon):
    def info(self):
        return f"Имя твоего покеомона: {self.name}, Хп твоего покемона: {self.hp}, Сила твоего покемона: {self.strength}, Манна твоего покемона: {self.manna}, Класс твоего покемона: Боец" 
    def attack(self,enemy):
        enemy.hp -= self.strength*2
        if enemy.hp <0:
        
            return f"{enemy.pokemon_trainer} проиграл, {self.pokemon_trainer} выиграл"
        else: 
            return f"{enemy.pokemon_trainer} имеет {enemy.hp} хп, {self.pokemon_trainer} имеет {self.hp} хп"
    pass