# def basic():
#     print("This is a pretty basic function")
# basic()

# the number of arguments passed should be equal to the number of parameters for a basic function.
# def add(c):
#     print(c + 10)
# add(3)

# def passd():
#     a = input("Password here: ")
#     while True:
#         passd2 = input("repeat password here:")
#         if a == passd2:
#             print("login successful")
#             break
#         else:
#             pass
# passd()


# import time
# def use():
#     for i in range(10, 0, -1): 
#         for j in range(10, 0, -1):
#             for f in range(60, 0, -1):
#                 for r in range(60, 0, -1): 
#                     print(i,"hrs", ":", j,"mins", ":", f, "secs", ":", r)
#                     time.sleep(0.5)

# use()

# def increment(num):
    # return num + 2

# def use(hours, minutes, seconds):
#     for i in range(increment(hours)): 
#         for j in range(increment(minutes)):
#             for f in range(increment(seconds)):
#                 for r in range(60, 0, -1): 
#                     print(i, "hrs", ":", j, "mins", ":", f, "secs", ":", r)
# use(2, 10, 6)

# def use(hours, minutes, seconds):
#     for i in range(hours): 
#         for j in range(minutes):
#             for f in range(seconds): 
#                print(i, "hrs", " ", j, "mins", " ", f, "secs")
# use(10, 10, 10)

# def restructure(hours, minutes, seconds):
    # return f"{hours}hrs {minutes}mins {seconds}secs"

# restructure(10, 2, 2)

# def use(hours, minutes, seconds):
#     for i in range(increment(hours)): 
#         for j in range(increment(minutes)):
#             for f in range(increment(seconds)):
#                 for r in range(60, 0, -1):
#                     print(restructure(i, j, f))
# use(2, 10, 6)




# from datetime import datetime as dt
# dar = ["23/5/2021", "30/3/2020", "13/1/2022", "16/7/2019", "4/12/2021"]
# dar = list(map(lambda d : dt.strptime(d, "%d/%m/%Y"), dar))
# fer = []

# fast = list(map(lambda a: a.weekday()<5, dar))
# # print(fast)
# fast = list(map(lambda a: str(a), fast))
# # print(fast[0])
# for entry in fast:
#     if entry == "False":
#         fix = entry.replace("False", "Weekend")
#         fer.append(fix)
#     else:
#         fin = entry.replace("True", "Weekday")
#         fer.append(fin)
#     # fer.append(change), fer.append(fix)
# print(fer)
# print(fer[1])
# print(fast[4])
# fast.replace("False","Weekend")
# print(fast)

# stir = "python"
# do = []
# for i in stir:
#     if i == "n":
#         break
#     print(i)
#     do.append(i)
# print(len(do))

r = []
y = range(1,6)
print(list(y))
for page in range(1,6):
    if page == 5:
        break
    pg = page * 2
    # print(pg)
    r.append(pg)
    # print(r)
print(r)

























