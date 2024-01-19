import pandas as pd
from bs4 import BeautifulSoup
import requests
import random


response=requests.get("https://unsplash.com/s/photos/domestic-cat")
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
all_cat_image_tags=soup.select('.MorZF img')
i=1
img_urls=[]
animal_type=[]
for img in all_cat_image_tags:
    img_urls.append([img['src']])
    animal_type.append('cat')


response=requests.get("https://unsplash.com/s/photos/animal")
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
all_animal_image_tags=soup.select('.MorZF img')
i=1
for img in all_animal_image_tags:
    img_urls.append([img['src']])
    animal_type.append('not a cat')

zipped = list(zip(animal_type, img_urls))
random.shuffle(zipped)
animal_type, img_urls = zip(*zipped)

dataset=pd.DataFrame({
    'type':animal_type,
    'url':img_urls
})

dataset.to_csv('datasheet.csv')





