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

    def retrieveExercisesbyBodyPart(self,bodyPart,nbrOfExercises):
        cur=self.cur
        if bodyPart == "legs":
            sql="select distinct * from exercises WHERE bodyPart like %s ORDER BY RAND() limit %s"
            bodyPart="%legs"
        else:
            sql="select distinct * from exercises WHERE bodyPart = %s ORDER BY RAND() limit %s"
        nbrOfExercises=int(nbrOfExercises)
        val=(bodyPart,nbrOfExercises)
        cur.execute(sql,val)
        exerciseResult = cur.fetchall()
        return(exerciseResult)

    def retrieveExercisesbyBodyPartTargetPart(self,bodyPart,target,nbrOfExercises):
        cur=self.cur
        sql="select distinct * from exercises WHERE bodyPart=%s and target = %s ORDER BY RAND() limit %s"
        nbrOfExercises=int(nbrOfExercises)
        val=(bodyPart,target,nbrOfExercises)
        cur.execute(sql,val)
        exerciseResult = cur.fetchall()
        return(exerciseResult)

    def retrieveExercisesbyTargetPart(self,target,nbrOfExercises):
        cur=self.cur
        sql="select distinct * from exercises WHERE target = %s ORDER BY RAND() limit %s"
        nbrOfExercises=int(nbrOfExercises)
        val=(target,nbrOfExercises)
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

    def retrieveListOfTargetTypes(self):
        cur=self.cur
        sql="select distinct target from exercises"
        cur.execute(sql)
        targetResult=cur.fetchall()
        #The result set has each itme formatted like a tuple ('value',) so I do this to create a new clean list
        newList=[]
        for target in targetResult:
            newList.append(target[0])
        return(newList)
    
    def retrieveExercisesBySelection(self,workoutSelection,*muscles):
        exerciseList=[]
        match workoutSelection:
            case 1:
                muscleGroup=["chest","triceps","abs"]
                for i in muscleGroup:
                    if i == "triceps":
                        #"bodyPart": "upper arms" | "target": "triceps"
                        val=self.retrieveExercisesbyTargetPart(i,3)
                    else:
                        val=self.retrieveExercisesbyBodyPart(i,3) #Randomly bring back 3 exercises per muscle group
                    exerciseList.extend(val)
            case 2:
                muscleGroup=["back", "biceps","abs"]
                for i in muscleGroup:
                    if i == "biceps":
                        #"bodyPart": "upper arms" | "target": "biceps"
                        val=self.retrieveExercisesbyTargetPart(i,3)
                    else:
                        val=self.retrieveExercisesbyBodyPart(i,3) #Randomly bring back 3 exercises per muscle group
                    exerciseList.extend(val)
            case 3:
                muscleGroup=["legs", "shoulders","abs"]
                #retrieve one exercise for each target group for legs
                for i in muscleGroup:
                    if i == "legs":
                        legs=["hamstrings","quads","glutes","adductors","calves"]
                        for j in legs:
                            val=self.retrieveExercisesbyTargetPart(j,1)
                            exerciseList.extend(val)
                    else:
                        val=self.retrieveExercisesbyBodyPart(i,3) #Randomly bring back 3 exercises per muscle group
                        exerciseList.extend(val)
            case 4:
                #Just legs - retrieve one exercise for each target group for legs
                legs=["hamstrings","quads","glutes","adductors","calves"]
                for j in legs:
                    val=self.retrieveExercisesbyTargetPart(j,2)
                    exerciseList.extend(val)
            case 5:
                muscleGroup=["chest","triceps","back","biceps","legs","shoulders","abs"] #one exercise per muscle group
                for i in muscleGroup:
                    if i in ["triceps", "biceps"]:
                        #"bodyPart": "upper arms" | "target": "triceps"
                        val=self.retrieveExercisesbyTargetPart(i,1)
                    else:
                        val=self.retrieveExercisesbyBodyPart(i,1)
                    exerciseList.extend(val)
            case 6:
                #Verify this later when I insert HIIT exercises into the database
                muscleGroup=["hiit"]
                val=self.retrieveExercisesbyBodyPart(muscleGroup,1)
                exerciseList.extend(val)
            case 7:
                #Custom
                muscleGroup=[item.strip() for item in muscles[0].split(',')]
                nbrOfExercises=muscles[1]
                nbrOfMuscles=len(muscleGroup)
                for i in muscleGroup:
                    if i in ['abs', 'pectorals', 'hamstrings', 'triceps', 'quads', 'biceps', 'glutes', 'delts', 'serratus anterior', 'forearms', 'calves', 'traps', 'upper back', 'lats', 'adductors', 'spine', 'cardiovascular system', 'abductors', 'levator scapulae']:
                        val=self.retrieveExercisesbyTargetPart(i,nbrOfExercises)
                        exerciseList.extend(val)
                    elif i in ['abs', 'chest', 'upper legs', 'upper arms', 'shoulders', 'lower arms', 'lower legs', 'back', 'cardio', 'neck']:
                        val=self.retrieveExercisesbyBodyPart(i,nbrOfExercises)
                        exerciseList.extend(val)
                    else:
                        print(f"The entry {i} is an invalid choice.")
            case 8:
                #Custom by exercise id
                exerciseList=[]
                exerciseGroup=[item.strip() for item in muscles[0].split(',')]
                for i in exerciseGroup:
                    val=self.retrieveExercisesbyExerciseId(i)
                    exerciseList.extend(val)
            case _:
                print(f"The entry {workoutSelection} is an invalid choice.")
                return()
        return(exerciseList)
    
    def element_exists_filter(self, element, muscleList):
        wasItemFound = filter(lambda x: x == element, muscleList)
        return any(wasItemFound)

    def retrieveCustomWorkoutPlan(self,workoutSelection,nbr):
        exerciseList=[]
        workoutSelection=workoutSelection.replace(", ",",") #in case the person enters a space between names
        specifiedMuscleList=workoutSelection.split(",")
        bodyParts=self.retrieveBodyPartTypes()
        for i in specifiedMuscleList:
            if self.element_exists_filter(i, bodyParts):
                val=self.retrieveExercisesbyBodyPart(i,nbr)
            else:
                val=self.retrieveExercisesbyTargetPart(i,nbr)
            exerciseList.extend(val)
        return(exerciseList)