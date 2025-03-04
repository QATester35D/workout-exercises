from docx import Document
from docx.shared import Inches
import databaseHelpers
import os

class CreateWorkoutPlan:
    def __init__(self):
        self.document = Document()

    def docCreateHeading(self):
        document=self.document
        document.add_heading('Workout Exercises brought to you by QATester35D', 0)
        
  



########################################################################################################
# document = Document()
nbrOfExercises=len(exercise)

bodyParts=dbHelpers.retrieveBodyPartTypes()

document.save('c:\\temp\\workoutExercises.docx')
