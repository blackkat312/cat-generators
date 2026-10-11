import random
from random import randint, choice

example_cat = {
    "sex": "",  # female or male
    "gender": "",  # female, male, non-binary, any other
    "fur_length": [  # L (short), l (long)
        "",
        ""
    ],
    "base_color": [  # bla (black), br (brown), gr (gray), blu (blue), si (silver)
        "",
        ""
    ],
    "ginger": [  # G (ginger), g (not ginger)
        "",
        ""
    ],
    "ginger_color": [  # gi (ginger), cr (cream), ye (yellow), ru (russet)
        "",
        ""
    ],
    "color_breakthrough": False,
    "patterning": [  # P (patterned), p (not patterned)
        "",
        ""
    ],
    "pattern_type": [  # T (tabby), m (mottled)
        "",
        ""
    ],
    "white": [  # W (full white), ws (white), w (not white)
        "",
        ""
    ],
    "white_grade": "",  # sum of numbers || 0 - 1 = low, 2 - 4 = medium, 5 - 6 = high
    "brightness": ""  # sum of numbers || 0 - 1 = dark, 2 - 4 = medium, 5 - 6 = light
}
parent_1 = {
    "sex": "",  # female or male
    "gender": "",  # female, male, non-binary, any other
    "fur_length": [  # L (short), l (long)
        "",
        ""
    ],
    "base_color": [  # bla (black), br (brown), gr (gray), blu (blue), si (silver)
        "",
        ""
    ],
    "ginger": [  # G (ginger), g (not ginger)
        "",
        ""
    ],
    "ginger_color": [  # gi (ginger), cr (cream), ye (yellow), ru (russet)
        "",
        ""
    ],
    "color_breakthrough": False,
    "patterning": [  # P (patterned), p (not patterned)
        "",
        ""
    ],
    "pattern_type": [  # T (tabby), m (mottled)
        "",
        ""
    ],
    "white": [  # W (full white), ws (white), w (not white)
        "",
        ""
    ],
    "white_grade": "",  # sum of numbers || 0 - 1 = low, 2 - 4 = medium, 5 - 6 = high
    "brightness": ""  # sum of numbers || 0 - 1 = dark, 2 - 4 = medium, 5 - 6 = light
}
parent_2 = {
    "sex": "",  # female or male
    "gender": "",  # female, male, non-binary, any other
    "fur_length": [  # L (short), l (long)
        "",
        ""
    ],
    "base_color": [  # bla (black), br (brown), gr (gray), blu (blue), si (silver)
        "",
        ""
    ],
    "ginger": [  # G (ginger), g (not ginger)
        "",
        ""
    ],
    "ginger_color": [  # gi (ginger), cr (cream), ye (yellow), ru (russet)
        "",
        ""
    ],
    "color_breakthrough": False,
    "patterning": [  # P (patterned), p (not patterned)
        "",
        ""
    ],
    "pattern_type": [  # T (tabby), m (mottled)
        "",
        ""
    ],
    "white": [  # W (full white), ws (white), w (not white)
        "",
        ""
    ],
    "white_grade": "",  # sum of numbers || 0 - 1 = low, 2 - 4 = medium, 5 - 6 = high
    "brightness": ""  # sum of numbers || 0 - 1 = dark, 2 - 4 = medium, 5 - 6 = light
}


