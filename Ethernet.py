class Ethernet(object):

    def __init__(self): 
        """ Constructeur des élements Etherne """

        self.dst="" 
        self.src="" 
        self.type="" 
    
    def macDestination(self,temp):
        mac=""
        for i in range(12): 
            if i%2==0:
                mac+= str(temp[i])   # mettre les : chaque 2 bits
            else:
                if i!=11:
                    mac+= str(temp[i]) 
                    mac+=":"
                else:
                    mac+= str(temp[i])
        self.dst=mac
        return self.dst
    

    def macSource(self, temp):
        mac2=""
        for i in range(12,24): 
            if i%2==0:
                mac2+= str(temp[i])     # mettre les : chaque 2 bits
            else:
                if i!=23:
                    mac2+= str(temp[i]) 
                    mac2+=":"
                else:
                    mac2+= str(temp[i])
        self.src=mac2
        return self.src

    def ethernet_type(self, temp):
        """ les types dans un dictionnaire de données """
        type = temp[24:28]
        Types={"0800":"IPv4" , "86dd":"Ipv6" , "86DD":"Ipv6" , "8100":"Vlan" , "0805":"X.25 niveau 3" , "0600":"XNS" , "0806":"ARP" , "8035":"RARP" , "8098":"AppleTalk"}
        
        if type in Types:   
            return Types[type]
        else:
            a="Je n'ai pas ce type de protocole dans ma tete"
            return a 
