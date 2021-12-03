import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_player import st_player
import numpy as np
from sklearn.neighbors import NearestNeighbors

link = "https://raw.githubusercontent.com/marcpiveteau/projet2/main/tableallege4.csv"
table = pd.read_csv(link)

link2="https://raw.githubusercontent.com/marcpiveteau/projet2/main/tablecompl3.csv"
tablelien =pd.read_csv(link2)


st.title('Bienvenue sur Marcflix!')


table2 =table[['titre','isAdult', 'année_du_film','durée_du_film','notes_du_film', 'numVotes','nb_genres']]

def description(x):
    st.write("c'est un film de ", x.iloc[0,2]," réalisé par", x.iloc[0,6], "sénarisé par ",x.iloc[0,9])
    st.write("c'est un film", x.iloc[0,4], "qui a une note moyenne par les téléspectateur de", x.iloc[0,7], "avec ",x.iloc[0,8], "de personnes qui ont voté" )
    st.write("il dure ", x.iloc[0,3]," minutes et", x.iloc[0,10], " jouent dedans")

def erreur():
    st.write("pas de film trouvé, attention au majuscule et et l'ortographe")
    st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/projet2/main/not%20found.gif)")
    st.stop()

recherche = st.selectbox('tu veux rechercher ton film par :',['titre','acteur ou actrice'])
choix = st.text_input('ecrit ta recherche')
if recherche=='titre':
    lignedufilm = table.loc[table['titre'].str.contains(choix)]
    if len(lignedufilm)==0:
        erreur()
    if len(lignedufilm) >1:
        st.write('il y a ', len(lignedufilm), 'de votre film le quel choisissez vous')
        for i in range (len(lignedufilm)):
            st.write(lignedufilm.iloc[i,5], ' réalisé par ', lignedufilm.iloc[i,6],'en',lignedufilm.iloc[i,2], '  si oui tapez :', i)
            st.write('------------------')
if recherche=='acteur ou actrice':
    lignedufilm = table.loc[table['acteur_actrisse'].str.contains(choix)]
    if len(lignedufilm)==0:
        erreur()
    if len(lignedufilm) >1:
        st.write('il y a ', len(lignedufilm), 'de votre film le quel choisissez vous')
        for i in range (len(lignedufilm)):
            st.write(lignedufilm.iloc[i,5], ' réalisé par ', lignedufilm.iloc[i,6],'en',lignedufilm.iloc[i,2], '  si oui tapez :', i)
            st.write('------------------')   
choixf = st.number_input('votre choix :',step=1)
lignefilm= lignedufilm[lignedufilm['numVotes'] ==lignedufilm.iloc[choixf,8]]
    #if len(lignedufilm) ==1:
        #lignefilm=lignedufilm
