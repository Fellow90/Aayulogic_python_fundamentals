import requests



url = 'https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json'
response = requests.get(url)
if response.status_code == 200:
    books = response.json()
else:
    print("Failed to fetch data from the URL")



'''
print("BOOKS MORE THAN 200 PAGES: ")

booksMorethan200pages = []
count = 0
for book in books:
    page = book['pages']
    if page > 200:
        booksMorethan200pages.append(book)
        count+=1
print(f"There are {count} books more than 200 pages in the file.\n THEY ARE:")

## print books with more than 200 pages
for i in booksMorethan200pages:
    print("\n",i)

countrySeparatedBooks = {}
for book in books:
    country = book['country']
    if country not in countrySeparatedBooks:
        countrySeparatedBooks[country] = [book]
    else:
        countrySeparatedBooks[country].append(book)
    # countrySeparatedBooks[country] = [book] if country not in countrySeparatedBooks else countrySeparatedBooks[country].append(book)
    
print("The books distinguished are: ")
for key,value in countrySeparatedBooks.items():
    print("\n",key,":",value)'''

listofkeys = []
for key in books[0].keys():
    listofkeys.append(key.capitalize())

print(listofkeys)




# a = 'author'.capitalize()
# print(a)


'''countryFrance = [book for book in books if book['country'] == 'France']
for i in countryFrance:
    print("\n",i)'''

