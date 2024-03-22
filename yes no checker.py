# yes_no checker
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please answer yes/no")


played_before = yes_no("Have you played this game before? (yes/no): ")



