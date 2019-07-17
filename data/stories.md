## story 01
* greet 
    - utter_greet

## story 02
* goodbye
    - utter_goodbye

## story 03
* actor_info
    - utter_ask_actor

## story 04
* actor_info
    - action_actorinfo

## story 05
* movie_search
    - utter_ask_actor

## story 06
* movie_search
    - action_movie

## story 07
* movie_info
    - utter_ask_movie

## story 08
* movie_info
    - action_movieinfo
## story 09
* popular_search
    - utter_ask_genre

## story 10
* popular_search
    - action_genrerating
  
## Generated Story 2876300752515972473
* greet
    - utter_greet
* popular_search{"popularity": "good", "genre": "thriller", "query": "movies"}
    - slot{"popularity": "good"}
    - slot{"genre": "thriller"}
    - slot{"query": "movies"}
    - action_genrerating
    - slot{"genre": "thriller"}
* movie_search{"query": "movies", "actor": "alison lohman"}
    - slot{"query": "movies"}
    - slot{"actor": "alison lohman"}
    - action_movie
    - slot{"actor": "alison lohman"}
* goodbye
    - utter_goodbye
    
## Generated Story -2360037594823534688
* greet
    - utter_greet
* movie_info{"query": "movie", "movie": "iron man"}
    - slot{"query": "movie"}
    - slot{"movie": "iron man"}
    - action_movieinfo
    - slot{"movie": "iron man"}
* popular_search{"popularity": "good", "genre": "action", "query": "movies"}
    - slot{"popularity": "good"}
    - slot{"genre": "action"}
    - slot{"query": "movies"}
    - action_genrerating
    - slot{"genre": "action"}
* goodbye
    - utter_goodbye
    
## Generated Story -1941858590316812377
* greet
    - utter_greet
* movie_search{"query": "movies", "actor": "bryan adams"}
    - slot{"query": "movies"}
    - slot{"actor": "bryan adams"}
    - action_movie
    - slot{"actor": "bryan adams"}
* goodbye
    - export
    
## Generated Story -2441749379625186280
* greet
    - utter_greet
* movie_info{"query": "movie", "movie": "private ryan"}
    - slot{"query": "movie"}
    - slot{"movie": "private ryan"}
    - action_movieinfo
    - slot{"movie": "private ryan"}
* popular_search{"popularity": "other", "genre": "war", "query": "movies"}
    - slot{"popularity": "other"}
    - slot{"genre": "war"}
    - slot{"query": "movies"}
    - action_genrerating
    - slot{"genre": "war"}
* goodbye
    - utter_goodbye
    
## Generated Story -9176675997473606764
* greet
    - utter_greet
* movie_info{"query": "movie", "movie": "dunkirk"}
    - slot{"query": "movie"}
    - slot{"movie": "dunkirk"}
    - action_movieinfo
    - slot{"movie": "dunkirk"}
* movie_search{"query": "movies", "actor": "leonardo di"}
    - slot{"query": "movies"}
    - slot{"actor": "leonardo dicaprio"}
    - action_movie
    - slot{"actor": "leonardo dicaprio"}
    
## Generated Story -3632101943044679813
* greet
    - utter_greet
* movie_search{"query": "movies", "actor": "meryl streep"}
    - slot{"query": "movies"}
    - slot{"actor": "meryl streep"}
    - action_movie
    - slot{"actor": "meryl streep"}
* actor_info{"info": "information", "actor": "meryl streep"}
    - slot{"info": "information"}
    - slot{"actor": "meryl streep"}
    - action_actorinfo
    - slot{"actor": "meryl streep"}
* movie_info{"query": "movie", "actor": "the woods"}
    - slot{"query": "movie"}
    - slot{"actor": "the woods"}
    - action_movieinfo
* actor_info{"info": "about", "actor": "kate winslet"}
    - slot{"info": "about"}
    - slot{"actor": "kate winslet"}
    - action_actorinfo
    - slot{"actor": "kate winslet"}
* goodbye
    - utter_goodbye
    - export

## Generated Story -8732772903368922490
* actor_info{"info": "about", "actor": "johnny depp"}
    - slot{"info": "about"}
    - slot{"actor": "johnny depp"}
    - action_actorinfo
    - slot{"actor": "johnny depp"}
* movie_info{"query": "movie", "movie": "dunkirk"}
    - slot{"query": "movie"}
    - slot{"movie": "dunkirk"}
    - action_movieinfo
    - slot{"movie": "dunkirk"}
