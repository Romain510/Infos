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
    def __init__(self, nom="military airplane", mission="Pas de mission"):
        self.nom=nom
        self.mission=mission
    
    def __str__(self):
        return f"{self.nom}{self.mission}"

class CargoAircraft(AirPlane):
    def __init__(self, nom="cargo airplane", shipment="Pas de cargaison"):
        self.nom=nom
        self.shipment=shipment
    
    def __str__(self):
        return f"{self.nom}{self.shipment}"

class CivilAircraft(AirPlane):
    def __init__(self, nom="military airplane", nb_passager="Pas de passager"):
        self.nom=nom
        self.nb_passager=nb_passager
    
    def __str__(self):
        return f"{self.nom}{self.nb_passager}"



if __name__=="__main__":
    etat=AirPlane("Airbus A380")
    print(etat)