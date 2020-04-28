import requests
from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt
import cv2

def get_unique_occupations(celebs):
    unique_occupations = []
    for i in range(0,len(celebs)):
        length_of_occupation=len(celebs[i].occupation)
        for j in range(0,length_of_occupation):
            if celebs[i].occupation[j] not in unique_occupations:
                unique_occupations.append(celebs[i].occupation[j])
    return unique_occupations

def get_barplot(stats,array_of_occupations):
    plt.xticks(range(0,len(stats)),array_of_occupations)
    plt.xticks(rotation=90)
    plt.bar(range(0,len(array_of_occupations)),stats)
    plt.title('Bar plot of various Skills')
    plt.show()

def open_image(name):
    img = cv2.imread(name+'.jpg')
    cv2.imshow(name,img)
    while True:
        cv2.imshow(name,img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            cv2.destroyAllWindows()
            break
def get_skill_name(person,celebs):
    for celeb in celebs:
        if person == celeb.name:
            return celeb.occupation
            break
def get_stats(occupations,celebs):
    stats = [0]*len(occupations)
    for j in range(0,len(celebs)):
        for i in range(0,len(celebs[j].occupation)):
            stats[occupations.index(celebs[j].occupation[i])] +=1
    return stats

def whoiswho(string,celebs):
    array = []
    for celeb in celebs:
        if string in celeb.occupation:
            array.append(celeb.name)
    return array

class Celebrity:
    def __init__(self):
        self.name = None
        self.imagelink=None
        self.occupation=None
        self.linkpersonal = None
    def get_occupation(self):
        source_code = requests.get(self.linkpersonal)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,features = "lxml")
        for link in soup.findAll('div',{'class':'artist_designation'}):
            designation = link.string
            designation = designation.replace('\t','')
            designation = designation.replace('\n','')
            designation = designation.replace(' ','')
            self.occupation = designation.split(',')          
    def get_images(self):
        url = self.imagelink
        filename = '{}.jpg'.format(self.name)
        urllib.request.urlretrieve(url=url,filename=filename)

class ListOfCelebrities:
    link = 'https://in.bookmyshow.com/person'
    def __init__(self):
        self.list_of_occupation = None
        self.list_of_names = []
        self.list_of_images  =[]
        self.list_of_personallinks=[]

    @staticmethod
    def get_text(link):
        source_code = requests.get(link)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,features="lxml")
        return soup
    
    def get_links(self,soup):
        for link in soup.findAll('a',{'class':'__art-name'}):
            title = link.string
            self.list_of_names.append(title)
        for link in soup.findAll('a',{'class':'__art-name'}):
            href = link.get('href')
            self.list_of_personallinks.append(href)
    def get_images(self,soup):
        for name in self.list_of_names:
            for link in soup.findAll('img',{'title':name}):
                src = 'https:'+link.get('src')
                self.list_of_images.append(src)
    @classmethod
    def get_soup(cls):
        soup = ListOfCelebrities.get_text(cls.link)
        return soup

bookmyshow = ListOfCelebrities()
soup = bookmyshow.get_soup()
bookmyshow.get_links(soup)
bookmyshow.get_images(soup)

celebs = []
for i in range(0,len(bookmyshow.list_of_names)):
    celebs.append(Celebrity())
for i in range(0,len(bookmyshow.list_of_names)):
    celebs[i].name = bookmyshow.list_of_names[i]
    celebs[i].imagelink = bookmyshow.list_of_images[i]
    celebs[i].linkpersonal = 'https://in.bookmyshow.com'+bookmyshow.list_of_personallinks[i]

for celeb in celebs:
    celeb.get_occupation()
    celeb.get_images()
'''this loop takes care of downloading the images'''
array_of_occupations = get_unique_occupations(celebs)
stats = get_stats(array_of_occupations,celebs)
'''The above 2 arrays are required for the bar plot'''
#bar_plot
get_barplot(stats,array_of_occupations)

print('\n')
print('Sample for whoiswho function:')
print('this fucntion lists out all the celebrities who have a particular skill')
print('for example, Let us see who all have the skill of a Writer')
print(whoiswho('Writer',celebs))

print('\n')
print('Sample for getting the occupation of a particular celebrity')
print('Let\'s try this function on the celebrity \'Mani Ratnam\' ')
print(get_skill_name('Mani Ratnam',celebs))
print('\n')

print('Here is the example of open_image function')
print('For example, lets open the image of Amitabh Bachchan')
print('This function should create a window of the name of the celebrity including his image')
open_image('Amitabh Bachchan')
