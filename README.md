# Code_for_BiPolarIntern
Title of the Code : Crawl popular websites & create a database of Indian movie celebrities with their images and personality traits.

Good Evening,

I've written my code in Python.
I have written a web crawler which crawls the website 'bookmyshow' and extracts the celebrity's information listed in the website. In this case there are around 30 celebrities with different skill set.
Through this code, we can download the images of those celebrities and store them in the folder which contains the python code.

I have written 5 functions in the code which are as follows:

1)get_occupation : This function creates an array of skills of a particular celebrity.
2)download_images : This function downloads the images of the reqired celebrity
3)whoiswho : This function returns the list of celebrities who have a particular skill. for example whoiswho('Singer',celebrities) gives a list of people who are designated as singers.
4)Histogram: A histogram is created for all the skills.
5)open_image: This function opens an image, the window exits until and unless the user presses the letter 'q'

In the code, I have created 2 objects namely Celebrity and ListOfCelebrities.

The former one is kind of a blueprint wherein it stores the information of name,occupation,link to the personal page, link to the image
The latter one stores the information of a website which includes list of all celebrities, their occupations, images and their perosnal links.

All the information of the celebrities is stored in the array celebs.

python IDE used - spyder(Anaconda)
