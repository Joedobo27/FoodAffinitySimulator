from enum import Enum


class Recipe(Enum):

    pass


class Rarity(Enum):
    NONE = -1
    COMMON = 0
    RARE = 1
    SUPREME = 2
    FANTASTIC = 3
    pass


class ItemTemplateType(Enum):
    none = -1
    hollow = 1
    weapon_slash = 2
    shield = 3
    armour = 4
    food = 5
    magic = 6
    tool_field = 7
    body_part = 8
    inventory = 9
    tool_mining = 10
    tool_carpentry = 11
    tool_smithing = 12
    weapon_pierce = 13
    weapon_crush = 14
    weapon_axe = 15
    weapon_sword = 16
    weapon_knife = 17
    weapon_misc = 18
    tool_digging = 19
    seed = 20
    wood = 21
    metal = 22
    leather = 23
    cloth = 24
    stone = 25
    liquid = 26
    melting = 27
    meat = 28
    vegetable = 29
    pottery = 30
    no_take = 31
    light = 32
    container_liquid = 33
    liquid_inflammable = 34
    weapon_melee = 35
    fish = 36
    weapon = 37
    tool = 38
    lock = 39
    indestructible = 40
    key = 41
    no_drop = 42
    dust = 43
    repairable = 44
    temporary = 45
    combine = 46
    lockable = 47
    has_data = 48
    outside_only = 49
    coin = 50
    turnable = 51
    decoration = 52
    full_price = 53
    no_rename = 54
    low_nutrition = 55
    draggable = 56
    village_deed = 57
    home_stead_deed = 58
    always_poll = 59
    floating = 60
    no_trade = 61
    butchered = 62
    no_put = 63
    lead_creature = 64
    fire = 65
    domain = 66
    use_ground_only = 67
    huge_altar = 68
    artifact = 69
    unique = 70
    destroy_huge_altar = 71
    pass_full_data = 72
    form = 73
    medium_nutrition = 74
    good_nutrition = 75
    high_nutrition = 76
    food_maker = 77
    herb = 78
    poison = 79
    fruit = 80
    desc_is_exam = 81
    dish = 82
    server_bound = 83
    two_handed = 84
    kingdom_marker = 85
    destroyable = 86
    material_price_effect = 87
    liquid_cooking = 88
    positive_decay = 89
    liquid_drinkable = 90
    color = 91
    colorable = 92
    gem = 93
    weapon_bow = 94
    weapon_bow_unstrung = 95
    egg = 96
    newbie_item = 97
    tile_aligned = 98
    dragon_armour = 99
    compass = 100
    oil_consuming = 101
    healing_power_1 = 102
    healing_power_2 = 103
    healing_power_3 = 104
    healing_power_4 = 105
    healing_power_5 = 106
    healing = 107
    named = 108
    one_per_tile = 109
    bed = 110
    inside_only = 111
    no_bank = 112
    recycled = 113
    loaded = 114
    flickering = 115
    light_bright = 116
    vehicle = 117
    flower = 118
    improve_item = 119
    death_prot = 120
    tool_belt = 121
    royal = 122
    no_move = 123
    wind = 124
    dredge = 125
    mine_door = 126
    no_sell_back = 127
    spring_filled = 128
    decay_destroys = 129
    rechargeable = 130
    server_portal = 131
    trap = 132
    disarm_trap = 133
    vehicle_dragged = 134
    owner_destroyable = 135
    creature_wearable = 136
    no_nutrition = 137
    puppet = 138
    over_ride_enchant = 139
    meditation = 140
    transmutable = 141
    sign = 142
    streetlamp = 143
    visible_decay = 144
    bulk_container = 145
    bulk = 146
    mission = 147
    combine_cold = 148
    spawns_trees = 149
    kills_trees = 150
    crude = 151
    minable = 152
    enchant_jewelry = 153
    weapon_polearm = 154
    always_bankable = 155
    always_lit = 156
    not_mission = 157
    mass_production = 158
    can_have_inscription = 159
    no_work_parent = 160
    war_target = 161
    source_spring = 162
    source = 163
    color_component = 164
    tutorial = 165
    ten_per_tile = 166
    four_per_tile = 167
    ability = 168
    planted_flowerpot = 169
    equipment_slot = 170
    inventory_group = 171
    magical_staff = 172
    improve_uses_type_as_material = 173
    no_discard = 174
    instant_discard = 175
    transportable = 176
    war_machine = 177
    never_show_creation_window_option = 178
    brazier = 179
    uses_specified_container_volume = 180
    tent = 181
    use_material_and_kingdom = 182
    smearable = 183
    carpet = 184
    one_per_tile_border = 185
    nature_plantable = 186
    no_improve = 187
    tapestry = 188
    chall_newbie = 189
    unfinished_no_take = 190
    milk = 191
    cheese = 192
    cart = 193
    owner_turnable = 194
    owner_moveable = 195
    unfired = 196
    chair = 197
    lead_multiple_creatures = 198
    plantable = 199
    plant_one_a_week = 200
    hitch_target = 201
    spice = 205
    potable = 206
    no_create = 207
    food_group = 208
    cooker = 209
    tool_cooking = 210
    recipe_item = 211
    uses_food_state = 212
    fermented = 213
    distilled = 214
    sealable = 215
    use_real_template_icon = 216
    cooking_oil = 217
    hover = 218
    food_bonus_hot = 219
    food_bonus_cold = 220
    potted = 221
    can_be_papyrus_wrapped = 222
    can_be_raw_wrapped = 223
    can_be_cloth_wrapped = 224
    surface_only = 225
    mushroom = 226
    harvestable = 227
    show_raw = 228
    not_spell_target = 229
    trellis = 230
    ingredients_only = 231
    component_item = 232
    uses_real_template = 233
    larder = 234
    rune = 235
    pegable = 236
    decay_on_deed = 237
    insulated = 238
    guard_tower = 239
    parent_on_ground = 240
    road_marker = 241
    paveable = 242
    cave_paveable = 243
    decoration_when_planted = 244
    desc_is_name = 245
    any_cereal_food_group = 1157
    any_veggie_food_group = 1156
    any_cheese_food_group = 1198
    any_milk_food_group = 1200
    any_meat_food_group = 1261
    any_fish_food_group = 1201
    any_mushroom_food_group = 1199
    any_herb_food_group = 1158
    any_flower_food_group = 1267
    any_berry_food_group = 1179
    any_nut_food_group = 1197
    any_fruit_food_group = 1163
    any_spice_food_group = 1159
    pass


