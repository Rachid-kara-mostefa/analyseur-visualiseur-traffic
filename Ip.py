class Ip(object): 
    def __init__(self):
        """constructeur de IP """
        self.version = ""
        self.ipheaderlength = ""
        self.typeofservice = "" 
        self.totalL = ""
        self.identification = "" 
        self.flagR = ""
        self.flagDF = ""
        self.flagMF = ""
        self.OffsetFragment = "" 
        self.TTL = ""
        self.protocol = ""
        self.hchecksum = ""
        self.ipsrc = ""
        self.ipdest = ""
        self.option_length = ""
        self.optionType = ""
        self.option_padd = ""

        # version de l'ip
    def versionIp(self,temp):
        self.version = temp[28:29]
        return self.version

        # Ip Header Length IHL
    def ihl(self,temp):
        ihl=temp[29:30]
        len=0
        l=int(ihl,base=16)
        self.ipheaderlength = str(l*4)
        return self.ipheaderlength


        # Type Of Service  TOS
    def tos(self,temp):
        t=temp[30:32]
        self.typeofservice=str(t)
        return self.typeofservice

        # Total Length
    def totalLength(self,temp):
        totalL=temp[32:36]
        self.totalL=str(int(totalL,base=16))
        return self.totalL

        # Identificateur
    def id(self,temp):
        id=temp[36:40]
        id=int(id,base=16)
        self.identification = str(id)
        return self.identification

        # flags
    def flagBitR(self,temp):
        flags=temp[40:41]
        flagsDec=int(flags,base=16)
        flag=format(flagsDec, "04b")
        self.flagR=str(flag[0])
        return self.flagR
    def flagDontFragment(self,temp):
        flags=temp[40:41]
        flagsDec=int(flags,base=16)
        flag=format(flagsDec, "04b")
        self.flagDF=str(flag[1])
        return self.flagDF
    def flagMoreFragment(self,temp):
        flags=temp[40:41]
        flagsDec=int(flags,base=16)
        flag=format(flagsDec, "04b")
        self.flagMF=str(flag[2])       
        return self.flagMF

        #fragments
    def offset(self,temp):
        fragment=temp[40:44]
        offsetDec=int(fragment,base=16)
        offset=format(offsetDec, "16b")
        offset=offset[3:16]
        self.OffsetFragment=str(int(offset,base=2))
        return self.OffsetFragment

        # ttl
    def ttl(self,temp):
        t=temp[44:46]
        ttlDecimal=int(t,base=16)
        self.TTL = str(ttlDecimal)
        return self.TTL

        # protocole
    def protocole(self,temp):
        p=temp[46:48]
        proto=str(int(p,base=16))
        pcl={"1":"ICMP" , "2":"IGMP" , "6":"TCP" , "8":"Exterior Gateway Protocol" , "9":"IGP" , "17":"DP" , "36":"XTP" , "46":"Reservation Protocol"}
        if proto in pcl:
            self.protocol=pcl[proto]
            return self.protocol
        else:
            return "je ne connais pas ce protocole!"

        # Header Checksum
    def headerChecksum(self,temp):
        hChecksum=temp[48:52]
        self.hchecksum = str(int(hChecksum,base=16))
        return self.hchecksum

        # Ip source
    def ipSource(self,temp):
        IPsource = temp[52:60]
        h1=IPsource[0:2]
        d1=int(h1,base=16)
        h2=IPsource[2:4]
        d2=int(h2,base=16)
        h3=IPsource[4:6]
        d3=int(h3,base=16)
        h4=IPsource[6:8]
        d4=int(h4,base=16)
        self.ipsrc = str(d1)+"."+str(d2)+"."+str(d3)+"."+str(d4)
        return self.ipsrc


        # Ip destination
    def ipDestination(self,temp):
        IPdestination = temp[60:68]
        h1=IPdestination[0:2]
        d1=int(h1,base=16)
        h2=IPdestination[2:4]
        d2=int(h2,base=16)
        h3=IPdestination[4:6]
        d3=int(h3,base=16)
        h4=IPdestination[6:8]
        d4=int(h4,base=16)
        self.dest = str(d1)+"."+str(d2)+"."+str(d3)+"."+str(d4)
        return self.dest

        #option
    def ipoptionType(self,temp):
        if(int(self.ipheaderlength) >20):
            optionType=temp[68:70]
            optiontp=str(int(optionType,base=16))
            opt = {"0":"End Of Options" , "1":"No Operation" , "7":"Record Route" , "68":"TimeStamp" , "130":"Security" , "82":"Trace Route" , "131":"Loose Source Route" , "137":"Strict Source Route"}
            if optiontp in opt:
                self.optionType=opt[optiontp]  
            else:
                self.optionType="je ne connais pas cette option helas "          
        else:                
            self.optionType = "pas d'option"

        return self.optionType

        # option Length
    def optionLength(self,temp):
        if(int(self.ipheaderlength) >20):
            optionL=temp[70:72]
            self.option_length=int(optionL,base=16)
            self.option_length =str(self.option_length)
            return self.option_length

                 # padding / Bourrage
    def optionPadding(self,temp):
        if int(self.ipheaderlength)>20:
            c=int(self.ipheaderlength)-int(self.option_length)+3   # 3 octets pour les details de l'option
            self.option_padd="il y a "+str(c)+" octets de bourrage"
            return self.option_padd

