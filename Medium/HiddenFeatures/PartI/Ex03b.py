places = ["India", "London", "Poland", "Netherlands"]
for place in places:
    if place.startswith(('Lo', 'Po')):
        print(place)