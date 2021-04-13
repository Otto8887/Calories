import json 
import Sqlitetest
import sqlite3
filename="product_dict.json"
datafile="calories_data.json"

with open(filename, "r") as f:
	product_dictionary=json.load(f)
class Calories:
	def __init__(self, calories_total):
		self.calories_total=calories_total
	def greet_user(self):
		#makes the user choose whether they want to log calories today, or add a product to the dictionary
		while True:
			answer=input("view data, log data or add products? log/add/view")
			if answer=="log":
				x.log_calories()
			elif answer=="add":
				x.add_product()
			elif answer=="view":
				x.view_data()
			else:
				print("please choose add or log")
	def log_calories(self):
		#makes the user log calories
		while True:
			logged_product=input("which product did u eat?(press f to save calories for today):")
			if logged_product=="f":
				x.save_data()
			elif logged_product not in product_dictionary:
				x.add_product()
			else:
				logged_product_calories=product_dictionary.get(logged_product)
				gram_amount=input("Enter amount of gram:")
				gram_amount=int(gram_amount)
				calories_in_gram=logged_product_calories/100*gram_amount
				calories_in_gram=int(calories_in_gram)
				self.calories_total+=calories_in_gram
				print(f"you have eaten {self.calories_total} calories today")	
	def add_product(self):
		#makes the user add a product to the dictionary
		added_product=input("product unknown, add it to the list \nproduct name:")
		added_product_calories=input("amount of calories pr 100g:")
		added_product_calories=int(added_product_calories)
		product_dictionary[added_product]=added_product_calories
		with open(filename, "w") as f:
			json.dump(product_dictionary, f)
		x.greet_user()
	def save_data(self):
		data_dato=input("Enter the date 00-00-00:")
		data_name=input("Enter your name:")
		data_calories=self.calories_total
		Sqlitetest.insert_user_data(data_dato, data_name, data_calories)
		x.greet_user()
	def view_data(self):
		view_data_name=input("Enter your name:")
		Sqlitetest.get_user_data(view_data_name)
		x.greet_user()
		
x=Calories(0)
x.greet_user()