* popular_search{"popularity": "best", "genre": "war", "query": "movies"}
    - slot{"popularity": "best"}
    - slot{"genre": "war"}
    - slot{"query": "movies"}
    - action_genrerating
    - slot{"genre": "war"}
* movie_search{"query": "movies", "actor": "will smith"}
    - slot{"query": "movies"}
    - slot{"actor": "will smith"}
    - action_movie
    - slot{"actor": "will smith"}

## Generated Story 6000702663607661375
* actor_info{"info": "about", "actor": "jack nicholson"}
    - slot{"info": "know"}
    - slot{"info": "about"}
    - slot{"actor": "jack nicholson"}
    - action_actorinfo
    - slot{"actor": "jack nicholson"}
* movie_search{"query": "movies", "info": "know", "actor": "daniel day"}
    - slot{"query": "movies"}
    - slot{"info": "know"}
    - slot{"actor": "daniel day"}
    - action_movie
    - slot{"actor": "daniel day"}
    - export

## Generated Story -4790874590553800881
* greet
    - utter_greet
* actor_info{"query": "actor"}
    - slot{"query": "actor"}
    - utter_ask_actor
* actor_info{"actor": "will smith"}
    - slot{"actor": "will smith"}
    - action_actorinfo
    - slot{"actor": "will smith"}
* 
* movie_search{"query": "movies", "actor": "dustin hoffman"}
    - slot{"query": "movies"}
    - slot{"actor": "dustin hoffman"}
    - action_movie
    - slot{"actor": "dustin hoffman"}
* movie_info{"info": "information", "query": "movie", "movie": "the cobbler"}
    - slot{"info": "information"}
    - slot{"query": "movie"}
    - slot{"movie": "the cobbler"}
    - action_movieinfo
    - slot{"movie": "the cobbler"}
* popular_search{"genre": "drama", "query": "movies"}
    - slot{"genre": "drama"}
    - slot{"query": "movies"}
    - action_genrerating
    - slot{"genre": "drama"}

## Generated Story -3731420330238483984
* greet
    - utter_greet
* actor_info{"info": "information", "actor": "actor pomidoras"}
    - slot{"info": "information"}
    - slot{"actor": "actor pomidoras"}
    - action_actorinfo
    - slot{"actor": "actor pomidoras"}
* movie_info{"query": "movie", "movie": "matrix"}
    - slot{"query": "movie"}
    - slot{"movie": "matrix"}
    - action_movieinfo
    - slot{"movie": "matrix"}
* popular_search{"popularity": "best", "genre": "war", "query": "movies"}
    - slot{"popularity": "best"}
    - slot{"genre": "war"}
    - slot{"query": "movies"}
    - action_genrerating
    - slot{"genre": "war"}
* movie_info{"info": "know", "query": "movie", "movie": "overlord"}
    - slot{"info": "know"}
    - slot{"query": "movie"}
    - slot{"movie": "overlord"}
    - action_movieinfo
    - slot{"movie": "overlord"}

## Generated Story 288390243277691086
* greet
    - utter_greet
* actor_info{"info": "about", "actor": "actor harrison ford"}
    - slot{"info": "about"}
    - slot{"actor": "actor harrison ford"}
    - action_actorinfo
    - slot{"actor": "actor harrison ford"}
* actor_info{"info": "information", "actor": "harrison ford"}
    - slot{"info": "information"}
    - slot{"actor": "harrison ford"}
    - action_actorinfo
    - slot{"actor": "harrison ford"}
* 
* movie_search{"query": "movies", "actor": "brad pitt"}
    - slot{"query": "movies"}
    - slot{"actor": "brad pitt"}
    - action_movie
    - slot{"actor": "brad pitt"}
* popular_search{"popularity": "best", "genre": "action", "query": "movies"}
    - slot{"popularity": "best"}
    - slot{"genre": "action"}
    - slot{"query": "movies"}
    - action_genrerating
    - slot{"genre": "action"}

## Generated Story -7110551634769625323
* movie_info{"query": "movie", "movie": "the fast"}
    - slot{"query": "movie"}
    - slot{"movie": "the fast"}
    - action_movieinfo
    - slot{"movie": "the fast"}

## Generated Story 3129002799676315311
* greet
    - utter_greet
* actor_info{"info": "about", "actor": "woody allen"}
    - slot{"info": "about"}
    - slot{"actor": "woody allen"}
    - action_actorinfo
    - slot{"actor": "woody allen"}
* movie_info{"query": "movie"}
    - slot{"query": "movie"}
    - action_movieinfo
* goodbye
    - utter_goodbye

