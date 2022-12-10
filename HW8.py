import matplotlib.pyplot as plt
import os
import sqlite3
import unittest

def get_restaurant_data(db_filename):
    """
    This function accepts the file name of a database as a parameter and returns a list of
    dictionaries. The key:value pairs should be the name, category, building, and rating
    of each restaurant in the database.
    """
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    names = cur.execute("SELECT id, name FROM restaurants").fetchall()
    sort_names = sorted(names, key=lambda x:x[0])
    # print(len(sort_names))
    # print(sort_names)

    cat_ids = cur.execute("SELECT categories.category FROM categories JOIN restaurants ON restaurants.category_id=categories.id").fetchall()
    # print(len(cat_ids))
    # print(cat_ids)

    building_nums = cur.execute("SELECT buildings.building FROM buildings JOIN restaurants ON restaurants.building_id=buildings.id").fetchall()
    # print(len(building_nums))
    # print(building_nums)

    ratings = cur.execute("SELECT rating FROM restaurants").fetchall()
    # print(ratings)
    # print(ratings)

    lst = []


    for i in range(len(sort_names)):

        name = sort_names[i][1]
        cat = cat_ids[i][0]
        building_name = building_nums[i][0]
        rate = ratings[i][0]

        dictionary = {}
        
        dictionary["name"]= name
        dictionary["category"]= cat
        dictionary["building"] = building_name
        dictionary["rating"] = rate

        # print(dictionary)
        lst.append(dictionary)
    # print(lst)
    # print(lst)
        
    return lst

    pass

def barchart_restaurant_categories(db_filename):
    """
    This function accepts a file name of a database as a parameter and returns a dictionary. The keys should be the
    restaurant categories and the values should be the number of restaurants in each category. The function should
    also create a bar chart with restaurant categories and the counts of each category.
    """

    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    cats2 = cur.execute("SELECT restaurants.name, categories.category FROM categories JOIN restaurants ON restaurants.category_id=categories.id").fetchall()
    print(cats2)
    dictionary = {}
    for i in range(len(cats2)):
        category = cats2[i][1]
        if category not in dictionary:
            dictionary[category]=1
        elif category in dictionary:
            dictionary[category]+=1
    print(dictionary)

    values = dictionary.values()
    for val in values:
        plt.bar(x, height, width=0.8, bottom=None, *, align='center')

    return dictionary

    pass

#EXTRA CREDIT
def highest_rated_category(db_filename):#Do this through DB as well
    """
    This function finds the average restaurant rating for each category and returns a tuple containing the
    category name of the highest rated restaurants and the average rating of the restaurants
    in that category. This function should also create a bar chart that displays the categories along the y-axis
    and their ratings along the x-axis in descending order (by rating).
    """
    pass

#Try calling your functions here
def main():
    get_restaurant_data("South_U_Restaurants.db")
    pass

class TestHW8(unittest.TestCase):
    def setUp(self):
        self.rest_dict = {
            'name': 'M-36 Coffee Roasters Cafe',
            'category': 'Cafe',
            'building': 1101,
            'rating': 3.8
        }
        self.cat_dict = {
            'Asian Cuisine ': 2,
            'Bar': 4,
            'Bubble Tea Shop': 2,
            'Cafe': 3,
            'Cookie Shop': 1,
            'Deli': 1,
            'Japanese Restaurant': 1,
            'Juice Shop': 1,
            'Korean Restaurant': 2,
            'Mediterranean Restaurant': 1,
            'Mexican Restaurant': 2,
            'Pizzeria': 2,
            'Sandwich Shop': 2,
            'Thai Restaurant': 1
        }
        self.best_category = ('Deli', 4.6)

    def test_get_restaurant_data(self):
        rest_data = get_restaurant_data('South_U_Restaurants.db')
        self.assertIsInstance(rest_data, list)
        self.assertEqual(rest_data[0], self.rest_dict)
        self.assertEqual(len(rest_data), 25)

    def test_barchart_restaurant_categories(self):
        cat_data = barchart_restaurant_categories('South_U_Restaurants.db')
        self.assertIsInstance(cat_data, dict)
        self.assertEqual(cat_data, self.cat_dict)
        self.assertEqual(len(cat_data), 14)

    def test_highest_rated_category(self):
        best_category = highest_rated_category('South_U_Restaurants.db')
        self.assertIsInstance(best_category, tuple)
        self.assertEqual(best_category, self.best_category)

if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)