class ItemTemplate(Enum):
    NONE = dict({'name': 'none', 'ItemTemplateId': -1})
    GREEN_APPLE = dict({'name': 'green apple', 'ItemTemplateId': 6})
    HAND = dict({'name': 'hand', 'ItemTemplateId': 14})
    SHAFT = dict({'name': 'shaft', 'ItemTemplateId': 23})
    BARLEY = dict({'name': 'barley', 'ItemTemplateId': 28})
    WHEAT = dict({'name': 'wheat', 'ItemTemplateId': 29})
    RYE = dict({'name': 'rye', 'ItemTemplateId': 30})
    OAT = dict({'name': 'oat', 'ItemTemplateId': 31})
    CORN = dict({'name': 'corn', 'ItemTemplateId': 32})
    PUMPKIN = dict({'name': 'pumpkin', 'ItemTemplateId': 33})
    PUMPKIN_SEED = dict({'name': 'pumpkin seed', 'ItemTemplateId': 34})
    POTATO = dict({'name': 'potato', 'ItemTemplateId': 35})
    CAMPFIRE = dict({'name': 'campfire', 'ItemTemplateId': 37})
    CHEESE_DRILL = dict({'name': 'cheese drill', 'ItemTemplateId': 65})
    CHEESE = dict({'name': 'cheese', 'ItemTemplateId': 66})
    GOAT_CHEESE = dict({'name': 'goat cheese', 'ItemTemplateId': 67})
    FETA_CHEESE = dict({'name': 'feta cheese', 'ItemTemplateId': 68})
    BUFFALO_CHEESE = dict({'name': 'buffalo cheese', 'ItemTemplateId': 69})
    HONEY = dict({'name': 'honey', 'ItemTemplateId': 70})
    LYE = dict({'name': 'lye', 'ItemTemplateId': 73})
    FRYING_PAN = dict({'name': 'frying pan', 'ItemTemplateId': 75})
    POTTERY_JAR = dict({'name': 'pottery jar', 'ItemTemplateId': 76})
    POTTERY_BOWL = dict({'name': 'pottery bowl', 'ItemTemplateId': 77})
    MEAT = dict({'name': 'meat', 'ItemTemplateId': 92})
    BUTCHERING_KNIFE = dict({'name': 'butchering knife', 'ItemTemplateId': 93})
    HANDLE = dict({'name': 'handle', 'ItemTemplateId': 99})
    WATER = dict({'name': 'water', 'ItemTemplateId': 128})
    COOKED_MEAT = dict({'name': 'cooked meat', 'ItemTemplateId': 129})
    CANDLE = dict({'name': 'candle', 'ItemTemplateId': 133})
    HAZELNUTS = dict({'name': 'hazelnuts', 'ItemTemplateId': 134})
    FAT = dict({'name': 'fat', 'ItemTemplateId': 140})
    MILK = dict({'name': 'milk', 'ItemTemplateId': 142})
    COTTON_SEED = dict({'name': 'cotton seed', 'ItemTemplateId': 145})
    PIKE = dict({'name': 'pike', 'ItemTemplateId': 157})
    SMALLMOUTH_BASS = dict({'name': 'smallmouth bass', 'ItemTemplateId': 158})
    HERRING = dict({'name': 'herring', 'ItemTemplateId': 159})
    CATFISH = dict({'name': 'catfish', 'ItemTemplateId': 160})
    SNOOK = dict({'name': 'snook', 'ItemTemplateId': 161})
    ROACH = dict({'name': 'roach', 'ItemTemplateId': 162})
    PERCH = dict({'name': 'perch', 'ItemTemplateId': 163})
    CARP = dict({'name': 'carp', 'ItemTemplateId': 164})
    BROOK_TROUT = dict({'name': 'brook trout', 'ItemTemplateId': 165})
    WOOD_SCRAP = dict({'name': 'wood scrap', 'ItemTemplateId': 169})
    LEATHER_PIECES = dict({'name': 'leather pieces', 'ItemTemplateId': 172})
    PIG_FOOD = dict({'name': 'pig food', 'ItemTemplateId': 173})
    OVEN = dict({'name': 'oven', 'ItemTemplateId': 178})
    FORGE = dict({'name': 'forge', 'ItemTemplateId': 180})
    DOUGH = dict({'name': 'dough', 'ItemTemplateId': 200})
    FLOUR = dict({'name': 'flour', 'ItemTemplateId': 201})
    GRINDSTONE = dict({'name': 'grindstone', 'ItemTemplateId': 202})
    BREAD = dict({'name': 'bread', 'ItemTemplateId': 203})
    GREEN_MUSHROOM = dict({'name': 'green mushroom', 'ItemTemplateId': 246})
    BLACK_MUSHROOM = dict({'name': 'black mushroom', 'ItemTemplateId': 247})
    BROWN_MUSHROOM = dict({'name': 'brown mushroom', 'ItemTemplateId': 248})
    YELLOW_MUSHROOM = dict({'name': 'yellow mushroom', 'ItemTemplateId': 249})
    BLUE_MUSHROOM = dict({'name': 'blue mushroom', 'ItemTemplateId': 250})
    RED_MUSHROOM = dict({'name': 'red mushroom', 'ItemTemplateId': 251})
    SPOON = dict({'name': 'spoon', 'ItemTemplateId': 257})
    KNIFE = dict({'name': 'knife', 'ItemTemplateId': 258})
    FORK = dict({'name': 'fork', 'ItemTemplateId': 259})
    CORPSE = dict({'name': 'corpse', 'ItemTemplateId': 272})
    OPEN_HELM = dict({'name': 'open helm', 'ItemTemplateId': 287})
    TOOTH = dict({'name': 'tooth', 'ItemTemplateId': 303})
    HORN = dict({'name': 'horn', 'ItemTemplateId': 304})
    HOOF = dict({'name': 'hoof', 'ItemTemplateId': 306})
    TAIL = dict({'name': 'tail', 'ItemTemplateId': 307})
    EYE = dict({'name': 'eye', 'ItemTemplateId': 308})
    BLADDER = dict({'name': 'bladder', 'ItemTemplateId': 309})
    GLAND = dict({'name': 'gland', 'ItemTemplateId': 310})
    TWISTED_HORN = dict({'name': 'twisted horn', 'ItemTemplateId': 311})
    LONG_HORN = dict({'name': 'long horn', 'ItemTemplateId': 312})
    STEW = dict({'name': 'stew', 'ItemTemplateId': 345})
    CASSEROLE = dict({'name': 'casserole', 'ItemTemplateId': 346})
    MEAL = dict({'name': 'meal', 'ItemTemplateId': 347})
    GULASCH = dict({'name': 'gulasch', 'ItemTemplateId': 348})
    SALT = dict({'name': 'salt', 'ItemTemplateId': 349})
    SAUCE_PAN = dict({'name': 'sauce pan', 'ItemTemplateId': 350})
    CAULDRON = dict({'name': 'cauldron', 'ItemTemplateId': 351})
    SOUP = dict({'name': 'soup', 'ItemTemplateId': 352})
    LOVAGE = dict({'name': 'lovage', 'ItemTemplateId': 353})
    SAGE = dict({'name': 'sage', 'ItemTemplateId': 354})
    ONION = dict({'name': 'onion', 'ItemTemplateId': 355})
    GARLIC = dict({'name': 'garlic', 'ItemTemplateId': 356})
    OREGANO = dict({'name': 'oregano', 'ItemTemplateId': 357})
    PARSLEY = dict({'name': 'parsley', 'ItemTemplateId': 358})
    BASIL = dict({'name': 'basil', 'ItemTemplateId': 359})
    THYME = dict({'name': 'thyme', 'ItemTemplateId': 360})
    BELLADONNA = dict({'name': 'belladonna', 'ItemTemplateId': 361})
    STRAWBERRIES = dict({'name': 'strawberries', 'ItemTemplateId': 362})
    ROSEMARY = dict({'name': 'rosemary', 'ItemTemplateId': 363})
    BLUEBERRY = dict({'name': 'blueberry', 'ItemTemplateId': 364})
    NETTLES = dict({'name': 'nettles', 'ItemTemplateId': 365})
    SASSAFRAS = dict({'name': 'sassafras', 'ItemTemplateId': 366})
    LINGONBERRY = dict({'name': 'lingonberry', 'ItemTemplateId': 367})
    MEAT_FILLET = dict({'name': 'meat fillet', 'ItemTemplateId': 368})
    FISH_FILLET = dict({'name': 'fish fillet', 'ItemTemplateId': 369})
    PORRIDGE = dict({'name': 'porridge', 'ItemTemplateId': 373})
    CHERRIES = dict({'name': 'cherries', 'ItemTemplateId': 409})
    LEMON = dict({'name': 'lemon', 'ItemTemplateId': 410})
    BLUE_GRAPES = dict({'name': 'blue grapes', 'ItemTemplateId': 411})
    OLIVES = dict({'name': 'olives', 'ItemTemplateId': 412})
    FRUIT_PRESS = dict({'name': 'fruit press', 'ItemTemplateId': 413})
    GREEN_GRAPES = dict({'name': 'green grapes', 'ItemTemplateId': 414})
    MAPLE_SYRUP = dict({'name': 'maple syrup', 'ItemTemplateId': 415})
    MAPLE_SAP = dict({'name': 'maple sap', 'ItemTemplateId': 416})
    FRUIT_JUICE = dict({'name': 'fruit juice', 'ItemTemplateId': 417})
    OLIVE_OIL = dict({'name': 'olive oil', 'ItemTemplateId': 418})
    RED_WINE = dict({'name': 'red wine', 'ItemTemplateId': 419})
    WHITE_WINE = dict({'name': 'white wine', 'ItemTemplateId': 420})
    CAMELLIA = dict({'name': 'camellia', 'ItemTemplateId': 422})
    OLEANDER = dict({'name': 'oleander', 'ItemTemplateId': 423})
    LAVENDER_FLOWER = dict({'name': 'lavender flower', 'ItemTemplateId': 424})
    TEA = dict({'name': 'tea', 'ItemTemplateId': 425})
    ROSE_FLOWER = dict({'name': 'rose flower', 'ItemTemplateId': 426})
    LEMONADE = dict({'name': 'lemonade', 'ItemTemplateId': 427})
    JAM = dict({'name': 'jam', 'ItemTemplateId': 428})
    COCHINEAL = dict({'name': 'cochineal', 'ItemTemplateId': 439})
    EGG = dict({'name': 'egg', 'ItemTemplateId': 464})
    HUGE_EGG = dict({'name': 'huge egg', 'ItemTemplateId': 465})
    SANDWICH = dict({'name': 'sandwich', 'ItemTemplateId': 488})
    BOUQUET_OF_YELLOW_FLOWERS = dict({'name': 'bouquet of yellow flowers', 'ItemTemplateId': 498})
    BOUQUET_OF_ORANGE_RED_FLOWERS = dict({'name': 'bouquet of orange-red flowers', 'ItemTemplateId': 499})
    BOUQUET_OF_PURPLE_FLOWERS = dict({'name': 'bouquet of purple flowers', 'ItemTemplateId': 500})
    BOUQUET_OF_WHITE_FLOWERS = dict({'name': 'bouquet of white flowers', 'ItemTemplateId': 501})
    BOUQUET_OF_BLUE_FLOWERS = dict({'name': 'bouquet of blue flowers', 'ItemTemplateId': 502})
    BOUQUET_OF_GREENISH_YELLOW_FLOWERS = dict({'name': 'bouquet of greenish-yellow flowers', 'ItemTemplateId': 503})
    BOUQUET_OF_WHITE_DOTTED_FLOWERS = dict({'name': 'bouquet of white-dotted flowers', 'ItemTemplateId': 504})
    MARLIN = dict({'name': 'marlin', 'ItemTemplateId': 569})
    BLUE_SHARK = dict({'name': 'blue shark', 'ItemTemplateId': 570})
    WHITE_SHARK = dict({'name': 'white shark', 'ItemTemplateId': 571})
    OCTOPUS = dict({'name': 'octopus', 'ItemTemplateId': 572})
    SAILFISH = dict({'name': 'sailfish', 'ItemTemplateId': 573})
    DORADO = dict({'name': 'dorado', 'ItemTemplateId': 574})
    TUNA = dict({'name': 'tuna', 'ItemTemplateId': 575})
    DISHWATER = dict({'name': 'dishwater', 'ItemTemplateId': 634})
    HEART = dict({'name': 'heart', 'ItemTemplateId': 636})
    SLEEP_POWDER = dict({'name': 'sleep powder', 'ItemTemplateId': 666})
    BRANCH = dict({'name': 'branch', 'ItemTemplateId': 688})
    CAKE = dict({'name': 'cake', 'ItemTemplateId': 729})
    CAKE_SLICE = dict({'name': 'cake slice', 'ItemTemplateId': 730})
    REED_FIBRE = dict({'name': 'reed fibre', 'ItemTemplateId': 745})
    RICE = dict({'name': 'rice', 'ItemTemplateId': 746})
    PRESS = dict({'name': 'press', 'ItemTemplateId': 747})
    PAPYRUS_SHEET = dict({'name': 'papyrus sheet', 'ItemTemplateId': 748})
    STRAWBERRY_SEEDS = dict({'name': 'strawberry seeds', 'ItemTemplateId': 750})
    BLACK_INK = dict({'name': 'black ink', 'ItemTemplateId': 753})
    COOKED_RICE = dict({'name': 'cooked rice', 'ItemTemplateId': 754})
    KELP = dict({'name': 'kelp', 'ItemTemplateId': 755})
    SOURCE = dict({'name': 'source', 'ItemTemplateId': 763})
    SOURCE_SALT = dict({'name': 'source salt', 'ItemTemplateId': 764})
    WINE_BARREL = dict({'name': 'wine barrel', 'ItemTemplateId': 768})
    WALNUT = dict({'name': 'walnut', 'ItemTemplateId': 832})
    CHESTNUT = dict({'name': 'chestnut', 'ItemTemplateId': 833})
    RICE_PORRIDGE = dict({'name': 'rice porridge', 'ItemTemplateId': 856})
    RISOTTO = dict({'name': 'risotto', 'ItemTemplateId': 857})
    RICE_WINE = dict({'name': 'rice wine', 'ItemTemplateId': 858})
    CRAB_MEAT = dict({'name': 'crab meat', 'ItemTemplateId': 900})
    SHEEP_MILK = dict({'name': 'sheep milk', 'ItemTemplateId': 1012})
    BISON_MILK = dict({'name': 'bison milk', 'ItemTemplateId': 1013})
    RIFT_WOOD = dict({'name': 'rift wood', 'ItemTemplateId': 1104})
    MINT = dict({'name': 'mint', 'ItemTemplateId': 1130})
    FENNEL = dict({'name': 'fennel', 'ItemTemplateId': 1131})
    FENNEL_PLANT = dict({'name': 'fennel plant', 'ItemTemplateId': 1132})
    CARROT = dict({'name': 'carrot', 'ItemTemplateId': 1133})
    CABBAGE = dict({'name': 'cabbage', 'ItemTemplateId': 1134})
    TOMATO = dict({'name': 'tomato', 'ItemTemplateId': 1135})
    SUGAR_BEET = dict({'name': 'sugar beet', 'ItemTemplateId': 1136})
    LETTUCE = dict({'name': 'lettuce', 'ItemTemplateId': 1137})
    PEA_POD = dict({'name': 'pea pod', 'ItemTemplateId': 1138})
    SUGAR = dict({'name': 'sugar', 'ItemTemplateId': 1139})
    CUMIN = dict({'name': 'cumin', 'ItemTemplateId': 1140})
    GINGER = dict({'name': 'ginger', 'ItemTemplateId': 1141})
    NUTMEG = dict({'name': 'nutmeg', 'ItemTemplateId': 1142})
    PAPRIKA = dict({'name': 'paprika', 'ItemTemplateId': 1143})
    TURMERIC = dict({'name': 'turmeric', 'ItemTemplateId': 1144})
    CARROT_SEED = dict({'name': 'carrot seed', 'ItemTemplateId': 1145})
    CABBAGE_SEED = dict({'name': 'cabbage seed', 'ItemTemplateId': 1146})
    TOMATO_SEED = dict({'name': 'tomato seed', 'ItemTemplateId': 1147})
    SUGAR_BEET_SEED = dict({'name': 'sugar beet seed', 'ItemTemplateId': 1148})
    LETTUCE_SEED = dict({'name': 'lettuce seed', 'ItemTemplateId': 1149})
    PEA = dict({'name': 'pea', 'ItemTemplateId': 1150})
    FENNEL_SEED = dict({'name': 'fennel seed', 'ItemTemplateId': 1151})
    COCOA = dict({'name': 'cocoa', 'ItemTemplateId': 1152})
    PAPRIKA_SEED = dict({'name': 'paprika seed', 'ItemTemplateId': 1153})
    TURMERIC_SEED = dict({'name': 'turmeric seed', 'ItemTemplateId': 1154})
    COCOA_BEAN = dict({'name': 'cocoa bean', 'ItemTemplateId': 1155})
    ANY_VEG = dict({'name': 'any veg', 'ItemTemplateId': 1156})
    ANY_CEREAL = dict({'name': 'any cereal', 'ItemTemplateId': 1157})
    ANY_HERB = dict({'name': 'any herb', 'ItemTemplateId': 1158})
    ANY_SPICE = dict({'name': 'any spice', 'ItemTemplateId': 1159})
    ANY_FRUIT = dict({'name': 'any fruit', 'ItemTemplateId': 1163})
    PIE_DISH = dict({'name': 'pie dish', 'ItemTemplateId': 1165})
    CAKE_TIN = dict({'name': 'cake tin', 'ItemTemplateId': 1166})
    BAKING_STONE = dict({'name': 'baking stone', 'ItemTemplateId': 1167})
    ROASTING_DISH = dict({'name': 'roasting dish', 'ItemTemplateId': 1169})
    SLICE_OF_BREAD = dict({'name': 'slice of bread', 'ItemTemplateId': 1170})
    PLATE = dict({'name': 'plate', 'ItemTemplateId': 1173})
    BATTER = dict({'name': 'batter', 'ItemTemplateId': 1174})
    FUDGE_SAUCE = dict({'name': 'fudge sauce', 'ItemTemplateId': 1176})
    PIE = dict({'name': 'pie', 'ItemTemplateId': 1177})
    STILL = dict({'name': 'still', 'ItemTemplateId': 1178})
    ANY_BERRY = dict({'name': 'any berry', 'ItemTemplateId': 1179})
    MEAD = dict({'name': 'mead', 'ItemTemplateId': 1180})
    CIDER = dict({'name': 'cider', 'ItemTemplateId': 1181})
    BEER = dict({'name': 'beer', 'ItemTemplateId': 1182})
    WHISKY = dict({'name': 'whisky', 'ItemTemplateId': 1183})
    PINENUT = dict({'name': 'pinenut', 'ItemTemplateId': 1184})
    CHOCOLATE = dict({'name': 'chocolate', 'ItemTemplateId': 1185})
    BUTTER = dict({'name': 'butter', 'ItemTemplateId': 1186})
    OMELETTE = dict({'name': 'omelette', 'ItemTemplateId': 1187})
    CURRY = dict({'name': 'curry', 'ItemTemplateId': 1188})
    SALAD = dict({'name': 'salad', 'ItemTemplateId': 1189})
    SAUSAGE = dict({'name': 'sausage', 'ItemTemplateId': 1190})
    BACON = dict({'name': 'bacon', 'ItemTemplateId': 1191})
    CORN_DOUGH = dict({'name': 'corn dough', 'ItemTemplateId': 1192})
    COOKING_OIL = dict({'name': 'cooking oil', 'ItemTemplateId': 1193})
    GRAVY = dict({'name': 'gravy', 'ItemTemplateId': 1194})
    CUSTARD = dict({'name': 'custard', 'ItemTemplateId': 1195})
    RASPBERRIES = dict({'name': 'raspberries', 'ItemTemplateId': 1196})
    ANY_NUT = dict({'name': 'any nut', 'ItemTemplateId': 1197})
    ANY_CHEESE = dict({'name': 'any cheese', 'ItemTemplateId': 1198})
    ANY_MUSHROOM = dict({'name': 'any mushroom', 'ItemTemplateId': 1199})
    ANY_MILK = dict({'name': 'any milk', 'ItemTemplateId': 1200})
    ANY_FISH = dict({'name': 'any fish', 'ItemTemplateId': 1201})
    BISCUIT = dict({'name': 'biscuit', 'ItemTemplateId': 1202})
    FRIES = dict({'name': 'fries', 'ItemTemplateId': 1203})
    GELATINE = dict({'name': 'gelatine', 'ItemTemplateId': 1204})
    HONEY_WATER = dict({'name': 'honey water', 'ItemTemplateId': 1205})
    PASSATA = dict({'name': 'passata', 'ItemTemplateId': 1206})
    PASTA = dict({'name': 'pasta', 'ItemTemplateId': 1207})
    PASTRY = dict({'name': 'pastry', 'ItemTemplateId': 1208})
    PESTO = dict({'name': 'pesto', 'ItemTemplateId': 1209})
    STOCK = dict({'name': 'stock', 'ItemTemplateId': 1210})
    TOMATO_KETCHUP = dict({'name': 'tomato ketchup', 'ItemTemplateId': 1211})
    WHITE_SAUCE = dict({'name': 'white sauce', 'ItemTemplateId': 1212})
    WORT = dict({'name': 'wort', 'ItemTemplateId': 1213})
    RAT_ON_A_STICK = dict({'name': 'rat-on-a-stick', 'ItemTemplateId': 1214})
    HOG_ROAST = dict({'name': 'hog roast', 'ItemTemplateId': 1215})
    LAMB_SPIT = dict({'name': 'lamb spit', 'ItemTemplateId': 1216})
    MUSHY_PEAS = dict({'name': 'mushy peas', 'ItemTemplateId': 1217})
    CROUTONS = dict({'name': 'croutons', 'ItemTemplateId': 1218})
    HAGGIS = dict({'name': 'haggis', 'ItemTemplateId': 1219})
    CORNFLOUR = dict({'name': 'cornflour', 'ItemTemplateId': 1220})
    CHEESECAKE = dict({'name': 'cheesecake', 'ItemTemplateId': 1221})
    KIELBASA = dict({'name': 'kielbasa', 'ItemTemplateId': 1222})
    MUSHROOM = dict({'name': 'mushroom', 'ItemTemplateId': 1223})
    STUFFED_MUSHROOM = dict({'name': 'stuffed mushroom', 'ItemTemplateId': 1224})
    CRISPS = dict({'name': 'crisps', 'ItemTemplateId': 1225})
    JELLY = dict({'name': 'jelly', 'ItemTemplateId': 1226})
    SCONE = dict({'name': 'scone', 'ItemTemplateId': 1227})
    TOAST = dict({'name': 'toast', 'ItemTemplateId': 1228})
    PASTY = dict({'name': 'pasty', 'ItemTemplateId': 1229})
    CHOCOLATE_NUT_SPREAD = dict({'name': 'chocolate nut spread', 'ItemTemplateId': 1230})
    VODKA = dict({'name': 'vodka', 'ItemTemplateId': 1231})
    BRANDY = dict({'name': 'brandy', 'ItemTemplateId': 1232})
    MOONSHINE = dict({'name': 'moonshine', 'ItemTemplateId': 1233})
    GIN = dict({'name': 'gin', 'ItemTemplateId': 1234})
    PINEAPPLE = dict({'name': 'pineapple', 'ItemTemplateId': 1235})
    SAUSAGE_SKIN = dict({'name': 'sausage skin', 'ItemTemplateId': 1236})
    MORTAR_AND_PESTLE = dict({'name': 'mortar and pestle', 'ItemTemplateId': 1237})
    ROCK_SALT = dict({'name': 'rock salt', 'ItemTemplateId': 1238})
    SPAGHETTI = dict({'name': 'spaghetti', 'ItemTemplateId': 1240})
    ICING = dict({'name': 'icing', 'ItemTemplateId': 1241})
    CAKE_MIX = dict({'name': 'cake mix', 'ItemTemplateId': 1242})
    BREADCRUMBS = dict({'name': 'breadcrumbs', 'ItemTemplateId': 1244})
    MEATBALLS = dict({'name': 'meatballs', 'ItemTemplateId': 1245})
    VINEGAR = dict({'name': 'vinegar', 'ItemTemplateId': 1246})
    CUCUMBER = dict({'name': 'cucumber', 'ItemTemplateId': 1247})
    CUCUMBER_SEED = dict({'name': 'cucumber seed', 'ItemTemplateId': 1248})
    CREAM = dict({'name': 'cream', 'ItemTemplateId': 1249})
    GOBLIN_SKULL = dict({'name': 'goblin skull', 'ItemTemplateId': 1250})
    BISCUIT_MIX = dict({'name': 'biscuit mix', 'ItemTemplateId': 1256})
    SCONE_MIX = dict({'name': 'scone mix', 'ItemTemplateId': 1257})
    TART = dict({'name': 'tart', 'ItemTemplateId': 1258})
    STIR_FRY = dict({'name': 'stir fry', 'ItemTemplateId': 1259})
    NORI = dict({'name': 'nori', 'ItemTemplateId': 1260})
    ANY_MEAT = dict({'name': 'any meat', 'ItemTemplateId': 1261})
    PIZZA = dict({'name': 'pizza', 'ItemTemplateId': 1262})
    ANY_OIL = dict({'name': 'any oil', 'ItemTemplateId': 1263})
    SUSHI = dict({'name': 'sushi', 'ItemTemplateId': 1264})
    PICKLE = dict({'name': 'pickle', 'ItemTemplateId': 1265})
    PUDDING = dict({'name': 'pudding', 'ItemTemplateId': 1266})
    ANY_FLOWER = dict({'name': 'any flower', 'ItemTemplateId': 1267})
    BROTH = dict({'name': 'broth', 'ItemTemplateId': 1268})
    WOOD_PULP = dict({'name': 'wood pulp', 'ItemTemplateId': 1270})
    PAPER_SHEET = dict({'name': 'paper sheet', 'ItemTemplateId': 1272})
    HOPS = dict({'name': 'hops', 'ItemTemplateId': 1273})
    SNOWBALL = dict({'name': 'snowball', 'ItemTemplateId': 1276})
    COCONUT = dict({'name': 'coconut', 'ItemTemplateId': 1280})
    ICE_CREAM = dict({'name': 'ice cream', 'ItemTemplateId': 1281})
    SWEET = dict({'name': 'sweet', 'ItemTemplateId': 1282})
    ORANGE = dict({'name': 'orange', 'ItemTemplateId': 1283})
    BOILER = dict({'name': 'boiler', 'ItemTemplateId': 1284})
    RUM = dict({'name': 'rum', 'ItemTemplateId': 1286})
    MUFFIN = dict({'name': 'muffin', 'ItemTemplateId': 1287})
    COOKIE = dict({'name': 'cookie', 'ItemTemplateId': 1288})
    pass


