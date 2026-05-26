import random
def fack_fun_headline():
    subjects = [
    "A lazy programmer",
    "An overthinking student",
    "A midnight gamer",
    "A chai addicted engineer",
    "A smart village inventor",
    "An AI learning emotions",
    "A confused robot assistant",
    "A school topper with no sleep",
    "A food loving traveler",
    "A cricket obsessed uncle"
    ]

    actions = [
        "accidentally developed",
        "spent 12 hours debugging",
        "went viral after testing",
        "secretly created",
        "surprised everyone by inventing",
        "challenged the internet with",
        "became famous for designing",
        "failed successfully while building",
        "confused scientists after making",
        "celebrated after launching"
    ]

    places_things = [
        "a fan that works only when exams are near",
        "an AI that predicts chai cravings",
        "a cricket bat with Bluetooth",
        "a robot that argues with humans",
        "a smart pillow that wakes students politely",
        "a refrigerator that orders food automatically",
        "a calculator that gives motivational quotes",
        "a gaming chair with built in snacks",
        "a smartwatch that detects fake excuses",
        "a laptop powered by sunlight and optimism"
    ]

    subject = random.choice(subjects)
    action = random.choice(actions)
    place_thing = random.choice(places_things)

    print(f"Breaking News: {subject} {action} {place_thing}")

fack_fun_headline()