def appearance_string(cat, name="This cat"):
    tabby_string = ""
    white_string = " with a "
    gender_to_pronouns = {
        "female": {
            "subject": "she",
            "object": "her",
            "possessive determiner": "her",
            "possessive pronoun": "hers",
            "reflexive": "herself",
            "are_is": "is"
        },
        "male": {
            "subject": "he",
            "object": "him",
            "possessive determiner": "his",
            "possessive pronoun": "his",
            "reflexive": "himself",
            "are_is": "is"
        },
        "other": {
            "subject": "they",
            "object": "them",
            "possessive determiner": "their",
            "possessive pronoun": "theirs",
            "reflexive": "themself",
            "are_is": "are"
        }
    }

    if cat["gender"] == "female":
        gender_string = "molly"
        pronoun_gender = "female"
    elif cat["gender"] == "male":
        gender_string = "tom"
        pronoun_gender = "male"
    else:
        if cat["gender"] in ["demigirl", "demiboy"]:
            gender_string = cat["gender"]
        else:
            gender_string = f"{cat['gender']} cat"
        gender_string = gender_string.replace("girl", "molly")
        gender_string = gender_string.replace("boy", "tom")
        pronoun_gender = "other"

    #

    if "L" not in cat["fur_length"]:
        fur_length_string = "long-furred "
    else:
        fur_length_string = "short-furred "

    #

    if cat["base_color"][0] == "bla":
        if cat["color_breakthrough"] is False:
            color_string = "black"
        elif cat["base_color"][1] == "br":
            color_string = "brownish-black"
        elif cat["base_color"][1] == "gr":
            color_string = "deep gray"
        elif cat["base_color"][1] == "blu":
            color_string = "blueish-black"
        elif cat["base_color"][1] == "si":
            color_string = "dark gray"
        else:
            color_string = "black"
    elif cat["base_color"][0] == "br":
        if cat["color_breakthrough"] is False:
            color_string = "brown"
        elif cat["base_color"][1] == "gr":
            color_string = "grayish-brown"
        elif cat["base_color"][1] == "blu":
            color_string = "brownish-gray"
        elif cat["base_color"][1] == "si":
            color_string = "pale brown"
        else:
            color_string = "brown"
    elif cat["base_color"][0] == "gr":
        if cat["color_breakthrough"] is False:
            color_string = "gray"
        elif cat["base_color"][1] == "blu":
            color_string = "blueish-gray"
        elif cat["base_color"][1] == "si":
            color_string = "pale gray"
        else:
            color_string = "gray"
    elif cat["base_color"][0] == "blu":
        if cat["color_breakthrough"] is False:
            color_string = "grayish-blue"
        elif cat["base_color"][1] == "si":
            color_string = "pale grayish-blue"
        else:
            color_string = "grayish-blue"
    else:
        color_string = "smoke"

    #

    if cat["ginger_color"][0] == "gi":
        if cat["color_breakthrough"] is False:
            ginger_color = "ginger"
        elif cat["ginger_color"][1] == "cr":
            ginger_color = "creamy ginger"
        elif cat["ginger_color"][1] == "ye":
            ginger_color = "yellowish-ginger"
        elif cat["ginger_color"][1] == "ru":
            ginger_color = "reddish-ginger"
        else:
            ginger_color = "ginger"
    elif cat["ginger_color"][0] == "cr":
        if cat["color_breakthrough"] is False:
            ginger_color = "cream"
        elif cat["ginger_color"][1] == "ye":
            ginger_color = "yellowish-cream"
        elif cat["ginger_color"][1] == "ru":
            ginger_color = "pinkish-cream"
        else:
            ginger_color = "cream"
    elif cat["ginger_color"][0] == "ye":
        if cat["color_breakthrough"] is False:
            ginger_color = "yellow"
        elif cat["ginger_color"][1] == "ru":
            ginger_color = "golden"
        else:
            ginger_color = "yellow"
    else:
        ginger_color = "russet"

    #

    if cat["ginger"] == ["G", "g"]:
        tabby_string = " tortie"
        color_string += f" and {ginger_color}"
        color_string = color_string.replace(" ", "-")
    elif "G" in cat["ginger"]:
        color_string = ginger_color

    #

    if cat["patterning"][0] == "P":
        color_string = color_string.replace("smoke", "silver")
        if "T" in cat["pattern_type"]:
            if "tortie" in tabby_string:
                tabby_string += "-"
            else:
                tabby_string += " "
            tabby_string += "tabby"
        else:
            color_string = "mottled " + color_string

    #

    if "W" in cat["white"]:
        color_string = "white"
        tabby_string = ""
        white_string = ""
    else:
        grade_sum = 0
        for polygene in cat["white_grade"]:
            grade_sum += int(polygene)
        if grade_sum in [0, 1]:
            grade = "low"
        elif grade_sum in [2, 3, 4]:
            grade = "medium"
        else:  # grade_sum in [5, 6]
            grade = "high"

        if cat["white"][0] != "w":
            if cat["white"][1] == "w":
                if grade == "low":
                    white_string += "low"
                elif grade == "medium":
                    white_string += "medium-low"
                else:  # grade == "high"
                    white_string += "medium"
                    tabby_string = tabby_string.replace("tortie", "calico")
            else:
                tabby_string = tabby_string.replace("tortie", "calico")
                if grade == "low":
                    white_string += "medium"
                elif grade == "medium":
                    white_string += "medium-high"
                else:  # grade == "high"
                    white_string += "high"
            white_string += " amount of white"
        else:
            white_string = ""

    #

    return_string = f"{name} is a {fur_length_string}{color_string}{tabby_string} {gender_string}{white_string}."

    #

    if color_string != "white":
        brightness_sum = 0
        for polygene in cat["brightness"]:
            brightness_sum += int(polygene)
        if brightness_sum not in [2, 3, 4]:
            return_string += (
                f" Additionally, {gender_to_pronouns.get(pronoun_gender).get('subject')} "
                f"{gender_to_pronouns.get(pronoun_gender).get('are_is')} "
            )
            if brightness_sum >= 5:
                return_string += "light-colored."
            elif brightness_sum <= 1:
                return_string += "dark-colored."

    #

    return return_string