class Creature(Enum):
    NONE = dict({"creatureId": 0, "name": "None", "description": "None"})
    HUMAN = dict({"creatureId": 1, "name": "Human", "description": "Another explorer."})
    SALESMAN = dict(
        {"creatureId": 9, "name": "Salesman", "description": "An envoy from the king, buying and selling items."})
    BROWN_COW = dict({"creatureId": 3, "name": "Brown cow", "description": "A brown docile cow."})
    GUARDTOUGH = dict(
        {"creatureId": 7, "name": "guardTough", "description": "This warrior would pose problems for any intruder."})
    GUARDBRUTAL = dict(
        {"creatureId": 8, "name": "guardBrutal", "description": "Not many people would like to cross this warrior."})
    BLACK_WOLF = dict({"creatureId": 10, "name": "Black wolf",
                       "description": "This dark shadow of the forests glares hungrily at you."})
    TROLL = dict({"creatureId": 11, "name": "Troll",
                  "description": "A dark green stinking troll. Always hungry. Always deadly."})
    BROWN_BEAR = dict({"creatureId": 12, "name": "Brown bear",
                       "description": "The brown bear has a distinctive hump on the shoulders, and long deadly claws "
                                      "on the front paws."})
    black_bear = dict({"creatureId": 42, "name": "Black bear",
                       "description": "The black bear looks pretty kind, but has strong, highly curved claws ready to "
                                      "render you to pieces."})
    LARGE_RAT = dict({"creatureId": 13, "name": "Large rat",
                      "description": "This is an unnaturally large version of a standard black rat."})
    CAVE_BUG = dict({"creatureId": 43, "name": "Cave bug",
                     "description": "Some kind of unnaturally large and deformed insect lunges at you from the dark. "
                                    "It has a grey carapace, with small patches of lichen growing here and there."})
    MOUNTAIN_LION = dict({"creatureId": 14, "name": "Mountain lion",
                          "description": "Looking like a huge cat, it is tawny-coloured, with a small head and small, "
                                         "rounded, black-tipped ears."})
    WILD_CAT = dict({"creatureId": 15, "name": "Wild cat", "description": "A small wild cat, fierce and aggressive."})
    JOE_THE_STUPE = dict({"creatureId": 2, "name": "Joe the Stupe",
                          "description": "A hollow-eyed person is standing here, potentially dangerous but stupid as "
                                         "ever."})
    RED_DRAGON = dict({"creatureId": 16, "name": "Red dragon",
                       "description": "The menacing huge dragon, with scales in every possible red color."})
    GREEN_DRAGON_HATCHLING = dict({"creatureId": 17, "name": "Green dragon hatchling",
                                   "description": "The green dragon hatchling is not as large as a full-grown dragon "
                                                  "and unable to fly."})
    BLACK_DRAGON_HATCHLING = dict({"creatureId": 18, "name": "Black dragon hatchling",
                                   "description": "The black dragon hatchling is not as large as a full-grown dragon "
                                                  "and unable to fly."})
    WHITE_DRAGON_HATCHLING = dict({"creatureId": 19, "name": "White dragon hatchling",
                                   "description": "The white dragon hatchling is not as large as a full-grown dragon "
                                                  "and unable to fly."})
    FOREST_GIANT = dict({"creatureId": 20, "name": "Forest giant",
                         "description": "With an almost sad look upon its face, this filthy giant might be mistaken "
                                        "for a harmless huge baby."})
    UNICORN = dict(
        {"creatureId": 21, "name": "Unicorn", "description": "A bright white unicorn with a slender twisted horn."})
    KYKLOPS = dict({"creatureId": 22, "name": "Kyklops",
                    "description": "This large drooling one-eyed giant is obviously too stupid to feel any mercy."})
    GOBLIN = dict({"creatureId": 23, "name": "Goblin",
                   "description": "This small, dirty creature looks at you greedily, and would go into a frenzy if "
                                  "you show pain."})
    HUGE_SPIDER = dict({"creatureId": 25, "name": "Huge spider",
                        "description": "Monstrously huge and fast, these spiders love to be played with."})
    LAVA_SPIDER = dict({"creatureId": 56, "name": "Lava spider",
                        "description": "Lava spiders usually lurk in their lava pools, catching curious prey."})
    GOBLIN_LEADER = dict({"creatureId": 26, "name": "Goblin leader",
                          "description": "Always on the brink of cackling wildly, this creature is possibly insane."})
    TROLL_KING = dict({"creatureId": 27, "name": "Troll king",
                       "description": "This troll has a scary clever look in his eyes. He surely knows what he is "
                                      "doing."})
    SPIRIT_GUARD = dict({"creatureId": 28, "name": "Spirit guard",
                         "description": "This fierce spirit vaguely resembles a human warrior, and for some reason "
                                        "guards here."})
    SPIRIT_SENTRY = dict({"creatureId": 29, "name": "Spirit sentry",
                          "description": "This spirit vaguely resembles a human being, and for some reason guards here."
                          })
    SPIRIT_AVENGER = dict({"creatureId": 30, "name": "Spirit avenger",
                           "description": "This restless spirit vaguely resembles a human being, that for some reason "
                                          "has chosen to guard this place."})
    SPIRIT_BRUTE = dict({"creatureId": 31, "name": "Spirit brute",
                         "description": "This fierce spirit seems restless and upset but for some reason has chosen "
                                        "to guard this place."})
    SPIRIT_TEMPLAR = dict({"creatureId": 32, "name": "Spirit templar",
                           "description": "The spirit of a proud knight has decided to protect this place."})
    SPIRIT_SHADOW = dict({"creatureId": 33, "name": "Spirit shadow",
                          "description": "A dark humanoid shadow looms about, its intentions unclear."})
    JENN_KELLON_TOWER_GUARD = dict({"creatureId": 34, "name": "Jenn - Kellon tower guard",
                                    "description": "This person seems to be able to put up some resistance. These "
                                                   "guards will help defend you if you say help."})
    HORDE_OF_THE_SUMMONED_TOWER_GUARD = dict({"creatureId": 35, "name": "Horde of the Summoned tower guard",
                                              "description": "This person seems to be able to put up some resistance. "
                                                             "These guards will help defend you if you say help."})
    MOL_REHAN_TOWER_GUARD = dict({"creatureId": 36, "name": "Mol - Rehan tower guard",
                                  "description": "This person seems to be able to put up some resistance. These "
                                                 "guards will help defend you if you say help."})
    ISLES_TOWER_GUARD = dict({"creatureId": 67, "name": "Isles tower guard",
                              "description": "This person seems to be able to put up some resistance. These guards "
                                             "will help defend you if you say help."})
    BARTENDER = dict({"creatureId": 41, "name": "Bartender",
                      "description": "A fat and jolly bartender, eager to help people settling in."})
    SANTA_CLAUS = dict({"creatureId": 46, "name": "Santa Claus",
                        "description": "Santa Claus is standing here, with a jolly face behind his huge white beard."})
    EVIL_SANTA = dict({"creatureId": 47, "name": "Evil Santa",
                       "description": "Some sort of Santa Claus is standing here, with a fat belly, yellow eyes, "
                                      "and a bad breath."})
    WILD_BOAR = dict(
        {"creatureId": 37, "name": "Wild boar", "description": "A large and strong boar is grunting here."})
    MOUNTAIN_GORILLA = dict({"creatureId": 39, "name": "Mountain gorilla",
                             "description": "This normally calm mountain gorilla may suddenly become a very fierce "
                                            "and dangerous foe if annoyed."})
    ANACONDA = dict({"creatureId": 38, "name": "Anaconda",
                     "description": "An over 3 meters long muscle, this grey-green snake is formidable."})
    RABID_HYENA = dict({"creatureId": 40, "name": "Rabid hyena",
                        "description": "Normally this doglike creature would act very cowardly, but some sickness "
                                       "seems to have driven it mad and overly aggressive."})
    PIG = dict({"creatureId": 44, "name": "Pig", "description": "A pig is here, wallowing in the mud."})
    HEN = dict({"creatureId": 45, "name": "Hen", "description": "A fine hen proudly prods around here."})
    ROOSTER = dict({"creatureId": 52, "name": "Rooster", "description": "A proud rooster struts around here."})
    CHICKEN = dict({"creatureId": 48, "name": "Chicken", "description": "A cute chicken struts around here."})
    DOG = dict({"creatureId": 51, "name": "Dog",
                "description": "Occasionally this dog will bark and scratch itself behind the ears."})
    CALF = dict({"creatureId": 50, "name": "Calf", "description": "This calf looks happy and free."})
    BULL = dict({"creatureId": 49, "name": "Bull", "description": "This bull looks pretty menacing."})
    BISON = dict(
        {"creatureId": 82, "name": "Bison", "description": "The bison are impressive creatures when moving in hordes."})
    HORSE = dict({"creatureId": 64, "name": "Horse", "description": "Horses like this one have many uses."})
    FOAL = dict({"creatureId": 65, "name": "Foal", "description": "A foal skips around here merrily."})
    EASTER_BUNNY = dict({"creatureId": 53, "name": "Easter bunny",
                         "description": "Wow, the mystical easter bunny skips around here joyfully!"})
    DEER = dict({"creatureId": 54, "name": "Deer", "description": "A fallow deer is here, watching for enemies."})
    PHEASANT = dict(
        {"creatureId": 55, "name": "Pheasant", "description": "The pheasant slowly paces here, vigilant as always."})
    LAVA_FIEND = dict({"creatureId": 57, "name": "Lava fiend",
                       "description": "These lava creatures enter the surface through lava pools, probably in order "
                                      "to hunt. Or burn."})
    CROCODILE = dict({"creatureId": 58, "name": "Crocodile",
                      "description": "This meat-eating reptile swims very well but may also perform quick rushes on "
                                     "land in order to catch you."})
    SCORPION = dict({"creatureId": 59, "name": "Scorpion",
                     "description": "The monstruously large type of scorpion found in woods and caves here is fairly "
                                    "aggressive."})
    TORMENTOR = dict({"creatureId": 60, "name": "Tormentor",
                      "description": "A particularly grim person stands here, trying to sort things out."})
    GUIDE = dict({"creatureId": 61, "name": "Guide",
                  "description": "A rather stressed out person is here giving instructions on how to survive to "
                                 "everyone who just arrived."})
    LADY_OF_THE_LAKE = dict({"creatureId": 62, "name": "Lady of the lake",
                             "description": "The hazy shape of a female spirit lingers below the waves."})
    COBRA_KING = dict({"creatureId": 63, "name": "Cobra King",
                       "description": "A huge menacing king cobra is guarding here, head swaying back and forth."})
    CHILD = dict({"creatureId": 66, "name": "Child", "description": "A small child is here, exploring the world."})
    AVENGER_OF_THE_LIGHT = dict({"creatureId": 68, "name": "Avenger of the Light",
                                 "description": "Some kind of giant lumbers here, hunting humans."})
    ZOMBIE = dict({"creatureId": 69, "name": "Zombie",
                   "description": "A very bleak humanlike creature stands here, looking abscent-minded."})
    SEA_SERPENT = dict({"creatureId": 70, "name": "Sea Serpent",
                        "description": "Sea Serpents are said to sleep in the dark caves of the abyss for years, "
                                       "then head to the surface to hunt once they get hungry."})
    HUGE_SHARK = dict({"creatureId": 71, "name": "Huge shark",
                       "description": "These huge sharks were apparently not just a rumour. How horrendous!"})
    SOL_DEMON = dict({"creatureId": 72, "name": "Sol Demon", "description": "This demon has been released from Sol."})
    DEATHCRAWLER_MINION = dict({"creatureId": 73, "name": "Deathcrawler minion",
                                "description": "The Deathcrawler minions usually spawn in large numbers. They have "
                                               "deadly poisonous bites."})
    SPAWN_OF_UTTACHA = dict({"creatureId": 74, "name": "Spawn of Uttacha",
                             "description": "Uttacha is a vengeful demigod who lives in the depths of an ocean on "
                                            "Valrei. These huge larvae are hungry and confused abominations here."})
    SON_OF_NOGUMP = dict({"creatureId": 75, "name": "Son of Nogump",
                          "description": "Nogump the dirty has given birth to this foul two-headed giant wielding a "
                                         "huge twohanded sword."})
    DRAKESPIRIT = dict({"creatureId": 76, "name": "Drakespirit",
                        "description": "Drakespirits are usually found in their gardens on Valrei. They are hungry "
                                       "and aggressive."})
    EAGLESPIRIT = dict({"creatureId": 77, "name": "Eaglespirit",
                        "description": "The Eaglespirits live on a glacier on Valrei. They will attack if hungry or "
                                       "threatened."})
    EPIPHANY_OF_VYNORA = dict({"creatureId": 78, "name": "Epiphany of Vynora",
                               "description": "This female creature is almost see-through, and you wonder if she is "
                                              "made of water or thoughts alone."})
    JUGGERNAUT_OF_MAGRANON = dict({"creatureId": 79, "name": "Juggernaut of Magranon",
                                   "description": "A ferocious beast indeed, the juggernaut can crush mountains with "
                                                  "its horned forehead."})
    MANIFESTATION_OF_FO = dict({"creatureId": 80, "name": "Manifestation of Fo",
                                "description": "Something seems to have gone wrong as Fo tried to create his "
                                               "manifestation. The thorns are not loving at all and it seems very "
                                               "aggressive."})
    INCARNATION_OF_LIBILA = dict({"creatureId": 81, "name": "Incarnation of Libila",
                                  "description": "This terrifying female apparition has something disturbing over it. "
                                                 "As if it's just one facet of Libila."})
    HELL_HORSE = dict({"creatureId": 83, "name": "Hell Horse",
                       "description": "This fiery creature is rumoured to be the mounts of the demons of Sol."})
    HELL_HOUND = dict({"creatureId": 84, "name": "Hell Hound",
                       "description": "The hell hound is said to be spies and assassins for the demons of Sol."})
    HELL_SCORPIOUS = dict(
        {"creatureId": 85, "name": "Hell Scorpious", "description": "The pets of the demons of Sol are very playful."})
    WORG = dict({"creatureId": 86, "name": "Worg",
                 "description": "This wolf-like creature is unnaturally big and clumsy. The Worg seems finicky and "
                                "nervous, which makes it unpredictable and dangerous to deal with."})
    SKELETON = dict(
        {"creatureId": 87, "name": "Skeleton", "description": "This abomination has been animated by powerful magic."})
    WRAITH = dict(
        {"creatureId": 88, "name": "Wraith", "description": "The wraith is born of darkness and shuns the daylight."})
    SEAL = dict({"creatureId": 93, "name": "Seal",
                 "description": "These creatures love to bathe in the sun and go for a swim hunting fish."})
    TORTOISE = dict({"creatureId": 94, "name": "Tortoise",
                     "description": "The tortoise is pretty harmless but can pinch you quite bad with its bite."})
    CRAB = dict({"creatureId": 95, "name": "Crab", "description": "Crabs are known to hide well and walk sideways."})
    SHEEP = dict({"creatureId": 96, "name": "Sheep",
                  "description": "A mythical beast of legends, it stares back at you with blood filled eyes and froth "
                                 "around the mouth."})
    BLUE_WHALE = dict({"creatureId": 97, "name": "Blue whale",
                       "description": "These gigantic creatures travel huge distances looking for food, while singing "
                                      "their mysterious songs."})
    SEAL_CUB = dict(
        {"creatureId": 98, "name": "Seal cub", "description": "A young seal, waiting to be fed luscious fish."})
    DOLPHIN = dict({"creatureId": 99, "name": "Dolphin",
                    "description": "A playful dolphin. They have been known to defend sailors in distress from their "
                                   "natural enemy, the shark."})
    OCTOPUS = dict({"creatureId": 100, "name": "Octopus",
                    "description": "Larger specimen have been known to pull whole ships down into the abyss. Luckily "
                                   "this one is small."})
    LAMB = dict({"creatureId": 101, "name": "Lamb", "description": "A small cuddly ball of fluff."})
    RAM = dict({"creatureId": 102, "name": "Ram",
                "description": "A mythical beast of legends, it stares back at you with blood filled eyes and froth "
                               "around the mouth."})
    BLACK_DRAGON = dict({"creatureId": 89, "name": "Black dragon",
                         "description": "The menacing huge dragon, with scales as dark as the night."})
    BLUE_DRAGON = dict(
        {"creatureId": 91, "name": "Blue dragon", "description": "The menacing huge dragon, with dark blue scales."})
    GREEN_DRAGON = dict({"creatureId": 90, "name": "Green dragon",
                         "description": "The menacing huge dragon, with emerald green scales."})
    WHITE_DRAGON = dict(
        {"creatureId": 92, "name": "White dragon", "description": "The menacing huge dragon, with snow white scales."})
    BLUE_DRAGON_HATCHLING = dict({"creatureId": 104, "name": "Blue dragon hatchling",
                                  "description": "The blue dragon hatchling is not as large as a full-grown dragon "
                                                 "and unable to fly."})
    RED_DRAGON_HATCHLING = dict({"creatureId": 103, "name": "Red dragon hatchling",
                                 "description": "The red dragon hatchling is not as large as a full-grown dragon and "
                                                "unable to fly."})
    FOG_SPIDER = dict({"creatureId": 105, "name": "Fog Spider",
                       "description": "Usually only encountered under foggy conditions, this creature is often "
                                      "considered an Omen."})
    RIFT_BEAST = dict({"creatureId": 106, "name": "Rift Beast",
                       "description": "These vile creatures emerge from the rift in great numbers."})
    RIFT_JACKAL = dict({"creatureId": 107, "name": "Rift Jackal",
                        "description": "The Jackals accompany the Beasts as they spew out of the rift."})
    RIFT_OGRE = dict({"creatureId": 108, "name": "Rift Ogre",
                      "description": "The Rift Ogres seem to bully Beasts and Jackals into following orders."})
    RIFT_WARMASTER = dict(
        {"creatureId": 109, "name": "Rift Warmaster", "description": "These plan and lead attacks from the rift."})
    RIFT_OGRE_MAGE = dict(
        {"creatureId": 111, "name": "Rift Ogre Mage", "description": "Ogre Mages have mysterious powers."})
    RIFT_CASTER = dict({"creatureId": 110, "name": "Rift Caster",
                        "description": "Proficient spell casters, but they seem to avoid direct contact."})
    RIFT_SUMMONER = dict({"creatureId": 112, "name": "Rift Summoner",
                          "description": "Summoners seem to be able to call for aid from the Rift."})
    NPC_HUMAN = dict({"creatureId": 113, "name": "NPC Human",
                      "description": "A relatively normal person stands here waiting for something to happen."})
    NPC_WAGONER = dict({"creatureId": 114, "name": "NPC Wagoner",
                        "description": "A relatively normal person stands here waiting to help transport bulk goods."})
    WAGON_CREATURE = dict({"creatureId": 115, "name": "Wagon Creature",
                           "description": "The wagon creature is only used for hauling a wagoner's wagon."})
    WEAPON_TEST_DUMMY = dict({"creatureId": 116, "name": "Weapon Test Dummy",
                              "description": "An immortal that shouts out any damage that it receives, "
                                             "then immediately heals."})
    pass


