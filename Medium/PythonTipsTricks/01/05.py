from operator import itemgetter

d = {"v3": 44, "v2": 33, "v4": 55, "v1": 22,}

sorted_d = dict(sorted(d.items(), key=itemgetter(1)))

print(sorted_d)