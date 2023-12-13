class Http(object):
    def __init__(self): 
        """ Constructeur de la mise en forme"""
        methode=""

    i=0

    def methode(self,temp,b):
        self.methode=""
        gt=temp[b:b+2]
        while(gt != "20"):
            gt=temp[b:b+2]
            self.methode+=chr(gt)
            i+=2
            b+=2
        return self.methode

    def url(self,temp,b):
        self.methode=""
        gt=temp[b:b+2]
        while(gt != "20"):
            gt=temp[b:b+2]
            self.methode+=chr(gt)
            b+=2
        return self.methode
