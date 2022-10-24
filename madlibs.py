# # putting strings together \
# # we want to create a string that says"subscribe to ________"
# youtuber = ""  # string variable

# # a few ways
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("adjective: ")
verb1 = input("verb 1: ")
verb2 = input("verb 2: ")
famous_person = input("Famous person: ")

madlib = f"Computer program is so {adj}! it makes me so excited all the time because \ I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)
