from docx import Document
import databaseHelpers
import os

dbHelpers=databaseHelpers.DatabaseOfExercises()
bodyParts=dbHelpers.retrieveBodyPartTypes()
os.system('cls')
print("The major body parts covered in the workout exercises in the database are:")
print(bodyParts)
print("Enter the number for the workout combo or select custom workout:")
print("1 - Chest, triceps, abs")
print("2 - Back, biceps, abs")
print("3 - Legs, shoulders, abs")
print("4 - Full body workout (one exercise per major muscle group)")
print("5 - HIIT workout")
print("6 - Custom (you can specify major and minor muscles here)")
print("q - Quit program")
workoutSelection=input("Enter the number of your workout selection: ")
match workoutSelection:
    case workoutSelection if workoutSelection in range (1,5):
        exercise=dbHelpers.retrieveExercisesBySelection(workoutSelection)
    case "6":
        os.system('cls')
        print("Custom workout by major and/or minor muscle group(s)...")
        print("The major body parts available are:")
        print(bodyParts)
        print("The minor body parts available are:")
        targetGroups=dbHelpers.retrieveTargetTypes()
        print(targetGroups)
        print(" ")
        muscleGroups=input("Enter in the muscle groups you want to workout, separated by commas (spelling matters): ")
        nbrOfExercises=input("How many exercises do you want brought back for each muscle group? ")
        exercise=dbHelpers.retrieveCustomWorkoutPlan(muscleGroups, nbrOfExercises)
    case "q" | "Q":
        print ("Quiting the program")
        exit()
    case _:
        print("Not a valid selection")
        exit()

########################################################################################################
document = Document()
document.add_heading('Workout Exercises', 0)
bodyParts=dbHelpers.retrieveBodyPartTypes()
print("The body parts covered with the exercises are:",bodyParts)
muscleGroups=input("Enter in the muscle groups you want to work separated by commas: ")

document.save('c:\\temp\\workoutExercises.docx')
