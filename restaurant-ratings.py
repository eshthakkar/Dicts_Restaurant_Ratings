import sys
from random import choice


def convert_to_dictionary():
    """Read file and creates dictionary key and value pairs."""
    
    filename = open(sys.argv[1])
    restaurant_ratings = {}
    
    for line in filename:
        line = line.rstrip()
        words = line.split(":")
        restaurant_ratings[words[0]] = words[1]

    filename.close()    
    return restaurant_ratings


def print_rating(restaurant_ratings):
    """Iterates through restaurant_ratings dictionary, sorts, and prints all items. """

    for restaurant, rating in sorted(restaurant_ratings.iteritems()):
        print "%s is rated at %s." % (restaurant, rating)
        # "{} is rated as {}".format(restaurant, rating)


def add_new_restaurant(restaurant_ratings):
    """Allows user to input new restaurant and its rating. """

    new_restaurant = raw_input("Enter a restaurant you want to rate: ")
    new_restaurant_rating = raw_input("Enter your rating for {}: ".format(new_restaurant))
    restaurant_ratings[new_restaurant] = new_restaurant_rating


def update_random_restaurant_rating(restaurant_ratings):
    """Allows user to update the rating of a randomly picked restaurant from dictionary. """
    
    random_restaurant = choice(restaurant_ratings.keys())
    print "The rating of {} is {}.".format(random_restaurant,restaurant_ratings[random_restaurant])
    print "What would you like the new rating to be?"
    updated_rating = raw_input(">>> ")

    restaurant_ratings[random_restaurant] = updated_rating


def update_chosen_restaurant_rating(restaurant_ratings):
    """Allows user to update the rating of a restaurant of their choice from dictionary. """

    print_rating(restaurant_ratings)
    print ""
    print "Which restaurant would you like to re-rate?"
    chosen_restaurant = raw_input(">>>")
    print "What is the new rating?"
    updated_rating = raw_input(">>>")

    restaurant_ratings[chosen_restaurant] = updated_rating


def prompt_user(restaurant_ratings):
    """Allows user to choose from a list of options: print, add, update, or quit. """

    while(True):
        print ""
        print "What would you like to do:" 
        print "1) See all the ratings (in alphabetical order)"
        print "2) Add a new restaurant (and rating it)"
        print "3) Update the rating of a random restaurant"
        print "4) Update the rating of a restaurant of your choice"
        print "5) Quit"
        print ""
        
        choice = raw_input(">>")
        print ""

        if choice == '1':
            print_rating(restaurant_ratings)
        elif choice == '2': 
            add_new_restaurant(restaurant_ratings)
        elif choice == "3":
            update_random_restaurant_rating(restaurant_ratings)    
        elif choice == "4":
            update_chosen_restaurant_rating(restaurant_ratings)
        elif choice == '5':
            break
        else:
            print "That's not a valid response. Please select 1, 2, or 3."
            continue



restaurant_ratings = convert_to_dictionary()
prompt_user(restaurant_ratings)


