class AirPlane:
    def __init__(self, nom=""):
        self.nom=nom
        self.fly=False

    def take_off(fly):
        return fly==True

    def land(fly):
        return fly==False

    def __str__(self):
        status="ground"
        if self.fly:
            status="flying"
        else:
            status="ground"
        return f"{self.nom}-{status}"

class MilitaryAircraft(AirPlane):
    def __init__(self, nom="military airplane"):
        self.nom=nom



if __name__=="__main__":
    etat=AirPlane("Airbus A380")
    print(etat)