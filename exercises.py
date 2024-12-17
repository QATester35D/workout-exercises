import requests
import json
import time

###################################################################################################
# Setup API request
class GetExercises:
    def __init__(self):
        self.url="https://exercisedb.p.rapidapi.com/exercises"
        self.headers = {
        'X-RapidAPI-Key': '65fee3dd8cmsh68753f6c119af56p16af81jsn70e7e93756dd', 
        'x-rapidapi-host': 'exercisedb.p.rapidapi.com'
        }

    # Retrieve a list of exercises by body part
    def get_exercises(self,bodyPart,limit,offset):
        url=self.url
        headers=self.headers
        exercisesURL=f"{url}/bodyPart/{bodyPart}?limit={limit}&offset={offset}"   # exercisesURL="https://exercisedb.p.rapidapi.com/exercises/bodyPart/back?limit=10&offset=0"

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            exercises = response.json()
            for post in exercises:
                # do something with the exercise here, probably just a log entry. DB update should be in another method
                print(f"Retrieved exercise: {exercises[0]['id']}, Name: {exercises[0]['name']}")
        else:
            print(f"Failed to retrieve any exercises. Status code: {response.status_code}")

a=GetExercises()
a.get_exercises("back",10,1)
time.sleep(1)