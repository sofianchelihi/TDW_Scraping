import requests
from bs4 import BeautifulSoup
import random

def desc(arg):
    if arg>=1 and arg<=20:
        return 'est un plat algerien connu facile a preparer qui contient des ingredient disponible,ce plat peut etre servi en plusieur fetes'
    if arg>=21 and arg<=30:
        return 'est un entree algerien connu facile a preparer qui contient des ingredient disponible,ce entre peut etre servi avant les differents plats'
    if arg>=31 and arg<=40:
        return 'est un boisson facile a preparer qui contient des ingredient disponible,qui peut etre servi en plusieur fetes'
    if arg>=41 and arg<=50:
        return 'est un desser facile a preparer qui contient des ingredient disponible,qui peut etre servi en plusieur fetes apres les repas'

tab=[]

def getHealthy():
    cmp = random.randint(0,50)
    if cmp<25 :
        return True
    else:
        return False


def getTimeR():
    return str(random.randint(0,10))


def getCalories():
    return random.randint(0,250)

class recette:
    titre_recette ='' 
    lien_image =''
    description =''
    categorie =''
    temp_prepa =''
    temp_repo =''
    temp_cuis =''
    new = False
    valide = True
    etapes = []
    ingredient=[]


liens = [
    "http://cuisinealgerie.com/category/plat-principal/riz-plat-principal/",
    "http://cuisinealgerie.com/category/plat-principal/pates/",
    "http://cuisinealgerie.com/category/entrees/",
    "http://cuisinealgerie.com/category/cuisine-algerienne/boissons/",
    "http://cuisinealgerie.com/category/desserts/"
]


for x in liens:
    result = requests.get(x)
    src= result.content
    page = BeautifulSoup(src,"lxml")
    cards = page.find_all("div",{"class":"post"})
    for i in range(len(cards)):
        cl = recette()
        ingredients=[]
        etapes=[]
        cl.lien_image = cards[i].find("img").get("src")
        cl.categorie = cards[i].find_all("h6",{"class":"category"})[0].text
        cl.titre_recette = cards[i].find_all("h4",{"class":"news-title"})[0].text
        href= cards[i].find_all("h4",{"class":"news-title"})[0].find("a").get("href")
    
        lien = requests.get(href)
        srcr = lien.content
        pager = BeautifulSoup(srcr,'lxml')

        cl.description = cl.titre_recette
           
        cl.temp_prepa = pager.find_all("span",{"class":"tempsprepa"})[0].next_sibling.text
        cl.temp_prepa=cl.temp_prepa.replace('min','')
        cl.temp_repo=getTimeR()
        
        cl.temp_cuis = pager.find_all("span",{"class":"tempscuisson"})[0].next_sibling.text
      
        if( str(pager.find_all("div",{"class":"post-content"})[0].find_all("ul")[0].text).find("Temps de\u00A0préparation")>0):
            p=1
        else:
            p=0
    
        ingr = pager.find_all("div",{"class":"post-content"})[0].find_all("ul")[p].find_all("li") 
        for j in range(len(ingr)):
            ingredients.append(ingr[j].text)
    
        cl.ingredient = ingredients
              
        test1 = pager.find_all("p",string="Préparation :")
        if(len(test1)>0):
            test=test1[0].find_next_sibling()
        else:
            test=  pager.find_all("p",string="Préparation :\u00A0")[0].find_next_sibling()
         
        if(test.name=="ul"):
            eta=test.find_all("li")
        else:
            eta=test.find("ul").find_all("li")
    
        for j in range(len(eta)):
            etapes.append(eta[j].text)
        
        cl.etapes = etapes
        tab.append(cl)
    

    
    
    
    
    
    
    

    
    


r = open("recette.txt", "a",encoding="utf-8")
e = open("etapes.txt", "a",encoding="utf-8")
i = open("ingr.txt", "a",encoding="utf-8")
ri = open("recette_ingr.txt", "a",encoding="utf-8")
etapes = ""
recettes = ""
ingr = ""
recette_ingr=""
ingredient_cmp=1

for k in range(len(tab)):
    recette_cmp = k+1
    recettes +="("
    recettes +="'"+tab[k].titre_recette+"',"
    recettes +="'http://localhost/Projet_TDW/public/assets/images/r"+str(recette_cmp)+"',"
    recettes +="'"+tab[k].description+" "+desc(recette_cmp)+"',"
    recettes +=tab[k].temp_prepa+","
    recettes +=tab[k].temp_repo+","
    recettes +=tab[k].temp_cuis+","
    recettes +="false,"
    recettes +="' ',"
    recettes +="true"
    recettes+="),\n"
    for j in range(len(tab[k].etapes)):
        etape_cmp = j+1
        etapes +="("
        etapes +=str(recette_cmp)+","
        etapes +=str(etape_cmp) +","
        etapes +="'"+tab[k].etapes[j]+"'),\n"
    for m in range(len(tab[k].ingredient)):
        ingr +="("
        ingr +="'"+tab[k].ingredient[m]+"',"
        ingr +=str(getHealthy())+","
        ingr +=str(getCalories())+")\n"
        
        recette_ingr +="("
        recette_ingr +=str( recette_cmp )+","
        recette_ingr +=str(ingredient_cmp)+")\n"   
        ingredient_cmp+=1

r.write(recettes)
i.write(ingr)
e.write(etapes)   
ri.write(recette_ingr)        
    
     
    
    
    
    