class Cooker(Enum):
    CAMPFIRE = dict({'itemTemplate': ItemTemplate.CAMPFIRE})
    OVEN = dict({'itemTemplate': ItemTemplate.OVEN})
    FORGE = dict({'itemTemplate': ItemTemplate.FORGE})

    # if (recipe.hasCooker()) {
    #    final Item cooker = target.getTopParentOrNull();
    #    if (cooker != null) {
    #        ibonus += cooker.getTemplateId();
    #        if (!Server.getInstance().isPS()) {
    #            ibonus += cooker.getRarity();
    #        }
    #    }
    # }

    def __init__(self):
        self.itemTemplate = ItemTemplate.NONE
        self.difficulty = 0
        self.rarity = Rarity.NONE

    pass


class Container(Enum):
    NONE = dict({"itemTemplate": ItemTemplate.NONE, "name": "none"})
    FRYING_PAN = dict({"itemTemplate": ItemTemplate.FRYING_PAN, "name": "frying pan"})
    POTTERY_JAR = dict({"itemTemplate": ItemTemplate.POTTERY_JAR, "name": "pottery jar"})
    POTTERY_BOWL = dict({"itemTemplate": ItemTemplate.POTTERY_BOWL, "name": "pottery bowl"})
    CORPSE = dict({"itemTemplate": ItemTemplate.CORPSE, "name": "corpse"})
    OPEN_HELM = dict({"itemTemplate": ItemTemplate.OPEN_HELM, "name": "open helm"})
    SAUCE_PAN = dict({"itemTemplate": ItemTemplate.SAUCE_PAN, "name": "sauce pan"})
    CAULDRON = dict({"itemTemplate": ItemTemplate.CAULDRON, "name": "cauldron"})
    WINE_BARREL = dict({"itemTemplate": ItemTemplate.WINE_BARREL, "name": "wine barrel"})
    PIE_DISH = dict({"itemTemplate": ItemTemplate.PIE_DISH, "name": "pie dish"})
    CAKE_TIN = dict({"itemTemplate": ItemTemplate.CAKE_TIN, "name": "cake tin"})
    BAKING_STONE = dict({"itemTemplate": ItemTemplate.BAKING_STONE, "name": "backing stone"})
    ROASTING_DISH = dict({"itemTemplate": ItemTemplate.ROASTING_DISH, "name": "roasting dish"})
    PLATE = dict({"itemTemplate": ItemTemplate.PLATE, "name": "plate"})
    MUSHROOM = dict({"itemTemplate": ItemTemplate.MUSHROOM, "name": "mushroom"})
    SAUSAGE_SKIN = dict({"itemTemplate": ItemTemplate.SAUSAGE_SKIN, "name": "sausage skin"})
    BOILER = dict({"itemTemplate": ItemTemplate.BOILER, "name": "boiler"})

    # ibonus += target.getTemplateId();

    def __init__(self):
        self.itemTemplate = ItemTemplate.NONE
        self.difficulty = 0

    pass


