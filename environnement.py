import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, simpledialog
from tkinter import *
import os, sys
import re

from Disposition import *
from Ethernet import *
from Ip import *
from Tcp import *

class Window(object):
    def __init__(self):
        rt = tk.Tk()
        self.root = rt
        self.root.geometry("800x600")
        self.root.title("VISUALISEUR DE TRAFIC RESEAU")
        self.I= Ip()
        self.E= Ethernet()
        self.T= Tcp()
        self.D = Disposition()
        self.analyse = ()
        self.filtre : Entry
        self.cpt = 0
        self.liste = [0,1]        
        self.flagsActifs = ""
        #self.run()
                
        self.frame  = Frame(self.root)
        #self.entry = Entry(self.frame)
        
        
                
        self.btn1 = Button(self.root, text = "Ouvrir Fichier", command = self.openfile)
        self.btn1.place(x = 0, y = 0)
        self.btn3 = Button(self.root,text = "Quitter",command = self.root.quit)
        self.btn3.place(x = 120, y = 0)
        
        self.label_01 = Label(self.root, text = "Fichier source : ")
         
    """ 
        def arrow(self,portSrc,portDst):
        ar = ""      
        label=tk.Label(self.frame,text=str(portSrc)+"-------->"+str(portDst)+"\n",bg="#76FF7B",font=20,compound='right')
        label.pack(side="top")
        ar=ar+"\t"
        self.frame.pack(side="left")
    """
    

        
    def cadre(self):
        self.tree_frame = Frame(self.root,padx = 400, pady = 500, bg = "lightblue")
        self.tree_frame.pack()
        
        self.treeScroll1 = Scrollbar(self.root, orient = VERTICAL)
        self.treeScroll1.pack(side = RIGHT,fill = Y)
        self.tree = ttk.Treeview(self.root,yscrollcommand = self.treeScroll1.set)
        self.treeScroll2 = Scrollbar(self.root, orient = HORIZONTAL)
        self.treeScroll2.pack(side = BOTTOM,fill = X)
        self.tree.config(xscrollcommand=self.treeScroll2.set)
        
        self.style = ttk.Style()
        self.style.configure("Treeview", background = "silver",foreground = "black", rowheight = 30,fieldbackground = "silver")
        
        
        
        #fil = Label(self.root, text = "VISUALISEUR DE TRAFIC RESEAU ", font=("Helvetica",24,"Bold"),bg = "lightblue")
        label_filtre = Label(self.root, text = "Filtre  ", font=("Helvetica",12,'bold'),bg = "lightblue")
        self.filtre = Entry(self.root)
        label_filtre.pack()
        #self.filtre.grid(row = 2,column = 2)
        self.filtre.pack()
        
        
        self.tree ['columns'] = ("Port Source","@Ip Source","Arrows","@Ip Destination", "Port Destination", "Flags","Commentaire")
        
        self.tree.column ("Port Source",anchor = CENTER, width = 120)
        self.tree.column ("@Ip Source",anchor = CENTER, width = 120)
        self.tree.column ("Arrows",anchor = CENTER , width = 150)
        self.tree.column ("@Ip Destination",anchor = CENTER , width = 120)
        self.tree.column ("Port Destination",anchor = CENTER , width = 120)
        self.tree.column ("Flags",anchor = W , width = 150)
        self.tree.column ("Commentaire",anchor =W , width = 200)
        
        self.tree.column("#0", stretch=False)
        self.tree.heading("Port Source", text = "Port Source",anchor = CENTER)
        self.tree.heading("@Ip Source", text = "@Ip Source",anchor = CENTER)
        self.tree.heading("Arrows", text = "Arrows",anchor = CENTER)
        self.tree.heading("@Ip Destination", text = "@Ip Destination",anchor = CENTER)
        self.tree.heading("Port Destination", text = "Port Destination",anchor = W)
        self.tree.heading("Flags", text = "Flags",anchor = CENTER)
        self.tree.heading("Commentaire", text = "Commentaire",anchor = W)
        self.tree.pack(pady=30,padx = 10)
        
        self.btn2 = Button(self.root,text = "Soumettre Filtre", command = self.filter)
        self.btn2.place(x = 500, y = 20)
        #self.aFiltrer = self.filtre.get()
        
        #self.openfile()
        
        
    
    def insertDonnees(self,portsource,ipsource,ipdesti,portdestination,flagsActifs,hTTptype,id):
        
        self.tree.insert(parent = '',index = 'end',iid = id,text = '',values = (portsource,ipsource," -------> ",ipdesti,portdestination,flagsActifs,hTTptype ))
            
        
        """self.label_1 = tk.Label(self.frame2, text = str(portSrc), anchor = tk.W)
        self.label_1.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
        #self.label_1_window = self.canvas.create_window(100, 200, anchor=tk.NW, window = self.label_1)
        self.label1_text1 = self.canvas.create_text(70, 200, text = str(portSrc), anchor = tk.W)

        self.label_2 = tk.Label(self.frame2, text = str(portDest), anchor = tk.W)
        self.label_2.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
        #self.label_2_window = self.canvas.create_window(400, 180, anchor=tk.NW, window=self.label_2)
        self.label_2_text2 = self.canvas.create_text(405, 200, text = str(portDest),anchor=tk.W)
        
        self.label_3 = tk.Label(self.frame2, text = str(flag), anchor = tk.W)
        self.label_3.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
        self.label_3_window = self.canvas.create_window(220, 170, anchor=tk.NW, window=self.label_3)
        self.canvas.create_line(0, 0, 0, 600, arrow = LAST)
        self.canvas.create_line(0, 600, 800, 600, arrow = LAST) 
        """
        
    
    
    def openfile(self):
        
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Ouvrir un fichier",
                                          defaultextension=".txt",
                                          filetypes = (("Text files",
                                                        "*.txt"),))
        self.file = filename
        self.label_01.config(text="fichier choisi a visualiser : "+filename)
        self.label_01.place(x=100,y=500)
                           
        print("fichier .txt choisi : ",filename)
        if(filename):
            f = open(filename,'r')          #ouvrir et lire le fichier  source
            fil_src = f.readlines()
            f.close()
            a=self.D.isHexa(fil_src)
            print("le fichier est en hexa ? True or False: ",a)
            
        if a:
            liste = self.D.decoupe_trames(filename)
            hTTptype = "No header HTTP"
            hTTpStatus = "No status HTTP"
            for trame in liste:
                self.cpt = self.cpt + 1
                
                    
                dest=self.E.macDestination(trame)
                src=self.E.macSource(trame)
                type=self.E.ethernet_type(trame)
                
                if type=="IPv4":
                
                    ipVersion = self.I.versionIp(trame)
                    ipihl= self.I.ihl(trame)
                    iptos=self.I.tos(trame)
                    iptotallength = self.I.totalLength(trame)
                    ipidentificateur = self.I.id(trame)
                    ipflagR = self.I.flagBitR(trame)
                    ipflagdf = self.I.flagDontFragment(trame)
                    ipflagmf = self.I.flagMoreFragment(trame)
                    ipoffset = self.I.offset(trame)
                    ipttl = self.I.ttl(trame)
                    ipprotocole = self.I.protocole(trame)
                    ipHeaderChecksum = self.I.headerChecksum(trame)
                    ipsource = self.I.ipSource(trame)
                    ipdesti = self.I.ipDestination(trame)
                    ipoptiontype = self.I.ipoptionType(trame)
                    ipoptionlength = self.I.optionLength(trame)
                    ipoptionpadding = self.I.optionPadding(trame)
                    
                    if ipprotocole=="TCP":
                        r=int(self.I.ihl(trame) )
                        r=28+(r*2)        # r = longueure de l'entete ip + entete ethernet
                        portsource = self.T.portSource(trame,r)
                        portdestination = self.T.portDestination(trame,r)
                        nsequence = self.T.nSequence(trame,r)
                        nack = self.T.nAck(trame,r)
                        dataoffset = self.T.offset(trame,r)
                        reserved = self.T.reserved(trame,r)
                        flags = self.T.lesFlags(trame,r)
                        urg = self.T.urg(flags)
                        ack = self.T.ack(flags)
                        psh = self.T.psh(flags)
                        rst = self.T.rst(flags)
                        syn = self.T.syn(flags)
                        fin = self.T.fin(flags)
                        window = self.T.window(trame,r)
                        tcpChecksum = self.T.checksum(trame,r)
                        urgentpointer = self.T.urgentPointer(trame,r)
                        #optTcp=T.options(fichier_src,r)
                        
                        dict = {"URG":urg , "ACK":ack,"PSH":psh,"RST":rst,"SYN":syn,"FIN":fin} 
                        tmpf = ""
                        comment = ""
                        for cle, valeur in dict.items():
                            if valeur == str(1):
                                tmpf += " ["+cle+"]"
                            tmpf = tmpf
                        self.flagsActifs = tmpf
                        self.analyse = (src,dest,ipsource,ipdesti,portsource,portdestination,tmpf)
                        #print("analyse :",self.analyse)  
                    
                    
                        if portdestination=="80" or portsource=="80":
                            
                            hTTPval=self.T.httpval(trame)
                            hTTptype=self.T.httpType()
                            hTTpStatus = self.T.httpStatus()
            
                        self.insertDonnees(portsource,ipsource,ipdesti,portdestination,self.flagsActifs,("TCP /"+hTTptype+" & "+hTTpStatus),self.cpt )                 
                    else:
                        self.insertDonnees(" ",ipsource,ipdesti," "," ",hTTptype,self.cpt )
                else:
                    self.insertDonnees("","NOT IPV4","NOT IPV4","","",hTTptype,self.cpt)
            
            print("le nombre de trames est : ",self.cpt) 
            
        
    def analyse(self):
       return self.E.macSource,self.I.ipSource,self.T.portSource,self.E.macDestination,self.I.ipDestination,self.T.portDestination
    
    def getFlags(self):
        return self.flagsActifs
        
    def getFilename(self):
        return self.file
    
    def savefile(self):
        pass
    
        
    def estFiltrer(self,child_id):
        self.tree.focus(child_id) 
        self.tree.selection_set(child_id)
        self.style.map('Treeview', background=[('selected', 'blue')])
        
    def filter(self):
        user =  self.filtre.get()
        print("filtre a appliquer : "+ user)
        expressionADroite = re.search(".*=(.*$)", user).group(1)
        print("expressionADroite : ",expressionADroite)
        for child in self.tree.get_children():
            row = self.tree.item(child)["values"]
            id=self.tree.focus()
            #print(row)
            if re.search(str(expressionADroite), str(row)):
                self.tree.bind("<select>", self.estFiltrer(child))
                
                
        #col=int(self.tree.identify_column(event.x).replace('#',''))-1
        #Create list of 'id's
        #listOfEntriesInTreeView=self.tree.get_children()

        #for each in listOfEntriesInTreeView:
        #    print(self.tree.item(each)['values'][col])  #e.g. prints data in clicked cell
        #    self.tree.detach(each) 
            
                
                
        
if __name__ == '__main__':
    
    window = Window()
    window.cadre()
    #window.insertDonnees()
    window.root.mainloop()