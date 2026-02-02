import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nutritionbackend.settings')
django.setup()

from nutritionAPI.models import Foods

# --- SCREENSHOT 1: Bliss Breakfast ---

msu_bakers_plain_bagel = Foods.objects.create(
    food_name="MSU Bakers Plain Bagel - 4 oz",
    serving_size="118g",
    brand="MSU",
    calories=271.0, protein=11.0, carbs=54.0, fat=1.5, fiber=2.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=480.0, potassium=23.9, vitamin_A=0.0, vitamin_C=15.0, calcium=0.0
)

assorted_msu_bakers_bagels = Foods.objects.create(
    food_name="Assorted MSU Bakers Bagels",
    serving_size="Each (131g)",
    brand="MSU",
    calories=301.0, protein=11.0, carbs=61.0, fat=1.5, fiber=2.0, sugar=6.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=510.0, potassium=27.5, vitamin_A=0.0, vitamin_C=15.0, calcium=0.0
)

vegan_chocolate_banana_muffin = Foods.objects.create(
    food_name="Vegan Chocolate Banana Muffin - 4 oz",
    serving_size="122g",
    brand="MSU",
    calories=372.0, protein=4.0, carbs=61.0, fat=14.0, fiber=2.0, sugar=34.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=240.0, potassium=0.0, vitamin_A=0.0, vitamin_C=20.0, calcium=0.0
)

