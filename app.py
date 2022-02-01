import dbi as db


username = input("Please enter your username:")
print("Please select from the following options:")
print("Option 1. Write a new post")
print("Option 2. See all other posts")

db = db.DbInteraction()
user_selection = input()
user_selection = int(user_selection)

if user_selection == 1:
    post_input = input("Make your post:")
    result = db.make_post(username, post_input)
    print("Your post has been added")
    exit()

elif user_selection == 2:
    result = db.print_posts()

else:
    print("Invalid entry")
