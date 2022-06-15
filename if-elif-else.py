def need_umbrella(weather):
    if weather == "sunny":
        print("bring parasol")
    elif weather == "rain":
        print("bring umbrella")
    elif weather == "overcast":
        print("no umbrella needed")
    else:
        print("weather pattern not in database yet")


def how_tired(energy):
    if energy == 0:
        print("unconscious")


weather = "rain"
need_umbrella(weather)
weather = "sunny"
need_umbrella(weather)