assorted_cake_donuts = Foods.objects.create(
    food_name="Assorted Cake Donuts",
    serving_size="Each (71g)",
    brand="MSU",
    calories=300.0, protein=3.0, carbs=39.0, fat=14.0, fiber=1.0, sugar=21.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=280.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

assorted_yeast_donuts = Foods.objects.create(
    food_name="Assorted Yeast Donuts",
    serving_size="Each (71g)",
    brand="MSU",
    calories=300.0, protein=3.0, carbs=39.0, fat=14.0, fiber=1.0, sugar=21.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=280.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

# --- SCREENSHOT 2: Bliss Lunch & Dinner ---

chocolate_chip_cookie = Foods.objects.create(
    food_name="Chocolate Chip Cookie",
    serving_size="Each (29g)",
    brand="MSU",
    calories=122.0, protein=1.0, carbs=17.0, fat=6.0, fiber=1.0, sugar=10.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=160.0, potassium=37.8, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

double_chocolate_chip_cookie = Foods.objects.create(
    food_name="Double Chocolate Chip Cookie",
    serving_size="Each (29g)",
    brand="MSU",
    calories=122.0, protein=1.0, carbs=17.0, fat=6.0, fiber=1.0, sugar=10.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=70.0, potassium=22.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

mm_cookie = Foods.objects.create(
    food_name="M&M Cookie",
    serving_size="Each (28g)",
    brand="MSU",
    calories=121.0, protein=1.0, carbs=17.0, fat=6.0, fiber=0.0, sugar=10.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=210.0, potassium=14.1, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

sugar_cookie = Foods.objects.create(
    food_name="Sugar Cookie",
    serving_size="Each (28g)",
    brand="MSU",
    calories=126.0, protein=1.0, carbs=16.0, fat=6.0, fiber=0.0, sugar=8.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=125.0, potassium=3.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

brownie = Foods.objects.create(
    food_name="Brownie",
    serving_size="Ounce (30g)",
    brand="MSU",
    calories=130.0, protein=2.0, carbs=16.0, fat=7.0, fiber=1.0, sugar=11.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=115.0, potassium=8.2, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

vegan_chocolate_cake = Foods.objects.create(
    food_name="Vegan Chocolate Cake",
    serving_size="2 oz (67g)",
    brand="MSU",
    calories=203.0, protein=2.0, carbs=38.0, fat=5.0, fiber=1.0, sugar=15.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

white_iced_white_sheet_cake = Foods.objects.create(
    food_name="White Iced White Sheet Cake",
    serving_size="3oz (86g)",
    brand="MSU",
    calories=255.0, protein=2.0, carbs=36.0, fat=11.0, fiber=0.0, sugar=13.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=270.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

caramel_iced_banana_layer_cake = Foods.objects.create(
    food_name="Caramel Iced Banana Layer Cake",
    serving_size="Ounce (31g)",
    brand="MSU",
    calories=120.0, protein=0.0, carbs=16.0, fat=6.0, fiber=0.0, sugar=13.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=105.0, potassium=5.8, vitamin_A=0.0, vitamin_C=2.0, calcium=2.0
)

cinnamon_apple_pie_crepe = Foods.objects.create(
    food_name="Cinnamon Apple Pie Crepe",
    serving_size="Each (60g)",
    brand="MSU",
    calories=120.0, protein=1.0, carbs=17.0, fat=5.0, fiber=1.0, sugar=11.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=70.0, potassium=21.4, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

vegan_lemon_cake = Foods.objects.create(
    food_name="Vegan Lemon Cake",
    serving_size="2oz (60g)",
    brand="MSU",
    calories=209.0, protein=2.0, carbs=31.0, fat=9.0, fiber=0.0, sugar=16.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=200.0, potassium=0.1, vitamin_A=0.0, vitamin_C=4.0, calcium=2.0
)

chocolate_iced_chocolate_sheet_cake = Foods.objects.create(
    food_name="Chocolate Iced Chocolate Sheet Cake",
    serving_size="3oz (70g)",
    brand="MSU",
    calories=265.0, protein=3.0, carbs=37.0, fat=12.0, fiber=1.0, sugar=28.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=300.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

white_iced_marble_sheet_cake = Foods.objects.create(
    food_name="White Iced Marble Sheet Cake",
    serving_size="3oz (70g)",
    brand="MSU",
    calories=270.0, protein=2.0, carbs=38.0, fat=12.0, fiber=1.0, sugar=28.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=290.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

hot_fudge_sundae_torte = Foods.objects.create(
    food_name="Hot Fudge Sundae Torte",
    serving_size="3 oz (67g)",
    brand="MSU",
    calories=227.0, protein=3.0, carbs=36.0, fat=9.0, fiber=1.0, sugar=27.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=200.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

# --- SCREENSHOT 3: Brimstone & GLP Breakfast ---

black_bean_burger = Foods.objects.create(
    food_name="Black Bean Burger",
    serving_size="Each (132g)",
    brand="MSU",
    calories=249.0, protein=10.0, carbs=37.0, fat=8.0, fiber=7.0, sugar=5.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=650.0, potassium=385.6, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

cheeseburger = Foods.objects.create(
    food_name="Cheeseburger",
    serving_size="Each (123g)",
    brand="MSU",
    calories=297.0, protein=24.0, carbs=19.0, fat=14.0, fiber=1.0, sugar=3.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=70.0, sodium=410.0, potassium=288.7, vitamin_A=4.0, vitamin_C=0.0, calcium=10.0
)

quarter_pound_burger = Foods.objects.create(
    food_name="Quarter Pound Burger",
    serving_size="Each (103g)",
    brand="MSU",
    calories=246.0, protein=20.0, carbs=17.0, fat=11.0, fiber=1.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=55.0, sodium=230.0, potassium=271.9, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

grilled_chicken_sandwich = Foods.objects.create(
    food_name="Grilled Chicken Sandwich",
    serving_size="Each (154g)",
    brand="MSU",
    calories=377.0, protein=36.0, carbs=17.0, fat=18.0, fiber=1.0, sugar=2.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=90.0, sodium=250.0, potassium=304.8, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

chicken_patty_sandwich = Foods.objects.create(
    food_name="Chicken Patty Sandwich",
    serving_size="Each (121g)",
    brand="MSU",
    calories=322.0, protein=14.0, carbs=29.0, fat=16.0, fiber=1.0, sugar=2.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=720.0, potassium=34.2, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

battered_pollock = Foods.objects.create(
    food_name="Battered Pollock",
    serving_size="Each (92g)",
    brand="MSU",
    calories=130.0, protein=10.0, carbs=14.0, fat=5.0, fiber=5.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=470.0, potassium=194.5, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

crinkle_fries = Foods.objects.create(
    food_name="Crinkle Fries",
    serving_size="3oz (85g)",
    brand="MSU",
    calories=265.0, protein=3.0, carbs=35.0, fat=13.0, fiber=3.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=492.4, vitamin_A=0.0, vitamin_C=6.0, calcium=0.0
)

cheese_bread_garlic_butter = Foods.objects.create(
    food_name="Cheese Bread with Garlic Butter",
    serving_size="Slice (41g)",
    brand="MSU",
    calories=140.0, protein=5.0, carbs=11.0, fat=8.0, fiber=1.0, sugar=1.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=230.0, potassium=21.9, vitamin_A=4.0, vitamin_C=0.0, calcium=10.0
)

cheese_pizza_slice = Foods.objects.create(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="MSU",
    calories=215.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

coney_dog_pizza_slice = Foods.objects.create(
    food_name="Coney Dog Pizza - Slice",
    serving_size="118g",
    brand="MSU",
    calories=256.0, protein=16.0, carbs=22.0, fat=13.0, fiber=2.0, sugar=2.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=640.0, potassium=72.2, vitamin_A=6.0, vitamin_C=0.0, calcium=20.0
)

scrambled_eggs = Foods.objects.create(
    food_name="Scrambled Eggs",
    serving_size="4oz (117g)",
    brand="MSU",
    calories=193.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

oatmeal = Foods.objects.create(
    food_name="Oatmeal",
    serving_size="6oz (294g)",
    brand="MSU",
    calories=113.0, protein=4.0, carbs=19.0, fat=2.5, fiber=3.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=25.0, potassium=110.9, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

tofu_scramble = Foods.objects.create(
    food_name="Tofu Scramble",
    serving_size="3oz (87g)",
    brand="MSU",
    calories=78.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

belgian_waffle = Foods.objects.create(
    food_name="Belgian Waffle",
    serving_size="2 Waffles (136g)",
    brand="MSU",
    calories=360.0, protein=8.0, carbs=54.0, fat=12.0, fiber=2.0, sugar=12.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=60.0, sodium=740.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

hard_cooked_eggs = Foods.objects.create(
    food_name="Hard Cooked Eggs",
    serving_size="Each (57g)",
    brand="MSU",
    calories=88.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

cheesy_ranch_hash_browns = Foods.objects.create(
    food_name="Cheesy Ranch Hash Browns",
    serving_size="9oz (257g)",
    brand="MSU",
    calories=409.0, protein=17.0, carbs=27.0, fat=26.0, fiber=2.0, sugar=2.0,
    saturated_fat=11.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=245.0, sodium=1020.0, potassium=468.4, vitamin_A=20.0, vitamin_C=15.0, calcium=25.0
)

chicken_sausage_patties = Foods.objects.create(
    food_name="Chicken Sausage Patties",
    serving_size="Each (40g)",
    brand="MSU",
    calories=76.0, protein=6.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=250.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties = Foods.objects.create(
    food_name="Veggie Sausage Patties",
    serving_size="2 Patties (70g)",
    brand="MSU",
    calories=102.0, protein=5.0, carbs=2.0, fat=8.0, fiber=1.0, sugar=1.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

# --- SCREENSHOT 4: GLP Lunch / Veg Out Dinner ---

vegetable_egg_rolls = Foods.objects.create(
    food_name="Vegetable Egg Rolls",
    serving_size="Each (85g)",
    brand="MSU",
    calories=100.0, protein=5.0, carbs=17.0, fat=1.0, fiber=2.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=550.0, potassium=200.1, vitamin_A=30.0, vitamin_C=30.0, calcium=30.0
)

sesame_shrimp_lo_mein = Foods.objects.create(
    food_name="Sesame Shrimp Lo Mein",
    serving_size="6oz (142g)",
    brand="MSU",
    calories=180.0, protein=9.0, carbs=22.0, fat=6.0, fiber=2.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=260.0, potassium=130.2, vitamin_A=80.0, vitamin_C=60.0, calcium=4.0
)

sesame_vegetable_blend = Foods.objects.create(
    food_name="Sesame Vegetable Blend",
    serving_size="4oz (117g)",
    brand="MSU",
    calories=60.0, protein=4.0, carbs=9.0, fat=2.0, fiber=4.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=85.0, potassium=95.5, vitamin_A=100.0, vitamin_C=45.0, calcium=4.0
)

orange_ginger_sauce = Foods.objects.create(
    food_name="Orange Ginger Sauce",
    serving_size="Tablespoon (14g)",
    brand="MSU",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=4.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=15.0, potassium=18.3, vitamin_A=0.0, vitamin_C=4.0, calcium=0.0
)

general_tsos_tofu_vegetables = Foods.objects.create(
    food_name="General Tso's Tofu and Vegetables",
    serving_size="8oz (303g)",
    brand="MSU",
    calories=277.0, protein=6.0, carbs=31.0, fat=15.0, fiber=4.0, sugar=18.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=1120.0, potassium=211.8, vitamin_A=120.0, vitamin_C=130.0, calcium=10.0
)

thai_vegetable_dumpling = Foods.objects.create(
    food_name="Thai Vegetable Dumpling",
    serving_size="3 Potstickers (85g)",
    brand="MSU",
    calories=128.0, protein=4.0, carbs=28.0, fat=1.0, fiber=4.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=450.0, potassium=0.0, vitamin_A=20.0, vitamin_C=2.0, calcium=2.0
)

sesame_brown_rice = Foods.objects.create(
    food_name="Sesame Brown Rice",
    serving_size="3oz (91g)",
    brand="MSU",
    calories=76.0, protein=1.0, carbs=9.0, fat=4.0, fiber=1.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=105.0, potassium=6.3, vitamin_A=0.0, vitamin_C=2.0, calcium=2.0
)

sweet_and_sour_sauce = Foods.objects.create(
    food_name="Sweet and Sour Sauce",
    serving_size="Tablespoon (13g)",
    brand="MSU",
    calories=26.0, protein=0.0, carbs=6.0, fat=0.0, fiber=0.0, sugar=5.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=110.0, potassium=1.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

jerk_chicken = Foods.objects.create(
    food_name="Jerk Chicken",
    serving_size="4oz (122g)",
    brand="MSU",
    calories=187.0, protein=20.0, carbs=0.0, fat=12.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=95.0, sodium=110.0, potassium=1.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

coconut_rice = Foods.objects.create(
    food_name="Coconut Rice",
    serving_size="4oz (105g)",
    brand="MSU",
    calories=353.0, protein=11.0, carbs=75.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=4.9, vitamin_A=2.0, vitamin_C=2.0, calcium=0.0
)

caribbean_roasted_vegetables = Foods.objects.create(
    food_name="Caribbean Roasted Vegetables",
    serving_size="3oz (78g)",
    brand="MSU",
    calories=48.0, protein=1.0, carbs=5.0, fat=3.0, fiber=1.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=100.0, potassium=70.6, vitamin_A=15.0, vitamin_C=70.0, calcium=2.0
)

salsa_criolla = Foods.objects.create(
    food_name="Salsa Criolla",
    serving_size="Tablespoon (13g)",
    brand="MSU",
    calories=8.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.1, vitamin_A=0.0, vitamin_C=4.0, calcium=0.0
)

jerk_sauce = Foods.objects.create(
    food_name="Jerk Sauce",
    serving_size="Tablespoon (13g)",
    brand="MSU",
    calories=47.0, protein=2.0, carbs=2.0, fat=4.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=40.0, potassium=9.1, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

vegan_mexican_rice = Foods.objects.create(
    food_name="Vegan Mexican Rice",
    serving_size="4.5oz (131g)",
    brand="MSU",
    calories=194.0, protein=3.0, carbs=32.0, fat=6.0, fiber=1.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=2.6, vitamin_A=8.0, vitamin_C=25.0, calcium=2.0
)