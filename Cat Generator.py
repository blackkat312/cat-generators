import random
from random import randint, choice
from statistics import mean

example_cat = {
    "sex": "",  # female, male
    "gender": "",  # female, male, non-binary, anything
    "eye_color": {
        # orange, amber, gold, yellow, hazel, yellow-green, green, blue-green, mint green, cyan, blue, indigo
        "left_color": "",
        "right_color": "",
        "is_left_light": False,  # True (light), False (normal)
        "is_right_light": False
    },
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
    "color_breakthrough": False,  # True, False
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
    "white_grade": "",  # three numbers || sum: 0 - 1 = low, 2 - 4 = medium, 5 - 6 = high
    "brightness": ""  # three numbers || sum: 0 - 1 = dark, 2 - 4 = medium, 5 - 6 = light
}
parent_1 = {
    "sex": "",  # female, male
    "gender": "",  # female, male, non-binary, anything
    "eye_color": {
        # orange, amber, gold, yellow, hazel, yellow-green, green, blue-green, mint green, cyan, blue, indigo
        "left_color": "",
        "right_color": "",
        "is_left_light": False,  # True (light), False (normal)
        "is_right_light": False
    },
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
    "color_breakthrough": False,  # True, False
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
    "white_grade": "",  # three numbers || sum: 0 - 1 = low, 2 - 4 = medium, 5 - 6 = high
    "brightness": ""  # three numbers || sum: 0 - 1 = dark, 2 - 4 = medium, 5 - 6 = light
}
parent_2 = {
    "sex": "",  # female, male
    "gender": "",  # female, male, non-binary, anything
    "eye_color": {
        # orange, amber, gold, yellow, hazel, yellow-green, green, blue-green, mint green, cyan, blue, indigo
        "left_color": "",
        "right_color": "",
        "is_left_light": False,  # True (light), False (normal)
        "is_right_light": False
    },
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
    "color_breakthrough": False,  # True, False
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
    "white_grade": "",  # three numbers || sum: 0 - 1 = low, 2 - 4 = medium, 5 - 6 = high
    "brightness": ""  # three numbers || sum: 0 - 1 = dark, 2 - 4 = medium, 5 - 6 = light
}

# CONFIG
alt_print = False  # Alternate style of printing (True: more newlines; for pasting into other programs, False: less
# newlines; easier visibility)
kitty = {
    "sex": None,  # Forces a particular sex
    "gender": None,  # Forces a particular gender
    "name": None  # Uses kitty["name"] instead of "This cat"
}
generate_kit = False  # True: generates a kit, False: randomizes a cat
parent_2_sex = None  # If parent_2 is an unmodified dict, you can set their sex here (opt.)


