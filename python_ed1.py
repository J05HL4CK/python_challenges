# pseudocode to code
# print a message depending on the day

# def messenger(day):
#     """Returns a message based on the day of the week"""
#     if day == "wednesday":
#         print("It\'s Wednesday!")
#     else:
#         print("What day is it?")
#         day_2 = input("Day: ")
#         if day_2.endswith("y") != True:
#             print("Thats not a day!")
#         if day_2 == "wednesday":
#             print("HAHA Funny guy!")
#         else:
#             print(f"Thanks for letting me know it\'s {day_2}")

# messenger(day = input("enter a day: ")

print("What day is it today?")
day = input("day: ")
def messenger(day):
    """Returns a message based on the day."""
    if day == "wednesday":
        print("It\'s Wednesday!")
    if day.endswith("y") != True:
        print("Thats not a day!")
    else:
        funny = input("What day is it?")
        if funny == "wednesday":
            print("funny guy!")
        else:
            print("quit messin with me!")
messenger(day)