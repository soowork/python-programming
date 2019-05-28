breakfast = ['Quaker Harvest Crunch', "Instant Oatmeal", "Froot Loops", "Corn Flakes"]

def cereal_time():
    for cereal in breakfast:
        if cereal[-1] == "s":
            print(cereal + " are yummy!")
        else:
            print(cereal + " is yummy!")

cereal_time()