import sys

restaurant_ratings = {}

def convert_to_dictionary(filename):
    """Read file and creates dictionary key and value pairs."""

    for line in filename:
        line = line.rstrip()
        words = line.split(":")
        restaurant_ratings[words[0]] = words[1]

    return


def print_rating():
    """Iterates through restaurant_ratings dictionary, sorts, and prints all items. """

    for restaurant, rating in sorted(restaurant_ratings.iteritems()):
        print "%s is rated at %s." % (restaurant, rating)
        # "{} is rated as {}".format(restaurant, rating)


filename = open(sys.argv[1])
convert_to_dictionary(filename)
print_rating()
filename.close()