def dict_translation(cat, alt=False):
    white_grade_string = 0
    brightness_string = 0
    for polygene in cat["white_grade"]:
        white_grade_string += int(polygene)
    for polygene in cat["brightness"]:
        brightness_string += int(polygene)

    if alt is True:
        return (
            f"Sex:\n{cat['sex'].capitalize()}\n\n"
            f"Gender:\n{cat['gender'].capitalize()}\n\n"
            f"Fur Length:\n{cat['fur_length'][0]}, {cat['fur_length'][1]}\n\n"
            f"Base Color:\n{cat['base_color'][0]}, {cat['base_color'][1]}\n\n"
            f"Ginger-ness:\n{cat['ginger'][0]}, {cat['ginger'][1]}\n\n"
            f"Ginger Color:\n{cat['ginger_color'][0]}, {cat['ginger_color'][1]}\n\n"
            f"Color Breakthrough:\n{cat['color_breakthrough']}\n\n"
            f"Patterning:\n{cat['patterning'][0]}, {cat['patterning'][1]}\n\n"
            f"Pattern Type:\n{cat['pattern_type'][0]}, {cat['pattern_type'][1]}\n\n"
            f"White:\n{cat['white'][0]}, {cat['white'][1]}\n\n"
            f"White Grade:\n{cat['white_grade']} - {str(white_grade_string)}\n\n"
            f"Brightness:\n{cat['brightness']} - {str(brightness_string)}\n"
        )
    else:
        return (
            f"Sex: {cat['sex']}\n"
            f"Gender: {cat['gender']}\n"
            f"Fur Length: [{cat['fur_length'][0]}, {cat['fur_length'][1]}]\n"
            f"Base Color: [{cat['base_color'][0]}, {cat['base_color'][1]}]\n"
            f"Ginger-ness: [{cat['ginger'][0]}, {cat['ginger'][1]}]\n"
            f"Ginger Color: [{cat['ginger_color'][0]}, {cat['ginger_color'][1]}]\n"
            f"Color Breakthrough: {cat['color_breakthrough']}\n"
            f"Patterning: [{cat['patterning'][0]}, {cat['patterning'][1]}]\n"
            f"Pattern Type: [{cat['pattern_type'][0]}, {cat['pattern_type'][1]}]\n"
            f"White: [{cat['white'][0]}, {cat['white'][1]}]\n"
            f"White Grade: {cat['white_grade']} - {str(white_grade_string)}\n"
            f"Brightness: {cat['brightness']} - {str(brightness_string)}\n"
        )


def randomize_pelt(cat, sex=None, gender=None):
    types_of_fur_length = [
        "L",
        "l"
    ]
    types_of_color = [
        "1bla",
        "1bla",
        "1bla",
        "1bla",
        "2br",
        "2br",
        "2br",
        "2br",
        "3gr",
        "3gr",
        "3gr",
        "3gr",
        "4blu",
        "4blu",
        "4blu",
        "5si",
        "5si"
    ]
    types_of_ginger = [
        "G",
        "g",
        "g",
        "g"
    ]
    types_of_ginger_color = [
        "1gi",
        "1gi",
        "1gi",
        "2cr",
        "2cr",
        "3ye",
        "3ye",
        "4ru",
        "4ru"
    ]
    types_of_color_breakthrough = [
        True,
        True,
        False,
        False,
        False
    ]
    types_of_patterning = [
        "P",
        "p"
    ]
    types_of_pattern_type = [
        "T",
        "T",
        "T",
        "T",
        "m"
    ]
    types_of_white = [
        "1W",
        "2ws",
        "2ws",
        "2ws",
        "2ws",
        "3w",
        "3w",
        "3w",
        "3w",
        "3w",
        "3w"
    ]
    polygenes = ["0", "1", "2"]
    sex_to_trans_gender = {
        "female": "male",
        "male": "female"
    }
    nonbinary = generate_nonbinary()

    # SEX AND GENDER
    if sex and sex in ["female", "male"]:
        cat["sex"] = sex
    else:
        cat["sex"] = choice(["female", "male"])
    if gender and gender is not None and gender != "":
        cat["gender"] = gender
    else:
        cat["gender"] = cat["sex"]
        if randint(1, 15) == 1:
            cat["gender"] = choice([sex_to_trans_gender.get(cat["sex"]), sex_to_trans_gender.get(cat["sex"]),
                                    sex_to_trans_gender.get(cat["sex"]), nonbinary, nonbinary])

    # FUR LENGTH
    cat["fur_length"][0] = choice(types_of_fur_length)
    cat["fur_length"][1] = choice(types_of_fur_length)
    cat["fur_length"].sort()

    # BASE COLOR
    cat["base_color"][0] = choice(types_of_color)
    cat["base_color"][1] = choice(types_of_color)
    cat["base_color"].sort()
    temp = cat["base_color"][0]
    cat["base_color"][0] = temp[1:]
    temp = cat["base_color"][1]
    cat["base_color"][1] = temp[1:]

    # GINGER-NESS
    cat["ginger"][0] = choice(types_of_ginger)
    cat["ginger"][1] = choice(types_of_ginger)
    cat["ginger"].sort()

    if cat["sex"] == "male" and cat["ginger"] == ["G", "g"] and randint(1, 20) != 1:
        cat["ginger"] = choice([["g", "g"], ["G", "G"]])

    # GINGER COLOR
    cat["ginger_color"][0] = choice(types_of_ginger_color)
    cat["ginger_color"][1] = choice(types_of_ginger_color)
    cat["ginger_color"].sort()
    temp = cat["ginger_color"][0]
    cat["ginger_color"][0] = temp[1:]
    temp = cat["ginger_color"][1]
    cat["ginger_color"][1] = temp[1:]

    # COLOR BREAKTHROUGH
    cat["color_breakthrough"] = choice(types_of_color_breakthrough)

    # PATTERNING
    cat["patterning"][0] = choice(types_of_patterning)
    cat["patterning"][1] = choice(types_of_patterning)
    cat["patterning"].sort()

    # PATTERN TYPE
    cat["pattern_type"][0] = choice(types_of_pattern_type)
    cat["pattern_type"][1] = choice(types_of_pattern_type)
    cat["pattern_type"].sort()

    # WHITE
    cat["white"][0] = choice(types_of_white)
    cat["white"][1] = choice(types_of_white)
    cat["white"].sort()
    temp = cat["white"][0]
    cat["white"][0] = temp[1:]
    temp = cat["white"][1]
    cat["white"][1] = temp[1:]

    # POLYGENETIC WHITE GRADE AND BRIGHTNESS VARIATION
    for i in range(3):
        cat["white_grade"] += choice(polygenes)
        cat["brightness"] += choice(polygenes)


