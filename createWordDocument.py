from docx import Document
import databaseHelpers
import os

dbHelpers=databaseHelpers.DatabaseOfExercises()
bodyParts=dbHelpers.retrieveBodyPartTypes()
os.system('cls')
print("The body parts covered in the workout exercises in the database are:")
print(bodyParts)
print("Enter the number for the workout combo or select custom workout:")
print("1 - Chest, triceps, abs")
print("2 - Back, biceps, abs")
print("3 - Legs, shoulders, abs")
print("4 - Full body workout (one exercise per muscle group)")
print("5 - HIIT workout")
print("6 - Custom")
muscleGroups=input("Enter in the muscle groups you want to work separated by commas: ")
exercise=dbHelpers.retrieveExercisesBySelection(muscleGroups)
########################################################################################################
document = Document()
document.add_heading('Workout Exercises', 0)
bodyParts=dbHelpers.retrieveBodyPartTypes()
print("The body parts covered with the exercises are:",bodyParts)
muscleGroups=input("Enter in the muscle groups you want to work separated by commas: ")

document.save('c:\\temp\\workoutExercises.docx')
