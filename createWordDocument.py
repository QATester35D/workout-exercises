from docx import Document

#What exercises do you want?

document = Document()
document.add_heading('Workout Exercises', 0)


document.save('c:\\temp\\workoutExercises.docx')