class CookedState(Enum):
    NONE = dict({"cookedStateId": -1, "name": "none"})
    RAW = dict({"cookedStateId": 0, "name": "raw"})
    FRIED = dict({"cookedStateId": 1, "name": "fried"})
    GRILLED = dict({"cookedStateId": 2, "name": "grilled"})
    BOILED = dict({"cookedStateId": 3, "name": "boiled"})
    ROASTED = dict({"cookedStateId": 4, "name": "roasted"})
    STEAMED = dict({"cookedStateId": 5, "name": "steamed"})
    BAKED = dict({"cookedStateId": 6, "name": "baked"})
    COOKED = dict({"cookedStateId": 7, "name": "cooked"})
    CANDIED = dict({"cookedStateId": 8, "name": "candied"})
    CHOCOLATE_COATED = dict({"cookedStateId": 9, "name": "chocolate coated"})

    # Recipes.convertCookingStateIntoByte(). Only one cooked state can exists for an item.
    # The first 16 values of auxData (of which 0-9 are used below) is reserved for remember anyone of these states.
    # see Item.setRightAuxData() and its uses.

    pass


class PreparedState(Enum):
    NONE = 0B0
    CHOPPED = 0B00010000
    DICED = 0B00010000
    GROUND = 0B00010000
    UNFERMENTED = 0B00010000
    ZOMBIEFIED = 0B00010000
    WHIPPED = 0B00010000
    MASHED = 0B00100000
    MINCED = 0B00100000
    FERMENTING = 0B00100000
    CLOTTED = 0B00100000
    WRAPPED = 0B01000000
    UNDISTILLED = 0B01000000
    SALTED = 0B10000000
    FRESH = 0B10000000
    # Multiple states can exists at once. A mask is used to toggle a bit position. some states use the same
    # position and can't exists simultaneously.
    # see Recipes.convertPhysicalStateIntoByte(). Different states are referenced with the "+".
    # This is stored in the last 4 bytes of auxData.
    pass


