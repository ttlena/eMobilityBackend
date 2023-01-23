#Script to calculate the coordinates of the next Map Element, based on rotation of street Element and rotation of Npc Vehicle


import random
class NpcDriveScript():

    def __init__(self, x,z, streetRotation, carRotation, objectTypeId):
       
        self.currentCarRotation = carRotation
        self.newCarRotation = -1
        self.currentMapEle = MapEle(x,z,streetRotation,objectTypeId)
        self.nextUpperMapEle = MapEle(-1,-1,-1,-1)
        
        print('x_coord: {}'.format(self.currentMapEle.x_coord))
        print('z_coord: {}'.format(self.currentMapEle.z_coord))
        print('streetRotation: {}'.format(self.currentMapEle.streetRotation))
        print('carRotation: {}'.format(self.currentCarRotation))
        print('streetId: {}'.format(self.currentMapEle.objectTypeId))

    #determines if MapElement contains straight, curve or intersection and exectues driving calculation 
    def determineDrivingDirection(self):
        if self.currentMapEle.objectTypeId == 0:
            self.drive()
        elif self.currentMapEle.objectTypeId == 1:
            self.curveStreet()
        elif self.currentMapEle.objectTypeId == 2:
            print("Intersectttt me!")
            self.intersectionStreet()

    #determines the new x and y(z) coordinates of next MapElem, depending on the car car rotation.
    #gets executed directly if mapElement contains straight. 
    # if MapElement contained a curve,curve algorithm gets exucuted first than drive() method gets called.
    def drive(self):
        print("script drive")
        if self.currentCarRotation == 0:
            self.nextUpperMapEle.x_coord = self.currentMapEle.x_coord - 1
            self.nextUpperMapEle.z_coord = self.currentMapEle.z_coord
            if self.newCarRotation == -1:
                self.newCarRotation = self.currentCarRotation
        elif self.currentCarRotation == 1:
            self.nextUpperMapEle.x_coord = self.currentMapEle.x_coord
            self.nextUpperMapEle.z_coord = self.currentMapEle.z_coord + 1
            if self.newCarRotation == -1:
                self.newCarRotation = self.currentCarRotation
        elif self.currentCarRotation == 2:
            self.nextUpperMapEle.x_coord = self.currentMapEle.x_coord + 1
            self.nextUpperMapEle.z_coord = self.currentMapEle.z_coord
            if self.newCarRotation == -1:
                self.newCarRotation = self.currentCarRotation
        elif self.currentCarRotation == 3:
            self.nextUpperMapEle.x_coord = self.currentMapEle.x_coord
            self.nextUpperMapEle.z_coord = self.currentMapEle.z_coord - 1
            if self.newCarRotation == -1:
                self.newCarRotation = self.currentCarRotation
        
        print('NEW car rotation: {}'.format(self.newCarRotation))
        print('NEW x_coord: {}'.format(self.nextUpperMapEle.x_coord))
        print('NEW z_coord: {}'.format(self.nextUpperMapEle.z_coord))
        print("\n")

    #determines car rotation if MapElement contained an intersection. Turn direction determined randomly.
    def intersectionStreet(self):
        print("Intersection")
        num = random.randint(-1,1)
        self.newCarRotation = self.currentCarRotation + num
      

        if(self.newCarRotation > 3):
            self.newCarRotation = 0
        elif(self.newCarRotation < 0):
            self.newCarRotation = 3

        self.drive()

    #determines correct car rotation, if MapElement contained a curve
    def curveStreet(self):
        print("curve")
        if self.currentMapEle.streetRotation == 0:
            if self.currentCarRotation == 0:
                self.newCarRotation = self.currentCarRotation + 1
            elif self.currentCarRotation == 3:
                self.newCarRotation = self.currentCarRotation - 1
                
        elif self.currentMapEle.streetRotation == 1:
            if self.currentCarRotation == 1:
                self.newCarRotation = self.currentCarRotation + 1
            elif self.currentCarRotation == 0:
                self.newCarRotation = self.currentCarRotation + 3
        
        elif self.currentMapEle.streetRotation == 2:
            if self.currentCarRotation == 1:
                self.newCarRotation = self.currentCarRotation - 1
            elif self.currentCarRotation == 2:
                self.newCarRotation = self.currentCarRotation + 1

        elif self.currentMapEle.streetRotation == 3:
            if self.currentCarRotation == 2:
                self.newCarRotation = self.currentCarRotation - 1
            elif self.currentCarRotation == 3:
                self.newCarRotation = 0
        
        self.drive()

    def getCurrentCarRotation(self):
        return self.currentCarRotation

    def getNewCarRotation(self):
        return self.newCarRotation

    def getCurrentXCoord(self):
        return self.currentMapEle.x_coord

    def getCurrentZCoord(self):
        return self.currentMapEle.z_coord

    def setNextUpperMapEle(self,MapEle):
        self.nextUpperMapEle = MapEle
        print("naechstes upperMapElement", MapEle)

    def getNextUpperMapEle(self):
        return self.nextUpperMapEle

    def getNextUpperMapEleX(self):
        return self.nextUpperMapEle.x_coord

    def getNextUpperMapEleZ(self):
        return self.nextUpperMapEle.z_coord

class MapEle():
     def __init__(self,x,z,streetRotation,objectTypeId):
        self.x_coord = x
        self.z_coord = z
        self.streetRotation = streetRotation
        self.objectTypeId = objectTypeId
        


       