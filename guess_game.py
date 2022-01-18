figure = input("Input figures here:\n")
Name = input("Input Name here:")
figure = figure.split(" ")
fig = map(lambda a: int(a), figure)
fid = list(fig)
# print(fid)

from os import name
import random as rd
rand = rd.randrange(fid[0],fid[1])
# print(rand)
tries = 0
while True:
    guess_number = input("Guess number:")
    guess_number = int(guess_number)
    tries += 1
    if guess_number == rand:
        print("YOU WIN!!!")
        break
    elif guess_number < rand:
        print("YOU LOSE!!!  Hint: YOUR NUMBER IS LESS!!")
    elif guess_number > rand:
        print("YOU LOSE!!!  Hint: YOUR NUMBER IS MORE!!")
    else:
        pass

print("you tried:", tries, "time(s)")

def data_collector():
    figure = input("Input figures here:\n")
    name = input("Input Name here:")
    figure = figure.split(" ")
    fig = map(lambda a: int(a), figure)
    fid = list(fig)

    rand = rd.randrange(fid[0],fid[1])
    print(rand)

    return rand, name 



def play_game():
    
    tries = 0

    rand, name = data_collector()

    while True:
        guess_number = input("Guess number:")
        guess_number = int(guess_number)
        tries += 1
        if guess_number == rand:
            print("YOU WIN!!!")
            break
        elif guess_number < rand:
            print("YOU LOSE!!!  Hint: YOUR NUMBER IS LESS!!")
        elif guess_number > rand:
            print("YOU LOSE!!!  Hint: YOUR NUMBER IS MORE!!")
        else:
            pass
    data_collector(name, tries)
    # return name, tries

# def play(name, tries):
    # name, tries = play_game()
#     with open("data.csv", "a", newline = "") as our_file:
#         our_file.write(f"{name}: {tries} \n")
# play_game()
# play_game()



# def file()

# with open("database.csv", "a") as our_log_file:

#     name = "Atha"
#     tries = 5
#     our_log_file.write(f"{name}, {tries}")
#     print("Logged session")


# def write_to_file(name, tries):
#     with open("database.csv", "a") as our_log_file:

#         our_log_file.write(f"{name}, {tries}")
        
#     print("Logged session")

# write_to_file("Roukie", 7)

# import csv



# import csv
# from csv import writer
# def play():
#     name, tries = play_game()
#     with open("data.csv", "a", newline = "") as our_file:
#         csv_writer = writer(our_file)
#         csv_writer.writerow([name, tries])
#         # our_file.write(f"{name}: {tries}")
# play()
# csv_writer.writerow({"Name", "Tries"})


