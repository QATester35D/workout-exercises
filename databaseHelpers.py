import mysql.connector

################################################################################################
class DatabaseOfExercises:
    def __init__(self):
        self.mydb = mysql.connector.connect(user='root', password='root', database='workout_exercises')
        self.cur = self.mydb.cursor()

    def dbInsertExercise(self, exercise):
        cur=self.cur
        bodyPart=exercise['bodyPart']
        equipment=exercise['equipment']
        gifUrl=exercise['gifUrl']
        id=exercise['id']
        name=exercise['name']
        target=exercise['target']
        secondaryMuscles=exercise['secondaryMuscles']
        secondaryMusclesList=self.createListForBLOB(secondaryMuscles)
        instructions=exercise['instructions']
        instructionsList=self.createListForBLOB(instructions)

        sql="INSERT INTO exercises (id, bodyPart, equipment, gifUrl, name, target, secondaryMuscles, instructions) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val=(id, bodyPart, equipment, gifUrl, name, target, secondaryMusclesList, instructionsList)
        cur.execute(sql, val)
        self.mydb.commit()

    def createListForBLOB(self,jsonList):
        listSize=len(jsonList)
        for i in range(0,listSize):
            muscle=jsonList[i].strip("'")
            if i == 0:
                listValues=jsonList[i]
            else:
                listValues=listValues+","+jsonList[i]
        return(listValues)