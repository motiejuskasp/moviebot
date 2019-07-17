from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

import re
import tmdbsimple as tmdb
tmdb.API_KEY = '4e451d47079417d82742022a3cf54988'


class ActionActorInfo(Action):
    def name(self):
        return 'action_actorinfo'
    
    def run(self, dispatcher, tracker, domain):
        
        #actor from user text
        actor_name = tracker.get_slot('actor')
        if actor_name == '':
            response = "Sorry, found no actor name in that sentence. Try with different wording."
            dispatcher.utter_message(response)
            return [SlotSet('actor',actor_name)]
        
        search = tmdb.Search()
        response = search.person(query=actor_name)
        
        if len(search.results) > 0:
            actor_id = search.results[0]['id']
            person = tmdb.People(actor_id)
            response = person.info()
            biography = re.split(r'(?<=\.) ', person.biography)
            
            response = "Birthday - " + person.birthday + "\n" \
            + "Place of birth - " + person.place_of_birth + "\n" \
            + "Biography - " + biography[0] + " " + biography[1] + " " + biography[2]
        else:
            response = "Searched for actor " + actor_name + " but found no information. Check spelling and try again."
    
        dispatcher.utter_message(response)
        return [SlotSet('actor',actor_name)]


class ActionMovie(Action):
    def name(self):
        return 'action_movie'
    
    def run(self, dispatcher, tracker, domain):
        movieResultArray = []
        movieResultFormatted = ""
        i = 0
        
        #actor from user text
        actor_name = tracker.get_slot('actor')
        if actor_name == '':
            response = "Sorry, found no actor name in that sentence. Try with different wording."
            dispatcher.utter_message(response)
            return [SlotSet('actor',actor_name)]

        search = tmdb.Search()
        response = search.person(query=actor_name)

        if len(search.results) > 0:
            actor_id = search.results[0]['id']

            person = tmdb.People(actor_id)
            response = person.movie_credits()
            cast = person.cast

            cast.sort(key=lambda x: x["popularity"], reverse = True)

            while (i < 5) and (i < len(person.cast)):
                myString = "    " + person.cast[i]['title'] + " as " + person.cast[i]['character']
                movieResultArray.append(myString)
                i += 1

            for x in movieResultArray:
                movieResultFormatted += x + "\n"
                
                response = search.results[0]['name'] + " acts in movies:\n" + movieResultFormatted
        else:
            response = "Searched for movies with " + actor_name + " but found no information. Check spelling and try again."
    
        dispatcher.utter_message(response)
        return [SlotSet('actor',actor_name)]
    

class ActionMovieInfo(Action):
    def name(self):
        return 'action_movieinfo'
        
    def run(self, dispatcher, tracker, domain):
        genres = ""
        
        #movie from user text
        movie_name = tracker.get_slot('movie')
        if movie_name == '':
            response = "Sorry, found no movie name in that sentence. Try with different wording."
            dispatcher.utter_message(response)
            return [SlotSet('movie',movie_name)]
        
        search = tmdb.Search()
        response = search.movie(query=movie_name)
        
        if len(search.results) > 0:
            movie_id = search.results[0]['id']
        
            movie = tmdb.Movies(movie_id)
            response = movie.info()
        
            for x in range (0, len(movie.genres)):
                genres += " " + movie.genres[x]['name']

            response = """{} information:
            title - {}, release date - {},
            genres:{},
            runtime - {} minutes.""".format(movie.title, movie.title,
                                movie.release_date, genres, movie.runtime)
        else:
            response = "Searched for movie " + movie_name + " but found no information. Check spelling and try again."
        
        dispatcher.utter_message(response)
        return [SlotSet('movie',movie_name)]


class ActionGenreRating(Action):
    def name(self):
        return 'action_genrerating'
    
    def run(self, dispatcher, tracker, domain):
        
        #genre from user text
        genre_name = tracker.get_slot('genre')
        if genre_name == '':
            response = "Sorry, found no genre name in that sentence. Try with different wording."
            dispatcher.utter_message(response)
            return [SlotSet('genre',genre_name)]
        
        genre = tmdb.Genres()
        response = genre.movie_list()
        movie_id = 0
        movie_genre = ''
        
        for x in range (0, len(genre.genres)):
            if genre.genres[x]['name'].lower() == genre_name:
                movie_id = genre.genres[x]['id']
                movie_genre = genre.genres[x]['name']
        
        discover = tmdb.Discover()
        response = discover.movie(page=1, sort_by='popularity.desc',
                        include_adult=False, include_video=False, with_genres=movie_id)
        
        if len(discover.results) > 0:
            response = """Most popular {} movies:
            {}, {},
            {}, {},
            {}, {},
            {}, {},
            {}, {}.""".format(movie_genre,
            discover.results[0]['title'], discover.results[0]['release_date'],
            discover.results[1]['title'], discover.results[1]['release_date'],
            discover.results[2]['title'], discover.results[2]['release_date'],
            discover.results[3]['title'], discover.results[3]['release_date'],
            discover.results[4]['title'], discover.results[4]['release_date'])
        else:
            response = "Searched for genre " + genre_name + " movies but found no information. Check spelling and try again."
        
        dispatcher.utter_message(response)
        return [SlotSet('genre',genre_name)]