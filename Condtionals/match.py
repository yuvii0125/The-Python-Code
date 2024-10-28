value = int(input("Enter a number: "))

match value:
        case 1:
            print("Case 1 matched")
        case 2:
            print("Case 2 matched")
        case _:
            print("No match found")

#Match is as same as Switch case
#_ is used as default case

# case 401 | 403 | 404: # can be used for several different cases
#     return "Not allowed"

#you can use conditions in case 

# point1 = int(input("Enter point 1:"))
# point2 = int(input("Enter point 2:"))
# point = (point1, point2)

# #match is similar to switch case)
# # point is an (x, y) tuple
# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")
