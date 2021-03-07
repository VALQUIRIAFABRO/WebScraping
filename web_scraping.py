import wget
import os
import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
url = "https://images.google.com/imghp?hl=en&gl=ar&gws_rd=ssl"

browser.open(url)
print(browser.get_url())

# get HTML
browser.get_current_page()

# target search input
browser.select_form()
browser.get_current_form().print_summary()

# search for term
search_term = 'ocean'

# tag id from HTML
browser["q"] = search_term

# submit click search
browser.launch_browser()
response = browser.submit_selected()

# google will redirect to another page so will print the content of the response, should return the HTML
print("new url: ", browser.get_url())
print("response:\n ", response.text[:500])

# apend new url
new_url = browser.get_url()
browser.open(new_url)

# get HTML
page = browser.get_current_page()
all_images = page.find_all('img')
# all_images
# we don´t need the entire image tag, only the source value

# we dont need the entire image tag, only the source value
# target the source attribute
image_source = []
for image in all_images:
    image = image.get('src')
    image_source.append(image)

image_source

# using list comprehension
image_source = [image for image in image_source if image.startswith('https')]
image_source

# saving the images
# pip install python3-wget

path = os.getcwd()

# to create a dynamic name of the path
path = os.path.join(path, search_term + 's')

# create the directory
os.mkdir(path)

path

# download the images
# loop will help to rename the individual images
counter = 0
for image in image_source:
    save_as = os.path.join(path, search_term + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
