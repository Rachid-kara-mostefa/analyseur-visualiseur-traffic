#!/usr/bin/env python

from Ethernet import *
from Ip import *
from Disposition import *
from Tcp import *
import time
import subprocess


I= Ip()
E= Ethernet()
D= Disposition()
T= Tcp()

# Import x and y variables using file_name.variable_name notation  
print("Veuillez entrer le chemin vers votre fichier a analyser pour que notre logiciel puisse vous generer un fichier .txt en retour : ")
fic = input()
if fic == "":
    print("Nous vous redemendons de rentrer le chemin vers votre fichier,veuillez recommencer svp ")
else:
    fic = str(fic)
    
#if(len(sys.argv) != 2):
#        print ("Usage: ./Mymain.py <filename> && <filename> is a file with hexa values and must have a .txt extension")
#        sys.exit(1)
#fic = sys.argv[1]

f = open(fic,'r')          
fil_src = f.readlines()
f.close()

a=D.isHexa(fil_src)
print("le fichier est en hexa : ",a)

if a:
    trames=D.decoupe_trames(fic)
    g=open("destination.txt","w")
    compteur=1
    for fichier_src in trames:
        g.write("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤ TRAME "+str(compteur)+" ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n")
        
        dest=E.macDestination(fichier_src)
        src=E.macSource(fichier_src)
        type=E.ethernet_type(fichier_src)
        g.write("\n-------------------------ETHERNET----------------------------\n\n")
        g.write("MAC destination  :  "+dest+"\n")
        g.write("MAC source  :  "+src+"\n")
        g.write("MAC type  :  "+type+"\n")

#¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤

        if type=="IPv4":
                
            ipVersion=I.versionIp(fichier_src)
            ipihl=I.ihl(fichier_src)
            iptos=I.tos(fichier_src)
            iptotallength=I.totalLength(fichier_src)
            ipidentificateur=I.id(fichier_src)
            ipflagR=I.flagBitR(fichier_src)
            ipflagdf=I.flagDontFragment(fichier_src)
            ipflagmf=I.flagMoreFragment(fichier_src)
            ipoffset=I.offset(fichier_src)
            ipttl=I.ttl(fichier_src)
            ipprotocole=I.protocole(fichier_src)
            ipHeaderChecksum=I.headerChecksum(fichier_src)
            ipsource=I.ipSource(fichier_src)
            ipdesti=I.ipDestination(fichier_src)
            ipoptiontype=I.ipoptionType(fichier_src)
            ipoptionlength=I.optionLength(fichier_src)
            ipoptionpadding=I.optionPadding(fichier_src)


            g.write("\n-------------------------ENTETE IP -----------------------------------\n"+"\n")
            g.write("ip version   :  "+ipVersion+"\n")
            g.write("ip THL   :  "+ipihl+"\n")
            g.write("ip Type Of Service   :  "+iptos+"\n")
            g.write("ip Total Length   :  "+iptotallength+"\n")
            g.write("ip identificateur   :  "+ipidentificateur+"\n")
            g.write("ip flags   :  "+ipflagR+ipflagdf+ipflagmf+"\n")
            g.write("ip offset   :  "+str(ipoffset)+"\n")
            g.write("ip Time To Live   :  "+ipttl+"\n")
            g.write("ip protocole   :  "+ipprotocole+"\n")
            g.write("ip cehcksum   :  "+ipHeaderChecksum+"\n")
            g.write("ip @ source   :  "+ipsource+"\n")
            g.write("ip @ destination   :  "+ipdesti+"\n")
            if int(ipihl)>20:
                g.write("ip option   :  "+ipoptiontype+"\n")
                g.write("ip option length   :  "+str(ipoptionlength)+"\n")
                g.write("ip option padding   :  "+str(ipoptionpadding)+" octets \n\n")
            else:
                g.write("pas d'option pour l'ip\n\n")


#¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤

            if ipprotocole=="TCP":
                r=int( I.ihl(fichier_src) )
                r=28+(r*2)         # r = longueure de l'entete ip + entete ethernet
                portsource = T.portSource(fichier_src,r)
                portdestination = T.portDestination(fichier_src,r)
                nsequence = T.nSequence(fichier_src,r)
                nack = T.nAck(fichier_src,r)
                dataoffset = T.offset(fichier_src,r)
                reserved = T.reserved(fichier_src,r)
                flags = T.lesFlags(fichier_src,r)
                urg=T.urg(flags)
                ack=T.ack(flags)
                psh=T.psh(flags)
                rst=T.rst(flags)
                syn=T.syn(flags)
                fin=T.fin(flags)
                window=T.window(fichier_src,r)
                tcpChecksum=T.checksum(fichier_src,r)
                urgentpointer=T.urgentPointer(fichier_src,r)
                optTcp=T.options(fichier_src,r)

                
                g.write("\n--------------------ENTETE TCP -----------------------------------\n"+"\n")
                g.write("port source  :     :  "+portsource+"\n")
                g.write("port destination   :  "+portdestination+"\n")
                g.write("numero de sequence   :  "+nsequence+"\n")
                g.write("numero d'acquetement   :  "+nack+"\n")
                g.write("Thl   :  "+dataoffset+"\n")
                g.write("reserved :   "+reserved+"\n")
                g.write("les flags   :  "+flags+"\n")
                g.write("flag URG   :  "+urg+"\n")
                g.write("flag ACK   :  "+ack+"\n")
                g.write("flag PSH   :  "+psh+"\n")
                g.write("flag RST   :  "+rst+"\n")
                g.write("flag SYN   :  "+syn+"\n")
                g.write("flag FIN   :  "+fin+"\n")
                g.write("window   :  "+window+"\n")
                g.write("checksum   :  "+tcpChecksum+"\n")
                g.write("urgent pointer   :  "+urgentpointer+"\n")
                if(optTcp !=""):
                    g.write("options tcp   :  "+"\n")
                    for elm in optTcp:
                        g.write("\t"+elm+"\n")
                    g.write("\n")
                else:
                    g.write("Pas d'option TCP \n\n")
#¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
               
                if portdestination=="80" or portsource=="80":
                    g.write("\n-------------------------------------------------------HTTP---------------------------------------\n\n")
                    hTTPval=T.httpval(fichier_src)
                    hTTptype=T.httpType()
                    hTTpStatus=T.httpStatus()
                    if hTTptype != "none":
                        g.write("HTTP methode  :  "+hTTptype+"\n")
                        if hTTptype == "HTTP\ 1.1":  
                            g.write("http status  :  "+hTTpStatus+"\n")
                        try:
                            g.write("ligne d'entete  : "+hTTPval+"\n")
                        except:
                            g.write(" - \n")
                    else:
                        g.write("Pas d'entete http pour cette trame\n\n")

                else:
                    g.write("Autre protocole de la couche application que http\n")
                #print(ipsource+" || "+portsource+" \t---------->\t"+ipdesti+" || "+portdestination+"\t")
            
            else:
                g.write("protocole  : "+ipprotocole+" autre que tcp\n")

        else:
            g.write("type : "+type+" ce n'est pas un paquet ipv4\n")
            
        compteur+=1
    g.close()
    
    
time.sleep(1)
print("====================== Fin de l'analyse ... ==========================")
print("\n")
print("Vos donnees se trouvent dans le fichier destination.txt")
time.sleep(1)
print("\n")
print("Le Visualisateur de trafic reseau demarre dans 3 secondes pour une meilleure visualisation, veuillez patientez chef !")
time.sleep(1)
print("   ================================= 3 ================================ ")
time.sleep(1)
print("   ================================= 2 ================================ ")
time.sleep(1)
print("   ================================= 1 ================================ ")
time.sleep(1)
subprocess.call("python environnement.py", shell=True) 