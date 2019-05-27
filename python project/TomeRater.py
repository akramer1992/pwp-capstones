#Alexander Kramer
#Submitted 5/27/19
#Codecademy: Programming with Python
#Tome Rater

#The extension idea to be implemented is contrasting analysis methods from the provided TomeRater methods such as: Least Positive User, Lowest Rated Book, and Least Read Book
#The logic from flipping from most to least is explained and implemented in order to get accurate results

#Creating a user that has the following:
#-Constructor method that takes in self, name, and email
#-Method get_email that returns email
#-Method change_email that updates with a new email
#-Method __repr__ that returns an information string for the user
#-Method __eq__ that returns True or False based on similar name and email
#-Method read_book which adds a key:value pair to book list
#-Method get_average_rating which returns the average rating of a book based on values of book list

class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This user's email has been updated!")

    def __repr__(self):
        return "User: {name}, E-Mail: {email}, Books Read: {books}".format(name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        ratingavg=0
        count=0
        for ratings in self.books.values():
            if ratings == None:
                ratingavg = ratingavg
            else:
                ratingavg+=ratings
                count=count+1
        if count == 0:
            return None
        else:
            return ratingavg/count

#Creating a book that has the following:
#-Constructor method that takes in self, title, and isbn
#-Method get_title that returns title
#-Method get_isbn that returns isbn
#-Method set_isbn that updates with a new isbn
#-Method add_rating that updates with a valid rating
#-Method __eq__ that returns True or False based on similar book properties
#-Method get_average_rating which calculates average rating from valid ratings
#-Method __hash__ to make our book object hashable

class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This book's ISBN has been updated!")

    def add_rating(self, rating):
        if rating < 0 or rating > 4 or rating == None:
            print("Invalid rating!")
        else:
            self.ratings+=rating
            print("Your rating has been received!")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        ratingavg=0
        count=0
        for ratings in self.ratings:
            if ratings == None:
                ratingavg = ratingavg
            else:
                ratingavg+=ratings
                count=count+1
        if count == 0:
            return None
        else:
            return ratinglist/count

#Method __hash__ provided by TomeRater Instructions

    def __hash__(self):
        return hash((self.title, self.isbn))

#Creating a Fiction class, which is a book subclass with properties title, author, and isbn

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

#Creating a Non_Fiction class, which is a book subclass with properties title, subject, level, and isbn

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

#Changed a -> the, so the word a is not in front of a word that starts with a vowel

    def __repr__(self):
        return "{title}, the {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

#Creating the application TomeRater that has the following:
#Constructor method that takes in users and books
#-Method create_book which returns book with a title and isbn
#-Method create_novel which returns a fiction book with a title, author, and isbn
#-Method create_non_fiction which returns a non-fiction book with a tible, subject, level, and isbn
#-Method add_book_to_user which adds a book to user and does not add if there is no valid email
#-Method add_user which adds a user to TomeRater with a name, email, books they have read if any
#-Method print_catalog which prints all books in the catalog
#-Method print_users which prints all users in the database
#-Method most_read_book which returns the most read book by users
#-Method highest_rated_book which returns the highest rated book by users
#-Method most_positive_user which returns the user that gives the highest average rating

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def print_catalog(self):
        for books in self.books.keys():
            print(books)

    def print_users(self):
        for users in self.users.values():
            print(users)

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with email {email}!".format(email=email))
        else:
            self.users[email].read_book(book, rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
            
    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

#Initialize largest to -1 (as books cannot be read or rated below 0)
                
    def most_read_book(self):
        largest_book = None
        largest_freq = -1
        for book, freq in self.books.items():
            if freq > largest_freq:
                largest_freq = freq
                largest_book = book
        return largest_book

    def highest_rated_book(self):
        largest_book = None
        largest_rating = -1
        for book, rating in self.books.items():
            if rating > largest_rating:
                largest_rating = rating
                largest_book = book
        return largest_book

    def most_positive_user(self):
        largest_user = None
        largest_rating = -1
        for user in self.users.values():
            avg_rating = user.get_average_rating()
            if avg_rating > largest_rating:
                largest_rating = avg_rating
                largest_user = user
        return largest_user

#Initialize smallest to infinity (as books cannot be rated above 4 and read an infinite amount of times)
    
    def least_read_book(self):
        smallest_book = None
        smallest_freq = float('inf')
        for book, freq in self.books.items():
            if freq < smallest_freq:
                smallest_freq = freq
                smallest_book = book
        return smallest_book

    def lowest_rated_book(self):
        smallest_book = None
        smallest_rating = float('inf')
        for book, rating in self.books.items():
            if rating < smallest_rating:
                smallest_rating = rating
                smallest_book = book
        return smallest_book

    def least_positive_user(self):
        smallest_user = None
        smallest_rating = float('inf')
        for user in self.users.values():
            avg_rating = user.get_average_rating()
            if avg_rating < smallest_rating:
                smallest_rating = avg_rating
                smallest_user = user
        return smallest_user

#Below code is from provided populate.py
#Used to test functionality of the application TomeRater

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())

#Below code was added to test extension idea
print("Least positive user:")
print(Tome_Rater.least_positive_user())
print("Lowest rated book:")
print(Tome_Rater.lowest_rated_book())
print("Least read book:")
print(Tome_Rater.least_read_book())
