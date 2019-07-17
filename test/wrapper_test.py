import operator
import re

import tmdbsimple as tmdb
tmdb.API_KEY = '4e451d47079417d82742022a3cf54988'
'''

'''

actor_name = 'Johnny Depp'
genre_name = 'western'
#actor_name = 'Ponas Agurkas'
#movie_name = 'Gladiator'

search = tmdb.Search()
response = search.person(query=actor_name)

#if len(search.results)
#print(len(search.results))

actor_id = search.results[0]['id']
person = tmdb.People(actor_id)
response = person.info()

if len(search.results) > 0:
    actor_id = search.results[0]['id']
    person = tmdb.People(actor_id)
    response = person.info()
    #biography = person.biography.split('\n\n')
    biography = re.split(r'(?<=\.) ', person.biography)
    #print(biography[0])
    
    response = "Birthday - " + person.birthday + "\n" \
    + "Place of birth - " + person.place_of_birth + "\n" \
    + "Biography - " + biography[0] + " " + biography[1] + " " + biography[2]
else:
    response = "Sorry, found no information. Check spelling."
    
print(response)

'''
movieResultArray = []
movieResultFormatted = ""
i = 0

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
    response = "Sorry, found no information. Check spelling."

print(response)

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
    {}, {}.""".format(movie_genre,
    discover.results[0]['title'], discover.results[0]['release_date'],
    discover.results[1]['title'], discover.results[1]['release_date'],
    discover.results[2]['title'], discover.results[2]['release_date'])
else:
    response = "Sorry, found no information. Check spelling."
    '''