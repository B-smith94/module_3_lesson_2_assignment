#Task 1
traveler_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Linda", "Brussels", "Paris")]

def flight_itinerary_format(itineraries):
    index = 0
    while index < len(itineraries):
        for itinerary in traveler_itineraries:
            name, origin, destination = itinerary
            print(f"Itinerary {itineraries.index(itinerary) + 1}: {name} - From {origin} to {destination}")
            index += 1
             
flight_itinerary_format(traveler_itineraries)