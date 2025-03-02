import json
import time
import apiCalls
import databaseHelpers
import os

########################################################################################################
# Instantiate the classes for the API and database calls
exercises=apiCalls.GetExercises()
dbHelpers=databaseHelpers.DatabaseOfExercises()

########################################################################################################
#Temp area
bodyPartList=dbHelpers.retrieveBodyPartTypes()
exerciseResult=dbHelpers.retrieveExercisesBySelection(1)
time.sleep(1)

########################################################################################################
# Process through this folder opening each JSON file and insert the values into the database
# folderName="C:\\Users\\shawn\\OneDrive\\Documents\\Tech\\jsonFilesForWorkouts\\misc_exercises.json"
folderName="C:\\Users\\shawn\\OneDrive\\Documents\\Tech\\jsonFilesForWorkouts\\"

# iterate over files in the directory
for filename in os.listdir(folderName):
    fullName = os.path.join(folderName, filename)
    # checking if it is a file
    if os.path.isfile(fullName):
        print("Processing the exercise file",fullName)
        # origFile = open(fullName, encoding="utf-8") #open original file

        with open(fullName, 'r') as file:
            data = json.load(file)
            sizeOfData=len(data)
            for i in range(0,sizeOfData):
                dbHelpers.dbInsertExercise(data[i])
    
        file.close()

time.sleep(1)

########################################################################################################
# API calls
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

fullExerciseList=exercises.get_exercises(limit=10,offset=0)
print("Size of the list of exercises is:",len(fullExerciseList))


exercisesById=exercises.get_exercises_by_id("0007")
dbHelpers.dbInsertExercise(exercisesById)
print("Size of the list of exercises is:",len(exercisesById))

exercisesByName=exercises.get_exercises_by_name(name="pulldown",limit=10,offset=0)
print("Size of the list of exercises is:",len(exercisesByName))

########################################################################################################
exerciseResult=dbHelpers.retrieveExercises("core")

time.sleep(1)