i = 1
def recomandation(x,cv):
    lignefilm2 = x[['isAdult', 'année_du_film','durée_du_film','notes_du_film', 'numVotes','nb_genres']]
    filmchoisi = x.iloc[0,5]
    st.write(filmchoisi)
    descrfilm = table[table['titre']==filmchoisi]
    description(descrfilm)
    testlienfilmchoisi = tablelien[tablelien['title']==filmchoisi]
    if len(testlienfilmchoisi)==1:
        lienfilm = testlienfilmchoisi.iloc[0,3]
        st_player(lienfilm)

        
  
    if recherche=='titre':
        table3= table.loc[table['titre'].str.contains(choix)]
        table4 =table3[['isAdult', 'année_du_film','durée_du_film','notes_du_film', 'numVotes','nb_genres']]
        table4.dropna(inplace=True)
    if recherche=='acteur ou actrice':
        table3= table.loc[table['acteur_actrisse'].str.contains(choix)]
        table4 =table3[['isAdult', 'année_du_film','durée_du_film','notes_du_film', 'numVotes','nb_genres']]
        table4.dropna(inplace=True)




    from sklearn.neighbors import NearestNeighbors
    if 3>len(table4)>1:
      Y = table4
      distanceKNN = NearestNeighbors(n_neighbors=2).fit(Y)
      arraydesvoisin = distanceKNN.kneighbors(lignefilm2)
      listvoisin = table3.iloc[arraydesvoisin[1][0]]
      nom2 =listvoisin['titre'].tolist()
    if len(table4)>2:
      Y = table4
      distanceKNN = NearestNeighbors(n_neighbors=3).fit(Y)
      arraydesvoisin = distanceKNN.kneighbors(lignefilm2)
      listvoisin = table3.iloc[arraydesvoisin[1][0]]
      nom2 =listvoisin['titre'].tolist()

    table5= table.loc[table['Réalisateur'].str.contains(x.iloc[0,6])] 
    try:
        index2 = listvoisin.index.tolist()
    except:
        index2=lignedufilm
    for i in range (1,3):
      try:
        table5.drop(index=index2[i], axis=0, inplace=True)
      except:
        pass
    table6 =table5[['isAdult', 'année_du_film', 'durée_du_film', 'notes_du_film', 'numVotes', 'nb_genres']]

    if 3>len(table6)>1:
      Z = table6
      distanceKNN = NearestNeighbors(n_neighbors=2).fit(Z)
      arraydesvoisin1 = distanceKNN.kneighbors(lignefilm2)
      listvoisin2 = table5.iloc[arraydesvoisin1[1][0]]
      nom3 =listvoisin2['titre'].tolist()
    if len(table6)>2:
      Z = table6
      distanceKNN = NearestNeighbors(n_neighbors=3).fit(Z)
      arraydesvoisin1 = distanceKNN.kneighbors(lignefilm2)
      listvoisin2 = table5.iloc[arraydesvoisin1[1][0]]
      nom3 =listvoisin2['titre'].tolist()


    lignefilm3 = descrfilm
    lignefilm3['genres'] = lignefilm3['genres'].str.split(',')
    genreexp1 = lignefilm3.iloc[0,4]
    if len(genreexp1)==1:
        genrerecherche = genreexp1[0]
        tablegenrevoisin =table.loc[table['genres'].str.contains(genrerecherche)]
    if len(genreexp1)>1:
        genrerecherche = genreexp1[0]
        tablegenrevoisi =table.loc[table['genres'].str.contains(genrerecherche)]
        genrerecherche2 =genreexp1[1]
        tablegenrevoisin=tablegenrevoisi.loc[table['genres'].str.contains(genrerecherche2)]
    for i in range (1,3):
      try:
        tablegenrevoisin.drop(index=index2[i], axis=0, inplace=True)
      except:
        pass
    X = tablegenrevoisin[['isAdult', 'année_du_film','durée_du_film','notes_du_film', 'numVotes','nb_genres']]
    distanceKNN = NearestNeighbors(n_neighbors=5).fit(X)
    arraydesvoisin = distanceKNN.kneighbors(lignefilm2)
    listvoisin = tablegenrevoisin.iloc[arraydesvoisin[1][0]]
    nom =listvoisin['titre'].tolist()
    st.write('pour ce film on vous recommande :')


    listedeschoix=[]
    if 3>len(table4)>1:
        film21 = tablelien[tablelien['title']==nom2[1]]
        if len(film21)==1:
            reco1= nom2[1]
            listedeschoix.append(reco1)
        if len(film21)!=1:
            reco1 = nom2[1]
            listedeschoix.append(reco1)
    if len(table4)>2:
        film22 = tablelien[tablelien['title']==nom2[1]]
        film23 = tablelien[tablelien['title']==nom2[2]]
        if len(film22)==1:
            reco1 = nom2[1]
            listedeschoix.append(reco1)
        if len(film22)!=1:
            reco1 = nom2[1]
            listedeschoix.append(reco1) 
        if len(film23)==1:
            reco2 = nom2[2]
            listedeschoix.append(reco2)
        if len(film23)!=1:
            reco2 = nom2[2]
            listedeschoix.append(reco2)
    if 3>len(table6)>1:
        film31 = tablelien[tablelien['title']==nom3[1]]
        if len(film31)==1:
            reco3 = nom3[1]
            listedeschoix.append(reco3)
        if len(film31)!=1:
            reco3 = nom3[1]
            listedeschoix.append(reco3)
    if len(table6)>2:
        film32 = tablelien[tablelien['title']==nom3[1]]
        film33 = tablelien[tablelien['title']==nom3[2]]
        if len(film32)==1:
            reco3 = nom3[1]
            listedeschoix.append(reco3)
        if len(film32)!=1:
            reco3 = nom3[1] 
            listedeschoix.append(reco3)
        if len(film33)==1:
            reco4 = nom3[2]
            listedeschoix.append(reco4)
        if len(film33)!=1:
            reco4 = nom3[2]
            listedeschoix.append(reco4)

    
    film1 = tablelien[tablelien['title']==nom[1]]
    film2 = tablelien[tablelien['title']==nom[2]]
    film3 = tablelien[tablelien['title']==nom[3]]
    film4 = tablelien[tablelien['title']==nom[4]]
    if len(film1)==1:
        reco5 = nom[1]
        listedeschoix.append(reco5) 
    if len(film1)!=1:
        reco5 = nom[1]
        listedeschoix.append(reco5)
    if len(film2)==1:
        reco6 = nom[2]
        listedeschoix.append(reco6)
    if len(film2)!=1:
        reco6 = nom[2]
        listedeschoix.append(reco6)
    if len(film3)==1:
        reco7 = nom[3]
        listedeschoix.append(reco7)
    if len(film3)!=1:
        reco7 = nom[3]
        listedeschoix.append(reco7)
    if len(film4)==1:
        reco8 = nom[4]
        listedeschoix.append(reco8)
    if len(film4)!=1:
        reco8 = nom[4]
        listedeschoix.append(reco8)
    position = str(cv)
    choixdereco = st.selectbox(position +'quel film choisit dans la recommandation?',listedeschoix)
    descrfilm1 =table[table['titre']==choixdereco]
    lienteaser =tablelien[tablelien['title']==choixdereco] 
    description(descrfilm1)
    if len(lienteaser)==1:
        if(st.button('voir teaser '+choixdereco)):
                lien1=lienteaser.iloc[0,3]
                st.write(lien1)
                st_player(lien1)
    lignefilm=descrfilm1
    choixdecontinuer = st.selectbox(position + 'voulez vous faire continuer la reco?',['non', 'oui'])
    if choixdecontinuer=='non':
        st.stop()
    if choixdecontinuer=='oui':
        i += 1
        recomandation(lignefilm,i)

recomandation(lignefilm,i)
        
