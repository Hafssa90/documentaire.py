class documentaire :
    _N=0
    def __init__(self,titre,date):
        self.titre=titre
        self.date=date
        documentaire._N +=1
        self.id=documentaire._N

    def get_titre(self):
        return self.titre

    def get_date(self):
        return self.date

    def set_titre(self,titre):
        self.titre=titre

    def set_date(self,date):
        self.date=date
    
    def ToString (self) :
        return "le titre est : ",str(self.titre),"le date est : ",str(self.date),"le id est : ",str(self.id)

    def Equals (self,y) :
        return self.id == y.id

class exemplaire(documentaire):

    def __init__(self,titre,date,numero,date_dachat ) :
        super()._init_(titre,date)
        self.numero = numero
        self.date_dachat =  date_dachat
        documentaire._nomber += 1

    def get_numero(self):
        return self.numero

    def set_numero(self,numero ):
        self.numero == numero

    def getdate_dachat(self):
        return self.date_dachat

    def setdate_dachat(self,date_dachat ):
        self.date_dachat == date_dachat

    def toString(self):
        return super().tostring()+self.numero+self.date_dachat

d = documentaire("hhhh",1977)
print(d.ToString())