import dbi as db

username = input("Please enter your username:")
print("Please select from the following options:")
print("Option 1. Write a new post")
print("Option 2. See all other posts")

db = db.DbInteraction()
option_input = input()
post_input = input("Make your post:")


if option_input == 1:
    db.make_post(username, post_input)
    print("Your post has been added")
    exit()
elif option_input == 2:
    result = db.print_posts()


# else:
#     print("Invalid entry")
