from docx import Document
from docx.shared import Inches
import databaseHelpers
import createWordDocument
import os

################
dbHelpers=databaseHelpers.DatabaseOfExercises()
bodyParts=dbHelpers.retrieveBodyPartTypes()
os.system('cls')
print("The major body parts covered in the workout exercises in the database are:")
print(bodyParts)
print("Enter the number for the workout combo or select custom workout:")
print("1 - Chest, triceps, abs")
print("2 - Back, biceps, abs")
print("3 - Legs, shoulders, abs")
print("4 - Just legs")
print("5 - Full body workout (one exercise per major muscle group)")
print("6 - HIIT workout")
print("7 - Custom (type in major and minor muscles separated by commas)")
print("8 - Custom by exercise id (type in exercise id separated by commas)")
print("q - Quit program")
workoutSelection=int(input("Enter the number of your workout selection: "))
match workoutSelection:
    case workoutSelection if workoutSelection in range (1,7):
        exerciseList=dbHelpers.retrieveExercisesBySelection(workoutSelection)
    case 7:
        os.system('cls')
        print("Custom workout by major and/or minor muscle group(s)...")
        print("The major body parts available are:")
        print(bodyParts)
        print("The minor body parts available are:")
        targetGroups=dbHelpers.retrieveListOfTargetTypes()
        print(targetGroups)
        print(" ")
        muscleGroups=input("Enter in the muscle groups you want to workout, separated by commas (spelling matters): ")
        nbrOfExercises=input("How many exercises do you want brought back for each muscle group? ")
        exerciseList=dbHelpers.retrieveExercisesBySelection(workoutSelection,muscleGroups, nbrOfExercises)
    case "q" | "Q":
        print ("Quiting the program")
        exit()
    case _:
        print("Not a valid selection")
        exit()


########################################################################################################
# Create the Word document
########################################################################################################
document=createWordDocument.CreateWorkoutPlan()
workOutFocus=document.docWorkOutSelection(workoutSelection)
document.docCreateHeading(workOutFocus)
document.docCreateParagraph(workOutFocus)
document.docWriteOutExercises(exerciseList)
document.docSave('c:\\temp\\workoutExercises.docx')
