import random
#import json

#print(json.dumps({'test' : 123}))

  # private HashSet<String> prefix = new HashSet<>(Arrays.asList("Black", "White", "Gray", "North",
  #         "South", "East", "West", "Frost", "Rime", "Oak", "Pine", "Birch", "Pale", "Stone", "Iron",
  #         "Green", "Ash", "Shear", "Ghost", "Deep", "Bleak", "Grim", "Gloom",
  #         "High", "Round", "Dark", "Dawn", "Sun", "Pale", "Cold", "Spring", "Gold", "Moon",
  #         "Silver", "Red", "Summer", "Winter", "Wind", "Dawn", "River", "Dark", "Night", "Clay",
  #         "Sky", "Wild", "Ash", "Heart", "Helm", "Crest", "Ember", "Wild", "Hazel", "Briar",
  #         "Silver", "Steel", "Bronze", "Skull", "Bone", "Salt", "Storm", "Willow", "Cedar", "Maple",
  #         "Thorn", "Water", "Dusk", "Moss"
  # ));

  # private HashSet<String> animals = new HashSet<>(Arrays.asList("Wolf", "Raven", "Bear", "Eagle",
  #         "Hawk", "Elk", "Boar", "Bull", "Lion", "Ox", "Horse", "Mule", "Goat", "Trout", "Salmon",
  #         "Crow", "Dove", "Dog", "Cat"
  # ));

  # private HashSet<String> monsters = new HashSet<>(Arrays.asList("Demon", "Drake", "Goblin", "Orc",
  #         "Ogre", "Troll", "Devil", "Harpy", "Dragon", "Wight", "Hag", "Wyvern", "Imp", "Gryphon",
  #         "Giant", "Wraith"
  # ));

  # private HashSet<String> creatureAdjectives = new HashSet<>(Arrays.asList("Old", "Dead", "Mad",
  #         "Dancing", "Lost", "Wild", "Howling", "Laughing", "Drunken", "Jolly", "Bleeding",
  #         "Screaming"
  # ));

part_dict = {
    'suffix': ["keep", "hold", "ville", "boro", "burg", "stone", "holt",
                "tower", "vale", "bridge", "guard", "brook", "field", "fall",
                "fell", "water", "ridge", "ford", "wood", "rock", "hollow",
                "haven", "spring", "bank", "barrow", "fort", "crest", "shore",
                "burn", "forge", "run", "port", "view", "helm","bluff", "moor",
                "rock", "watch", "march", "top", "bottom", "cross", "fork",
                "shield","trail", "wild", "worth", "stead", "moon", "star",
                "hill", "smith", "point", "briar", "gate", "town", "henge",
                "loft", "marsh", "bone", "skull", "well", "fog", "court", 
                "breach", "dell", "witch", "thorn", "veil", "vale", "gulch"],
    
    'plants': ['oak', 'ash', 'beech', 'maple', 'cedar', 'yew', 'briar',
                'moss', 'fern', 'hazel', 'pine', 'willow'],
    
    'seasons': ['spring', 'summer', 'fall', 'autumn', 'winter'],
    
    'weather': ['rime', 'frost', 'snow', 'storm', 'wind', 'thunder', 'cold',
                'warm'],
    
    'time': ['dawn', 'dusk', 'morn', 'eve', 'noon'],
    
    'adjectives': ['wild', 'bleak', 'grim', 'good'],
    
    'colors': ['green', 'red', 'white', 'black', 'grey', 'dark', 'light'],
    
    'landmarks_geo': ["canyon", "rock", "river", "hill", "bluff", "peak",
                      "crag", "stone", "pass", "point", "marsh", "mire",
                      "creek", "valley", "grove", "forest", "canyon", "gorge",
                      "forest", "woods", "cave", "grotto", "moor", "swamp",
                      "brook", "lake", "falls", "reach", "ridge","brook",
                      "stream", "spring", "crest", "summit", "deep", "trench",
                      "cavern", "spire", "basin", "dale", "plateau", "fen",
                      "savannah", "glade", "desert", "bluff", "spire",
                      "ravine", "hollow", "prairie", "sea", "jungle", "delta",
                      "plains", "steppe", "reef", "estuary", "chasm",
                      "meadow", "void", "foothills", "island", "desert",
                      "mesa", "highland","depths", "waste", "flats",
                      "dunes", "mountain", "barrens", "cairns", "oasis"],
    
    'landmarks_anthro': ["Tower", "Keep", "Watch", "Temple", "Monastery",
                         "Sanctum", "Refuge", "Bridge", "Mine", "Stronghold",
                         "Mill", "Plantation", "Barrow", "Henge", "Lookout",
                         "Outpost", "Castle", "Runestone", "Ruins", "Camp",
                         "Estate", "Inn", "Crossing", "Quarry", "Lighthouse",
                         "Beacon", "Bastion", "Tomb", "Trading Post", "Fort",
                         "Watchtower", "Quarry", "Ironworks", "Forge", "Road",
                         "Ford", "Crypt", "Sanctuary", "Catacombs",
                         "Graveyard", "Cairn", "Shrine", "Ruins","Sanctum",
                         "Encampment", "Necropolis", "Palace", "Academy",
                         "Harbor", "Observatory", "Citadel", 'Ziggurat',
                         'gate', 'crossing', 'ford', 'bridge', 'lookout',
                         'watch'],
    
    'nouns_flavor': ['skull', 'bottle', 'bucket', 'saddle', 'axe', 'bone',
                      'mirror', 'spear', 'tombstone', 'gallows', 'boot'],
    
    'adjectives_flavor': ['haunted', 'flaming', 'narrow', 'broken',
                           'whispering', 'frozen', 'salt', 'smoking', 'dead',
                           'grand', 'good', 'grim'],
    
    'numbers': []
    }


print(part_dict['plants'][random.randint(0, len(part_dict['plants'])-1)].capitalize() +
      part_dict['suffix'][random.randint(0, len(part_dict['suffix'])-1)]
      )