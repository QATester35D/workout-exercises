import mysql.connector
import time

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
    
    def retrieveExercisesbyBodyPart(self,bodyPart,nbrOfExercises):
        cur=self.cur
        # sql="SELECT * FROM exercises WHERE bodyPart = %s"
        match bodyPart:
            case bodyPart if bodyPart in ["biceps","triceps"]:
                sql="select distinct * from exercises WHERE target = %s ORDER BY RAND() limit %s"
            case _:
                sql="select distinct * from exercises WHERE bodyPart = %s ORDER BY RAND() limit %s"
        val=(bodyPart,nbrOfExercises, )
        cur.execute(sql,val)
        exerciseResult = cur.fetchall()
        return(exerciseResult)
    
    def retrieveBodyPartTypes(self):
        cur=self.cur
        sql="select distinct bodyPart from exercises"
        cur.execute(sql)
        bodyPartResult=cur.fetchall()
        #The result set has each itme formatted like a tuple ('value',) so I do this to create a new clean list
        newList=[]
        for bodyPart in bodyPartResult:
            newList.append(bodyPart[0])
        return(newList)

    def retrieveExercisesBySelection(self,workoutSelection):
        exerciseList=[]
        #Randomly bring back 3 exercises per muscle group
        match workoutSelection:
            case "1":
                muscleGroup=["chest","triceps","abs"]
                for i in muscleGroup:
                    val=self.retrieveExercisesbyBodyPart(i,3)
                    exerciseList.extend(val)
            case "2":
                muscleGroup=["back", "biceps","abs"]
                for i in muscleGroup:
                    val=self.retrieveExercisesbyBodyPart(i,3)
                    exerciseList.extend(val)
            case "3":
                muscleGroup=["legs", "shoulders","abs"]
                for i in muscleGroup:
                    val=self.retrieveExercisesbyBodyPart(i,3)
                    exerciseList.extend(val)
            case "4":
                muscleGroup=["chest","triceps","back", "biceps","legs", "shoulders","abs"] #one exercise per muscle group
                for i in muscleGroup:
                    val=self.retrieveExercisesbyBodyPart(i,1)
                    exerciseList.extend(val)
            case "5":
                muscleGroup=["hiit"]
                val=self.retrieveExercisesbyBodyPart(muscleGroup,1)
                exerciseList.extend(val)
            case "6":
                muscleGroup=["custom"]
                print("Need to figure out custom - separate method")
            case _:
                print("The entry is an invalid choice.")
                return()
        # cur=self.cur
        # sql="SELECT * FROM exercises WHERE bodyPart = %s"
        # val=(workoutSelection, )
        # cur.execute(sql,val)
        # exerciseResult = cur.fetchall()
        return(exerciseList)        