def generate_kits(parent1=None, parent2=None, sex=None, gender=None):
    kit = {
        "sex": "",  # female or male
        "gender": "",  # female, male, non-binary, any other
        "fur_length": [  # L (short), l (long)
            "",
            ""
        ],
        "base_color": [  # bla (black), br (brown), gr (gray), blu (blue), si (silver)
            "",
            ""
        ],
        "ginger": [  # G (ginger), g (not ginger)
            "",
            ""
        ],
        "ginger_color": [  # gi (ginger), cr (cream), ye (yellow), ru (russet)
            "",
            ""
        ],
        "color_breakthrough": False,
        "patterning": [  # P (patterned), p (not patterned)
            "",
            ""
        ],
        "pattern_type": [  # T (tabby), m (mottled)
            "",
            ""
        ],
        "white": [  # W (full white), ws (white), w (not white)
            "",
            ""
        ],
        "white_grade": "",  # sum of numbers || 0 - 1 = low, 2 - 4 = medium, 5 - 6 = high
        "brightness": ""  # sum of numbers || 0 - 1 = dark, 2 - 4 = medium, 5 - 6 = light
    }

    if not parent1 or parent1 is None or parent1 == {} or parent1 == kit:
        print("Oops! You forgot to input the first parent.")
    else:
        if not parent2 or parent2 is None or parent2 == {} or parent2 == kit:
            parent2 = kit.copy()
            randomize_pelt(parent2)

        return kit


# If you don't know the definitions of any of these, I recommend looking at the LGBTQIA+ Wiki!
# https://lgbtqia.wiki/wiki/LGBTQIA%2B_Wiki
def generate_nonbinary():
    genderfluid = [
        "genderfaer",
        "genderfaunet",
        "genderflor",
        "genderfloren",
        "genderflorer",
        "genderfloret",  # hey it's me!
        "genderfen"
    ]
    demigender = [
        "demiagender",
        "demineutrois",
        "deminonbinary",
        "demixenogender"
    ]

    if randint(1, 3) == 1:
        return "non-binary"
    else:
        category = randint(1, 3)
        if category == 1:
            if randint(1, 3) == 1:
                return "genderfluid"
            else:
                if randint(1, 5) <= 3:
                    return choice(["genderfae", "genderfaun"])
                else:
                    return choice(genderfluid)
        elif category == 2:
            if randint(1, 5) <= 3:
                return choice(["demigirl", "demiboy"])
            else:
                return choice(demigender)
        else:  # category == 3
            if randint(1, 5) <= 3:
                return choice(["girlflux", "boyflux"])
            else:
                return "enbyflux"


randomize_pelt(example_cat)
print(dict_translation(example_cat, False) + "\n" + appearance_string(example_cat))
