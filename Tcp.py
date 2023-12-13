from Ip import *

class Tcp(object):
    def __init__(self):
        self.portsrc=""
        self.portdst=""
        self.nSeq=""
        self.nak=""
        self.dataOff=""
        self.reser=""
        self.flags=""
        self.flagUrg=""
        self.flagAck=""
        self.flagPsh=""
        self.flagRst=""
        self.flagSyn="" 
        self.flagFin=""
        self.wind=""
        self.check=""
        self.uPointer=""
        self.opts=""
        self.I=Ip()
        self.pte=""
        self.methodo=""
        self.stat=""

    def portSource(self,temp,a):
        self.portsrc = temp[a:a+4]
        b=int(self.portsrc,base=16)
        self.portsrc=str(b)
        return self.portsrc

    def portDestination(self,temp,a):
        self.portdst = temp[a+4:a+8]
        b=int(self.portdst,base=16)
        self.portdst=str(b)
        return self.portdst

    def nSequence(self,temp,a):
        self.nSeq = temp[a+8:a+16]
        b=int(self.nSeq,base=16)
        self.nSeq=str(b)
        return self.nSeq

    def nAck(self,temp,a):
        self.nak = temp[a+16:a+24]
        b=int(self.nak,base=16)
        self.nak=str(b)
        return self.nak
    
    def offset(self,temp,a):
        self.dataOff=temp[a+24:a+25]
        b=int(self.dataOff,base=16)
        self.dataOff=str(b*4)
        return self.dataOff

    def reserved(self,temp,a):
        pkt1 = temp[a+25:a+26]
        pkt2 = temp[a+26:a+27]
        pkt1Dec = int(pkt1,base=16)
        pkt2Dec = int(pkt2,base=16)
        rsr = str(format(pkt1Dec, "04b"))+str(format(pkt2Dec, "04b"))
        self.reser = str(rsr[0])+str(rsr[1])+str(rsr[2])+str(rsr[3])+str(rsr[4])+str(rsr[5])
        return self.reser

    def lesFlags(self,temp,a):
        pkt3 = temp[a+26:a+27]
        pkt4 = temp[a+27:a+28]
        pkt3Dec = int(pkt3,base=16)
        pkt4Dec = int(pkt4,base=16)
        self.flags = str(format(pkt3Dec, "04b"))+str(format(pkt4Dec, "04b"))
        return self.flags
    
    def urg(self,lesflags):
        self.flagUrg = str(lesflags[2])
        return self.flagUrg
    def ack(self,lesflags):
        self.flagAck = str(lesflags[3])
        return self.flagAck
    def psh(self,lesflags):
        self.flagPsh = str(lesflags[4])
        return self.flagPsh
    def rst(self,lesflags):
        self.flagRst = str(lesflags[5])
        return self.flagRst
    def syn(self,lesflags):
        self.flagSyn = str(lesflags[6])
        return self.flagSyn
    def fin(self,lesflags):
        self.flagFin = str(lesflags[7])
        return self.flagFin

    def window(self,temp,a):
        self.wind=temp[a+28:a+32]
        b=int(self.wind,base=16)
        self.wind=str(b)
        return self.wind

    def checksum(self,temp,a):
        self.check=temp[a+32:a+36]
        b=int(self.check,base=16)
        self.check=str(b)
        return self.check

    def urgentPointer(self,temp,a):
        self.uPointer=temp[a+36:a+40]
        b=int(self.uPointer,base=16)
        self.uPointer=str(b)
        return self.uPointer
    
    def options(self,temp,a):
        l=[]
        pinto = a+40
        if int(self.dataOff) > 20:
            taille = pinto+2*int(self.dataOff)
            while(pinto<= taille):
                opt=temp[pinto:pinto+2]
                if(opt=="00"):
                   l.append("00:Fin options")
                   pinto+=2
                elif(opt=="01"):
                    l.append("01:No options")
                    pinto=pinto+2
                else:
                    optionz = {"02":"Maximum Segment Size " , "03":"Window scale " , "04":"SACK ", "08":"time stamp " }
                    if opt in optionz:
                        len = int(temp[pinto+2:pinto+4],base=16)
                        l.append(opt+":"+optionz[opt])
                    pinto=pinto+len*2
        else:
            l=""
        return l
              
    def httpval(self,temp):
        self.methodo=""
        debutHttp=14+int(self.I.ihl(temp))+int(self.dataOff)
        debutHttp=debutHttp*2
        p=debutHttp  #      un pointeur
        tL=2*int(self.I.totalLength(temp))
        while(p<tL):        #   tant que debut http < total Length
            gt=temp[p:p+2]
            if gt=="od":
                gt=temp[p+2:p+6]
                if gt=="0d0a0d":
                        break
            try:
                gtDec= int(gt, base=16)
                self.methodo += chr(gtDec)
                p += 2
            except:
                self.methodo+=" - "
                p += 2
        return self.methodo

    def httpType(self):
        lig=self.methodo[:3]
        if lig == "POS":
            self.pte="POST"
        elif lig == "HEA":
            self.pte="HEAD"
        elif lig == "DEL":
            self.pte="DELETE"
        elif lig == "GET":
            self.pte="GET"
        elif lig == "PUT":
            self.pte="PUT"
        elif lig == "HTT":
            self.pte="HTTP\ 1.1"
        else:
            self.pte="none"
        return self.pte

    def httpStatus(self):
        ligB=self.methodo[9:12]
        if ligB == "200":
            self.stat="200 OK"
        elif ligB == "301":
            self.stat="301 Moved permanently"
        elif ligB == "304":
            self.stat="304 Not modified"
        elif ligB == "400":
            self.stat="400 Bad request"
        elif ligB == "404":
            self.stat="404 Not found"
        return self.stat