class Material(Enum):
    NONE = dict({"materialId": 0, "name": "none"})
    FLESH = dict({"materialId": 1, "name": "flesh"})
    MEAT = dict({"materialId": 2, "name": "meat"})
    RYE = dict({"materialId": 3, "name": "rye"})
    OAT = dict({"materialId": 4, "name": "oat"})
    BARLEY = dict({"materialId": 5, "name": "barley"})
    WHEAT = dict({"materialId": 6, "name": "wheat"})
    GOLD = dict({"materialId": 7, "name": "gold"})
    SILVER = dict({"materialId": 8, "name": "silver"})
    STEEL = dict({"materialId": 9, "name": "steel"})
    COPPER = dict({"materialId": 10, "name": "copper"})
    IRON = dict({"materialId": 11, "name": "iron"})
    LEAD = dict({"materialId": 12, "name": "lead"})
    ZINC = dict({"materialId": 13, "name": "zinc"})
    BIRCHWOOD = dict({"materialId": 14, "name": "birchwood"})
    STONE = dict({"materialId": 15, "name": "stone"})
    LEATHER = dict({"materialId": 16, "name": "leather"})
    COTTON = dict({"materialId": 17, "name": "cotton"})
    CLAY = dict({"materialId": 18, "name": "clay"})
    POTTERY = dict({"materialId": 19, "name": "pottery"})
    GLASS = dict({"materialId": 20, "name": "glass"})
    MAGIC = dict({"materialId": 21, "name": "magic"})
    VEGETARIAN = dict({"materialId": 22, "name": "vegetarian"})
    FIRE = dict({"materialId": 23, "name": "fire"})
    OIL = dict({"materialId": 25, "name": "oil"})
    WATER = dict({"materialId": 26, "name": "water"})
    CHARCOAL = dict({"materialId": 27, "name": "charcoal"})
    DAIRY = dict({"materialId": 28, "name": "dairy"})
    HONEY = dict({"materialId": 29, "name": "honey"})
    BRASS = dict({"materialId": 30, "name": "brass"})
    BRONZE = dict({"materialId": 31, "name": "bronze"})
    FAT = dict({"materialId": 32, "name": "fat"})
    PAPER = dict({"materialId": 33, "name": "paper"})
    TIN = dict({"materialId": 34, "name": "tin"})
    BONE = dict({"materialId": 35, "name": "bone"})
    SALT = dict({"materialId": 36, "name": "salt"})
    PINEWOOD = dict({"materialId": 37, "name": "pinewood"})
    OAKENWOOD = dict({"materialId": 38, "name": "oakenwood"})
    CEDARWOOD = dict({"materialId": 39, "name": "cedarwood"})
    WILLOW = dict({"materialId": 40, "name": "willow"})
    MAPLEWOOD = dict({"materialId": 41, "name": "maplewood"})
    APPLEWOOD = dict({"materialId": 42, "name": "applewood"})
    LEMONWOOD = dict({"materialId": 43, "name": "lemonwood"})
    OLIVEWOOD = dict({"materialId": 44, "name": "olivewood"})
    CHERRYWOOD = dict({"materialId": 45, "name": "cherrywood"})
    LAVENDERWOOD = dict({"materialId": 46, "name": "lavenderwood"})
    ROSEWOOD = dict({"materialId": 47, "name": "rosewood"})
    THORN = dict({"materialId": 48, "name": "thorn"})
    GRAPEWOOD = dict({"materialId": 49, "name": "grapewood"})
    CAMELLIAWOOD = dict({"materialId": 50, "name": "camelliawood"})
    OLEANDERWOOD = dict({"materialId": 51, "name": "oleanderwood"})
    CRYSTAL = dict({"materialId": 52, "name": "crystal"})
    WEMP = dict({"materialId": 53, "name": "wemp"})
    DIAMOND = dict({"materialId": 54, "name": "diamond"})
    ANIMAL = dict({"materialId": 55, "name": "animal"})
    ADAMANTINE = dict({"materialId": 56, "name": "adamantine"})
    GLIMMERSTEEL = dict({"materialId": 57, "name": "glimmersteel"})
    TAR = dict({"materialId": 58, "name": "tar"})
    PEAT = dict({"materialId": 59, "name": "peat"})
    REED = dict({"materialId": 60, "name": "reed"})
    SLATE = dict({"materialId": 61, "name": "slate"})
    MARBLE = dict({"materialId": 62, "name": "marble"})
    CHESTNUT = dict({"materialId": 63, "name": "chestnut"})
    WALNUT = dict({"materialId": 64, "name": "walnut"})
    FIRWOOD = dict({"materialId": 65, "name": "firwood"})
    LINDENWOOD = dict({"materialId": 66, "name": "lindenwood"})
    SERYLL = dict({"materialId": 67, "name": "seryll"})
    IVY = dict({"materialId": 68, "name": "ivy"})
    WOOL = dict({"materialId": 69, "name": "wool"})
    STRAW = dict({"materialId": 70, "name": "straw"})
    HAZELNUTWOOD = dict({"materialId": 71, "name": "hazelnutwood"})
    BEAR = dict({"materialId": 72, "name": "bear"})
    BEEF = dict({"materialId": 73, "name": "beef"})
    CANINE = dict({"materialId": 74, "name": "canine"})
    FELINE = dict({"materialId": 75, "name": "feline"})
    DRAGON = dict({"materialId": 76, "name": "dragon"})
    FOWL = dict({"materialId": 77, "name": "fowl"})
    GAME = dict({"materialId": 78, "name": "game"})
    HORSE = dict({"materialId": 79, "name": "horse"})
    HUMAN = dict({"materialId": 80, "name": "human"})
    HUMANOID = dict({"materialId": 81, "name": "humanoid"})
    INSECT = dict({"materialId": 82, "name": "insect"})
    LAMB = dict({"materialId": 83, "name": "lamb"})
    PORK = dict({"materialId": 84, "name": "pork"})
    SEAFOOD = dict({"materialId": 85, "name": "seafood"})
    SNAKE = dict({"materialId": 86, "name": "snake"})
    TOUGH = dict({"materialId": 87, "name": "tough"})
    ORANGEWOOD = dict({"materialId": 88, "name": "orangewood"})
    RASPBERRYWOOD = dict({"materialId": 90, "name": "raspberrywood"})
    BLUEBERRYWOOD = dict({"materialId": 91, "name": "blueberrywood"})
    LINGONBERRYWOOD = dict({"materialId": 92, "name": "lingonberrywood"})
    pass


