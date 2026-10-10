from random import choice

"""
EXCLUSIONS


Prefixes given after birth/due to injury, e.g., Crooked- (Crookedstar), Dead- (Deadfoot), Half- (Halftail), etc.

Prefixes assigned to only one cat based off of (a) unique physical characteristic(s), e.g., Arch- (Archeye),
Badger- (Badgerfang), etc.

Names only occurring in the Field Guides/other books in that same vein, and names given by the authors in non-canon
material, by Su Susann, and from the family tree, e.g., Bluebell- (Bluebellkit), Chestnut- (Chestnutkit),
Cricket- (Cricketkit), etc.
(AKA, names from sources I don't consider fully/at all canon)

WarriorClan names, e.g., Bigteeth, Bugeater, -whistle (Clawwhistle), etc.

Prefixes from former non-Clancats that just had a suffix tacked onto them, e.g., Bella- (Bellaleaf),
Billy- (Billystorm), Blaze- (Blazefire), etc.

Jimmy, Dana, and Emmy Cherry's names: Braveheart, Shiningheart, and Brightspirit (I personally feel it wouldn't be
respectful to add them)

"""

prefixes = [
    "Acorn", "Adder", "Alder", "Amber", "Ant", "Apple", "Ash", "Aspen", "Bark", "Bay", "Bee", "Beech", "Beetle",
    "Berry", "Birch", "Bird", "Black", "Blizzard", "Bloom", "Blossom", "Blue", "Boulder", "Bracken", "Bramble",
    "Branch", "Breeze", "Briar", "Bright", "Brindle", "Bristle", "Brook", "Brown", "Brush", "Bumble", "Buzzard",
    "Cedar", "Cherry", "Chive", "Cinder", "Claw", "Cloud", "Clover", "Cone", "Copper", "Creek", "Crouch", "Crow",
    "Curl", "Curly", "Cypress", "Daisy", "Dandelion", "Dapple", "Dark", "Dawn", "Deer", "Dew", "Doe", "Dove", "Dusk",
    "Dust", "Eagle", "Echo", "Eel", "Ember", "Fallen", "Fallow", "Fawn", "Feather", "Fern", "Ferret", "Fidget", "Fin",
    "Finch", "Fir", "Fire", "Flail", "Flame", "Flash", "Flax", "Flicker", "Flint", "Flip", "Float", "Flower", "Fluff",
    "Flutter", "Fly", "Fog", "Fox", "Freckle", "Fringe", "Frog", "Frond", "Frost", "Furze", "Fuzzy", "Gale", "Golden",
    "Goose", "Gorse", "Grass", "Gravel", "Gray", "Green", "Gull", "Gust", "Hail", "Hare", "Hatch", "Haven", "Hawk",
    "Hazel", "Heather", "Heavy", "Heron", "Hickory", "Hollow", "Holly", "Honey", "Hoot", "Hop", "Hound", "Hunt", "Ice",
    "Ivy", "Jagged", "Jay", "Juniper", "Kestrel", "Kite", "Lake", "Larch", "Lark", "Leaf", "Leap", "Leopard", "Lichen",
    "Light", "Lightning", "Lily", "Lion", "Little", "Lizard", "Loud", "Lynx", "Mallow", "Maple", "Marigold", "Marsh",
    "Meadow", "Midge", "Milk", "Minnow", "Mint", "Mist", "Mistle", "Misty", "Mole", "Moon", "Morning", "Moss", "Mossy",
    "Mouse", "Mud", "Mumble", "Myrtle", "Nectar", "Needle", "Nettle", "Newt", "Night", "Nut", "Oak", "Oat", "Olive",
    "Otter", "Owl", "Pale", "Parsley", "Patch", "Peak", "Pear", "Pebble", "Perch", "Petal", "Pigeon", "Pike", "Pine",
    "Plum", "Pod", "Pool", "Poppy", "Pounce", "Prickle", "Primrose", "Puddle", "Puff", "Quail", "Quick", "Rabbit",
    "Rain", "Rapid", "Rat", "Raven", "Red", "Reed", "Ridge", "Ripple", "Robin", "Rock", "Rook", "Root", "Rose", "Rough",
    "Rowan", "Running", "Rush", "Russet", "Rustle", "Rye", "Sage", "Sand", "Sandy", "Scorch", "Sedge", "Seed", "Shade",
    "Sharp", "Shell", "Shimmer", "Shine", "Short", "Shrew", "Shy", "Silky", "Silver", "Sky", "Slate", "Sleek", "Slight",
    "Sloe", "Smoke", "Snail", "Snake", "Snap", "Snip", "Snow", "Soft", "Song", "Soot", "Sorrel", "Spark", "Sparrow",
    "Speckle", "Spider", "Spike", "Splash", "Spot", "Spotted", "Spruce", "Squirrel", "Stag", "Starling", "Stem",
    "Stoat", "Stone", "Storm", "Stream", "Stretch", "Strike", "Stripe", "Sun", "Sunny", "Swallow", "Sweet", "Swift",
    "Talon", "Tangle", "Tansy", "Tawny", "Thistle", "Thorn", "Thrift", "Thrush", "Tiger", "Timber", "Toad", "Trout",
    "Tumble", "Turtle", "Twig", "Vine", "Violet", "Vixen", "Vole", "Wasp", "Wave", "Weasel", "Web", "Weed", "Wet",
    "Whisker", "Whisper", "Whistle", "White", "Whorl", "Wild", "Willow", "Wind", "Wolf", "Wood", "Woolly", "Wren",
    "Yarrow"
]
suffixes = [
    "bark", "beam", "belly", "berry", "bird", "blaze", "bloom", "branch", "breeze", "briar", "bright", "brook", "brush",
    "burr", "bush", "call", "claw", "cloud", "crawl", "creek", "cry", "curl", "dapple", "dawn", "drift", "dusk", "dust",
    "ear", "eye", "face", "fall", "fang", "feather", "fern", "fire", "fish", "flake", "flame", "flight", "flower",
    "foot", "frond", "frost", "fur", "glow", "gorse", "grass", "hawk", "haze", "heart", "leaf", "leap", "light", "mist",
    "moon", "morning", "mouse", "nose", "pelt", "petal", "pod", "pool", "poppy", "pounce", "ripple", "runner",
    "scratch", "seed", "shade", "shimmer", "shine", "sight", "skip", "sky", "slip", "snap", "snout", "snow", "song",
    "speck", "speckle", "splash", "spot", "spots", "spring", "stalk", "stem", "step", "sting", "stone", "storm",
    "stream", "strike", "stripe", "swoop", "tail", "talon", "thistle", "thorn", "throat", "tip", "toe", "tooth", "tuft",
    "watcher", "water", "weed", "whisker", "whisper", "willow", "wind", "wing", "wish"
]
# This is mainly just for myself - will apply to anyone else living in PA (and prob nearby states too) though
non_local_prefixes = [
    "Adder", "Buzzard", "Fallow", "Ferret", "Furze", "Gorse", "Heather", "Kite", "Rook", "Sloe", "Thrift"
]
non_local_suffixes = [
    "gorse"
]

# CONFIG
special_suffix = ""  # kit, paw, star, ect., or leave blank
amount = 3
exclude_non_local_names = False

if exclude_non_local_names is True:
    for prefix in non_local_prefixes:
        if prefix in prefixes:
            prefixes.remove(prefix)
    for suffix in non_local_suffixes:
        if suffix in suffixes:
            suffixes.remove(suffix)

for i in range(amount):
    if amount != 1:
        nl = "\n"
    else:
        nl = ""

    chosen_prefix = choice(prefixes)
    chosen_suffix = choice(suffixes)
    while chosen_suffix == chosen_prefix.lower():
        chosen_suffix = choice(suffixes)

    if special_suffix != "":
        print(f"Hello! My name is {chosen_prefix}{special_suffix} (-{chosen_suffix}).{nl}")
    else:
        print(f"Hello! My name is {chosen_prefix}{chosen_suffix}.{nl}")
