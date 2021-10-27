# This program reads in a csv file with data on vehicles.

# Here is where you import needed modules for your program.
import csv
import copy

# Defining the vehicle dictionary.
myVehicle = {
    "vin": "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# Prints the default vehicle.
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Define an empty List for storing the vehicles from the csv file.
myInventoryList = []

# Here is where you read in the csv file
with open('Data_Files\car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f"Column names are: {','.join(row)}")
            lineCount += 1
        else:
            print(f"vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}")
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f"Proccessed {lineCount} lines.")

# Makes a deep copy of the default vehicle and stores it into the current vehicle variable.
currentVehicle = copy.deepcopy(myVehicle)
for key, value in currentVehicle.items():
    print(f"{key} : {value}")

print("-----")
# This prints the list of vehicles that were read in from the csv file.
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")