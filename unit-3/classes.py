'''
class Dog:
    # we will define the class here 

    # self is compulsory -- we use it only within the class
    # this notation sets default values for name & age 
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age 

    def bark_hello(self):
        print(f'Woof! I am called {self.name}. I am {self.age} human years old.')




# create a Dog object

# default for name was set to empty string
sandy = Dog()
print('name is',sandy.name)

flin = Dog('Shaggy', 3) 
print('name is',flin.name)

flin.bark_hello()

'''

# create an InstagramAccount class
# will have user_name, email, profile_picture, posts, followers

class InstagramAccount:

    # with no defaults for variables it will require that we pass them both in 
    def __init__(self,user_name,email):
        self.user_name = user_name
        self.email = email
        self.profile_picture = ''
        self.posts = []
        self.followers = []

    def make_post(self, post):
        self.posts.append(post)

    def follow_me(self,another_account):
        self.followers.append(another_account)
     
    def get_posts(self):
        return self.posts

    def get_followers(self):
        return self.followers

    def __repr__(self):
        # need to tell it how to represent our class as a string 
        return '[name='+self.user_name+', posts='+str(len(self.posts))+']'

account_one = InstagramAccount('swork','suework@gmail.com')
# print(type(account_one))
account_two = InstagramAccount('jsimons','joe@simonsfamily.ca')

account_one.make_post('this is my first instagram post!')
account_one.make_post('sue is tired')
print(account_one.get_posts())

account_one.follow_me(account_two)
print(account_one.get_followers())