# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:27:57 2021

@author: craig
"""

#Homework Assignment #9: Classes
import random

class Vehicle:
    def __init__(self,make,model,year,weight, NeedsMaintenance = False, TripsSinceMaintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance
        
 #Getters
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight

    def getNeedsMaintenace(self):
        return self.NeedsMaintenance

    def getTripsSinceMaintenance(self):
        return self.TripsSinceMaintenance
    
    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False

 #Setters
    def setMake(self,make):
        self.make = make
    
    def setModel(self,model):
        self.model = model
        
    def setYear(self,year):
        self.year = year
        
    def setWeight(self,weight):
        self.weight = weight
        
    def setNeedsMaintenance(self,NeedsMaintenance):
        self.Needsmaintenance = NeedsMaintenance
        
    def setTripsSinceMaintenance(self,TripsSinceMaintenance):
        self.TripsSinceMaintenance = TripsSinceMaintenance
        
class Car(Vehicle):
    def __init__(self, make, model, year, weight, isDriving = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = isDriving
        
    def Drive(self):
        self.isDriving = True
        
    def Stop(self):
        if self.isDriving:
            self.TripsSinceMaintenance += 1
            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = True
            
        self.isDriving = False
        
          
#Driving
def driveCar(Car):
    drive_times = random.randint(1,150)
    for i in range(drive_times):
        Car.Drive()
        Car.Stop()

        
def carValues(Car):
    print('Make ',Car.make)
    print('Model ',Car.model)
    print('Year ',Car.year)
    print('Weight ',Car.weight)
    print('Needs Maintenance ',Car.NeedsMaintenance)
    print('Trips Since Maintenance ',Car.TripsSinceMaintenance)
    print('Weight ',Car.weight)
    print("\n")                
        
               
        
carOne = Car("Ford", "Bronco", 2018, 4250 )
carTwo = Car("Ford", "Explorer", 2015, 3800 )
carThree = Car("Ford", "Mustang", 2020, 3200 )                
        
driveCar(carOne)
driveCar(carTwo)
driveCar(carThree)               
        
carValues(carOne)
carValues(carTwo)
carValues(carThree)                 
        
                 