class Active:
    def __init__(self):
        self.itemTemplate = ItemTemplate.NONE  # Json key: "id" in Wurm recipes
        self.cookedState = CookedState.NONE  # Json key: "cstate" in Wurm recipes
        self.preparedState = PreparedState.NONE  # Json key: "pstate" in wurm recipes
        self.material = Material.NONE  # Json key: "material" in wurm recipes
        self.realTemplate = ItemTemplate.NONE  # Json key: "realtemplate" in wurm recipes
        self.difficulty = 0  # Json key: "difficulty" in wurm recipes
        self.loss = 0  # Json key: "loss" in wurm recipes
        self.ratio = 0  # Json key: "ratio" in wurm recipes
        self.rarity = Rarity.NONE  # Not in recipes but needed for affinity simulation.

    # if (source != null & & recipe.hasActiveItem() & & recipe.getActiveItem().getTemplateId() != ItemList.bodyHand) {
    #     ibonus += source.getTemplateId();
    #     if (!Server.getInstance().isPS()) {
    #         ibonus += source.getRarity();
    #     }
    # }
    pass


class Target:
    def __init__(self):
        self.itemTemplate = ItemTemplate.NONE  # Json key: "id" in Wurm recipes
        self.cookedState = CookedState.NONE  # Json key: "cstate" in Wurm recipes
        self.preparedState = PreparedState.NONE  # Json key: "pstate" in wurm recipes
        self.material = Material.NONE  # Json key: "material" in wurm recipes
        self.realTemplate = ItemTemplate.NONE  # Json key: "realtemplate" in wurm recipes
        self.difficulty = 0  # Json key: "difficulty" in wurm recipes
        self.loss = 0  # Json key: "loss" in wurm recipes
        self.ratio = 0  # Json key: "ratio" in wurm recipes
        self.creature = Creature.NONE  # Json key: "creature" in wurm recipes
        self.rarity = Rarity.NONE

    # else {
    #     if (target.usesFoodState()) {
    #         ibonus += target.getAuxData();
    #     }
    #     ibonus += target.getMaterial();
    #     ibonus += target.getRealTemplateId();
    #     if (this.getTemplateId() == 272) {
    #         ibonus += target.getData1();
    #     }
    #     if (!Server.getInstance().isPS()) {
    #         ibonus += target.getRarity();
    #     }
    # }
    pass


