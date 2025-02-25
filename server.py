from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

scoreboard = [
    {
    "id": 1,
    "name": "Boston Bruins",
    "score": 7
    },

    {
    "id": 2,
    "name": "Tampa Bay Lightning", 
    "score": 5
    },

    {
    "id": 3,
    "name": "Toronto Maple Leafs", 
    "score": 2
    },

    {
    "id": 4,
    "name": "Florida Panthers", 
    "score": 1
    },

    {
    "id": 5,
    "name": "Buffalo Sabres", 
    "score": 1
    },
]


@app.route('/')
def show_scoreboard():
    return render_template('scoreboard.html', scoreboard = scoreboard) 

@app.route('/increase_score', methods=['GET', 'POST'])
def increase_score():
    global scoreboard

    json_data = request.get_json()   
    team_id = json_data["id"]  
    
#    for team in scoreboard:
#        if team["id"] == team_id:
#            team["score"] += 1

    #Create a new loop that update the score and swap locations of teams on the list
    previous_score = 0
    counter = 0
    flag = True
    while flag:
        score = 0
        if scoreboard[counter]["id"] == team_id:
            scoreboard[counter]["score"] += 1
            score = scoreboard[counter]["score"]

            if score > previous_score and counter != 0: #swap
                scoreboard[counter], scoreboard[counter - 1] = scoreboard[counter-1], scoreboard[counter]
            flag = False

        previous_score = scoreboard[counter]["score"]
        counter += 1
    
    return jsonify(scoreboard=scoreboard)


if __name__ == '__main__':
   app.run(debug = True)




