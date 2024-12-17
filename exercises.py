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

    # Retrieve a list of all the body parts that have exercises
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

    # Retrieve a list of exercises by body part
    def get_exercises_by_equipType(self,**equipmentInfo):
        url=self.url
        headers=self.headers

        exercisesURL=f"{url}/equipment/{equipmentInfo["type"]}?limit={equipmentInfo["limit"]}&offset={equipmentInfo["offset"]}"   # exercisesURL="https://exercisedb.p.rapidapi.com/exercises/bodyPart/back?limit=10&offset=0"

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print(f"Retrieved the exercises for equipment type: {equipmentInfo["type"]}.")
            return(response.json())
        else:
            print(f"Failed to retrieve the equipment type: {equipmentInfo["type"]}. Status code: {response.status_code}")

    # Retrieve a list of all the body parts that have exercises
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

    # Retrieve a list of exercises by body part
    def get_exercises_by_muscle(self,**muscleInfo):
        url=self.url
        headers=self.headers

        exercisesURL=f"{url}/target/{muscleInfo["target"]}?limit={muscleInfo["limit"]}&offset={muscleInfo["offset"]}"   # exercisesURL="https://exercisedb.p.rapidapi.com/exercises/bodyPart/back?limit=10&offset=0"

        response = requests.get(exercisesURL, headers=headers)
        if response.status_code == 200:
            print(f"Retrieved the exercises for equipment type: {muscleInfo["target"]}.")
            return(response.json())
        else:
            print(f"Failed to retrieve the equipment type: {muscleInfo["target"]}. Status code: {response.status_code}")

###################################################################################################
# Instantiate the class
exercises=GetExercises()

parts=exercises.get_body_part_list()
print("Size of the list of body parts returned is:",len(parts))
for i in parts:
    exerciseJson=exercises.get_exercises_by_bodypart(bodypart=i,limit=10,offset=0) #using keyword arguments
    print("The number of exercises returned is",len(exerciseJson))
    #items will be accessed like this: exerciseJson[0]['equipment']

equipment=exercises.get_equipment_list()
print("Size of the list of equipment returned is:",len(equipment))
for equipType in equipment:
    exerciseByEquipJson=exercises.get_exercises_by_equipType(type=equipType,limit=10,offset=0) #using keyword arguments
    print("The number of exercises returned is",len(exerciseByEquipJson))
    #items will be accessed like this: exerciseJson[0]['equipment']

muscles=exercises.get_muscle_list()
print("Size of the list of equipment returned is:",len(muscles))
for muscle in muscles:
    exerciseByMuscleJson=exercises.get_exercises_by_muscle(target=muscle,limit=10,offset=0) #using keyword arguments
    print("The number of exercises returned is",len(exerciseByMuscleJson))
    #items will be accessed like this: exerciseJson[0]['equipment']

time.sleep(1)