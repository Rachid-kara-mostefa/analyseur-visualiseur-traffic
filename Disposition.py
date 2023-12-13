class Disposition(object):
    def __init__(self): 
        """ Constructeur de la mise en forme"""
    trame=""
    
    def decoupe_trames(self,fichier):
        trames =[]
        cur=[]
        with open(fichier,'r') as f:
            lines=f.readlines()
            first=lines[0]
            print(f.read())
            pr='0000'
            for line in lines:
                l=line.strip().split(' ')
                if l[0]=='0000':
                    if cur !=[]:
                        trames.append(cur)
                        cur=[]
                
                line_sansE = l[1:]
                cur.extend(line_sansE)
                pr=l[0]
                pr=line_sansE
        trames.append(cur)
        a=[]
        tks=[]
        for trame in trames:
            sss = "".join(trame)
            tks.append(sss)   
        return tks
    
    def enleveOffset(self,fichier):  
        trameSansOffsets=""
        for line in fichier:              
            tt = line[5:]
            trameSansOffsets +=tt
        return trameSansOffsets

    def enleveEspace(self,fichier):
        trameSansEspaces=""
        for line in fichier:              
            tt = "".join((line).split())        
            trameSansEspaces +=tt
        return trameSansEspaces
      
    def isHexa(self,fichier):
        trameSansEspaces = self.enleveEspace(fichier)
        try: 
            trameDec=int(trameSansEspaces, 16) 
            b=True                                   
        except: 
            b=False 
            print("attention le fichier n'est pas en hexadecimal")
        return b