# -*- coding: utf-8 -*-
import pandas as pd
from math import sin,cos,pi,acos,asin

def deg2rad(dd):
    return dd/180*pi
    
   
#fname = "C:\Users\dorin\Desktop\py\data1.csv"
var = pd.read_csv('C:\Users\dorin\Desktop\py\data1.csv')
#print var

#print var["IDBASE"] #premiere colonne
#print var["X"] #2 colonne
#print var["Y"] #3 colonne

#metre ds une liste
tab1 = list(var["IDBASE"])
tab2 = list(var["X"])
tab3 = list(var["Y"])


tab_i = []
tab_j = []
tab_X = []
tab_Y = []

#print tab1, tab2, tab3
for i in range(0,len(tab2)-1):
    #print ("hello")
    lat1=deg2rad(tab2[i])
    long1=deg2rad(tab3[i])
    for j in range(1, len(tab3)-1):        
        lat2 = deg2rad(tab2[j])
        long2 = deg2rad(tab3[j])
             
        RT = 6378137 #Rayon terre
        #print "ID1:"+str(tab1[i])+" "+"ID2:"+str(tab1[j])+" dist sans acos: "+str(S1)+" dist avec acos: "+str(S)+" d= "+str(distance)
        # distance entre les 2 points, comptée sur un arc de grand cercle
        #return S*RT
        # angle en radians entre les 2 points
        S1 = (sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(long2-long1))
        if S1<1 :
            S =acos(S1)#le pb est le acos
            distance=S*RT
        if distance<50 :
            #écrire dans le fichier distance.csv  sous la forme 
            # ID1,ID2
            #raw_data = {'ID1':[tab1[i]], 'ID2':[tab1[j]], 'distance':[distance]}
            #df = pd.DataFrame(raw_data)
            tab_i.append(tab1[i])#rajoute un elem
            tab_j.append(tab1[j])
            tab_X.append(tab2[i])
            tab_Y.append(tab3[j])

            
df1 = pd.DataFrame(tab_i)
df2 = pd.DataFrame(tab_j)
df3 = pd.DataFrame(tab_X)
df4 = pd.DataFrame(tab_Y)
            
df0 = df1 #df0['a'] = df1 comme si on ecrivais ça
df0['b'] = df2
df0['c'] = df3
df0['d'] = df4

df0.columns = ['ID1','ID2','X' ,'Y']
export_csv = df0.to_csv('C:\Users\dorin\Desktop\py\distance.csv' , index = False)  
print (df0)               
                      
#Créer un graphe
#Lire chaque ligne de ton fichier csv
#pour chaque ligne, réupérer un node1 = ligne[0] et un node2=ligne[1]
#créer ensuite un edge avec node1 et node2
#dessiner le graphe
#plt.show()
     
#print len(tab2)