class Ingredient:
    NONE = dict({"itemTemplate": ItemTemplate.NONE, "name": "none"})

    def __init__(self):
        self.itemTemplate = ItemTemplate.NONE  # Json key: "id" in Wurm recipes
        self.cookedState = CookedState.NONE  # Json key: "cstate" in Wurm recipes
        self.preparedState = PreparedState.NONE  # Json key: "pstate" in wurm recipes
        self.material = Material.NONE  # Json key: "material" in wurm recipes
        self.realTemplate = ItemTemplate.NONE  # Json key: "realtemplate" in wurm recipes
        self.difficulty = 0  # Json key: "difficulty" in wurm recipes
        self.loss = 0  # Json key: "loss" in wurm recipes
        self.ratio = 0  # Json key: "ratio" in wurm recipes
        self.rarity = Rarity.NONE  # Not in recipes but needed for affinity simulation.

    # if (target.isFoodMaker()) {
    #     for (final Item item4: target.getItemsAsArray()) {
    #         ibonus += item4.getTemplateId();
    #     if (item4.usesFoodState()) {
    #         ibonus += item4.getAuxData();
    #     }
    #     ibonus += item4.getMaterial();
    #     ibonus += item4.getRealTemplateId();
    #     if (!Server.getInstance().isPS()) {
    #         ibonus += item4.getRarity();
    #     }
    #   }
    # }
    pass


class IngredientsGroup(Enum):
    # C(n,k) Combination(no repeat) "n" number of items choose "k" number of items.
    # ivc1, ivc2, ... ivcN  item variation count for each possible recipes ingredient.
    # oic optional ingredient count
    MANDATORY = dict({"name": "mandatory", "combinationFunction": "product(C(ivc1, 1), C(ivc2, 1), ... C(ivcN, 1))"})
    # Since it's choose 1 we don't actually need C formula. Summing each item's possibilities would give the same
    # result.
    OPTIONAL = dict({"name": "optional", "combinationFunction": "product(C(ivc1 + 1, 1), C(ivc2 + 1, 1), ... C(ivcN + "
                                                                "1, 1))"})
    # For each recipe optional ingredient add one, a none ingredient, to represent the exclusion of it. Optional are
    # one or none for each recipe ingredient.
    ONE_OF = dict({"name": "oneof", "combinationFunction": "sum(C(ivc1, 1), C(ivc2, 1), ... C(ivcN, 1))"})
    # Chose only one ingredient from this group.
    ZERO_OR_ONE = dict({"name": "zeroorone", "combinationFunction": "sum(C(ivc1 + 1, 1), C(ivc2 + 1, 1), ... C(ivcN + "
                                                                    "1, 1))"})
    # For each recipe zeroorone ingredient add one, a none ingredient, to represent the exclusion of it. zeroorone are
    # one or none for the entire group.
    ONE_OR_MORE = dict({"name": "oneormore", "combinationFunction": "sum(sum(C(icv1, 1), C(icv1, 2) ... C(icv1, "
                                                                    "icv1)), sum(C(icv2, 1), C(icv2, 2) ... C(icv2, "
                                                                    "icv2)) ... sum(C(icvN, 1), C(icvN, "
                                                                    "2) ... C(icvN, icvN)))"})
    # At least one or more from the entire group.
    ANY = dict({"name": "any", "combinationFunction": ""})
    NONE = dict({"name": "none", "combinationFunction": ""})

    # algorithm to make combinations of things.
    # comb({ 1 2 3 4 5 }, 3) =
    # { 1, comb({ 2 3 4 5 }, 2) } and
    # { 2, comb({ 3 4 5 }, 2) } and
    # { 3, comb({ 4 5 }, 2) }

    def __init__(self):
        self.groupType = IngredientsGroup.NONE
        self.ingredients = tuple(Ingredient.NONE)
    pass


class Result:

    def __init__(self):
        self.itemTemplate = ItemTemplate.NONE           # Json key: "id" in Wurm recipes and is the item's name.
        self.name = ""                                  # Json key: "name" custom name.
        self.cookedState = CookedState.NONE             # Json key: "cstate" in Wurm recipes
        self.preparedState = PreparedState.NONE         # Json key: "pstate" in wurm recipes
        self.material = Material.NONE                   # Json key: "material" in wurm recipes
        self.realTemplate = ItemTemplate.NONE           # Json key: "realtemplate" in wurm recipes
        self.referenceRealTemplate = ItemTemplate.NONE  #
        self.difficulty = 0                             # Json key: "difficulty" in wurm recipes
        self.description = ""                           # Json key: "description"
        self.achievement = ""
        self.useTemplateWeight = ""
        self.icon = ""

    pass