from googleapiclient.discovery import build
from google.oauth2 import service_account
import time
import serial
import PySimpleGUI as sg

import communicationFunctions
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data



def getIDList():
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    SAMPLE_SPREADSHEET_ID = '10H_6ovIscbxF6TNokWsnWNIIfrg3DIZS2ic_vWD_vVc'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Workers!C:C").execute()
    values = result.get('values', [])
    idList = [item for sublist in values for item in sublist]

    del idList[0]
    # print(idList)
    return idList


def getNamesList():
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    SAMPLE_SPREADSHEET_ID = '10H_6ovIscbxF6TNokWsnWNIIfrg3DIZS2ic_vWD_vVc'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Workers!A:A").execute()
    values = result.get('values', [])
    nameLst = [item for sublist in values for item in sublist]

    del nameLst[0]
    # print(idList)
    return nameLst


def getWorkersPhonesList():
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    SAMPLE_SPREADSHEET_ID = '10H_6ovIscbxF6TNokWsnWNIIfrg3DIZS2ic_vWD_vVc'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Workers!B:B").execute()
    values = result.get('values', [])
    phoneList = [item for sublist in values for item in sublist]

    del phoneList[0]
    # print(idList)
    return phoneList


def getWorkersChargingSpeedsList():
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    SAMPLE_SPREADSHEET_ID = '10H_6ovIscbxF6TNokWsnWNIIfrg3DIZS2ic_vWD_vVc'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Workers!D:D").execute()
    values = result.get('values', [])
    chrgSpeed = [item for sublist in values for item in sublist]

    del chrgSpeed[0]
    # print(idList)
    return chrgSpeed

def display(priorlist,idlist,station_List):
    new_list = []
    new_prior = priorlist
    new_prior.sort(reverse = True)
    for i in range(len(new_prior)):
        new_list[i] =idlist[priorlist.index(new_prior[i])]
    layout=[
        [sg.Text('station 1 -> ' + station_List[0])],
        [sg.Text('station 2 -> ' + station_List[1])],
        [sg.Text('waiting list -> ' + new_list[0])]
    ]
    window = sg.Window("EVcharge-Display", layout)

def getlistOfWorkersDistances():
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    SAMPLE_SPREADSHEET_ID = '10H_6ovIscbxF6TNokWsnWNIIfrg3DIZS2ic_vWD_vVc'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Workers!E:E").execute()
    values = result.get('values', [])
    distlist = [item for sublist in values for item in sublist]

    del distlist[0]
    # print(idList)
    return distlist


def getlistOfWorkersEmails():
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    SAMPLE_SPREADSHEET_ID = '10H_6ovIscbxF6TNokWsnWNIIfrg3DIZS2ic_vWD_vVc'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Workers!F:F").execute()
    values = result.get('values', [])
    emailLst = [item for sublist in values for item in sublist]

    del emailLst[0]
    # print(idList)
    return emailLst


listOfIDs = getIDList()
listOfWorkersNames = getNamesList()
listOfWorkersPhoneNumbers = getWorkersPhonesList()
listOfWorkersChargingSpeed = getWorkersChargingSpeedsList()
listOfWorkersDistances = getlistOfWorkersDistances()
listOfWorkersEmails = getlistOfWorkersEmails()
listOfPrioritiesScores = [None for _ in range(len(listOfIDs))]

activeParkersList = []
waitingToParkList = []
priorityList = list(range(len(listOfIDs)))
priorityMax = 6.6667
priorityMin = 0.03125

parking_spots = [None for _ in range(2)]

targetID = 0

#print(listOfWorkersDistances)



