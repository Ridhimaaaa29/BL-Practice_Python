"""
PROG 1: City Latitude and Longitude Lookup
=> For any of your 5 favorite cities of the world, find out the latitude and longitude of each city from google.
=> Create a dictionary where the city is the key and value is a tuple consisting of the latitude and longitude of that city.

=> Develop a program where a city name is entered by an user.
=> If that city exists in the dictionary, it prints the city name and its latitude and longitude, else it shares a suitable message. \
=> While checking the city name, the function ignores the case. This program runs till the user selection is not “exit’.
=> City name checking should be a function and return value will be the string to be printed.


Cities Dictionary:
{'mumbai': (19.076, 72.8777), 'bangalore': (12.9716, 77.5946), 'chennai': (13.0827, 80.2707), 'pune': (18.5204, 73.8567), 'hyderabad': (17.385, 78.4867)}

TESTCASE 1:

Input =>
Enter a city name (or type 'exit' to quit): Bang

Output =>
City not found in the dictionary.

TESTCASE 2:

Input =>
Enter a city name (or type 'exit' to quit): BANGALORE

Output =>
Bangalore: Latitude = 12.9716, Longitude = 77.5946

TESTCASE 3:

Input =>
Enter a city name (or type 'exit' to quit): Pune

Output =>
Pune: Latitude = 18.5204, Longitude = 73.8567

TESTCASE 4:

Input =>
Enter a city name (or type 'exit' to quit): exit

Output =>
Exiting the program.

Note =>
=> Everytime you execute the code, the output will differ according to the input
"""

# PROG 1: City Latitude and Longitude Lookup

# Dictionary with city names as keys and (latitude, longitude) as tuple values
cities = {
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "pune": (18.5204, 73.8567),
    "hyderabad": (17.3850, 78.4867)
}

# Function to search for a city
def check_city(city_name):
    city = city_name.lower()

    if city in cities:
        latitude, longitude = cities[city]
        return f"{city.title()}: Latitude = {latitude}, Longitude = {longitude}"
    else:
        return "City not found in the dictionary."


# Display dictionary
print("Cities Dictionary:")
print(cities)

# Run until user enters exit
while True:
    city_name = input("\nEnter a city name (or type 'exit' to quit): ")

    if city_name.lower() == "exit":
        print("Exiting the program.")
        break

    print(check_city(city_name))