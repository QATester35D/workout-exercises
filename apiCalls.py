import requests
import json

###################################################################################################
# Setup API request
class GetExercises:
    def __init__(self):
        self.url="https://exercisedb.p.rapidapi.com/exercises"
        self.headers = {
        'X-RapidAPI-Key': '65fee3dd8cmsh68753f6c119af56p16af81jsn70e7e93756dd', 
        'x-rapidapi-host': 'exercisedb.p.rapidapi.com'
        }

    # Retrieve a list of all the body parts that have exercises
    def get_body_part_list(self):
        url=self.url
        headers=self.headers
        exercisesURL=f"{url}/bodyPartList"

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print("Retrieved the body parts supported by exercises.")
            return(response.json())
        else:
            print(f"Failed to retrieve the body parts supported by exercises. Status code: {response.status_code}")

    # Retrieve a list of exercises by body part
    def get_exercises_by_bodypart(self,**exerciseInfo):
        url=self.url
        headers=self.headers

        exercisesURL=f"{url}/bodyPart/{exerciseInfo["bodypart"]}?limit={exerciseInfo["limit"]}&offset={exerciseInfo["offset"]}"   # exercisesURL="https://exercisedb.p.rapidapi.com/exercises/bodyPart/back?limit=10&offset=0"

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print(f"Retrieved the exercises for body part {exerciseInfo["bodypart"]}.")
            return(response.json())
        else:
            print(f"Failed to retrieve the exercises for body part {exerciseInfo["bodypart"]}. Status code: {response.status_code}")

    # Retrieve a list of all the equipment used in exercises
    def get_equipment_list(self):
        url=self.url
        headers=self.headers
        exercisesURL=f"{url}/equipmentList"

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print("Retrieved the list of equipment.")
            return(response.json())
        else:
            print(f"Failed to retrieve the list of equipment. Status code: {response.status_code}")

    # Retrieve a list of exercises by equipment
    def get_exercises_by_equipType(self,**equipmentInfo):
        url=self.url
        headers=self.headers

        exercisesURL=f"{url}/equipment/{equipmentInfo["type"]}?limit={equipmentInfo["limit"]}&offset={equipmentInfo["offset"]}" 

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print(f"Retrieved the exercises for equipment type: {equipmentInfo["type"]}.")
            return(response.json())
        else:
            print(f"Failed to retrieve the equipment type: {equipmentInfo["type"]}. Status code: {response.status_code}")

    # Retrieve a list of all the muscles that have exercises
    def get_muscle_list(self):
        url=self.url
        headers=self.headers
        exercisesURL=f"{url}/targetList"

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print("Retrieved the list of muscles.")
            return(response.json())
        else:
            print(f"Failed to retrieve the list of muscles. Status code: {response.status_code}")

    # Retrieve a list of exercises by muscle group
    def get_exercises_by_muscle(self,**muscleInfo):
        url=self.url
        headers=self.headers

        exercisesURL=f"{url}/target/{muscleInfo["target"]}?limit={muscleInfo["limit"]}&offset={muscleInfo["offset"]}" 

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print(f"Retrieved the exercises for equipment type: {muscleInfo["target"]}.")
            return(response.json())
        else:
            print(f"Failed to retrieve the equipment type: {muscleInfo["target"]}. Status code: {response.status_code}")

    # Retrieve a list of exercises
    def get_exercises(self,**exerciseInfo):
        url=self.url
        headers=self.headers

        exercisesURL=f"{url}?limit={exerciseInfo["limit"]}&offset={exerciseInfo["offset"]}" 

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print("Retrieved the exercises.")
            return(response.json())
        else:
            print(f"Failed to retrieve any exercises. Status code: {response.status_code}")

    # Retrieve a list of exercises by Id
    def get_exercises_by_id(self,exerciseId):
        url=self.url
        headers=self.headers

        exercisesURL=f"{url}/exercise/{exerciseId}" 

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print(f"Retrieved the exercises by id: {exerciseId}")
            return(response.json())
        else:
            print(f"Failed to retrieve any exercises by id {exerciseId}. Status code: {response.status_code}")

    # Retrieve a list of exercises by name
    def get_exercises_by_name(self,**nameInfo):
        url=self.url
        headers=self.headers

        exercisesURL=f"{url}/name/{nameInfo["name"]}?limit={nameInfo["limit"]}&offset={nameInfo["offset"]}" 

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print(f"Retrieved the exercises by the exercise name: {nameInfo["name"]}.")
            return(response.json())
        else:
            print(f"Failed to retrieve the exercises by the exercise name: {nameInfo["name"]}. Status code: {response.status_code}")
