# in this program, as one of cs50p's first assignment, we have to get the user to say something. 
# however, we coded it so that everything they say will be lowercase and won't have any white space.
# this is version of indoor.py is a custom version for code that wasn't required by the course.
something = input("what would you like to say? ").strip()
if something.isupper():
    print(f"you said: {something.lower()}", end=" ")
    print("be quiet next time, but this is a warning.")
else:
    print(f"you said: {something}")