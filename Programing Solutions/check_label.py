def check_label(passed):
    if -6 <= passed <= 6:
        print("Neutral")
    elif -18 <= passed <= -7:
        print("Skew left")
    elif -30 <= passed <= -19:
        print("Hyper-partisan left")
    elif -42 <= passed <= -31:
        print("Most extreme left")
    elif 7 <= passed <= 18:
        print("Skew right")
    elif 19 <= passed <= 30:
        print("Hyper-partisan right")
    elif 31 <= passed <= 42:
        print("Most extreme right")
    else:
        print("NAN")


check_label(-3)