while targetID != -1:
    layout = [
        [sg.Text('Please enter your ID', font = ('Any 26'))],
        [sg.Text('ID', font = ('Any 16'), size=(3, 1)), sg.InputText()],
        [sg.Text(size =(14, 1)),sg.Submit(font = ('Any 20'))]
    ]
    window = sg.Window("EVcharge", layout)
    x = window.read()[1]
    myID = x[0]
    window.close()
    # myID = input("enter your ID ")

    if myID in parking_spots:
        layout = [[sg.Text('you are leaving, have a nice day!')], [sg.OK()]]
        window = sg.Window("EVcharge", layout)
        window.close()
        # print("you are leaving, have a nice day!")
        communicationFunctions.sendEmail(listOfWorkersEmails[listOfIDs.index(myID)],
                                         listOfWorkersNames[listOfIDs.index(myID)],
                                         'goodbye, have a nice day.')
        parking_spots[parking_spots.index(myID)] = None
    else:
        if myID in waitingToParkList:
            communicationFunctions.sendEmail(listOfWorkersEmails[listOfIDs.index(myID)],
                                             listOfWorkersNames[listOfIDs.index(myID)],
                                             "goodbye, have a nice day. Sorry for the long wait")
      #      communicationFunctions.sendAWhatsApp(listOfWorkersPhoneNumbers[listOfIDs.index(myID)],"goodbye, have a nice day. Sorry for the long wait")
            # print("you are leaving, have a nice day! Sorry for the long wait")

            waitingToParkList[waitingToParkList.index(myID)] = None
        else:


            if myID in listOfIDs:
                indexOfWorker = listOfIDs.index(myID)
                layout = [
                    [sg.Text('Welcome ' + listOfWorkersNames[indexOfWorker] + '! Please enter your battery percentage', font = ('Any 26'))],
                    [sg.Text(size=(20, 1)),sg.Text('battery percentage', font = ('Any 16'), size=(16, 1)), sg.InputText()],
                    [sg.Text(size =(50, 1)),sg.Submit(font = ('Any 20'))]
                ]
                window = sg.Window("EVcharge", layout)
                x = window.read()[1]
                window.close()
                # workerBattery = float(input(
                 #   "Welcome " + listOfWorkersNames[indexOfWorker] + "! Please enter your battery percentage: "))
                workerBattery = float(x[0])
                if workerBattery < 10:
                   # workerBattery = 10
                    listOfPrioritiesScores[indexOfWorker] = priorityMax
                else:
                    if workerBattery > 80:
                        #workerBattery = 80
                        listOfPrioritiesScores[indexOfWorker] = priorityMin
                    else:

                        listOfPrioritiesScores[indexOfWorker] = float(listOfWorkersDistances[indexOfWorker]) / (float(
                            workerBattery) * float(listOfWorkersChargingSpeed[indexOfWorker]))


                for i in range(len(parking_spots)):
                    flag_insert=False
                    if parking_spots[i] is None:
                        parking_spots[i] = myID
                        flag_insert=True
                        break
                if not flag_insert:
                    waitingToParkList.append(listOfIDs[indexOfWorker])

                #for i in waitingToParkList:
                   # if i in parking_spots:
                    #    i = None

                print(parking_spots)

                for x in parking_spots:
                    availSpot=None
                    if x is None:
                        #print("spot number " + str(parking_spots.index(x) + 1) + " is available ")
                        availSpot = parking_spots.index(x)+1
                        print(availSpot)
                        break
                print (waitingToParkList)
                if not all(v is None for v in waitingToParkList):
                    #for i in range(len(waitingToParkList)):
                        #if waitingToParkList[i] is not None:
                         #   listOfPrioritiesScores[indexOfWorker] = float(listOfWorkersDistances[indexOfWorker]) / (float(
                          #      workerBattery) * float(listOfWorkersChargingSpeed[indexOfWorker]))

                    print(listOfPrioritiesScores)  # don't forget to erase

                # if not available_stations
                #
                # if sumOfEmptySpots == len(parking_spots): #list of spots is full, start removing people
                #     maxScore = max(listOfPrioritiesScores)
                #     if maxScore>parking_spots[0] or maxScore>parking_spots[0]
                #

                    for i in range(len(parking_spots)):
                       if parking_spots[i] is not None:  # compare scores
                            personWhoisParkedID = parking_spots[i]
                            indexOFParkedWorker = listOfIDs.index(personWhoisParkedID)
                           # alreadyParkedScore = listOfPrioritiesScores[indexOFParkedWorker]
                    parking_priority =  [listOfPrioritiesScores[listOfIDs.index(parking_spots[0])],listOfPrioritiesScores[listOfIDs.index(parking_spots[1])]]
                    alreadyParkedScore = min(parking_priority)
                    i = parking_priority.index(min(parking_priority))
                    indexOfPersonWhoWantsToPark = listOfIDs.index(myID)
                            #myScore = listOfPrioritiesScores[indexOfPersonWhoWantsToPark]
                    myScore = listOfPrioritiesScores[listOfIDs.index(myID)]
                    if alreadyParkedScore < myScore:
                        availSpot = i + 1
                        print(availSpot)
                        communicationFunctions.sendEmail(listOfWorkersEmails[indexOFParkedWorker],
                                                         listOfWorkersNames[indexOFParkedWorker],
                                                         "Please move your car.")

                        communicationFunctions.sendEmail(listOfWorkersEmails[indexOfPersonWhoWantsToPark],
                                                         listOfWorkersNames[indexOfPersonWhoWantsToPark],
                                                         "You may park your car at slot " + str(availSpot))
                        write_read(str(availSpot))
                        waitingToParkList.append(personWhoisParkedID)
                        parking_spots[i] = myID
                        waitingToParkList[waitingToParkList.index(myID)] = None
                        print(parking_spots)
                        #break

                    else:
                        availSpot=None
                        write_read(str(availSpot))



            else:
                guestID = myID
                guestBattery = float(input("Welcome Guest! Please enter your percentage"))
                guestEmail = input("Please enter your email adress")

                guestAvgDistance = 40
                guestAvgChargingSpeed = 1

                if guestBattery < 10:
                    guestBattery = 10
                    priorityList.append(priorityMax)

                if guestBattery > 80:
                    guestBattery = 80
                    priorityList.append(priorityMin)

                waitingToParkList.append(guestID)
                listOfIDs.append(guestID)

                for i in range(len(parking_spots)):
                    if parking_spots[i] is None:
                        parking_spots[i] = guestID
                        break

                for i in waitingToParkList:
                    if i in parking_spots:
                        i = None

                #print(parking_spots)

                for x in parking_spots:
                    if x is None:
                        print("spot number " + str(parking_spots.index(x) + 1) + " is available ")
                        availSpot = parking_spots.index(x) + 1
                        break

                if not all(v is None for v in waitingToParkList):
                    for i in range(len(waitingToParkList)):
                        if waitingToParkList[i] is not None:
                            listOfPrioritiesScores.append(float(guestAvgDistance) / (float(
                                guestBattery)))
                            break

                #print(listOfPrioritiesScores)  # don't forget to erase

                # if not available_stations
                #
                # if sumOfEmptySpots == len(parking_spots): #list of spots is full, start removing people
                #     maxScore = max(listOfPrioritiesScores)
                #     if maxScore>parking_spots[0] or maxScore>parking_spots[0]
                #

                for i in range(len(parking_spots)):
                    if parking_spots[i] is not None:  # compare scores
                        personWhoisParkedID = parking_spots[i]
                        indexOFParkedWorker = listOfIDs.index(personWhoisParkedID)
                        alreadyParkedScore = listOfPrioritiesScores[indexOFParkedWorker]
                        #alreadyParkedScore=1

                        indexOfPersonWhoWantsToPark = len(waitingToParkList)
                        #1print(listOfPrioritiesScores[len(listOfPrioritiesScores)-1])
                        myScore = listOfPrioritiesScores[len(listOfPrioritiesScores)-1]

                        #myScore=1

                        if alreadyParkedScore < myScore:
                            communicationFunctions.sendEmail(listOfWorkersEmails[indexOFParkedWorker],
                                                             listOfWorkersNames[indexOFParkedWorker], "Please move your car.")

                            communicationFunctions.sendEmail(guestEmail, "guest",
                                                             "You may park your car at slot " + str(availSpot))
                            write_read(str(availSpot))
                            waitingToParkList.append(personWhoisParkedID)
                            parking_spots[i] = myID
                            waitingToParkList[waitingToParkList.index(myID)] = None
                            break

    newListOfWorkersChargingSpeed = listOfWorkersChargingSpeed.copy()

    j=len(listOfWorkersChargingSpeed)
    while j!=len(listOfPrioritiesScores):
        newListOfWorkersChargingSpeed[j]=1
        j=j+1
        

    #time.sleep(1200)
    #for i in range(len(listOfPrioritiesScores)):
    #    if listOfPrioritiesScores[i] is not None:
    #        listOfPrioritiesScores[i]=listOfPrioritiesScores[i]+ ((70*1200)/(3600*listOfWorkersChargingSpeed[i]))

