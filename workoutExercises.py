import json
import time
import apiCalls

exercises=apiCalls.GetExercises()  # Instantiate the class

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
print("Size of the list of exercises is:",len(exercisesById))

exercisesByName=exercises.get_exercises_by_name(name="pulldown",limit=10,offset=0)
print("Size of the list of exercises is:",len(exercisesByName))

time.sleep(1)