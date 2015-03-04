"""Getting data source from Facebook"""
#license: CAAEuAis8fUgBAGQL61ZBlnOCxqGHhOe4BjtUipgbREO7tuZA6b3ZB6ZAS3v496lFZBuKPWOVOPmfHq9pZAVS6qUvz03QzNVNAeusDlUzzF1OATputvLLov6ei7I00krKnqaZAqiBZCojUa19oDXv10ghdRudZAmNWcXZB7wZAJX6f9ZAj6duZBynmOF5m

from pattern.web import * 
f = Facebook(license = 'CAAEuAis8fUgBAGQL61ZBlnOCxqGHhOe4BjtUipgbREO7tuZA6b3ZB6ZAS3v496lFZBuKPWOVOPmfHq9pZAVS6qUvz03QzNVNAeusDlUzzF1OATputvLLov6ei7I00krKnqaZAqiBZCojUa19oDXv10ghdRudZAmNWcXZB7wZAJX6f9ZAj6duZBynmOF5m')
me = f.profile()
my_friends = f.search(me[0], type=FRIENDS, count=10000)
for friend in my_friends:
	friend_news = f.search(friend.id, type=NEWS, count=10000)
	for news in friend_news:
		print news.text
		print news.author