def appearance_string(cat, name="This cat"):
    tabby_string = ""
    with_string = " with "
    withs = []
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

    #

    eye_to_string = {
        "gold": "golden",
        "yellow-green": "yellowish-green",
        "blue-green": "bluish-green",
        "mint green": "minty-green"
    }
    if cat["eye_color"]["left_color"] in eye_to_string:
        left_eye = eye_to_string.get(cat["eye_color"]["left_color"])
    else:
        left_eye = cat["eye_color"]["left_color"]
    left_light_string = "light "
    if left_eye in ["orange", "golden", "bluish-green", "minty-green", "indigo"]:
        left_light_string = "pale "

    if cat["eye_color"]["left_color"] == cat["eye_color"]["right_color"]:
        withs.append(f"{left_light_string if cat['eye_color']['is_left_light'] is True else ''}{left_eye} eyes")
    else:
        if cat["eye_color"]["right_color"] in eye_to_string:
            right_eye = eye_to_string.get(cat["eye_color"]["right_color"])
        else:
            right_eye = cat["eye_color"]["right_color"]
        right_light_string = "light "
        if right_eye in ["orange", "golden", "bluish-green", "minty-green", "indigo"]:
            right_light_string = "pale "

        withs.append(f"one {left_light_string if cat['eye_color']['is_left_light'] is True else ''}{left_eye} eye")
        withs.append(f"one {right_light_string if cat['eye_color']['is_right_light'] is True else ''}{right_eye} eye")

    #

    if "W" not in cat["white"] and "ws" in cat["white"]:
        grade_sum = 0
        for polygene in cat["white_grade"]:
            grade_sum += int(polygene)
        if grade_sum in [0, 1]:
            grade = "low"
        elif grade_sum in [2, 3, 4]:
            grade = "medium"
        else:  # grade_sum in [5, 6]
            grade = "high"

        white_string = "a "
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
        withs.append(white_string)

    #

    if len(withs) < 1:
        print("???")
    elif len(withs) == 1:
        with_string += withs[0]
    elif len(withs) == 2:
        with_string += withs[0] + " and " + withs[1]
    elif len(withs) > 2:
        with_string += ", ".join(withs[:-1])
        with_string += ", and " + withs[-1]

    #

    return_string = f"{name} is a {fur_length_string}{color_string}{tabby_string} {gender_string}{with_string}."

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
        if cat["eye_color"]["left_color"] == cat["eye_color"]["right_color"]:
            eye_color = f"Eye Color:\n{cat['eye_color']['left_color'].capitalize()}"
        else:
            eye_color = (
                f"Left Eye Color:\n{cat['eye_color']['left_color'].capitalize()}\n\n"
                f"Right Eye Color:\n{cat['eye_color']['right_color'].capitalize()}"
            )
        if cat["eye_color"]["is_left_light"] == cat["eye_color"]["is_right_light"]:
            eye_lightness = f"Are Eyes Light?\n{cat['eye_color']['is_left_light']}"
        else:
            eye_lightness = (
                f"Is Left Eye Light?\n{cat['eye_color']['is_left_light']}\n\n"
                f"Is Right Eye Light?\n{cat['eye_color']['is_right_light']}"
            )

        return (
            f"Sex:\n{cat['sex'].capitalize()}\n\n"
            f"Gender:\n{cat['gender'].capitalize()}\n\n"
            f"{eye_color}\n\n"
            f"{eye_lightness}\n\n"
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
        if cat["eye_color"]["left_color"] == cat["eye_color"]["right_color"]:
            eye_color = f"Eye Color: {cat['eye_color']['left_color']}"
        else:
            eye_color = (
                f"Left Eye Color: {cat['eye_color']['left_color']}\n"
                f"Right Eye Color: {cat['eye_color']['right_color']}"
            )
        if cat["eye_color"]["is_left_light"] == cat["eye_color"]["is_right_light"]:
            eye_lightness = f"Are Eyes Light? {cat['eye_color']['is_left_light']}"
        else:
            eye_lightness = (
                f"Is Left Eye Light? {cat['eye_color']['is_left_light']}\n"
                f"Is Right Eye Light? {cat['eye_color']['is_right_light']}"
            )

        return_string = (
            f"Sex: {cat['sex']}\n"
            f"Gender: {cat['gender']}\n"
            f"{eye_color}\n"
            f"{eye_lightness}\n"
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
        return_string = return_string.replace("? True", "? Yes")
        return_string = return_string.replace("? False", "? No")
        return_string = return_string.replace(": True", ": yes")
        return_string = return_string.replace(": False", ": no")

        return return_string


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

    if randint(1, 20) != 1:
        tries = 0
        while cat["sex"] == "male" and cat["ginger"] == ["G", "g"] and tries <= 25:
            cat["ginger"][0] = choice(types_of_ginger)
            cat["ginger"][1] = choice(types_of_ginger)
            cat["ginger"].sort()
            tries += 1

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

    # EYE COLOR (last, due to white generation)
    generate_eye_color(cat)


def generate_kits(cat, parent1=None, parent2=None, parent2_sex=None, sex=None, gender=None):
    template = {
        "sex": "",  # female, male
        "gender": "",  # female, male, non-binary, anything
        "eye_color": {
            # orange, amber, gold, yellow, hazel, yellow-green, green, blue-green, mint green, cyan, blue, indigo
            "left_color": "",
            "right_color": "",
            "is_left_light": False,  # True (light), False (normal)
            "is_right_light": False
        },
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
        "color_breakthrough": False,  # True, False
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
        "white_grade": "",  # three numbers || sum: 0 - 1 = low, 2 - 4 = medium, 5 - 6 = high
        "brightness": ""  # three numbers || sum: 0 - 1 = dark, 2 - 4 = medium, 5 - 6 = light
    }
    types_of_color_breakthrough = [
        True,
        True,
        False,
        False,
        False
    ]
    sex_to_trans_gender = {
        "female": "male",
        "male": "female"
    }
    nonbinary = generate_nonbinary()

    if not parent1 or parent1 is None or parent1 == {} or parent1 == template:
        print("Oops! You forgot to input the first parent.")
    else:
        print("PARENT 1")
        print(dict_translation(parent1, alt_print) + "\n" + appearance_string(parent1))

        if not parent2 or parent2 is None or parent2 == {} or parent2 == template:
            parent2 = template.copy()
            randomize_pelt(parent2, parent2_sex if parent2_sex is not None else choice(["female", "male"]))
        print("\n\nPARENT 2")
        print(dict_translation(parent2, alt_print) + "\n" + appearance_string(parent2))

        for i in range(0, 2):
            if parent1["base_color"][i] == "bla":
                parent1["base_color"][i] = "1bla"
            if parent1["base_color"][i] == "br":
                parent1["base_color"][i] = "2br"
            if parent1["base_color"][i] == "gr":
                parent1["base_color"][i] = "3gr"
            if parent1["base_color"][i] == "blu":
                parent1["base_color"][i] = "4blu"
            if parent1["base_color"][i] == "si":
                parent1["base_color"][i] = "5si"
            if parent1["ginger_color"][i] == "gi":
                parent1["ginger_color"][i] = "1gi"
            if parent1["ginger_color"][i] == "cr":
                parent1["ginger_color"][i] = "2cr"
            if parent1["ginger_color"][i] == "ye":
                parent1["ginger_color"][i] = "3ye"
            if parent1["ginger_color"][i] == "ru":
                parent1["ginger_color"][i] = "4ru"
            if parent1["white"][i] == "W":
                parent1["white"][i] = "1W"
            if parent1["white"][i] == "ws":
                parent1["white"][i] = "2ws"
            if parent1["white"][i] == "w":
                parent1["white"][i] = "3w"

            if parent2["base_color"][i] == "bla":
                parent2["base_color"][i] = "1bla"
            if parent2["base_color"][i] == "br":
                parent2["base_color"][i] = "2br"
            if parent2["base_color"][i] == "gr":
                parent2["base_color"][i] = "3gr"
            if parent2["base_color"][i] == "blu":
                parent2["base_color"][i] = "4blu"
            if parent2["base_color"][i] == "si":
                parent2["base_color"][i] = "5si"
            if parent2["ginger_color"][i] == "gi":
                parent2["ginger_color"][i] = "1gi"
            if parent2["ginger_color"][i] == "cr":
                parent2["ginger_color"][i] = "2cr"
            if parent2["ginger_color"][i] == "ye":
                parent2["ginger_color"][i] = "3ye"
            if parent2["ginger_color"][i] == "ru":
                parent2["ginger_color"][i] = "4ru"
            if parent2["white"][i] == "W":
                parent2["white"][i] = "1W"
            if parent2["white"][i] == "ws":
                parent2["white"][i] = "2ws"
            if parent2["white"][i] == "w":
                parent2["white"][i] = "3w"

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
        cat["fur_length"] = [choice([parent1["fur_length"][0], parent1["fur_length"][1]]),
                             choice([parent2["fur_length"][0], parent2["fur_length"][1]])]
        cat["fur_length"].sort()

        # BASE COLOR
        cat["base_color"] = [choice([parent1["base_color"][0], parent1["base_color"][1]]),
                             choice([parent2["base_color"][0], parent2["base_color"][1]])]
        cat["base_color"].sort()
        temp = cat["base_color"][0]
        cat["base_color"][0] = temp[1:]
        temp = cat["base_color"][1]
        cat["base_color"][1] = temp[1:]

        # GINGER-NESS
        cat["ginger"] = [choice([parent1["ginger"][0], parent1["ginger"][1]]),
                         choice([parent2["ginger"][0], parent2["ginger"][1]])]
        cat["ginger"].sort()

        if not (
                (parent1["ginger"] == ["G", "G"] and parent2["ginger"] == ["g", "g"]) or
                (parent1["ginger"] == ["g", "g"] and parent2["ginger"] == ["G", "G"])
        ) and randint(1, 20) != 1:
            tries = 0
            while cat["sex"] == "male" and cat["ginger"] == ["G", "g"] and tries <= 25:
                cat["ginger"] = [choice([parent1["ginger"][0], parent1["ginger"][1]]),
                                 choice([parent2["ginger"][0], parent2["ginger"][1]])]
                cat["ginger"].sort()
                tries += 1

        # GINGER COLOR
        cat["ginger_color"] = [choice([parent1["ginger_color"][0], parent1["ginger_color"][1]]),
                               choice([parent2["ginger_color"][0], parent2["ginger_color"][1]])]
        cat["ginger_color"].sort()
        temp = cat["ginger_color"][0]
        cat["ginger_color"][0] = temp[1:]
        temp = cat["ginger_color"][1]
        cat["ginger_color"][1] = temp[1:]

        # COLOR BREAKTHROUGH
        if randint(1, 4) != 1:
            cat["color_breakthrough"] = choice([parent1["color_breakthrough"], parent2["color_breakthrough"]])
        else:
            cat["color_breakthrough"] = choice(types_of_color_breakthrough)

        # PATTERNING
        cat["patterning"] = [choice([parent1["patterning"][0], parent1["patterning"][1]]),
                             choice([parent2["patterning"][0], parent2["patterning"][1]])]
        cat["patterning"].sort()

        # PATTERN TYPE
        cat["pattern_type"] = [choice([parent1["pattern_type"][0], parent1["pattern_type"][1]]),
                               choice([parent2["pattern_type"][0], parent2["pattern_type"][1]])]
        cat["pattern_type"].sort()

        # WHITE
        cat["white"] = [choice([parent1["white"][0], parent1["white"][1]]),
                        choice([parent2["white"][0], parent2["white"][1]])]
        cat["white"].sort()
        temp = cat["white"][0]
        cat["white"][0] = temp[1:]
        temp = cat["white"][1]
        cat["white"][1] = temp[1:]

        # POLYGENETIC WHITE GRADE
        first_skipped = False
        second_skipped = False
        poly_sum = 0
        inheritance_method = randint(1, 100)
        parent1_or_2 = randint(1, 2)
        adding = choice([True, False])
        num = 2 if randint(1, 15) == 1 else 1

        parent1_white = 0
        for polygene in parent1["white_grade"]:
            parent1_white += int(polygene)
        parent2_white = 0
        for polygene in parent2["white_grade"]:
            parent2_white += int(polygene)

        # More or less (30%)
        if 1 <= inheritance_method <= 30:
            if parent1_or_2 == 1:
                if adding is True and ((parent1_white < 6 and num == 1) or (parent1_white < 5 and num == 2)):
                    poly_sum = parent1_white + num
                elif adding is False and ((parent1_white > 0 and num == 1) or (parent1_white > 1 and num == 2)):
                    poly_sum = parent1_white - num
                else:
                    first_skipped = True
                    parent1_or_2 = 2
            else:
                first_skipped = True
            if parent1_or_2 == 2:
                if adding is True and ((parent2_white < 6 and num == 1) or (parent2_white < 5 and num == 2)):
                    poly_sum = parent2_white + num
                elif adding is False and ((parent2_white > 0 and num == 1) or (parent2_white > 1 and num == 2)):
                    poly_sum = parent2_white - num
                else:
                    second_skipped = True
            else:
                second_skipped = True

            if first_skipped and second_skipped:
                inheritance_method = randint(31, 100)

        # Direct inheritance (35%)
        if 31 <= inheritance_method <= 65:
            if randint(1, 2) == 1:
                poly_sum = parent1_white
            else:
                poly_sum = parent2_white

        # Mean (35%)
        if 66 <= inheritance_method <= 100:
            poly_sum = int(mean([parent1_white, parent2_white]))

        polygenes = ""
        temp_poly_sum = 67

        while temp_poly_sum != poly_sum:
            if temp_poly_sum != poly_sum:
                polygenes = ""
                temp_poly_sum = 0
            for gene in range(0, 3):
                polygenes += choice(["2", "1", "0"])
                temp_poly_sum += int(polygenes[gene])

        cat["white_grade"] = polygenes

        # POLYGENETIC BRIGHTNESS VARIATION
        first_skipped = False
        second_skipped = False
        poly_sum = 0
        inheritance_method = randint(1, 100)
        parent1_or_2 = randint(1, 2)
        adding = choice([True, False])
        num = 2 if randint(1, 15) == 1 else 1

        parent1_bright = 0
        for polygene in parent1["brightness"]:
            parent1_bright += int(polygene)
        parent2_bright = 0
        for polygene in parent2["brightness"]:
            parent2_bright += int(polygene)

        # More or less (30%)
        if 1 <= inheritance_method <= 30:
            if parent1_or_2 == 1:
                if adding is True and ((parent1_bright < 6 and num == 1) or (parent1_bright < 5 and num == 2)):
                    poly_sum = parent1_bright + num
                elif adding is False and ((parent1_bright > 0 and num == 1) or (parent1_bright > 1 and num == 2)):
                    poly_sum = parent1_bright - num
                else:
                    first_skipped = True
                    parent1_or_2 = 2
            else:
                first_skipped = True
            if parent1_or_2 == 2:
                if adding is True and ((parent2_bright < 6 and num == 1) or (parent2_bright < 5 and num == 2)):
                    poly_sum = parent2_bright + num
                elif adding is False and ((parent2_bright > 0 and num == 1) or (parent2_bright > 1 and num == 2)):
                    poly_sum = parent2_bright - num
                else:
                    second_skipped = True
            else:
                second_skipped = True

            if first_skipped and second_skipped:
                inheritance_method = randint(31, 100)

        # Direct inheritance (35%)
        if 31 <= inheritance_method <= 65:
            if randint(1, 2) == 1:
                poly_sum = parent1_bright
            else:
                poly_sum = parent2_bright

        # Mean (35%)
        if 66 <= inheritance_method <= 100:
            poly_sum = int(mean([parent1_bright, parent2_bright]))

        polygenes = ""
        temp_poly_sum = 67

        while temp_poly_sum != poly_sum:
            if temp_poly_sum != poly_sum:
                polygenes = ""
                temp_poly_sum = 0
            for gene in range(0, 3):
                polygenes += choice(["2", "1", "0"])
                temp_poly_sum += int(polygenes[gene])

        cat["brightness"] = polygenes

        # EYE COLOR (last, due to white generation)
        generate_eye_color(cat)


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


def generate_eye_color(cat):
    types_of_eye_color = {
        "orange": [
            "orange",
            "amber",
            "gold"
        ],
        "yellow": [
            "yellow",
            "hazel",
            "yellow-green"
        ],
        "green": [
            "green",
            "blue-green",
            "mint green"
        ],
        "blue": [
            "cyan",
            "blue",
            "indigo"
        ]
    }
    types_of_eye_lightness = [
        True,
        False,
        False
    ]

    if "W" in cat["white"]:
        chance_of_blue = 2
        chance_of_odd = 4
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

        chance_of_odd = 67
        if cat["white"][0] != "w":
            if cat["white"][1] == "w":
                if grade == "low":
                    chance_of_blue = 17
                elif grade == "medium":
                    chance_of_blue = 15
                else:  # grade == "high"
                    chance_of_blue = 12
                    chance_of_odd = 10
            else:
                if grade == "low":
                    chance_of_blue = 11
                    chance_of_odd = 9
                elif grade == "medium":
                    chance_of_blue = 6
                    chance_of_odd = 5
                else:  # grade == "high"
                    chance_of_blue = 4
                    chance_of_odd = 3
        else:
            chance_of_blue = 20

    pool = ["orange", "orange", "yellow", "yellow", "yellow", "green"]
    if randint(1, chance_of_blue) == 1:
        cat["eye_color"]["left_color"] = choice(types_of_eye_color["blue"])
        cat["eye_color"]["right_color"] = cat["eye_color"]["left_color"]
        if chance_of_odd != 67 and randint(1, chance_of_odd) == 1:
            if randint(1, 2) == 1:
                cat["eye_color"]["left_color"] = choice(types_of_eye_color[choice(pool)])
            else:
                cat["eye_color"]["right_color"] = choice(types_of_eye_color[choice(pool)])
    else:
        cat["eye_color"]["left_color"] = choice(types_of_eye_color[choice(pool)])
        cat["eye_color"]["right_color"] = cat["eye_color"]["left_color"]

    cat["eye_color"]["is_left_light"] = choice(types_of_eye_lightness)
    if cat["eye_color"]["left_color"] != cat["eye_color"]["right_color"] and randint(1, 2) == 1:
        cat["eye_color"]["is_right_light"] = choice(types_of_eye_lightness)
    else:
        cat["eye_color"]["is_right_light"] = cat["eye_color"]["is_left_light"]


if generate_kit:
    generate_kits(example_cat, parent_1, parent_2, parent_2_sex, kitty["sex"], kitty["gender"])
    print("\n\nKITTEN")
else:
    randomize_pelt(example_cat, kitty["sex"], kitty["gender"])
print(dict_translation(example_cat, alt_print) + "\n" + appearance_string(example_cat, (kitty["name"]
                                                                                        if kitty["name"] is not None
                                                                                        else "This cat")))
