import requests
import bs4
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

tab=[]

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

result = requests.get("http://cuisinealgerie.com/category/cuisine-algerienne/couscous/")
src= result.content
page = BeautifulSoup(src,"lxml")
cards = page.find_all("div",{"class":"post"})
for i in range(len(cards)):
#for i in [0,1,2,3]:
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
    
    
    cl.description = 'Plat algerienne qui peut etre server on plussieur fetes en plus elle est fasile a preparer et ne prend pas beaucoup de temps'
    cl.temp_prepa = pager.find_all("span",{"class":"tempsprepa"})[0].next_sibling.text
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
    
    


f = open("tmp.txt", "w",encoding="utf-8")
for k in range(len(tab)):
#for k in [0,1,2,3]:
    f.write("\n\n\n\n******************************************************************************\n\n")
    f.write("titre recette :  "+tab[k].titre_recette+"\n")
    f.write("categorie :  "+tab[k].categorie+"\n")
    f.write("description :  "+tab[k].description+"\n")
    f.write("lien_image :  "+tab[k].lien_image+"\n")
    f.write("temp_prepa :  "+tab[k].temp_prepa+"\n")
    f.write("temp_repo :  "+tab[k].temp_repo+"\n")
    f.write("temp_cuis :  "+tab[k].temp_cuis+"\n")
    
    f.write("\n Les ingredients  :\n")
    
    for item in tab[k].ingredient:
        f.write("              * "+item+".\n")  
    
    
    f.write("\n  Les etapes  :\n")
    for item in tab[k].etapes:
        f.write("              * "+item+".\n")
  
  
f.close()  
    
    
    
    