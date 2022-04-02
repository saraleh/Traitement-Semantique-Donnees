from tkinter import *
import _tkinter
from tkinter import Checkbutton
from rdflib import Graph
import rdflib
from sklearn.metrics import confusion_matrix
from py_stringmatching import Levenshtein
from py_stringmatching import Jaccard
from py_stringmatching import Jaro
from rdflib import Graph



fichier = open("dataa.txt", "w")

urlsource = 'https://raw.githubusercontent.com/DOREMUS-ANR/doremus-playground/master/DHT/source.ttl'
urltarget = 'https://raw.githubusercontent.com/DOREMUS-ANR/doremus-playground/master/DHT/target.ttl'


# creation de graphe
g1 = Graph()
g2 = Graph()
# Parse in an RDF file hosted on the Internet
g1.parse(urlsource, format='ttl')
g2.parse(urltarget, format='ttl')

from rdflib.namespace import FOAF, XSD

req1 = """
    PREFIX ecrm:  <http://erlangen-crm.org/current/> 

    SELECT ?p ?P102_has_title
    WHERE {
        ?p ecrm:P102_has_title ?P102_has_title.

    }
"""

req2 = """
    PREFIX ecrm:  <http://erlangen-crm.org/current/> 

    SELECT ?p ?P3_has_note 
    WHERE {
        ?p ecrm:P3_has_note ?P3_has_note .

    }
"""

req3 = """
    PREFIX mus: <http://data.doremus.org/ontology#> 

    SELECT ?p ?U12_has_genre 
    WHERE {
        ?p mus:U12_has_genre ?U12_has_genre .

    }
"""
req4 = """
    PREFIX mus: <http://data.doremus.org/ontology#> 

    SELECT ?p ?U11_has_key 
    WHERE {
        ?p mus:U11_has_key ?U11_has_key .

    }
"""

req5 = """
    PREFIX mus: <http://data.doremus.org/ontology#> 

    SELECT ?p ?U13_has_casting 
    WHERE {
        ?p mus:U13_has_casting ?U13_has_casting.

    }
"""

# Mesure de similarite Identity
def Identity(a, b):
    for r in g1.query(req1):
        for t in g2.query(req1):
            if r[a] == t[a]:
                 print(r[b])


seuil = 0.5
jaro = Jaro()
lev = Levenshtein()
jaccard = Jaccard()


def function_has_title(similarityList,seuil):
    pourcentage = 0
    longeur = len(g1.query(req1))
    for r in g1.query(req1):
        pourcentage +=1
        print((pourcentage*100)/longeur)
        for p in g2.query(req1):
            score = fun_get_similarity(similarityList,str(r["P102_has_title"] ), str(p["P102_has_title"]))
            if (score >= seuil):
                fichier.write("<"+str(r["p"]) +"> owl:sameAs <" + str(p["p"])+">.\n")
    fichier.close()

def function_has_note(similarityList,seuil):
    pourcentage = 0
    longeur = len(g1.query(req2))
    for r in g1.query(req2):
        pourcentage +=1
        print((pourcentage*100)/longeur)
        for p in g2.query(req2):
            score = fun_get_similarity(str(r["P3_has_note"]), str(p["P3_has_note"]))
            if (score >= seuil):
                fichier.write("<" + str(r["p"]) + "> owl:sameAs <" + str(p["p"]) + ">.\n")
                print("<" + str(r["p"]) + "> owl:sameAs <" + str(p["p"]) + ">.\n")

def function_has_genre(similarityList,seuil):
    pourcentage = 0
    longeur = len(g1.query(req3))
    for r in g1.query(req3):
        pourcentage +=1
        print((pourcentage*100)/longeur)
        for p in g2.query(req3):
            score = fun_get_similarity(str(r["U12_has_genre"]), str(p["U12_has_genre"])) 
            if (score >= seuil):
                fichier.write("<" + str(r["p"]) + "> owl:sameAs <" + str(p["p"]) + ">.\n")
                #print("<" + str(r["p"]) + "> owl:sameAs <" + str(p["p"]) + ">.\n")

def function_has_key(similarityList,seuil):
    pourcentage = 0
    longeur = len(g1.query(req4))
    for r in g1.query(req4):
        pourcentage +=1
        print((pourcentage*100)/longeur)
        for p in g2.query(req4):
            score= fun_get_similarity(str(r["U11_has_key"]), str(p["U11_has_key"])) 
            if (score >= seuil):
                fichier.write("<" + str(r["p"]) + "> owl:sameAs <" + str(p["p"]) + ">.\n")

def function_has_casting(similarityList,seuil):
    pourcentage = 0
    longeur = len(g1.query(req5))
    for r in g1.query(req5):
        pourcentage +=1
        print((pourcentage*100)/longeur)
        for p in g2.query(req5):
            score = fun_get_similarity(str(r["U13_has_casting"]), str(p["U13_has_casting"]))
            if (score >= seuil):
                fichier.write("<" + str(r["p"]) + "> owl:sameAs <" + str(p["p"]) + ">.\n")





def fun_get_similarity(similarityList ,text1,text2):
    sumOfPonderation=0
    score = 0
    for i in similarityList:
        tab = i.split(":")
        if tab[0]=="Levenshtein":
            score+=lev.get_sim_score(text1, text2) * float(tab[1])
            sumOfPonderation += float(tab[1])
        if tab[0] =="Jaro":
            score+=jaro.get_sim_score(text1, text2) * float(tab[1])
            sumOfPonderation += float(tab[1])
        if tab[0] == "Jaccard":
            score+=jaccard.get_sim_score(text1, text2) * float(tab[1])
            sumOfPonderation += float(tab[1])
        return round(score/sumOfPonderation,3)
