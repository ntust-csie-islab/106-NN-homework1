from mysql.connector import (connection)
import csv
import sys

cnx = connection.MySQLConnection(user='root', password='123', host='127.0.0.1', database='KDD')
cursor = cnx.cursor()
csvHeaderFlag = False # for writing csv header

#Monday
day1 = ['2016-09-19','2016-09-26','2016-10-03','2016-10-10','2016-10-17']
day1_next = ['2016-09-20','2016-09-27','2016-10-04','2016-10-11', '2016-10-18']
#Tuseday
day2 = ['2016-09-20','2016-09-27','2016-10-04','2016-10-11']
day3 = ['2016-09-21','2016-09-28','2016-10-05','2016-10-12']
day4 = ['2016-09-22','2016-09-29','2016-10-06','2016-10-13']
day5 = ['2016-09-23','2016-09-30','2016-10-07','2016-10-14']
day6 = ['2016-09-24','2016-10-01','2016-10-08','2016-10-15']
day7 = ['2016-09-25','2016-10-02','2016-10-09','2016-10-16']
day7_next = ['2016-09-26','2016-10-03','2016-10-10','2016-10-17']

week = [day1, day2, day3, day4, day5, day6, day7]
week_next = [day1_next, day3, day4, day5, day6, day7, day7_next]

def insertTocsv(avg, day, TX, DX):
    global csvHeaderFlag
    day += 1

    with open('KDD_withDB_version2_' + str(TX) + 'D' + str(DX) +'.csv', 'a') as csvfile:
        fieldnames = ['Day', 'startTime', 'x1', 'x2', 'h', 'y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if(not csvHeaderFlag):
            writer.writeheader()
            csvHeaderFlag = True
        STARTTIME_MORNING = 22
        STARTTIME_AFTERNOON = 49
        for i in range(6):
            writer.writerow({'Day' : day, 'startTime' : STARTTIME_MORNING - 21 + i, 'x1': avg[STARTTIME_MORNING + i], 'x2': avg[STARTTIME_MORNING+1+i], 'h': avg[len(avg)-2], 'y': avg[STARTTIME_MORNING+2+i]})
            writer.writerow({'Day' : day, 'startTime' : STARTTIME_AFTERNOON - 42 + i, 'x1': avg[STARTTIME_AFTERNOON + i], 'x2': avg[STARTTIME_AFTERNOON+1+i], 'h': avg[len(avg)-1], 'y': avg[STARTTIME_AFTERNOON+2+i]})

def sumHistory2(resultList):
    sumUpMorning = 0
    sumUpAfternoon = 0
    indexMorning = 0
    indexAfternoon = 0
    temp = []
    returnedTemp = []
 
    # get what we wants
    for data in [row[0] for row in resultList]:
        temp.append(data[0])

    for i in range(len(temp)):
        if i >= 22 and i <= 27:
            sumUpMorning += temp[i]
            indexMorning += 1
        elif i >= 49 and i <= 54:
            sumUpAfternoon += temp[i]
            indexAfternoon += 1
        returnedTemp.append(temp[i])
    
    returnedTemp.append(sumUpMorning/indexMorning)
    returnedTemp.append(sumUpAfternoon/indexAfternoon)
    return returnedTemp

def runSQLQuery(day, day_next, TX, DX, k):
    for i in range(len(day)):
        Hour = 0 # Hour = 0
        Min = 0  # Min = 0
        Hour_next = 0 # 0
        Min_next = 20 # 20
        singleResultList = []
        while True:
            if Hour == 23 and Min == 40:
                operation = "select count(*) from volmn6Data where time >= '" + day[i] + " " + str(Hour) + ":" + str(Min) + ":00' and time < '" + day_next[i] + " " + str(Hour_next) + ":" + str(Min_next) + ":00' and tollgate_id = '" + str(TX) + "' and direction = '" + str(DX) + "';"
            else:
                operation = "select count(*) from volmn6Data where time >= '" + day[i] + " " + str(Hour) + ":" + str(Min) + ":00' and time < '" + day[i] + " " + str(Hour_next) + ":" + str(Min_next) + ":00' and tollgate_id = '" + str(TX) + "' and direction = '" + str(DX) + "';"        
            #print str(operation)
            cursor.execute(operation, multi=True)
            for result in cursor.execute(operation, multi=True):
            #print result.fetchall() 
                tempResult = result.fetchall()
                #print tempResult
                if tempResult is not None:
                    singleResultList.append(tempResult)
            #print str(singleResultList)
            Min += 20
            Min_next += 20
            if Min == 60:
               Min = 0
               Hour += 1
               if Hour == 24: #24
                   break
            if Min_next == 60:
               Min_next = 0
               Hour_next += 1
               if Hour_next == 24:
                   Hour_next = 0
        #print str(singleResultList)
        avg = sumHistory2(singleResultList)
        # k is day
        insertTocsv(avg, k, TX, DX)

def main():
    global csvHeaderFlag
    TX = [1, 2, 3]
    DX = [0, 1]
    
    for i in range(len(TX)):
        for j in range(len(DX)):
            if(TX[i] == 2 and DX[j] == 1): # start at 0
                continue
            else:
                csvHeaderFlag = False
                for k in range(len(week)):
                    runSQLQuery(week[k], week_next[k], TX[i], DX[j], k)
            
            print 'Done DX ' + str(j)
        print 'Done TX ' + str(i)

main()

cnx.close()

