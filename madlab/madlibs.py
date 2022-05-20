# # string concatenation (aka how to put string together)
# # suppose we want to create a string that says "subscribe to ______"
# youtuber ="" # some string variable

# # a few ways to do this 
# print("subscribe to" + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

Name = input('Name: ')
age = input("Age: ")

midlib = f"What is your name?\
     My name is {Name}. How old are you? Iam {age} years old"
        
print(midlib)