# 1 Message: Write a function called display_message() that prints one sentence telling everyone what you are learning in this chapter. Call the function, and make sure the message displays correctly.
def display_message():
    print('I am learning about functions in this chapter')

display_message()

# 2 Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is... Call the function, making sure to include a book title as an argument in the function call. 
def favorite_book(title, author):
    print(f"\nOne of my favorite books is {title.title()} by {author.title()}.")

favorite_book('the god delusion','richard dawkins')

# 3 T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
def make_shirt(size, message):
    print(f"\nThe t-shirt will be a size {size} and display the message '{message}'.")

make_shirt('medium','I ♥︎ NY')

def make_shirt(message, size='large'):
    print(f"\nThe t-shirt will be a size {size} and display the message '{message}'.")

make_shirt(message ='I ♥︎ Python')

# 5 Cities: Write a function called describe_city() that accepts the name fo a city and its given country. The function should provide a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for 3 different cities, at least one that is not in the default country.
def describe_city(city, country= 'usa'):
    if country=='usa':
        print(f"{city.title()} is in the {country.upper()}.")
    else:
        print(f"{city.title()} is in {country.title()}.")

describe_city('new york')
describe_city('los angeles')
describe_city('london', 'england')

# 6 City Names: Write a function called city_country() that takes in the name of a city and its country. 
def city_country(city,country):
    print(f"{city.title()}, {country.title()}")

city_country('paris','france')
city_country('tokyo','japan')
city_country('berlin','germany')

# 7 Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
def make_album(artist_name, album_title,tracks=None):
    album = {'artist':artist_name,'title':album_title}
    if tracks:
        album['tracks'] = tracks
    return album
album1 = make_album('dance gavin dance','afterburner')
print(album1)
album2 = make_album('a day to remember','homesick',12)
print(album2)
album3 = make_album('as blood runs black', 'allegiance')
print(album3)

# 8 User Albums: Start with your program from the Exercise 7. Write a while loop that allows users to enter an album's artist and title. Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure to include a quit value in the while loop.
def make_album(artist_name, album_title, tracks=None):
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if tracks is not None:
        album['tracks'] = tracks
    return album

while True:
    print("\nEnter album information (or 'quit' to exit):")
    artist = input("Enter the artist name: ")
    if artist.lower() == 'quit':
        break
    title = input("Enter the album title: ")
    if title.lower() == 'quit':
        break

    album = make_album(artist, title)
    print(album)

