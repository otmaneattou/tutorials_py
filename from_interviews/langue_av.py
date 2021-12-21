

def translate(phrase):
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    result = ""
    j = 0
    i = 0
    for carac in phrase:
        i += 1
        if j != 0:
            j -= 1
        elif carac in voyelles:
            #result += carac
            result += "av"
            j += 3
        result += carac
    return result


if __name__ == "__main__":
    phrase = "Langue de feu"
    print(translate(phrase))
