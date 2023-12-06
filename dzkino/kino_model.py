import os.path
import pickle


class Article:
    def __init__(self, namefilm, genre, director, year, duration, atelier, actors, rating, box_office):
        self.name_film = namefilm
        self.genre = genre
        self.director = director
        self.year_of_release = year
        self.duration = duration
        self.atelier = atelier
        self.the_actors = actors
        self.rating = rating
        self.box_office = box_office

    def __str__(self):
        return f"{self.name_film} ({self.genre})"


class ArticleModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.articles = self.load_data()

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.name_film] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название фильма": article.namefilm,
            "Жанр фильма": article.genre,
            "Режиссера": article.director,
            "Год выпуска": article.year,
            "Длительность": article.duration,
            "Студию": article.atelier,
            "Актера": article.actors,
            "Рейтинг": article.raiting,
            "Кассовый сбор": article.box_office
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.articles, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()
