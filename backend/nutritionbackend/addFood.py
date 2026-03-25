import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nutritionbackend.settings')
django.setup()

from nutritionAPI.models import Foods

def create_food(**kwargs):
    Foods.objects.get_or_create(
        food_name=kwargs['food_name'],
        brand=kwargs.get('brand', 'MSU'),
        defaults=kwargs
    )

create_food(
    food_name="MSU Bakers Plain Bagel - 4 oz",
    serving_size="118g",
    brand="MSU",
    calories=270.0, protein=11.0, carbs=54.0, fat=1.5, fiber=2.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=480.0, potassium=23.9, vitamin_A=0.0, vitamin_C=15.0, calcium=0.0
)

caramel_topping_0 = create_food(
    food_name="Caramel Topping - Tablespoon",
    serving_size="17g",
    brand="Generic",
    calories=50.0, protein=0.0, carbs=13.0, fat=0.0, fiber=0.0, sugar=10.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=30.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chocolate_syrup_1 = create_food(
    food_name="Chocolate Syrup - Tablespoon",
    serving_size="19g",
    brand="Generic",
    calories=50.0, protein=0.0, carbs=12.0, fat=0.0, fiber=0.0, sugar=10.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chopped_mms_2 = create_food(
    food_name="Chopped M&Ms - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=70.0, protein=0.0, carbs=10.0, fat=3.5, fiber=0.0, sugar=9.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

marshmallow_topping_3 = create_food(
    food_name="Marshmallow Topping - Tablespoon",
    serving_size="20g",
    brand="Generic",
    calories=45.0, protein=0.0, carbs=12.0, fat=0.0, fiber=0.0, sugar=12.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=20.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

oreo_cookie_crumbs_4 = create_food(
    food_name="Oreo Cookie Crumbs - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=70.0, protein=0.0, carbs=10.0, fat=2.5, fiber=0.0, sugar=6.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=45.0, potassium=21.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chopped_reeses_peanut_butter_cups_5 = create_food(
    food_name="Chopped Reese's Peanut Butter Cups - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=70.0, protein=2.0, carbs=10.0, fat=3.0, fiber=1.0, sugar=8.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=20.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

strawberry_topping_6 = create_food(
    food_name="Strawberry Topping - Tablespoon",
    serving_size="20g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=7.0, fat=0.0, fiber=0.0, sugar=7.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

mochi_rice_cake_7 = create_food(
    food_name="Mochi Rice Cake - Each",
    serving_size="31g",
    brand="Generic",
    calories=70.0, protein=2.0, carbs=16.0, fat=1.0, fiber=0.0, sugar=5.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=35.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

gummi_worms_8 = create_food(
    food_name="Gummi Worms - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=90.0, protein=1.0, carbs=21.0, fat=0.0, fiber=0.0, sugar=15.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=5.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheese_bread_with_garlic_butter_9 = create_food(
    food_name="Cheese Bread with Garlic Butter - Slice",
    serving_size="41g",
    brand="Generic",
    calories=140.0, protein=5.0, carbs=11.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=230.0, potassium=21.9, vitamin_A=4.0, vitamin_C=0.0, calcium=10.0
)

buffalo_chicken_pizza_10 = create_food(
    food_name="Buffalo Chicken Pizza - Slice",
    serving_size="82g",
    brand="Generic",
    calories=230.0, protein=11.0, carbs=19.0, fat=13.0, fiber=1.0, sugar=1.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=620.0, potassium=68.9, vitamin_A=0.0, vitamin_C=0.0, calcium=15.0
)

sausage_pizza_11 = create_food(
    food_name="Sausage Pizza - Slice",
    serving_size="78g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=24.0, fat=9.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=480.0, potassium=71.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

cheese_bread_with_garlic_butter_12 = create_food(
    food_name="Cheese Bread with Garlic Butter - Slice",
    serving_size="41g",
    brand="Generic",
    calories=140.0, protein=5.0, carbs=11.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=230.0, potassium=21.9, vitamin_A=4.0, vitamin_C=0.0, calcium=10.0
)

buffalo_chicken_pizza_13 = create_food(
    food_name="Buffalo Chicken Pizza - Slice",
    serving_size="82g",
    brand="Generic",
    calories=230.0, protein=11.0, carbs=19.0, fat=13.0, fiber=1.0, sugar=1.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=620.0, potassium=68.9, vitamin_A=0.0, vitamin_C=0.0, calcium=15.0
)

sausage_pizza_14 = create_food(
    food_name="Sausage Pizza - Slice",
    serving_size="78g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=24.0, fat=9.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=480.0, potassium=71.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

cream_of_mushroom_soup_15 = create_food(
    food_name="Cream of Mushroom Soup - 4oz",
    serving_size="115g",
    brand="Generic",
    calories=240.0, protein=2.0, carbs=5.0, fat=24.0, fiber=0.0, sugar=3.0,
    saturated_fat=14.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=80.0, sodium=45.0, potassium=147.0, vitamin_A=6.0, vitamin_C=2.0, calcium=10.0
)

roasted_root_vegetable_soup_16 = create_food(
    food_name="Roasted Root Vegetable Soup - 6oz",
    serving_size="185g",
    brand="Generic",
    calories=40.0, protein=0.0, carbs=8.0, fat=1.0, fiber=1.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=260.0, potassium=100.3, vitamin_A=20.0, vitamin_C=20.0, calcium=2.0
)

chocolate_chip_cookie_17 = create_food(
    food_name="Chocolate Chip Cookie - Each",
    serving_size="29g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=17.0, fat=6.0, fiber=0.0, sugar=10.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=160.0, potassium=37.8, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

capn_crunch_marshmallow_bar_18 = create_food(
    food_name="Capn Crunch Marshmallow Bar - 1.5 oz",
    serving_size="53g",
    brand="Generic",
    calories=220.0, protein=2.0, carbs=38.0, fat=8.0, fiber=0.0, sugar=23.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=220.0, potassium=0.0, vitamin_A=4.0, vitamin_C=0.0, calcium=0.0
)

french_toast_crunch_bars_19 = create_food(
    food_name="French Toast Crunch Bars - 3 oz",
    serving_size="64g",
    brand="Generic",
    calories=260.0, protein=2.0, carbs=48.0, fat=7.0, fiber=2.0, sugar=27.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=15.0, vitamin_C=10.0, calcium=10.0
)

vegan_chocolate_cake_20 = create_food(
    food_name="Vegan Chocolate Cake - 2 oz",
    serving_size="67g",
    brand="Generic",
    calories=200.0, protein=2.0, carbs=38.0, fat=5.0, fiber=1.0, sugar=15.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

mm_iced_chocolate_cake_21 = create_food(
    food_name="M&M Iced Chocolate Cake - Ounce",
    serving_size="31g",
    brand="Generic",
    calories=130.0, protein=0.0, carbs=17.0, fat=7.0, fiber=0.0, sugar=14.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=95.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

vegan_vanilla_cupcake_22 = create_food(
    food_name="Vegan Vanilla Cupcake - Each",
    serving_size="90g",
    brand="Generic",
    calories=320.0, protein=1.0, carbs=54.0, fat=11.0, fiber=0.0, sugar=40.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=17.2, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

iced_cupcakes_23 = create_food(
    food_name="Iced Cupcakes - Each",
    serving_size="92g",
    brand="Generic",
    calories=330.0, protein=2.0, carbs=41.0, fat=17.0, fiber=0.0, sugar=31.0,
    saturated_fat=12.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=230.0, potassium=65.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

blueberry_pie_24 = create_food(
    food_name="Blueberry Pie - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=110.0, protein=0.0, carbs=13.0, fat=6.0, fiber=0.0, sugar=6.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=100.0, potassium=17.4, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

made_to_order_sandwiches_25 = create_food(
    food_name="Made to Order Sandwiches - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

made_to_order_sandwiches_26 = create_food(
    food_name="Made to Order Sandwiches - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

kung_pao_chicken_with_peanuts_27 = create_food(
    food_name="Kung Pao Chicken with Peanuts - 6oz",
    serving_size="175g",
    brand="Generic",
    calories=530.0, protein=22.0, carbs=27.0, fat=38.0, fiber=3.0, sugar=7.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=900.0, potassium=48.5, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

vegetable_egg_rolls_28 = create_food(
    food_name="Vegetable Egg Rolls - Each",
    serving_size="85g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=17.0, fat=1.0, fiber=2.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=550.0, potassium=200.1, vitamin_A=30.0, vitamin_C=30.0, calcium=30.0
)

kung_pao_tofu_29 = create_food(
    food_name="Kung Pao Tofu - 8oz",
    serving_size="212g",
    brand="Generic",
    calories=160.0, protein=9.0, carbs=24.0, fat=4.0, fiber=8.0, sugar=8.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=930.0, potassium=224.6, vitamin_A=25.0, vitamin_C=110.0, calcium=15.0
)

sauteed_bok_choy_and_shiitake_w_sesame_30 = create_food(
    food_name="Sauteed Bok Choy and Shiitake w/ Sesame - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=50.0, protein=2.0, carbs=4.0, fat=3.0, fiber=2.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=204.5, vitamin_A=80.0, vitamin_C=70.0, calcium=10.0
)

jasmine_rice_31 = create_food(
    food_name="Jasmine Rice - 4oz",
    serving_size="110g",
    brand="Generic",
    calories=140.0, protein=3.0, carbs=31.0, fat=0.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=130.0, potassium=1.2, vitamin_A=0.0, vitamin_C=8.0, calcium=2.0
)

peanuts_32 = create_food(
    food_name="Peanuts - Tablespoon",
    serving_size="9g",
    brand="Generic",
    calories=50.0, protein=2.0, carbs=2.0, fat=4.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sweet_and_sour_sauce_33 = create_food(
    food_name="Sweet and Sour Sauce - Cup",
    serving_size="227g",
    brand="Generic",
    calories=250.0, protein=0.0, carbs=50.0, fat=3.5, fiber=0.0, sugar=42.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=1130.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

mandarin_orange_tempura_pork_34 = create_food(
    food_name="Mandarin Orange Tempura Pork - 8oz",
    serving_size="202g",
    brand="Generic",
    calories=370.0, protein=16.0, carbs=46.0, fat=15.0, fiber=7.0, sugar=32.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=350.0, potassium=13.9, vitamin_A=2.0, vitamin_C=10.0, calcium=4.0
)

bulgogi_style_sesame_vegetables_35 = create_food(
    food_name="Bulgogi Style Sesame Vegetables - 5oz",
    serving_size="144g",
    brand="Generic",
    calories=90.0, protein=3.0, carbs=17.0, fat=1.5, fiber=4.0, sugar=10.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=250.0, potassium=202.5, vitamin_A=140.0, vitamin_C=50.0, calcium=6.0
)

kimchi_chicken_dumpling_36 = create_food(
    food_name="Kimchi Chicken Dumpling - 3 Potstickers",
    serving_size="85g",
    brand="Generic",
    calories=140.0, protein=7.0, carbs=20.0, fat=3.0, fiber=1.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=590.0, potassium=130.1, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

jasmine_rice_37 = create_food(
    food_name="Jasmine Rice - 4oz",
    serving_size="109g",
    brand="Generic",
    calories=130.0, protein=3.0, carbs=30.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=95.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

nuoc_cham_38 = create_food(
    food_name="Nuoc Cham - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=60.0, protein=0.0, carbs=4.0, fat=4.5, fiber=0.0, sugar=3.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=250.0, potassium=2.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

shredded_mild_cheddar_cheese_39 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

halal_fajita_chicken_40 = create_food(
    food_name="Halal Fajita Chicken - 4oz",
    serving_size="111g",
    brand="Generic",
    calories=160.0, protein=21.0, carbs=0.0, fat=10.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=100.0, sodium=70.0, potassium=1.1, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

lomo_saltado_with_tofu_41 = create_food(
    food_name="Lomo Saltado with Tofu - 7oz",
    serving_size="203g",
    brand="Generic",
    calories=160.0, protein=6.0, carbs=19.0, fat=7.0, fiber=3.0, sugar=3.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=174.5, vitamin_A=10.0, vitamin_C=30.0, calcium=8.0
)

sour_cream_42 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

cilantro_lime_rice_43 = create_food(
    food_name="Cilantro Lime Rice - 4oz",
    serving_size="99g",
    brand="Generic",
    calories=150.0, protein=3.0, carbs=35.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=35.0, potassium=49.3, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

cumin_black_beans_44 = create_food(
    food_name="Cumin Black Beans - 4oz",
    serving_size="114g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=17.0, fat=2.5, fiber=4.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=249.8, vitamin_A=2.0, vitamin_C=25.0, calcium=4.0
)

tortilla_chips_45 = create_food(
    food_name="Tortilla Chips - 15 Chips",
    serving_size="41g",
    brand="Generic",
    calories=200.0, protein=3.0, carbs=27.0, fat=9.0, fiber=3.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=90.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

sauteed_bell_peppers_and_onions_46 = create_food(
    food_name="Sauteed Bell Peppers and Onions - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=1.0, fat=0.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=90.0, potassium=0.9, vitamin_A=2.0, vitamin_C=25.0, calcium=0.0
)

jalapenos_47 = create_food(
    food_name="Jalapenos - Tablespoon",
    serving_size="12g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=120.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

fire_roasted_tomato_salsa_48 = create_food(
    food_name="Fire Roasted Tomato Salsa - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=50.0, potassium=2.1, vitamin_A=0.0, vitamin_C=4.0, calcium=0.0
)

mild_nacho_cheese_sauce_49 = create_food(
    food_name="Mild Nacho Cheese Sauce - Cup",
    serving_size="244g",
    brand="Generic",
    calories=290.0, protein=4.0, carbs=24.0, fat=20.0, fiber=0.0, sugar=0.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=2220.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=20.0
)

taco_flour_tortilla_50 = create_food(
    food_name="Taco Flour Tortilla - Each",
    serving_size="29g",
    brand="Generic",
    calories=80.0, protein=2.0, carbs=14.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=170.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cajun_halal_chicken_51 = create_food(
    food_name="Cajun Halal Chicken - 6oz",
    serving_size="173g",
    brand="Generic",
    calories=230.0, protein=27.0, carbs=0.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=125.0, sodium=1210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

blackened_tofu_52 = create_food(
    food_name="Blackened Tofu - 3oz",
    serving_size="85g",
    brand="Generic",
    calories=130.0, protein=6.0, carbs=5.0, fat=10.0, fiber=3.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=104.7, vitamin_A=6.0, vitamin_C=2.0, calcium=15.0
)

basmati_rice_53 = create_food(
    food_name="Basmati Rice - 4oz",
    serving_size="121g",
    brand="Generic",
    calories=160.0, protein=4.0, carbs=35.0, fat=0.5, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=47.3, vitamin_A=0.0, vitamin_C=50.0, calcium=2.0
)

edamame_succotash_with_herbs_54 = create_food(
    food_name="Edamame Succotash with Herbs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=120.0, protein=5.0, carbs=17.0, fat=4.5, fiber=5.0, sugar=3.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=3.7, vitamin_A=20.0, vitamin_C=45.0, calcium=4.0
)

remoulade_55 = create_food(
    food_name="Remoulade - Tablespoon",
    serving_size="12g",
    brand="Generic",
    calories=60.0, protein=0.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=105.0, potassium=2.3, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

woodys_tabbouleh_salad_56 = create_food(
    food_name="Woody's Tabbouleh Salad - Cup",
    serving_size="57g",
    brand="Generic",
    calories=60.0, protein=1.0, carbs=4.0, fat=4.0, fiber=1.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=25.0, potassium=0.0, vitamin_A=30.0, vitamin_C=35.0, calcium=6.0
)

woodys_garlic_scallion_hummus_57 = create_food(
    food_name="Woody's Garlic Scallion Hummus - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=40.0, protein=0.0, carbs=2.0, fat=3.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=37.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

remoulade_58 = create_food(
    food_name="Remoulade - Tablespoon",
    serving_size="12g",
    brand="Generic",
    calories=60.0, protein=0.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=105.0, potassium=2.3, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

scrambled_eggs_59 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

french_toast_sticks_60 = create_food(
    food_name="French Toast Sticks - 4 Sticks",
    serving_size="113g",
    brand="Generic",
    calories=330.0, protein=5.0, carbs=43.0, fat=15.0, fiber=1.0, sugar=5.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=190.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tofu_scramble_61 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_62 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

tater_tots_63 = create_food(
    food_name="Tater Tots - 4oz",
    serving_size="113g",
    brand="Generic",
    calories=230.0, protein=3.0, carbs=26.0, fat=11.0, fiber=3.0, sugar=0.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=460.0, potassium=318.1, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

chicken_sausage_patties_64 = create_food(
    food_name="Chicken Sausage Patties - Each",
    serving_size="40g",
    brand="Generic",
    calories=80.0, protein=6.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=250.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties_65 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_66 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_67 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_68 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

perfectly_peachy_smoothie_69 = create_food(
    food_name="Perfectly Peachy Smoothie - 4oz",
    serving_size="104g",
    brand="Generic",
    calories=80.0, protein=0.0, carbs=21.0, fat=0.0, fiber=0.0, sugar=19.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=15.0, potassium=26.7, vitamin_A=6.0, vitamin_C=6.0, calcium=2.0
)

scrambled_eggs_70 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

french_toast_sticks_71 = create_food(
    food_name="French Toast Sticks - 4 Sticks",
    serving_size="113g",
    brand="Generic",
    calories=330.0, protein=5.0, carbs=43.0, fat=15.0, fiber=1.0, sugar=5.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=190.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tofu_scramble_72 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_73 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

tater_tots_74 = create_food(
    food_name="Tater Tots - 4oz",
    serving_size="113g",
    brand="Generic",
    calories=230.0, protein=3.0, carbs=26.0, fat=11.0, fiber=3.0, sugar=0.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=460.0, potassium=318.1, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

chicken_sausage_patties_75 = create_food(
    food_name="Chicken Sausage Patties - Each",
    serving_size="40g",
    brand="Generic",
    calories=80.0, protein=6.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=250.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties_76 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_77 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_78 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_79 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

chicken_patty_sandwich_80 = create_food(
    food_name="Chicken Patty Sandwich - Each",
    serving_size="121g",
    brand="Generic",
    calories=320.0, protein=14.0, carbs=29.0, fat=16.0, fiber=0.0, sugar=2.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=720.0, potassium=34.2, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

slim_cut_french_fries_81 = create_food(
    food_name="Slim Cut French Fries - 3oz",
    serving_size="100g",
    brand="Generic",
    calories=150.0, protein=1.0, carbs=24.0, fat=6.0, fiber=1.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=700.0, potassium=271.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

bacon_82 = create_food(
    food_name="Bacon - 2 Slices",
    serving_size="18g",
    brand="Generic",
    calories=90.0, protein=6.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=250.0, potassium=101.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

green_onions_83 = create_food(
    food_name="Green Onions - Cup",
    serving_size="85g",
    brand="Generic",
    calories=25.0, protein=2.0, carbs=6.0, fat=0.0, fiber=3.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=15.0, potassium=232.2, vitamin_A=15.0, vitamin_C=25.0, calcium=6.0
)

cheese_sauce_84 = create_food(
    food_name="Cheese Sauce - Cup",
    serving_size="255g",
    brand="Generic",
    calories=320.0, protein=4.0, carbs=24.0, fat=24.0, fiber=0.0, sugar=0.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=1820.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=15.0
)

kfc_style_coleslaw_85 = create_food(
    food_name="KFC Style Coleslaw - 3oz",
    serving_size="83g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=11.0, fat=8.0, fiber=1.0, sugar=9.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=160.0, potassium=107.6, vitamin_A=20.0, vitamin_C=4.0, calcium=50.0
)

beef_and_cheddar_sandwich_86 = create_food(
    food_name="Beef and Cheddar Sandwich - Each",
    serving_size="241g",
    brand="Generic",
    calories=670.0, protein=32.0, carbs=48.0, fat=38.0, fiber=2.0, sugar=4.0,
    saturated_fat=11.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=105.0, sodium=550.0, potassium=278.8, vitamin_A=15.0, vitamin_C=0.0, calcium=15.0
)

baked_beans_with_bacon_87 = create_food(
    food_name="Baked Beans with Bacon - 3oz",
    serving_size="95g",
    brand="Generic",
    calories=130.0, protein=5.0, carbs=24.0, fat=2.0, fiber=3.0, sugar=14.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=550.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

onion_petals_88 = create_food(
    food_name="Onion Petals - 3oz",
    serving_size="85g",
    brand="Generic",
    calories=190.0, protein=2.0, carbs=22.0, fat=11.0, fiber=2.0, sugar=4.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=260.0, potassium=0.0, vitamin_A=0.0, vitamin_C=6.0, calcium=2.0
)

caballo_loco_salsa_89 = create_food(
    food_name="Caballo Loco Salsa - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=50.0, protein=0.0, carbs=0.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=75.0, potassium=0.6, vitamin_A=4.0, vitamin_C=2.0, calcium=2.0
)

snappy_horseradish_sauce_90 = create_food(
    food_name="Snappy Horseradish Sauce - 2oz",
    serving_size="62g",
    brand="Generic",
    calories=220.0, protein=0.0, carbs=5.0, fat=22.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=310.0, potassium=0.0, vitamin_A=0.0, vitamin_C=6.0, calcium=2.0
)

black_pepper_sirloin_91 = create_food(
    food_name="Black Pepper Sirloin - 3.5oz",
    serving_size="112g",
    brand="Generic",
    calories=230.0, protein=27.0, carbs=2.0, fat=11.0, fiber=0.0, sugar=1.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=85.0, sodium=470.0, potassium=334.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

steamed_broccoli_92 = create_food(
    food_name="Steamed Broccoli - 3oz",
    serving_size="91g",
    brand="Generic",
    calories=35.0, protein=2.0, carbs=6.0, fat=0.0, fiber=2.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=30.0, potassium=288.6, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

roasted_poblano_and_garlic_potatoes_93 = create_food(
    food_name="Roasted Poblano and Garlic Potatoes - 4oz",
    serving_size="122g",
    brand="Generic",
    calories=190.0, protein=6.0, carbs=34.0, fat=4.5, fiber=9.0, sugar=1.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=250.0, potassium=62.3, vitamin_A=120.0, vitamin_C=15.0, calcium=4.0
)

chimichurri_sauce_94 = create_food(
    food_name="Chimichurri Sauce - Tablespoon",
    serving_size="18g",
    brand="Generic",
    calories=60.0, protein=0.0, carbs=2.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=50.0, potassium=8.3, vitamin_A=6.0, vitamin_C=10.0, calcium=2.0
)

kfc_style_coleslaw_95 = create_food(
    food_name="KFC Style Coleslaw - 3oz",
    serving_size="83g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=11.0, fat=8.0, fiber=1.0, sugar=9.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=160.0, potassium=107.6, vitamin_A=20.0, vitamin_C=4.0, calcium=50.0
)

caballo_loco_salsa_96 = create_food(
    food_name="Caballo Loco Salsa - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=50.0, protein=0.0, carbs=0.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=75.0, potassium=0.6, vitamin_A=4.0, vitamin_C=2.0, calcium=2.0
)

snappy_horseradish_sauce_97 = create_food(
    food_name="Snappy Horseradish Sauce - 2oz",
    serving_size="62g",
    brand="Generic",
    calories=220.0, protein=0.0, carbs=5.0, fat=22.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=310.0, potassium=0.0, vitamin_A=0.0, vitamin_C=6.0, calcium=2.0
)

detroit_deep_dish_bbq_chicken_pizza_98 = create_food(
    food_name="Detroit Deep Dish BBQ Chicken Pizza - Slice",
    serving_size="103g",
    brand="Generic",
    calories=250.0, protein=12.0, carbs=30.0, fat=8.0, fiber=1.0, sugar=4.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=570.0, potassium=99.1, vitamin_A=6.0, vitamin_C=2.0, calcium=15.0
)

cheese_pizza_99 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

halal_pepperoni_pizza_100 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

detroit_deep_dish_bbq_chicken_pizza_101 = create_food(
    food_name="Detroit Deep Dish BBQ Chicken Pizza - Slice",
    serving_size="103g",
    brand="Generic",
    calories=250.0, protein=12.0, carbs=30.0, fat=8.0, fiber=1.0, sugar=4.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=570.0, potassium=99.1, vitamin_A=6.0, vitamin_C=2.0, calcium=15.0
)

cheese_pizza_102 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

halal_pepperoni_pizza_103 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

homestyle_chicken_noodle_soup_104 = create_food(
    food_name="Homestyle Chicken Noodle Soup - 4oz",
    serving_size="130g",
    brand="Generic",
    calories=140.0, protein=6.0, carbs=22.0, fat=3.5, fiber=0.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=55.0, sodium=290.0, potassium=40.1, vitamin_A=2.0, vitamin_C=2.0, calcium=0.0
)

vegan_creamy_tomato_soup_105 = create_food(
    food_name="Vegan Creamy Tomato Soup - 4oz",
    serving_size="169g",
    brand="Generic",
    calories=150.0, protein=2.0, carbs=9.0, fat=12.0, fiber=1.0, sugar=5.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=260.0, potassium=7.1, vitamin_A=10.0, vitamin_C=20.0, calcium=4.0
)

chocolate_chip_cookie_106 = create_food(
    food_name="Chocolate Chip Cookie - Each",
    serving_size="29g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=17.0, fat=6.0, fiber=0.0, sugar=10.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=160.0, potassium=37.8, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

french_toast_crunch_bars_107 = create_food(
    food_name="French Toast Crunch Bars - 3 oz",
    serving_size="64g",
    brand="Generic",
    calories=260.0, protein=2.0, carbs=48.0, fat=7.0, fiber=2.0, sugar=27.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=15.0, vitamin_C=10.0, calcium=10.0
)

oreo_brownie_108 = create_food(
    food_name="Oreo Brownie - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=130.0, protein=1.0, carbs=16.0, fat=6.0, fiber=0.0, sugar=11.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=105.0, potassium=15.2, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

vegan_chocolate_cake_109 = create_food(
    food_name="Vegan Chocolate Cake - 2 oz",
    serving_size="67g",
    brand="Generic",
    calories=200.0, protein=2.0, carbs=38.0, fat=5.0, fiber=1.0, sugar=15.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

white_iced_marble_sheet_cake_110 = create_food(
    food_name="White Iced Marble Sheet Cake - 3oz",
    serving_size="70g",
    brand="Generic",
    calories=270.0, protein=2.0, carbs=38.0, fat=12.0, fiber=0.0, sugar=28.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=290.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

lemon_berry_cheesecake_bar_111 = create_food(
    food_name="Lemon Berry Cheesecake Bar - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=100.0, protein=1.0, carbs=9.0, fat=6.0, fiber=0.0, sugar=6.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=105.0, potassium=3.9, vitamin_A=4.0, vitamin_C=2.0, calcium=0.0
)

vegan_vanilla_cupcake_112 = create_food(
    food_name="Vegan Vanilla Cupcake - Each",
    serving_size="90g",
    brand="Generic",
    calories=320.0, protein=1.0, carbs=54.0, fat=11.0, fiber=0.0, sugar=40.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=17.2, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

iced_cupcakes_113 = create_food(
    food_name="Iced Cupcakes - Each",
    serving_size="92g",
    brand="Generic",
    calories=330.0, protein=2.0, carbs=41.0, fat=17.0, fiber=0.0, sugar=31.0,
    saturated_fat=12.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=230.0, potassium=65.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

made_to_order_sandwiches_114 = create_food(
    food_name="Made to Order Sandwiches - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

made_to_order_sandwiches_115 = create_food(
    food_name="Made to Order Sandwiches - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

vegetable_egg_rolls_116 = create_food(
    food_name="Vegetable Egg Rolls - Each",
    serving_size="85g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=17.0, fat=1.0, fiber=2.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=550.0, potassium=200.1, vitamin_A=30.0, vitamin_C=30.0, calcium=30.0
)

sesame_beef_and_broccoli_stir_fry_117 = create_food(
    food_name="Sesame Beef and Broccoli Stir Fry - 8oz",
    serving_size="237g",
    brand="Generic",
    calories=450.0, protein=27.0, carbs=15.0, fat=33.0, fiber=3.0, sugar=4.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=65.0, sodium=660.0, potassium=288.2, vitamin_A=10.0, vitamin_C=140.0, calcium=10.0
)

hunan_tofu_and_sesame_vegetables_118 = create_food(
    food_name="Hunan Tofu and Sesame Vegetables - 6oz",
    serving_size="159g",
    brand="Generic",
    calories=190.0, protein=5.0, carbs=21.0, fat=11.0, fiber=2.0, sugar=15.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=660.0, potassium=151.1, vitamin_A=60.0, vitamin_C=40.0, calcium=10.0
)

jasmine_rice_119 = create_food(
    food_name="Jasmine Rice - 4oz",
    serving_size="110g",
    brand="Generic",
    calories=140.0, protein=3.0, carbs=31.0, fat=0.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=130.0, potassium=1.2, vitamin_A=0.0, vitamin_C=8.0, calcium=2.0
)

sweet_and_sour_sauce_120 = create_food(
    food_name="Sweet and Sour Sauce - Cup",
    serving_size="202g",
    brand="Generic",
    calories=320.0, protein=0.0, carbs=80.0, fat=0.0, fiber=0.0, sugar=68.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=0.0, vitamin_A=4.0, vitamin_C=20.0, calcium=2.0
)

sweet_and_spicy_shrimp_121 = create_food(
    food_name="Sweet and Spicy Shrimp - 4oz",
    serving_size="115g",
    brand="Generic",
    calories=160.0, protein=18.0, carbs=16.0, fat=2.5, fiber=0.0, sugar=15.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=130.0, sodium=380.0, potassium=11.1, vitamin_A=0.0, vitamin_C=2.0, calcium=4.0
)

sesame_tofu_stir_fry_122 = create_food(
    food_name="Sesame Tofu Stir Fry - 8oz",
    serving_size="224g",
    brand="Generic",
    calories=210.0, protein=10.0, carbs=22.0, fat=10.0, fiber=3.0, sugar=14.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=2320.0, potassium=124.9, vitamin_A=45.0, vitamin_C=60.0, calcium=15.0
)

jasmine_rice_123 = create_food(
    food_name="Jasmine Rice - 4oz",
    serving_size="109g",
    brand="Generic",
    calories=130.0, protein=3.0, carbs=30.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=95.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

thai_vegetable_spring_roll_w_sauce_124 = create_food(
    food_name="Thai Vegetable Spring Roll w/ Sauce - Each",
    serving_size="142g",
    brand="Generic",
    calories=160.0, protein=3.0, carbs=32.0, fat=2.0, fiber=3.0, sugar=12.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=620.0, potassium=0.0, vitamin_A=20.0, vitamin_C=2.0, calcium=2.0
)

steamed_mixed_vegetables_125 = create_food(
    food_name="Steamed Mixed Vegetables - 3oz",
    serving_size="84g",
    brand="Generic",
    calories=60.0, protein=2.0, carbs=11.0, fat=1.5, fiber=3.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=0.0, vitamin_A=70.0, vitamin_C=4.0, calcium=2.0
)

thai_chili_sauce_126 = create_food(
    food_name="Thai Chili Sauce - Cup",
    serving_size="283g",
    brand="Generic",
    calories=610.0, protein=0.0, carbs=132.0, fat=9.0, fiber=9.0, sugar=132.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=2110.0, potassium=0.0, vitamin_A=50.0, vitamin_C=0.0, calcium=0.0
)

cauliflower_and_garbanzo_masala_127 = create_food(
    food_name="Cauliflower and Garbanzo Masala - 6oz",
    serving_size="166g",
    brand="Generic",
    calories=100.0, protein=3.0, carbs=14.0, fat=4.0, fiber=4.0, sugar=4.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=143.2, vitamin_A=80.0, vitamin_C=70.0, calcium=4.0
)

coconut_curry_halal_chicken_128 = create_food(
    food_name="Coconut Curry Halal Chicken - 6oz",
    serving_size="173g",
    brand="Generic",
    calories=200.0, protein=16.0, carbs=12.0, fat=11.0, fiber=2.0, sugar=7.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=65.0, sodium=290.0, potassium=238.6, vitamin_A=15.0, vitamin_C=45.0, calcium=4.0
)

roasted_ginger_curry_carrots_129 = create_food(
    food_name="Roasted Ginger Curry Carrots - 3oz",
    serving_size="93g",
    brand="Generic",
    calories=70.0, protein=1.0, carbs=10.0, fat=5.0, fiber=3.0, sugar=4.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=60.0, potassium=274.2, vitamin_A=290.0, vitamin_C=10.0, calcium=4.0
)

spicy_vegetable_pakoras_130 = create_food(
    food_name="Spicy Vegetable Pakoras - 4 Pakoras",
    serving_size="76g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=15.0, fat=1.0, fiber=4.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=380.0, potassium=303.9, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

basmati_rice_131 = create_food(
    food_name="Basmati Rice - 4oz",
    serving_size="121g",
    brand="Generic",
    calories=160.0, protein=4.0, carbs=35.0, fat=0.5, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=47.3, vitamin_A=0.0, vitamin_C=50.0, calcium=2.0
)

green_chutney_132 = create_food(
    food_name="Green Chutney - 2oz",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=50.0, potassium=63.8, vitamin_A=20.0, vitamin_C=10.0, calcium=2.0
)

garlic_naan_bread_133 = create_food(
    food_name="Garlic Naan Bread - Each",
    serving_size="43g",
    brand="Generic",
    calories=120.0, protein=4.0, carbs=19.0, fat=4.0, fiber=0.0, sugar=2.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=250.0, potassium=28.3, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

kachumber_salad_indian_cucumber_salad_134 = create_food(
    food_name="Kachumber Salad (Indian Cucumber Salad) - 4oz",
    serving_size="128g",
    brand="Generic",
    calories=20.0, protein=1.0, carbs=5.0, fat=0.0, fiber=2.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=135.0, potassium=239.3, vitamin_A=40.0, vitamin_C=25.0, calcium=2.0
)

tandoori_halal_beef_135 = create_food(
    food_name="Tandoori Halal Beef - 9oz",
    serving_size="226g",
    brand="Generic",
    calories=300.0, protein=31.0, carbs=10.0, fat=16.0, fiber=2.0, sugar=4.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=85.0, sodium=360.0, potassium=376.2, vitamin_A=90.0, vitamin_C=25.0, calcium=6.0
)

indian_vegetable_curry_136 = create_food(
    food_name="Indian Vegetable Curry - 5.5oz",
    serving_size="164g",
    brand="Generic",
    calories=110.0, protein=2.0, carbs=13.0, fat=6.0, fiber=3.0, sugar=4.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=135.0, potassium=190.9, vitamin_A=8.0, vitamin_C=10.0, calcium=2.0
)

basmati_rice_137 = create_food(
    food_name="Basmati Rice - 4oz",
    serving_size="121g",
    brand="Generic",
    calories=160.0, protein=4.0, carbs=35.0, fat=0.5, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=47.3, vitamin_A=0.0, vitamin_C=50.0, calcium=2.0
)

cucumber_tomato_raita_138 = create_food(
    food_name="Cucumber Tomato Raita - Each",
    serving_size="55g",
    brand="Generic",
    calories=20.0, protein=2.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=95.0, potassium=55.7, vitamin_A=2.0, vitamin_C=6.0, calcium=2.0
)

woodys_tabbouleh_salad_139 = create_food(
    food_name="Woody's Tabbouleh Salad - Cup",
    serving_size="57g",
    brand="Generic",
    calories=60.0, protein=1.0, carbs=4.0, fat=4.0, fiber=1.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=25.0, potassium=0.0, vitamin_A=30.0, vitamin_C=35.0, calcium=6.0
)

green_chutney_140 = create_food(
    food_name="Green Chutney - 2oz",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=50.0, potassium=63.8, vitamin_A=20.0, vitamin_C=10.0, calcium=2.0
)

pita_chips_141 = create_food(
    food_name="Pita Chips - 6 Chips",
    serving_size="28g",
    brand="Generic",
    calories=70.0, protein=2.0, carbs=13.0, fat=0.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=55.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

woodys_garlic_scallion_hummus_142 = create_food(
    food_name="Woody's Garlic Scallion Hummus - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=40.0, protein=0.0, carbs=2.0, fat=3.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=37.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

scrambled_eggs_143 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

tofu_scramble_144 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_145 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

hash_brown_patty_146 = create_food(
    food_name="Hash Brown Patty - Each",
    serving_size="54g",
    brand="Generic",
    calories=90.0, protein=2.0, carbs=11.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=2.0
)

sausage_links_147 = create_food(
    food_name="Sausage Links - 2 Links",
    serving_size="45g",
    brand="Generic",
    calories=160.0, protein=8.0, carbs=0.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=270.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties_148 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_149 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_150 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_151 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

cinnamon_roll_bread_pudding_152 = create_food(
    food_name="Cinnamon Roll Bread Pudding - 3oz",
    serving_size="81g",
    brand="Generic",
    calories=190.0, protein=4.0, carbs=25.0, fat=8.0, fiber=0.0, sugar=17.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=65.0, sodium=170.0, potassium=50.9, vitamin_A=6.0, vitamin_C=0.0, calcium=8.0
)

scrambled_eggs_153 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

tofu_scramble_154 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_155 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

hash_brown_patty_156 = create_food(
    food_name="Hash Brown Patty - Each",
    serving_size="54g",
    brand="Generic",
    calories=90.0, protein=2.0, carbs=11.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=2.0
)

sausage_links_157 = create_food(
    food_name="Sausage Links - 2 Links",
    serving_size="45g",
    brand="Generic",
    calories=160.0, protein=8.0, carbs=0.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=270.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties_158 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_159 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_160 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_161 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

beef_taco_meat_162 = create_food(
    food_name="Beef Taco Meat - Ounce",
    serving_size="36g",
    brand="Generic",
    calories=60.0, protein=5.0, carbs=0.0, fat=4.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=160.0, potassium=67.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tex_mex_pinto_beans_163 = create_food(
    food_name="Tex Mex Pinto Beans - 3oz",
    serving_size="84g",
    brand="Generic",
    calories=60.0, protein=3.0, carbs=10.0, fat=0.5, fiber=3.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=290.0, potassium=147.1, vitamin_A=2.0, vitamin_C=10.0, calcium=10.0
)

shredded_mild_cheddar_cheese_164 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

tortilla_chips_165 = create_food(
    food_name="Tortilla Chips - 15 Chips",
    serving_size="14g",
    brand="Generic",
    calories=40.0, protein=0.0, carbs=7.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

con_queso_dip_166 = create_food(
    food_name="Con Queso Dip - Cup",
    serving_size="206g",
    brand="Generic",
    calories=570.0, protein=15.0, carbs=15.0, fat=50.0, fiber=0.0, sugar=7.0,
    saturated_fat=32.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=190.0, sodium=950.0, potassium=275.3, vitamin_A=30.0, vitamin_C=35.0, calcium=50.0
)

green_onions_167 = create_food(
    food_name="Green Onions - Cup",
    serving_size="85g",
    brand="Generic",
    calories=25.0, protein=2.0, carbs=6.0, fat=0.0, fiber=3.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=15.0, potassium=232.2, vitamin_A=15.0, vitamin_C=25.0, calcium=6.0
)

salsa_168 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=60.0, potassium=32.7, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

sour_cream_169 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

tomatoes_170 = create_food(
    food_name="Tomatoes - Cup",
    serving_size="85g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=3.0, fat=0.0, fiber=1.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=15.0, vitamin_C=20.0, calcium=0.0
)

cream_of_tomato_soup_171 = create_food(
    food_name="Cream of Tomato Soup - 4oz",
    serving_size="122g",
    brand="Generic",
    calories=70.0, protein=3.0, carbs=12.0, fat=1.5, fiber=1.0, sugar=8.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=290.0, potassium=237.8, vitamin_A=4.0, vitamin_C=6.0, calcium=8.0
)

grilled_ham_and_cheese_172 = create_food(
    food_name="Grilled Ham and Cheese - Each",
    serving_size="136g",
    brand="Generic",
    calories=360.0, protein=17.0, carbs=37.0, fat=17.0, fiber=2.0, sugar=3.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=1170.0, potassium=54.5, vitamin_A=15.0, vitamin_C=2.0, calcium=20.0
)

grilled_cheese_on_cheddar_bread_173 = create_food(
    food_name="Grilled Cheese on Cheddar Bread - Each",
    serving_size="184g",
    brand="Generic",
    calories=610.0, protein=18.0, carbs=44.0, fat=40.0, fiber=1.0, sugar=6.0,
    saturated_fat=16.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=60.0, sodium=950.0, potassium=28.5, vitamin_A=30.0, vitamin_C=15.0, calcium=35.0
)

grated_parmesan_cheese_174 = create_food(
    food_name="Grated Parmesan Cheese - Tablespoon",
    serving_size="5g",
    brand="Generic",
    calories=20.0, protein=2.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=75.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

hawaiian_roll_175 = create_food(
    food_name="Hawaiian Roll - Each",
    serving_size="49g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=25.0, fat=2.5, fiber=0.0, sugar=5.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=115.0, potassium=0.0, vitamin_A=0.0, vitamin_C=20.0, calcium=2.0
)

buttered_corn_176 = create_food(
    food_name="Buttered Corn - 3oz",
    serving_size="84g",
    brand="Generic",
    calories=120.0, protein=3.0, carbs=21.0, fat=2.5, fiber=2.0, sugar=2.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=0.0
)

yukon_mashed_potatoes_177 = create_food(
    food_name="Yukon Mashed Potatoes - 4oz",
    serving_size="101g",
    brand="Generic",
    calories=170.0, protein=3.0, carbs=17.0, fat=10.0, fiber=2.0, sugar=1.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=160.0, potassium=29.1, vitamin_A=10.0, vitamin_C=15.0, calcium=4.0
)

shaved_ribeye_beef_178 = create_food(
    food_name="Shaved Ribeye Beef - 4oz",
    serving_size="113g",
    brand="Generic",
    calories=80.0, protein=24.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=50.0, sodium=70.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

honey_butter_179 = create_food(
    food_name="Honey Butter - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=2.0, fat=10.0, fiber=0.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=8.0, vitamin_C=0.0, calcium=0.0
)

chicken_gravy_180 = create_food(
    food_name="Chicken Gravy - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=0.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=30.0, potassium=0.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

grated_parmesan_cheese_181 = create_food(
    food_name="Grated Parmesan Cheese - Tablespoon",
    serving_size="5g",
    brand="Generic",
    calories=20.0, protein=2.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=75.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

blueberry_streusel_pizza_182 = create_food(
    food_name="Blueberry Streusel Pizza - Slice",
    serving_size="125g",
    brand="Generic",
    calories=370.0, protein=7.0, carbs=60.0, fat=12.0, fiber=2.0, sugar=24.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=400.0, potassium=61.0, vitamin_A=8.0, vitamin_C=0.0, calcium=4.0
)

cheese_pizza_183 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

halal_pepperoni_pizza_184 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

blueberry_streusel_pizza_185 = create_food(
    food_name="Blueberry Streusel Pizza - Slice",
    serving_size="125g",
    brand="Generic",
    calories=370.0, protein=7.0, carbs=60.0, fat=12.0, fiber=2.0, sugar=24.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=400.0, potassium=61.0, vitamin_A=8.0, vitamin_C=0.0, calcium=4.0
)

cheese_pizza_186 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

halal_pepperoni_pizza_187 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

chicken_and_rice_soup_188 = create_food(
    food_name="Chicken and Rice Soup - 4oz",
    serving_size="125g",
    brand="Generic",
    calories=50.0, protein=4.0, carbs=7.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=410.0, potassium=53.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

southwest_vegetable_soup_189 = create_food(
    food_name="Southwest Vegetable Soup - 6oz",
    serving_size="158g",
    brand="Generic",
    calories=70.0, protein=3.0, carbs=10.0, fat=2.5, fiber=3.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=360.0, potassium=84.0, vitamin_A=20.0, vitamin_C=60.0, calcium=2.0
)

chocolate_chip_cookie_190 = create_food(
    food_name="Chocolate Chip Cookie - Each",
    serving_size="29g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=17.0, fat=6.0, fiber=0.0, sugar=10.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=160.0, potassium=37.8, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

bakerys_monster_cookie_191 = create_food(
    food_name="Bakery's Monster Cookie - Each",
    serving_size="29g",
    brand="Generic",
    calories=130.0, protein=1.0, carbs=18.0, fat=6.0, fiber=0.0, sugar=11.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=75.0, potassium=15.1, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

double_chocolate_chip_cookie_192 = create_food(
    food_name="Double Chocolate Chip Cookie - Each",
    serving_size="29g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=17.0, fat=6.0, fiber=0.0, sugar=10.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=70.0, potassium=22.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

oreo_brownie_193 = create_food(
    food_name="Oreo Brownie - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=130.0, protein=1.0, carbs=16.0, fat=6.0, fiber=0.0, sugar=11.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=105.0, potassium=15.2, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

vegan_chocolate_cake_194 = create_food(
    food_name="Vegan Chocolate Cake - 2 oz",
    serving_size="67g",
    brand="Generic",
    calories=200.0, protein=2.0, carbs=38.0, fat=5.0, fiber=1.0, sugar=15.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

white_iced_marble_sheet_cake_195 = create_food(
    food_name="White Iced Marble Sheet Cake - 3oz",
    serving_size="70g",
    brand="Generic",
    calories=270.0, protein=2.0, carbs=38.0, fat=12.0, fiber=0.0, sugar=28.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=290.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

confetti_cake_196 = create_food(
    food_name="Confetti Cake - 3 oz",
    serving_size="78g",
    brand="Generic",
    calories=300.0, protein=2.0, carbs=36.0, fat=16.0, fiber=0.0, sugar=25.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=250.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheesecake_197 = create_food(
    food_name="Cheesecake - 3 oz",
    serving_size="104g",
    brand="Generic",
    calories=360.0, protein=6.0, carbs=28.0, fat=25.0, fiber=0.0, sugar=21.0,
    saturated_fat=13.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=125.0, sodium=340.0, potassium=19.4, vitamin_A=15.0, vitamin_C=0.0, calcium=8.0
)

vegan_vanilla_cupcake_198 = create_food(
    food_name="Vegan Vanilla Cupcake - Each",
    serving_size="90g",
    brand="Generic",
    calories=320.0, protein=1.0, carbs=54.0, fat=11.0, fiber=0.0, sugar=40.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=17.2, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

made_to_order_sandwiches_199 = create_food(
    food_name="Made to Order Sandwiches - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

jalapeno_cheese_grinder_bread_200 = create_food(
    food_name="Jalapeno Cheese Grinder Bread - Grinder",
    serving_size="271g",
    brand="Generic",
    calories=700.0, protein=25.0, carbs=100.0, fat=22.0, fiber=5.0, sugar=3.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=35.0, sodium=630.0, potassium=10.1, vitamin_A=8.0, vitamin_C=15.0, calcium=25.0
)

white_italian_bread_201 = create_food(
    food_name="White Italian Bread - Each",
    serving_size="32g",
    brand="Generic",
    calories=80.0, protein=3.0, carbs=16.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=250.0, potassium=24.6, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

whole_wheat_hearty_bread_202 = create_food(
    food_name="100% Whole Wheat Hearty Bread - Slice",
    serving_size="49g",
    brand="Generic",
    calories=120.0, protein=4.0, carbs=24.0, fat=2.5, fiber=3.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=113.0, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

pretzel_roll_203 = create_food(
    food_name="Pretzel Roll - Each",
    serving_size="91g",
    brand="Generic",
    calories=250.0, protein=6.0, carbs=45.0, fat=4.5, fiber=2.0, sugar=4.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=260.0, potassium=68.5, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

roast_beef_204 = create_food(
    food_name="Roast Beef - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=45.0, protein=8.0, carbs=0.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=10.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheddar_cheese_205 = create_food(
    food_name="Cheddar Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=90.0, protein=5.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=140.0, potassium=22.4, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

provolone_cheese_206 = create_food(
    food_name="Provolone Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=80.0, protein=5.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=180.0, potassium=28.5, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

swiss_cheese_207 = create_food(
    food_name="Swiss Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=80.0, protein=6.0, carbs=1.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=45.0, potassium=28.1, vitamin_A=2.0, vitamin_C=0.0, calcium=15.0
)

cucumbers_208 = create_food(
    food_name="Cucumbers - Cup",
    serving_size="113g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=166.7, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

mayonnaise_209 = create_food(
    food_name="Mayonnaise - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=90.0, protein=0.0, carbs=0.0, fat=10.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=85.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

leaf_lettuce_210 = create_food(
    food_name="Leaf Lettuce - Cup",
    serving_size="57g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=15.0, potassium=0.0, vitamin_A=80.0, vitamin_C=8.0, calcium=2.0
)

dijon_mustard_211 = create_food(
    food_name="Dijon Mustard - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

mustard_212 = create_food(
    food_name="Mustard - Tablespoon",
    serving_size="17g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=200.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

black_olives_213 = create_food(
    food_name="Black Olives - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=45.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

red_onions_214 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

banana_peppers_215 = create_food(
    food_name="Banana Peppers - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

green_bell_peppers_216 = create_food(
    food_name="Green Bell Peppers - Cup",
    serving_size="193g",
    brand="Generic",
    calories=40.0, protein=2.0, carbs=9.0, fat=0.0, fiber=3.0, sugar=5.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=5.0, potassium=0.0, vitamin_A=15.0, vitamin_C=260.0, calcium=2.0
)

jalapenos_217 = create_food(
    food_name="Jalapenos - Tablespoon",
    serving_size="12g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=120.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dill_pickle_chips_218 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

ham_219 = create_food(
    food_name="Ham - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=35.0, protein=6.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

hard_salami_220 = create_food(
    food_name="Hard Salami - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=110.0, protein=5.0, carbs=0.0, fat=9.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=35.0, sodium=450.0, potassium=0.0, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

chipotle_aioli_221 = create_food(
    food_name="Chipotle Aioli - Tablespoon",
    serving_size="17g",
    brand="Generic",
    calories=110.0, protein=0.0, carbs=0.0, fat=12.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=90.0, potassium=0.6, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

spinach_222 = create_food(
    food_name="Spinach - Cup",
    serving_size="85g",
    brand="Generic",
    calories=20.0, protein=2.0, carbs=3.0, fat=0.0, fiber=2.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=473.4, vitamin_A=160.0, vitamin_C=40.0, calcium=8.0
)

tomatoes_223 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

tomato_tortilla_224 = create_food(
    food_name="Tomato Tortilla - Each",
    serving_size="94g",
    brand="Generic",
    calories=280.0, protein=7.0, carbs=44.0, fat=8.0, fiber=3.0, sugar=2.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=540.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

turkey_breast_225 = create_food(
    food_name="Turkey Breast - Slice",
    serving_size="28g",
    brand="Generic",
    calories=25.0, protein=5.0, carbs=1.0, fat=1.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=78.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheddar_cheese_226 = create_food(
    food_name="Cheddar Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=90.0, protein=5.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=140.0, potassium=22.4, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

cucumbers_227 = create_food(
    food_name="Cucumbers - Cup",
    serving_size="113g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=166.7, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

mayonnaise_228 = create_food(
    food_name="Mayonnaise - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=90.0, protein=0.0, carbs=0.0, fat=10.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=85.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dijon_mustard_229 = create_food(
    food_name="Dijon Mustard - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

red_onions_230 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

banana_peppers_231 = create_food(
    food_name="Banana Peppers - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dill_pickle_chips_232 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

ham_233 = create_food(
    food_name="Ham - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=35.0, protein=6.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

tomatoes_234 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

turkey_breast_235 = create_food(
    food_name="Turkey Breast - Slice",
    serving_size="28g",
    brand="Generic",
    calories=25.0, protein=5.0, carbs=1.0, fat=1.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=78.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

spicy_soy_marinated_chicken_thighs_236 = create_food(
    food_name="Spicy Soy Marinated Chicken Thighs - 5oz",
    serving_size="145g",
    brand="Generic",
    calories=230.0, protein=23.0, carbs=0.0, fat=16.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=105.0, sodium=150.0, potassium=17.5, vitamin_A=2.0, vitamin_C=4.0, calcium=0.0
)

sriracha_sesame_tofu_237 = create_food(
    food_name="Sriracha Sesame Tofu - 10oz",
    serving_size="262g",
    brand="Generic",
    calories=250.0, protein=19.0, carbs=9.0, fat=18.0, fiber=5.0, sugar=3.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=800.0, potassium=359.4, vitamin_A=2.0, vitamin_C=2.0, calcium=40.0
)

soft_boiled_soy_egg_238 = create_food(
    food_name="Soft Boiled Soy Egg - Each",
    serving_size="77g",
    brand="Generic",
    calories=100.0, protein=10.0, carbs=2.0, fat=6.0, fiber=0.0, sugar=1.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=1150.0, potassium=5.1, vitamin_A=6.0, vitamin_C=0.0, calcium=4.0
)

sesame_roasted_shiitake_cremini_mushroom_239 = create_food(
    food_name="Sesame Roasted Shiitake Cremini Mushroom - Tablespoon",
    serving_size="21g",
    brand="Generic",
    calories=40.0, protein=0.0, carbs=2.0, fat=3.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=45.0, potassium=19.9, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

yaki_soba_noodle_240 = create_food(
    food_name="Yaki Soba Noodle - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=80.0, protein=3.0, carbs=15.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=60.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

green_onions_241 = create_food(
    food_name="Green Onions - Cup",
    serving_size="85g",
    brand="Generic",
    calories=25.0, protein=2.0, carbs=6.0, fat=0.0, fiber=3.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=15.0, potassium=232.2, vitamin_A=15.0, vitamin_C=25.0, calcium=6.0
)

chicken_and_pork_ramen_broth_242 = create_food(
    food_name="Chicken and Pork Ramen Broth - Cup",
    serving_size="229g",
    brand="Generic",
    calories=20.0, protein=1.0, carbs=1.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=75.0, potassium=1.9, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheese_stuffed_breadsticks_243 = create_food(
    food_name="Cheese Stuffed Breadsticks - Each",
    serving_size="85g",
    brand="Generic",
    calories=210.0, protein=12.0, carbs=25.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=400.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

steamed_broccoli_244 = create_food(
    food_name="Steamed Broccoli - 3oz",
    serving_size="91g",
    brand="Generic",
    calories=35.0, protein=2.0, carbs=6.0, fat=0.0, fiber=2.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=30.0, potassium=288.6, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

broiled_chicken_245 = create_food(
    food_name="Broiled Chicken - 4oz",
    serving_size="109g",
    brand="Generic",
    calories=200.0, protein=33.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=90.0, sodium=160.0, potassium=270.7, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

grated_parmesan_cheese_246 = create_food(
    food_name="Grated Parmesan Cheese - Tablespoon",
    serving_size="5g",
    brand="Generic",
    calories=20.0, protein=2.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=75.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

fettuccine_pasta_247 = create_food(
    food_name="Fettuccine Pasta - Ounce",
    serving_size="29g",
    brand="Generic",
    calories=40.0, protein=1.0, carbs=8.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheese_alfredo_sauce_248 = create_food(
    food_name="3 Cheese Alfredo Sauce - Cup",
    serving_size="230g",
    brand="Generic",
    calories=370.0, protein=14.0, carbs=18.0, fat=27.0, fiber=0.0, sugar=6.0,
    saturated_fat=15.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=70.0, sodium=900.0, potassium=200.6, vitamin_A=15.0, vitamin_C=20.0, calcium=45.0
)

crispy_italian_tofu_249 = create_food(
    food_name="Crispy Italian Tofu - 4oz",
    serving_size="102g",
    brand="Generic",
    calories=150.0, protein=6.0, carbs=21.0, fat=3.5, fiber=2.0, sugar=0.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=170.0, potassium=97.8, vitamin_A=2.0, vitamin_C=0.0, calcium=15.0
)

garlic_naan_250 = create_food(
    food_name="Garlic Naan - 2 Slices",
    serving_size="46g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=20.0, fat=5.0, fiber=0.0, sugar=1.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=330.0, potassium=0.8, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

coconut_curry_halal_chicken_251 = create_food(
    food_name="Coconut Curry Halal Chicken - 6oz",
    serving_size="173g",
    brand="Generic",
    calories=200.0, protein=16.0, carbs=12.0, fat=11.0, fiber=2.0, sugar=7.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=65.0, sodium=290.0, potassium=238.6, vitamin_A=15.0, vitamin_C=45.0, calcium=4.0
)

falafel_252 = create_food(
    food_name="Falafel - 1oz",
    serving_size="34g",
    brand="Generic",
    calories=70.0, protein=5.0, carbs=18.0, fat=3.5, fiber=9.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=15.4, vitamin_A=4.0, vitamin_C=4.0, calcium=4.0
)

battered_pollock_253 = create_food(
    food_name="Battered Pollock - Each",
    serving_size="92g",
    brand="Generic",
    calories=130.0, protein=10.0, carbs=14.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=470.0, potassium=194.5, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

fried_chile_cabbage_254 = create_food(
    food_name="Fried Chile Cabbage - 5oz",
    serving_size="131g",
    brand="Generic",
    calories=70.0, protein=2.0, carbs=9.0, fat=2.5, fiber=3.0, sugar=4.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=60.0, potassium=189.5, vitamin_A=20.0, vitamin_C=6.0, calcium=100.0
)

basmati_rice_255 = create_food(
    food_name="Basmati Rice - 4oz",
    serving_size="121g",
    brand="Generic",
    calories=160.0, protein=4.0, carbs=35.0, fat=0.5, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=47.3, vitamin_A=0.0, vitamin_C=50.0, calcium=2.0
)

feta_cheese_256 = create_food(
    food_name="Feta Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=20.0, protein=1.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=75.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

iceberg_lettuce_257 = create_food(
    food_name="Iceberg Lettuce - Cup",
    serving_size="80g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=8.0, vitamin_C=4.0, calcium=0.0
)

red_onions_258 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tartar_sauce_259 = create_food(
    food_name="Tartar Sauce - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=50.0, protein=0.0, carbs=2.0, fat=5.0, fiber=0.0, sugar=2.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=110.0, potassium=0.2, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tomatoes_260 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

garlic_naan_261 = create_food(
    food_name="Garlic Naan - 2 Slices",
    serving_size="46g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=20.0, fat=5.0, fiber=0.0, sugar=1.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=330.0, potassium=0.8, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

ginger_lemongrass_halal_beef_w_sesame_262 = create_food(
    food_name="Ginger Lemongrass Halal Beef w/ Sesame - 3oz",
    serving_size="81g",
    brand="Generic",
    calories=150.0, protein=15.0, carbs=14.0, fat=4.0, fiber=0.0, sugar=13.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=270.0, potassium=1.1, vitamin_A=6.0, vitamin_C=0.0, calcium=0.0
)

ginger_and_garlic_sauteed_snow_peas_263 = create_food(
    food_name="Ginger and Garlic Sauteed Snow Peas - 2oz",
    serving_size="53g",
    brand="Generic",
    calories=40.0, protein=2.0, carbs=5.0, fat=1.5, fiber=1.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=290.0, potassium=4.6, vitamin_A=10.0, vitamin_C=45.0, calcium=2.0
)

coconut_rice_264 = create_food(
    food_name="Coconut Rice - 4oz",
    serving_size="105g",
    brand="Generic",
    calories=350.0, protein=11.0, carbs=75.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=4.9, vitamin_A=2.0, vitamin_C=2.0, calcium=0.0
)

vegetable_samosas_265 = create_food(
    food_name="Vegetable Samosas - Each",
    serving_size="23g",
    brand="Generic",
    calories=50.0, protein=1.0, carbs=8.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=120.0, potassium=45.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

feta_cheese_266 = create_food(
    food_name="Feta Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=20.0, protein=1.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=75.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

iceberg_lettuce_267 = create_food(
    food_name="Iceberg Lettuce - Cup",
    serving_size="80g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=8.0, vitamin_C=4.0, calcium=0.0
)

red_onions_268 = create_food(
    food_name="Red Onions - Cup",
    serving_size="125g",
    brand="Generic",
    calories=50.0, protein=1.0, carbs=11.0, fat=0.0, fiber=2.0, sugar=5.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=15.0, calcium=2.0
)

tzatziki_269 = create_food(
    food_name="Tzatziki - Quart",
    serving_size="933g",
    brand="Generic",
    calories=580.0, protein=74.0, carbs=47.0, fat=9.0, fiber=3.0, sugar=29.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=2090.0, potassium=857.4, vitamin_A=6.0, vitamin_C=25.0, calcium=100.0
)

tomatoes_270 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

scrambled_eggs_271 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

quiche_lorraine_272 = create_food(
    food_name="Quiche Lorraine - 3.5oz",
    serving_size="143g",
    brand="Generic",
    calories=420.0, protein=18.0, carbs=16.0, fat=31.0, fiber=0.0, sugar=1.0,
    saturated_fat=13.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=215.0, sodium=650.0, potassium=80.7, vitamin_A=6.0, vitamin_C=0.0, calcium=20.0
)

tofu_scramble_273 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_274 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

bacon_275 = create_food(
    food_name="Bacon - 2 Slices",
    serving_size="18g",
    brand="Generic",
    calories=90.0, protein=6.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=250.0, potassium=101.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tater_tots_276 = create_food(
    food_name="Tater Tots - 4oz",
    serving_size="113g",
    brand="Generic",
    calories=230.0, protein=3.0, carbs=26.0, fat=11.0, fiber=3.0, sugar=0.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=460.0, potassium=318.1, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

veggie_sausage_patties_277 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_278 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_279 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_280 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

cherry_ginger_and_lime_smoothie_281 = create_food(
    food_name="Cherry, Ginger and Lime Smoothie - Cup",
    serving_size="242g",
    brand="Generic",
    calories=150.0, protein=5.0, carbs=30.0, fat=2.0, fiber=1.0, sugar=23.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=80.0, potassium=231.8, vitamin_A=15.0, vitamin_C=10.0, calcium=15.0
)

scrambled_eggs_282 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

tofu_scramble_283 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_284 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

bacon_285 = create_food(
    food_name="Bacon - 2 Slices",
    serving_size="18g",
    brand="Generic",
    calories=90.0, protein=6.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=250.0, potassium=101.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tater_tots_286 = create_food(
    food_name="Tater Tots - 4oz",
    serving_size="113g",
    brand="Generic",
    calories=230.0, protein=3.0, carbs=26.0, fat=11.0, fiber=3.0, sugar=0.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=460.0, potassium=318.1, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

chicken_sausage_patties_287 = create_food(
    food_name="Chicken Sausage Patties - Each",
    serving_size="40g",
    brand="Generic",
    calories=80.0, protein=6.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=250.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties_288 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_289 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_290 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_291 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

lamb_gyro_292 = create_food(
    food_name="Lamb Gyro - Each",
    serving_size="234g",
    brand="Generic",
    calories=550.0, protein=24.0, carbs=48.0, fat=30.0, fiber=2.0, sugar=5.0,
    saturated_fat=10.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=65.0, sodium=1090.0, potassium=273.1, vitamin_A=20.0, vitamin_C=6.0, calcium=20.0
)

greek_fries_293 = create_food(
    food_name="Greek Fries - 4oz",
    serving_size="114g",
    brand="Generic",
    calories=110.0, protein=3.0, carbs=20.0, fat=2.0, fiber=3.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=70.0, potassium=337.5, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

feta_cheese_294 = create_food(
    food_name="Feta Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=20.0, protein=1.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=75.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

iceberg_lettuce_295 = create_food(
    food_name="Iceberg Lettuce - Cup",
    serving_size="80g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=8.0, vitamin_C=4.0, calcium=0.0
)

tzatziki_296 = create_food(
    food_name="Tzatziki - Quart",
    serving_size="933g",
    brand="Generic",
    calories=580.0, protein=74.0, carbs=47.0, fat=9.0, fiber=3.0, sugar=29.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=2090.0, potassium=857.4, vitamin_A=6.0, vitamin_C=25.0, calcium=100.0
)

tomatoes_297 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

burger_bun_298 = create_food(
    food_name="Burger Bun - Each",
    serving_size="35g",
    brand="Generic",
    calories=90.0, protein=3.0, carbs=17.0, fat=1.5, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=34.2, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

black_bean_burger_299 = create_food(
    food_name="Black Bean Burger - Each",
    serving_size="132g",
    brand="Generic",
    calories=250.0, protein=10.0, carbs=37.0, fat=8.0, fiber=7.0, sugar=5.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=650.0, potassium=385.6, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

bacon_cheeseburger_300 = create_food(
    food_name="Bacon Cheeseburger - Each",
    serving_size="166g",
    brand="Generic",
    calories=420.0, protein=31.0, carbs=19.0, fat=25.0, fiber=0.0, sugar=3.0,
    saturated_fat=10.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=95.0, sodium=720.0, potassium=331.3, vitamin_A=6.0, vitamin_C=0.0, calcium=15.0
)

burger_301 = create_food(
    food_name="Burger - Each",
    serving_size="120g",
    brand="Generic",
    calories=290.0, protein=24.0, carbs=17.0, fat=13.0, fiber=0.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=70.0, sodium=240.0, potassium=331.3, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

french_fries_302 = create_food(
    food_name="French Fries - 3oz",
    serving_size="85g",
    brand="Generic",
    calories=130.0, protein=1.0, carbs=20.0, fat=5.0, fiber=1.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=360.0, potassium=232.9, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

pecan_smoked_bacon_303 = create_food(
    food_name="Pecan Smoked Bacon - Each",
    serving_size="31g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=0.0, fat=9.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=300.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

iceberg_lettuce_304 = create_food(
    food_name="Iceberg Lettuce - Cup",
    serving_size="80g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=8.0, vitamin_C=4.0, calcium=0.0
)

red_onions_305 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

caramelized_onions_306 = create_food(
    food_name="Caramelized Onions - Tablespoon",
    serving_size="60g",
    brand="Generic",
    calories=40.0, protein=0.0, carbs=6.0, fat=1.5, fiber=0.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=350.0, potassium=0.0, vitamin_A=0.0, vitamin_C=4.0, calcium=2.0
)

dill_pickle_chips_307 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

olive_sauce_308 = create_food(
    food_name="Olive Sauce - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=60.0, protein=0.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=160.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tomatoes_309 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

hawaiian_dinner_roll_310 = create_food(
    food_name="Hawaiian Dinner Roll - Each",
    serving_size="35g",
    brand="Generic",
    calories=100.0, protein=4.0, carbs=19.0, fat=1.5, fiber=1.0, sugar=5.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=160.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

tangy_bbq_pork_ribs_311 = create_food(
    food_name="Tangy BBQ Pork Ribs - 4.5oz",
    serving_size="140g",
    brand="Generic",
    calories=350.0, protein=15.0, carbs=26.0, fat=20.0, fiber=0.0, sugar=24.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=65.0, sodium=720.0, potassium=0.2, vitamin_A=10.0, vitamin_C=10.0, calcium=0.0
)

buttered_corn_312 = create_food(
    food_name="Buttered Corn - 3oz",
    serving_size="84g",
    brand="Generic",
    calories=120.0, protein=3.0, carbs=21.0, fat=2.5, fiber=2.0, sugar=2.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=0.0
)

baked_sweet_potato_313 = create_food(
    food_name="Baked Sweet Potato - Each",
    serving_size="137g",
    brand="Generic",
    calories=120.0, protein=2.0, carbs=28.0, fat=0.5, fiber=4.0, sugar=6.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=457.9, vitamin_A=0.0, vitamin_C=6.0, calcium=4.0
)

honey_butter_314 = create_food(
    food_name="Honey Butter - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=2.0, fat=10.0, fiber=0.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=8.0, vitamin_C=0.0, calcium=0.0
)

feta_cheese_315 = create_food(
    food_name="Feta Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=20.0, protein=1.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=75.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

cucumbers_316 = create_food(
    food_name="Cucumbers - Cup",
    serving_size="113g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=166.7, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

iceberg_lettuce_317 = create_food(
    food_name="Iceberg Lettuce - Cup",
    serving_size="80g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=8.0, vitamin_C=4.0, calcium=0.0
)

tzatziki_318 = create_food(
    food_name="Tzatziki - Quart",
    serving_size="933g",
    brand="Generic",
    calories=580.0, protein=74.0, carbs=47.0, fat=9.0, fiber=3.0, sugar=29.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=2090.0, potassium=857.4, vitamin_A=6.0, vitamin_C=25.0, calcium=100.0
)

tomatoes_319 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

cheese_pizza_320 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

detroit_deep_dish_halal_pepperoni_pizza_321 = create_food(
    food_name="Detroit Deep Dish Halal Pepperoni Pizza - Slice",
    serving_size="73g",
    brand="Generic",
    calories=190.0, protein=7.0, carbs=26.0, fat=6.0, fiber=1.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=530.0, potassium=91.1, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

spinach_tomato_onion_and_feta_pizza_322 = create_food(
    food_name="Spinach, Tomato, Onion, and Feta Pizza - Slice",
    serving_size="73g",
    brand="Generic",
    calories=160.0, protein=8.0, carbs=19.0, fat=6.0, fiber=2.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=390.0, potassium=54.0, vitamin_A=6.0, vitamin_C=4.0, calcium=15.0
)

cheese_pizza_323 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

detroit_deep_dish_halal_pepperoni_pizza_324 = create_food(
    food_name="Detroit Deep Dish Halal Pepperoni Pizza - Slice",
    serving_size="73g",
    brand="Generic",
    calories=190.0, protein=7.0, carbs=26.0, fat=6.0, fiber=1.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=530.0, potassium=91.1, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

spinach_tomato_onion_and_feta_pizza_325 = create_food(
    food_name="Spinach, Tomato, Onion, and Feta Pizza - Slice",
    serving_size="73g",
    brand="Generic",
    calories=160.0, protein=8.0, carbs=19.0, fat=6.0, fiber=2.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=390.0, potassium=54.0, vitamin_A=6.0, vitamin_C=4.0, calcium=15.0
)

homestyle_chicken_noodle_soup_326 = create_food(
    food_name="Homestyle Chicken Noodle Soup - 4oz",
    serving_size="130g",
    brand="Generic",
    calories=140.0, protein=6.0, carbs=22.0, fat=3.5, fiber=0.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=55.0, sodium=290.0, potassium=40.1, vitamin_A=2.0, vitamin_C=2.0, calcium=0.0
)

vegetable_tortilla_soup_327 = create_food(
    food_name="Vegetable Tortilla Soup - 6oz",
    serving_size="166g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=1.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=63.7, vitamin_A=2.0, vitamin_C=15.0, calcium=2.0
)

chocolate_chip_cookie_328 = create_food(
    food_name="Chocolate Chip Cookie - Each",
    serving_size="29g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=17.0, fat=6.0, fiber=0.0, sugar=10.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=160.0, potassium=37.8, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

sugar_cookie_329 = create_food(
    food_name="Sugar Cookie - Each",
    serving_size="28g",
    brand="Generic",
    calories=130.0, protein=1.0, carbs=16.0, fat=6.0, fiber=0.0, sugar=8.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=125.0, potassium=3.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

french_toast_crunch_bars_330 = create_food(
    food_name="French Toast Crunch Bars - 3 oz",
    serving_size="64g",
    brand="Generic",
    calories=260.0, protein=2.0, carbs=48.0, fat=7.0, fiber=2.0, sugar=27.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=15.0, vitamin_C=10.0, calcium=10.0
)

mint_brownie_331 = create_food(
    food_name="Mint Brownie - Ounce",
    serving_size="39g",
    brand="Generic",
    calories=160.0, protein=1.0, carbs=24.0, fat=6.0, fiber=0.0, sugar=18.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=115.0, potassium=7.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

vegan_chocolate_cake_332 = create_food(
    food_name="Vegan Chocolate Cake - 2 oz",
    serving_size="67g",
    brand="Generic",
    calories=200.0, protein=2.0, carbs=38.0, fat=5.0, fiber=1.0, sugar=15.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

creamsicle_sheet_cake_333 = create_food(
    food_name="Creamsicle Sheet Cake - 3 oz",
    serving_size="76g",
    brand="Generic",
    calories=180.0, protein=2.0, carbs=26.0, fat=8.0, fiber=0.0, sugar=7.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

pink_lemonade_cake_334 = create_food(
    food_name="Pink Lemonade Cake - 3 oz",
    serving_size="118g",
    brand="Generic",
    calories=460.0, protein=1.0, carbs=57.0, fat=25.0, fiber=0.0, sugar=35.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=300.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chocolate_iced_white_cake_335 = create_food(
    food_name="Chocolate Iced White Cake - Ounce",
    serving_size="32g",
    brand="Generic",
    calories=130.0, protein=0.0, carbs=18.0, fat=7.0, fiber=0.0, sugar=15.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=100.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

up_pound_cake_336 = create_food(
    food_name="7 Up Pound Cake - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=110.0, protein=1.0, carbs=16.0, fat=4.5, fiber=0.0, sugar=10.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=10.0, potassium=4.7, vitamin_A=4.0, vitamin_C=0.0, calcium=0.0
)

vegan_vanilla_cupcake_337 = create_food(
    food_name="Vegan Vanilla Cupcake - Each",
    serving_size="90g",
    brand="Generic",
    calories=320.0, protein=1.0, carbs=54.0, fat=11.0, fiber=0.0, sugar=40.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=17.2, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

apple_pie_338 = create_food(
    food_name="Apple Pie - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=80.0, protein=0.0, carbs=10.0, fat=5.0, fiber=0.0, sugar=4.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=90.0, potassium=6.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

made_to_order_sandwiches_339 = create_food(
    food_name="Made to Order Sandwiches - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

white_italian_bread_340 = create_food(
    food_name="White Italian Bread - Each",
    serving_size="32g",
    brand="Generic",
    calories=80.0, protein=3.0, carbs=16.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=250.0, potassium=24.6, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

whole_wheat_hearty_bread_341 = create_food(
    food_name="100% Whole Wheat Hearty Bread - Slice",
    serving_size="49g",
    brand="Generic",
    calories=120.0, protein=4.0, carbs=24.0, fat=2.5, fiber=3.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=113.0, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

pretzel_roll_342 = create_food(
    food_name="Pretzel Roll - Each",
    serving_size="91g",
    brand="Generic",
    calories=250.0, protein=6.0, carbs=45.0, fat=4.5, fiber=2.0, sugar=4.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=260.0, potassium=68.5, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

roast_beef_343 = create_food(
    food_name="Roast Beef - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=45.0, protein=8.0, carbs=0.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=10.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheddar_cheese_344 = create_food(
    food_name="Cheddar Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=90.0, protein=5.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=140.0, potassium=22.4, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

provolone_cheese_345 = create_food(
    food_name="Provolone Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=80.0, protein=5.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=180.0, potassium=28.5, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

swiss_cheese_346 = create_food(
    food_name="Swiss Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=80.0, protein=6.0, carbs=1.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=45.0, potassium=28.1, vitamin_A=2.0, vitamin_C=0.0, calcium=15.0
)

cucumbers_347 = create_food(
    food_name="Cucumbers - Cup",
    serving_size="113g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=166.7, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

mayonnaise_348 = create_food(
    food_name="Mayonnaise - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=90.0, protein=0.0, carbs=0.0, fat=10.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=85.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dijon_mustard_349 = create_food(
    food_name="Dijon Mustard - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

mustard_350 = create_food(
    food_name="Mustard - Tablespoon",
    serving_size="17g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=200.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

black_olives_351 = create_food(
    food_name="Black Olives - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=45.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

red_onions_352 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

banana_peppers_353 = create_food(
    food_name="Banana Peppers - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

green_bell_peppers_354 = create_food(
    food_name="Green Bell Peppers - Cup",
    serving_size="193g",
    brand="Generic",
    calories=40.0, protein=2.0, carbs=9.0, fat=0.0, fiber=3.0, sugar=5.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=5.0, potassium=0.0, vitamin_A=15.0, vitamin_C=260.0, calcium=2.0
)

jalapenos_355 = create_food(
    food_name="Jalapenos - Tablespoon",
    serving_size="12g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=120.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dill_pickle_chips_356 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

ham_357 = create_food(
    food_name="Ham - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=35.0, protein=6.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

hard_salami_358 = create_food(
    food_name="Hard Salami - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=110.0, protein=5.0, carbs=0.0, fat=9.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=35.0, sodium=450.0, potassium=0.0, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

chipotle_aioli_359 = create_food(
    food_name="Chipotle Aioli - Tablespoon",
    serving_size="17g",
    brand="Generic",
    calories=110.0, protein=0.0, carbs=0.0, fat=12.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=90.0, potassium=0.6, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

spinach_360 = create_food(
    food_name="Spinach - Cup",
    serving_size="85g",
    brand="Generic",
    calories=20.0, protein=2.0, carbs=3.0, fat=0.0, fiber=2.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=473.4, vitamin_A=160.0, vitamin_C=40.0, calcium=8.0
)

tomatoes_361 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

turkey_breast_362 = create_food(
    food_name="Turkey Breast - Slice",
    serving_size="28g",
    brand="Generic",
    calories=25.0, protein=5.0, carbs=1.0, fat=1.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=78.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheddar_cheese_363 = create_food(
    food_name="Cheddar Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=90.0, protein=5.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=140.0, potassium=22.4, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

cucumbers_364 = create_food(
    food_name="Cucumbers - Cup",
    serving_size="113g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=166.7, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

mayonnaise_365 = create_food(
    food_name="Mayonnaise - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=90.0, protein=0.0, carbs=0.0, fat=10.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=85.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dijon_mustard_366 = create_food(
    food_name="Dijon Mustard - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

red_onions_367 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

banana_peppers_368 = create_food(
    food_name="Banana Peppers - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dill_pickle_chips_369 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

ham_370 = create_food(
    food_name="Ham - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=35.0, protein=6.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

tomatoes_371 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

turkey_breast_372 = create_food(
    food_name="Turkey Breast - Slice",
    serving_size="28g",
    brand="Generic",
    calories=25.0, protein=5.0, carbs=1.0, fat=1.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=78.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sesame_tofu_lo_mein_373 = create_food(
    food_name="Sesame Tofu Lo Mein - 8.5oz",
    serving_size="207g",
    brand="Generic",
    calories=300.0, protein=9.0, carbs=28.0, fat=18.0, fiber=4.0, sugar=5.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=710.0, potassium=177.4, vitamin_A=60.0, vitamin_C=80.0, calcium=10.0
)

shrimp_fried_rice_374 = create_food(
    food_name="Shrimp Fried Rice - 5oz",
    serving_size="134g",
    brand="Generic",
    calories=200.0, protein=8.0, carbs=19.0, fat=10.0, fiber=1.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=65.0, sodium=640.0, potassium=69.5, vitamin_A=15.0, vitamin_C=20.0, calcium=4.0
)

thai_sesame_vegetable_spring_roll_375 = create_food(
    food_name="Thai Sesame Vegetable Spring Roll - 3 Rolls",
    serving_size="85g",
    brand="Generic",
    calories=100.0, protein=3.0, carbs=20.0, fat=1.0, fiber=3.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=340.0, potassium=0.0, vitamin_A=20.0, vitamin_C=2.0, calcium=2.0
)

ginger_and_garlic_sauteed_snow_peas_376 = create_food(
    food_name="Ginger and Garlic Sauteed Snow Peas - 2oz",
    serving_size="53g",
    brand="Generic",
    calories=40.0, protein=2.0, carbs=5.0, fat=1.5, fiber=1.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=290.0, potassium=4.6, vitamin_A=10.0, vitamin_C=45.0, calcium=2.0
)

thai_sweet_chili_sauce_377 = create_food(
    food_name="Thai Sweet Chili Sauce - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=40.0, protein=0.0, carbs=10.0, fat=0.0, fiber=0.0, sugar=9.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=260.0, potassium=10.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

thai_sesame_grilled_chicken_378 = create_food(
    food_name="Thai Sesame Grilled Chicken - 3oz",
    serving_size="114g",
    brand="Generic",
    calories=190.0, protein=33.0, carbs=1.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=90.0, sodium=300.0, potassium=279.2, vitamin_A=4.0, vitamin_C=2.0, calcium=2.0
)

spicy_sesame_green_beans_379 = create_food(
    food_name="Spicy Sesame Green Beans - 4oz",
    serving_size="111g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=13.0, fat=2.5, fiber=3.0, sugar=7.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=840.0, potassium=215.0, vitamin_A=15.0, vitamin_C=20.0, calcium=4.0
)

thai_vegetable_dumpling_380 = create_food(
    food_name="Thai Vegetable Dumpling - 3 Potstickers",
    serving_size="85g",
    brand="Generic",
    calories=130.0, protein=4.0, carbs=28.0, fat=1.0, fiber=4.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=450.0, potassium=0.0, vitamin_A=20.0, vitamin_C=2.0, calcium=2.0
)

sesame_hawaiian_fried_rice_381 = create_food(
    food_name="Sesame Hawaiian Fried Rice - 4oz",
    serving_size="127g",
    brand="Generic",
    calories=150.0, protein=7.0, carbs=17.0, fat=6.0, fiber=1.0, sugar=3.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=60.0, sodium=380.0, potassium=74.2, vitamin_A=10.0, vitamin_C=40.0, calcium=2.0
)

potsticker_sesame_sauce_382 = create_food(
    food_name="Potsticker Sesame Sauce - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=3.0, fat=0.5, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=350.0, potassium=2.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

garlic_naan_383 = create_food(
    food_name="Garlic Naan - 2 Slices",
    serving_size="46g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=20.0, fat=5.0, fiber=0.0, sugar=1.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=330.0, potassium=0.8, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

moroccan_spiced_halal_chicken_384 = create_food(
    food_name="Moroccan Spiced Halal Chicken - 4oz",
    serving_size="115g",
    brand="Generic",
    calories=190.0, protein=18.0, carbs=0.0, fat=13.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=85.0, sodium=510.0, potassium=5.7, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

spicy_cauliflower_with_dill_385 = create_food(
    food_name="Spicy Cauliflower with Dill - 3oz",
    serving_size="89g",
    brand="Generic",
    calories=45.0, protein=2.0, carbs=5.0, fat=2.0, fiber=2.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=2.6, vitamin_A=2.0, vitamin_C=80.0, calcium=2.0
)

spinach_and_artichoke_couscous_386 = create_food(
    food_name="Spinach and Artichoke Couscous - 4oz",
    serving_size="119g",
    brand="Generic",
    calories=130.0, protein=5.0, carbs=21.0, fat=4.0, fiber=4.0, sugar=1.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=400.0, potassium=245.6, vitamin_A=30.0, vitamin_C=10.0, calcium=6.0
)

basmati_rice_387 = create_food(
    food_name="Basmati Rice - 4oz",
    serving_size="121g",
    brand="Generic",
    calories=160.0, protein=4.0, carbs=35.0, fat=0.5, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=47.3, vitamin_A=0.0, vitamin_C=50.0, calcium=2.0
)

garlic_yogurt_sauce_388 = create_food(
    food_name="Garlic Yogurt Sauce - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=10.0, protein=1.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=50.0, potassium=14.6, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

naan_bread_389 = create_food(
    food_name="Naan Bread - Each",
    serving_size="43g",
    brand="Generic",
    calories=120.0, protein=4.0, carbs=20.0, fat=3.0, fiber=0.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=320.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

halal_chicken_butter_sauce_390 = create_food(
    food_name="Halal Chicken Butter Sauce - 7 oz. Serving",
    serving_size="217g",
    brand="Generic",
    calories=320.0, protein=23.0, carbs=6.0, fat=23.0, fiber=0.0, sugar=2.0,
    saturated_fat=9.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=140.0, sodium=470.0, potassium=52.2, vitamin_A=8.0, vitamin_C=8.0, calcium=6.0
)

tofu_vindaloo_391 = create_food(
    food_name="Tofu Vindaloo - 6oz",
    serving_size="169g",
    brand="Generic",
    calories=110.0, protein=5.0, carbs=11.0, fat=5.0, fiber=4.0, sugar=6.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=110.0, potassium=101.1, vitamin_A=10.0, vitamin_C=110.0, calcium=10.0
)

basmati_rice_392 = create_food(
    food_name="Basmati Rice - 4oz",
    serving_size="121g",
    brand="Generic",
    calories=160.0, protein=4.0, carbs=35.0, fat=0.5, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=47.3, vitamin_A=0.0, vitamin_C=50.0, calcium=2.0
)

roasted_zucchini_blend_393 = create_food(
    food_name="Roasted Zucchini Blend - 3oz",
    serving_size="85g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=5.0, fat=11.0, fiber=1.0, sugar=2.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=115.0, potassium=6.7, vitamin_A=2.0, vitamin_C=20.0, calcium=4.0
)

feta_cheese_394 = create_food(
    food_name="Feta Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=20.0, protein=1.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=75.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

iceberg_lettuce_395 = create_food(
    food_name="Iceberg Lettuce - Cup",
    serving_size="80g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=8.0, vitamin_C=4.0, calcium=0.0
)

red_onions_396 = create_food(
    food_name="Red Onions - Cup",
    serving_size="125g",
    brand="Generic",
    calories=50.0, protein=1.0, carbs=11.0, fat=0.0, fiber=2.0, sugar=5.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=15.0, calcium=2.0
)

tzatziki_397 = create_food(
    food_name="Tzatziki - Quart",
    serving_size="933g",
    brand="Generic",
    calories=580.0, protein=74.0, carbs=47.0, fat=9.0, fiber=3.0, sugar=29.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=2090.0, potassium=857.4, vitamin_A=6.0, vitamin_C=25.0, calcium=100.0
)

tomatoes_398 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

scrambled_eggs_399 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

buttermilk_pancakes_400 = create_food(
    food_name="Buttermilk Pancakes - Each",
    serving_size="55g",
    brand="Generic",
    calories=110.0, protein=2.0, carbs=20.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=320.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

tofu_scramble_401 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_402 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

seasoned_diced_potatoes_403 = create_food(
    food_name="Seasoned Diced Potatoes - 3.5oz",
    serving_size="109g",
    brand="Generic",
    calories=170.0, protein=3.0, carbs=22.0, fat=8.0, fiber=3.0, sugar=1.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=430.0, potassium=311.3, vitamin_A=0.0, vitamin_C=20.0, calcium=0.0
)

sausage_patties_404 = create_food(
    food_name="Sausage Patties - Each",
    serving_size="57g",
    brand="Generic",
    calories=210.0, protein=7.0, carbs=0.0, fat=21.0, fiber=0.0, sugar=0.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=45.0, sodium=380.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties_405 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_406 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_407 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_408 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

scrambled_eggs_409 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

buttermilk_pancakes_410 = create_food(
    food_name="Buttermilk Pancakes - Each",
    serving_size="55g",
    brand="Generic",
    calories=110.0, protein=2.0, carbs=20.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=320.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

tofu_scramble_411 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_412 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

seasoned_diced_potatoes_413 = create_food(
    food_name="Seasoned Diced Potatoes - 3.5oz",
    serving_size="109g",
    brand="Generic",
    calories=170.0, protein=3.0, carbs=22.0, fat=8.0, fiber=3.0, sugar=1.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=430.0, potassium=311.3, vitamin_A=0.0, vitamin_C=20.0, calcium=0.0
)

sausage_patties_414 = create_food(
    food_name="Sausage Patties - Each",
    serving_size="57g",
    brand="Generic",
    calories=210.0, protein=7.0, carbs=0.0, fat=21.0, fiber=0.0, sugar=0.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=45.0, sodium=380.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties_415 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_416 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_417 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_418 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

captain_crunch_french_toast_419 = create_food(
    food_name="Captain Crunch French Toast - Each",
    serving_size="92g",
    brand="Generic",
    calories=270.0, protein=6.0, carbs=36.0, fat=11.0, fiber=0.0, sugar=21.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=140.0, sodium=270.0, potassium=66.1, vitamin_A=4.0, vitamin_C=0.0, calcium=4.0
)

bacon_420 = create_food(
    food_name="Bacon - 2 Slices",
    serving_size="18g",
    brand="Generic",
    calories=90.0, protein=6.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=250.0, potassium=101.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

seasoned_diced_potatoes_421 = create_food(
    food_name="Seasoned Diced Potatoes - 3.5oz",
    serving_size="109g",
    brand="Generic",
    calories=170.0, protein=3.0, carbs=22.0, fat=8.0, fiber=3.0, sugar=1.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=430.0, potassium=311.3, vitamin_A=0.0, vitamin_C=20.0, calcium=0.0
)

cherry_sauce_422 = create_food(
    food_name="Cherry Sauce - Cup",
    serving_size="212g",
    brand="Generic",
    calories=190.0, protein=1.0, carbs=48.0, fat=0.0, fiber=3.0, sugar=40.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=3.6, vitamin_A=10.0, vitamin_C=6.0, calcium=2.0
)

apple_topping_423 = create_food(
    food_name="Apple Topping - Ounce",
    serving_size="32g",
    brand="Generic",
    calories=40.0, protein=0.0, carbs=7.0, fat=1.5, fiber=0.0, sugar=6.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=20.7, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

buttermilk_biscuits_424 = create_food(
    food_name="Buttermilk Biscuits - Each",
    serving_size="72g",
    brand="Generic",
    calories=300.0, protein=5.0, carbs=27.0, fat=19.0, fiber=0.0, sugar=2.0,
    saturated_fat=10.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=600.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

honey_butter_425 = create_food(
    food_name="Honey Butter - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=2.0, fat=10.0, fiber=0.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=8.0, vitamin_C=0.0, calcium=0.0
)

steamed_corn_426 = create_food(
    food_name="Steamed Corn - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=110.0, protein=3.0, carbs=23.0, fat=1.0, fiber=3.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=4.0, vitamin_C=0.0, calcium=0.0
)

yukon_mashed_potatoes_427 = create_food(
    food_name="Yukon Mashed Potatoes - 4oz",
    serving_size="101g",
    brand="Generic",
    calories=170.0, protein=3.0, carbs=17.0, fat=10.0, fiber=2.0, sugar=1.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=160.0, potassium=29.1, vitamin_A=10.0, vitamin_C=15.0, calcium=4.0
)

shredded_mild_cheddar_cheese_428 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

tempura_chicken_429 = create_food(
    food_name="Tempura Chicken - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=60.0, protein=5.0, carbs=5.0, fat=2.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=150.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chicken_gravy_430 = create_food(
    food_name="Chicken Gravy - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=0.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=30.0, potassium=0.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

smoked_bbq_chicken_431 = create_food(
    food_name="Smoked BBQ Chicken - 5oz",
    serving_size="142g",
    brand="Generic",
    calories=320.0, protein=23.0, carbs=3.0, fat=23.0, fiber=0.0, sugar=3.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=80.0, sodium=110.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

steamed_green_beans_432 = create_food(
    food_name="Steamed Green Beans - 3oz",
    serving_size="86g",
    brand="Generic",
    calories=35.0, protein=1.0, carbs=6.0, fat=1.5, fiber=2.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=5.0, potassium=179.5, vitamin_A=10.0, vitamin_C=15.0, calcium=2.0
)

sweet_potato_casserole_with_pecans_433 = create_food(
    food_name="Sweet Potato Casserole with Pecans - 8oz",
    serving_size="270g",
    brand="Generic",
    calories=550.0, protein=5.0, carbs=90.0, fat=20.0, fiber=10.0, sugar=26.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=230.0, potassium=1633.5, vitamin_A=10.0, vitamin_C=60.0, calcium=6.0
)

tennessee_bbq_sauce_434 = create_food(
    food_name="Tennessee BBQ Sauce - Tablespoon",
    serving_size="16g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=0.0, vitamin_A=2.0, vitamin_C=2.0, calcium=0.0
)

honey_butter_435 = create_food(
    food_name="Honey Butter - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=2.0, fat=10.0, fiber=0.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=8.0, vitamin_C=0.0, calcium=0.0
)

shredded_mild_cheddar_cheese_436 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

cheese_pizza_437 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

cheeseburger_pizza_438 = create_food(
    food_name="Cheeseburger Pizza - Slice",
    serving_size="80g",
    brand="Generic",
    calories=170.0, protein=9.0, carbs=19.0, fat=7.0, fiber=1.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=340.0, potassium=103.3, vitamin_A=2.0, vitamin_C=2.0, calcium=10.0
)

halal_pepperoni_pizza_439 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

cheese_pizza_440 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

cheeseburger_pizza_441 = create_food(
    food_name="Cheeseburger Pizza - Slice",
    serving_size="80g",
    brand="Generic",
    calories=170.0, protein=9.0, carbs=19.0, fat=7.0, fiber=1.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=340.0, potassium=103.3, vitamin_A=2.0, vitamin_C=2.0, calcium=10.0
)

halal_pepperoni_pizza_442 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

pepper_jack_crab_soup_443 = create_food(
    food_name="Pepper Jack Crab Soup - 4oz",
    serving_size="120g",
    brand="Generic",
    calories=240.0, protein=8.0, carbs=7.0, fat=21.0, fiber=0.0, sugar=0.0,
    saturated_fat=11.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=60.0, sodium=270.0, potassium=46.5, vitamin_A=10.0, vitamin_C=10.0, calcium=20.0
)

coconut_curry_lentil_soup_444 = create_food(
    food_name="Coconut Curry Lentil Soup - 6oz",
    serving_size="221g",
    brand="Generic",
    calories=240.0, protein=15.0, carbs=39.0, fat=3.5, fiber=7.0, sugar=2.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=160.0, potassium=484.7, vitamin_A=2.0, vitamin_C=10.0, calcium=2.0
)

chocolate_chip_cookie_445 = create_food(
    food_name="Chocolate Chip Cookie - Each",
    serving_size="29g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=17.0, fat=6.0, fiber=0.0, sugar=10.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=160.0, potassium=37.8, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

sugar_cookie_446 = create_food(
    food_name="Sugar Cookie - Each",
    serving_size="28g",
    brand="Generic",
    calories=130.0, protein=1.0, carbs=16.0, fat=6.0, fiber=0.0, sugar=8.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=125.0, potassium=3.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

french_toast_crunch_bars_447 = create_food(
    food_name="French Toast Crunch Bars - 3 oz",
    serving_size="64g",
    brand="Generic",
    calories=260.0, protein=2.0, carbs=48.0, fat=7.0, fiber=2.0, sugar=27.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=15.0, vitamin_C=10.0, calcium=10.0
)

mint_brownie_448 = create_food(
    food_name="Mint Brownie - Ounce",
    serving_size="39g",
    brand="Generic",
    calories=160.0, protein=1.0, carbs=24.0, fat=6.0, fiber=0.0, sugar=18.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=115.0, potassium=7.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

vegan_chocolate_cake_449 = create_food(
    food_name="Vegan Chocolate Cake - 2 oz",
    serving_size="67g",
    brand="Generic",
    calories=200.0, protein=2.0, carbs=38.0, fat=5.0, fiber=1.0, sugar=15.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

creamsicle_sheet_cake_450 = create_food(
    food_name="Creamsicle Sheet Cake - 3 oz",
    serving_size="76g",
    brand="Generic",
    calories=180.0, protein=2.0, carbs=26.0, fat=8.0, fiber=0.0, sugar=7.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

pink_lemonade_cake_451 = create_food(
    food_name="Pink Lemonade Cake - 3 oz",
    serving_size="118g",
    brand="Generic",
    calories=460.0, protein=1.0, carbs=57.0, fat=25.0, fiber=0.0, sugar=35.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=300.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

up_pound_cake_452 = create_food(
    food_name="7 Up Pound Cake - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=110.0, protein=1.0, carbs=16.0, fat=4.5, fiber=0.0, sugar=10.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=10.0, potassium=4.7, vitamin_A=4.0, vitamin_C=0.0, calcium=0.0
)

cheesecake_with_fruit_453 = create_food(
    food_name="Cheesecake with Fruit - Ounce",
    serving_size="18g",
    brand="Generic",
    calories=60.0, protein=0.0, carbs=6.0, fat=3.5, fiber=0.0, sugar=3.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=55.0, potassium=5.7, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_cheesecake_454 = create_food(
    food_name="Sour Cream Cheesecake - Ounce",
    serving_size="29g",
    brand="Generic",
    calories=100.0, protein=1.0, carbs=10.0, fat=6.0, fiber=0.0, sugar=5.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=90.0, potassium=9.3, vitamin_A=4.0, vitamin_C=0.0, calcium=2.0
)

vegan_vanilla_cupcake_455 = create_food(
    food_name="Vegan Vanilla Cupcake - Each",
    serving_size="90g",
    brand="Generic",
    calories=320.0, protein=1.0, carbs=54.0, fat=11.0, fiber=0.0, sugar=40.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=17.2, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

apple_pie_456 = create_food(
    food_name="Apple Pie - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=80.0, protein=0.0, carbs=10.0, fat=5.0, fiber=0.0, sugar=4.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=90.0, potassium=6.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

made_to_order_sandwiches_457 = create_food(
    food_name="Made to Order Sandwiches - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheddar_cheese_458 = create_food(
    food_name="Cheddar Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=90.0, protein=5.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=140.0, potassium=22.4, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

cucumbers_459 = create_food(
    food_name="Cucumbers - Cup",
    serving_size="113g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=166.7, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

mayonnaise_460 = create_food(
    food_name="Mayonnaise - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=90.0, protein=0.0, carbs=0.0, fat=10.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=85.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dijon_mustard_461 = create_food(
    food_name="Dijon Mustard - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

red_onions_462 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

banana_peppers_463 = create_food(
    food_name="Banana Peppers - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dill_pickle_chips_464 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

ham_465 = create_food(
    food_name="Ham - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=35.0, protein=6.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

tomatoes_466 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

turkey_breast_467 = create_food(
    food_name="Turkey Breast - Slice",
    serving_size="28g",
    brand="Generic",
    calories=25.0, protein=5.0, carbs=1.0, fat=1.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=78.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheddar_cheese_468 = create_food(
    food_name="Cheddar Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=90.0, protein=5.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=140.0, potassium=22.4, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

cucumbers_469 = create_food(
    food_name="Cucumbers - Cup",
    serving_size="113g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=166.7, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

mayonnaise_470 = create_food(
    food_name="Mayonnaise - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=90.0, protein=0.0, carbs=0.0, fat=10.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=85.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dijon_mustard_471 = create_food(
    food_name="Dijon Mustard - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

red_onions_472 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

banana_peppers_473 = create_food(
    food_name="Banana Peppers - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dill_pickle_chips_474 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

ham_475 = create_food(
    food_name="Ham - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=35.0, protein=6.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

tomatoes_476 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

turkey_breast_477 = create_food(
    food_name="Turkey Breast - Slice",
    serving_size="28g",
    brand="Generic",
    calories=25.0, protein=5.0, carbs=1.0, fat=1.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=78.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

garlic_texas_toast_478 = create_food(
    food_name="Garlic Texas Toast - Slice",
    serving_size="74g",
    brand="Generic",
    calories=290.0, protein=7.0, carbs=20.0, fat=20.0, fiber=1.0, sugar=2.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=350.0, potassium=40.2, vitamin_A=15.0, vitamin_C=2.0, calcium=15.0
)

broccoli_and_zucchini_parmesan_479 = create_food(
    food_name="Broccoli and Zucchini Parmesan - 4oz",
    serving_size="120g",
    brand="Generic",
    calories=120.0, protein=4.0, carbs=7.0, fat=9.0, fiber=2.0, sugar=3.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=260.0, potassium=2.1, vitamin_A=25.0, vitamin_C=150.0, calcium=10.0
)

cavatappi_pasta_480 = create_food(
    food_name="Cavatappi Pasta - 4oz",
    serving_size="113g",
    brand="Generic",
    calories=170.0, protein=6.0, carbs=33.0, fat=1.0, fiber=2.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

pesto_and_mushroom_tortellini_alfredo_481 = create_food(
    food_name="Pesto and Mushroom Tortellini Alfredo - 7oz",
    serving_size="193g",
    brand="Generic",
    calories=320.0, protein=13.0, carbs=34.0, fat=14.0, fiber=2.0, sugar=3.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=490.0, potassium=147.3, vitamin_A=30.0, vitamin_C=15.0, calcium=25.0
)

grated_parmesan_cheese_482 = create_food(
    food_name="Grated Parmesan Cheese - Tablespoon",
    serving_size="5g",
    brand="Generic",
    calories=20.0, protein=2.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=75.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

diced_roasted_chicken_483 = create_food(
    food_name="Diced Roasted Chicken - Ounce",
    serving_size="29g",
    brand="Generic",
    calories=45.0, protein=5.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

alfredo_sauce_484 = create_food(
    food_name="Alfredo Sauce - Cup",
    serving_size="236g",
    brand="Generic",
    calories=340.0, protein=11.0, carbs=20.0, fat=24.0, fiber=0.0, sugar=7.0,
    saturated_fat=12.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=60.0, sodium=740.0, potassium=233.2, vitamin_A=10.0, vitamin_C=25.0, calcium=35.0
)

italian_tomato_sauce_485 = create_food(
    food_name="Italian Tomato Sauce - Cup",
    serving_size="225g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=19.0, fat=5.0, fiber=4.0, sugar=13.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=160.0, potassium=382.6, vitamin_A=0.0, vitamin_C=190.0, calcium=0.0
)

fried_eggs_486 = create_food(
    food_name="Fried Eggs - 2 Eggs",
    serving_size="118g",
    brand="Generic",
    calories=220.0, protein=15.0, carbs=1.0, fat=17.0, fiber=0.0, sugar=1.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=425.0, sodium=140.0, potassium=0.0, vitamin_A=10.0, vitamin_C=0.0, calcium=6.0
)

kimchi_487 = create_food(
    food_name="Kimchi - 3oz",
    serving_size="86g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=9.0, fat=0.0, fiber=3.0, sugar=6.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=830.0, potassium=143.9, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

seasoned_rice_488 = create_food(
    food_name="Seasoned Rice - 3oz",
    serving_size="75g",
    brand="Generic",
    calories=200.0, protein=4.0, carbs=44.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=55.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

vegetables_for_bibimbap_489 = create_food(
    food_name="Vegetables for Bibimbap - 2oz",
    serving_size="57g",
    brand="Generic",
    calories=25.0, protein=1.0, carbs=4.0, fat=1.5, fiber=1.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=30.0, potassium=165.7, vitamin_A=70.0, vitamin_C=15.0, calcium=2.0
)

bibimbap_beef_w_sesame_490 = create_food(
    food_name="Bibimbap Beef w/ Sesame - 3.5oz",
    serving_size="101g",
    brand="Generic",
    calories=170.0, protein=21.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=140.0, potassium=1.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

green_onions_491 = create_food(
    food_name="Green Onions - Cup",
    serving_size="85g",
    brand="Generic",
    calories=25.0, protein=2.0, carbs=6.0, fat=0.0, fiber=3.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=15.0, potassium=232.2, vitamin_A=15.0, vitamin_C=25.0, calcium=6.0
)

gochujang_sesame_sauce_for_bibimbap_492 = create_food(
    food_name="Gochujang Sesame Sauce for Bibimbap - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=45.0, protein=0.0, carbs=6.0, fat=2.0, fiber=0.0, sugar=4.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=250.0, potassium=54.4, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

marinated_tofu_493 = create_food(
    food_name="Marinated Tofu - 4oz",
    serving_size="119g",
    brand="Generic",
    calories=120.0, protein=10.0, carbs=6.0, fat=7.0, fiber=2.0, sugar=3.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=1640.0, potassium=124.1, vitamin_A=0.0, vitamin_C=0.0, calcium=15.0
)

baked_old_bay_fish_494 = create_food(
    food_name="Baked Old Bay Fish - Each",
    serving_size="144g",
    brand="Generic",
    calories=120.0, protein=25.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=50.0, sodium=330.0, potassium=0.0, vitamin_A=2.0, vitamin_C=6.0, calcium=2.0
)

stuffed_portabella_cap_495 = create_food(
    food_name="Stuffed Portabella Cap - Each",
    serving_size="169g",
    brand="Generic",
    calories=130.0, protein=5.0, carbs=19.0, fat=4.5, fiber=3.0, sugar=4.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=190.0, potassium=380.2, vitamin_A=8.0, vitamin_C=45.0, calcium=2.0
)

spinach_quiche_496 = create_food(
    food_name="Spinach Quiche - 4.5oz",
    serving_size="126g",
    brand="Generic",
    calories=310.0, protein=13.0, carbs=17.0, fat=21.0, fiber=1.0, sugar=2.0,
    saturated_fat=9.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=190.0, sodium=420.0, potassium=80.7, vitamin_A=20.0, vitamin_C=8.0, calcium=20.0
)

steamed_broccoli_florets_497 = create_food(
    food_name="Steamed Broccoli Florets - 3oz",
    serving_size="85g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=6.0, fat=0.0, fiber=2.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=30.0, potassium=0.0, vitamin_A=10.0, vitamin_C=130.0, calcium=4.0
)

old_bay_roasted_potatoes_and_onions_498 = create_food(
    food_name="Old Bay Roasted Potatoes and Onions - 4oz",
    serving_size="115g",
    brand="Generic",
    calories=130.0, protein=3.0, carbs=22.0, fat=3.0, fiber=2.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=12.6, vitamin_A=4.0, vitamin_C=25.0, calcium=2.0
)

tartar_sauce_499 = create_food(
    food_name="Tartar Sauce - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=50.0, protein=0.0, carbs=2.0, fat=5.0, fiber=0.0, sugar=2.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=110.0, potassium=0.2, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chipotle_glazed_fresh_fish_500 = create_food(
    food_name="Chipotle Glazed Fresh Fish - Each",
    serving_size="178g",
    brand="Generic",
    calories=240.0, protein=20.0, carbs=26.0, fat=7.0, fiber=0.0, sugar=23.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=430.0, potassium=56.9, vitamin_A=6.0, vitamin_C=20.0, calcium=2.0
)

citrus_glazed_tofu_501 = create_food(
    food_name="Citrus Glazed Tofu - 8.5oz",
    serving_size="240g",
    brand="Generic",
    calories=300.0, protein=14.0, carbs=44.0, fat=9.0, fiber=4.0, sugar=36.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=60.0, potassium=256.4, vitamin_A=0.0, vitamin_C=15.0, calcium=30.0
)

steamed_broccoli_502 = create_food(
    food_name="Steamed Broccoli - 3oz",
    serving_size="91g",
    brand="Generic",
    calories=35.0, protein=2.0, carbs=6.0, fat=0.0, fiber=2.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=30.0, potassium=288.6, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

spicy_roasted_sweet_potatoes_503 = create_food(
    food_name="Spicy Roasted Sweet Potatoes - 3oz",
    serving_size="116g",
    brand="Generic",
    calories=150.0, protein=2.0, carbs=32.0, fat=1.5, fiber=5.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=925.3, vitamin_A=4.0, vitamin_C=30.0, calcium=2.0
)

woodys_tabbouleh_salad_504 = create_food(
    food_name="Woody's Tabbouleh Salad - Cup",
    serving_size="57g",
    brand="Generic",
    calories=60.0, protein=1.0, carbs=4.0, fat=4.0, fiber=1.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=25.0, potassium=0.0, vitamin_A=30.0, vitamin_C=35.0, calcium=6.0
)

woodys_original_hummus_505 = create_food(
    food_name="Woody's Original Hummus - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=40.0, protein=1.0, carbs=2.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=70.0, potassium=37.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

country_scramble_506 = create_food(
    food_name="Country Scramble - 4oz",
    serving_size="108g",
    brand="Generic",
    calories=250.0, protein=12.0, carbs=6.0, fat=20.0, fiber=0.0, sugar=0.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=195.0, sodium=240.0, potassium=55.5, vitamin_A=15.0, vitamin_C=25.0, calcium=15.0
)

scrambled_eggs_507 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

tofu_scramble_508 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_509 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

hash_brown_patty_510 = create_food(
    food_name="Hash Brown Patty - Each",
    serving_size="54g",
    brand="Generic",
    calories=90.0, protein=2.0, carbs=11.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=2.0
)

veggie_sausage_patties_511 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_512 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_513 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chicken_sausage_link_514 = create_food(
    food_name="Chicken Sausage Link - Each",
    serving_size="40g",
    brand="Generic",
    calories=80.0, protein=6.0, carbs=2.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=35.0, sodium=240.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_515 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

tropical_smoothie_516 = create_food(
    food_name="Tropical Smoothie - Cup",
    serving_size="201g",
    brand="Generic",
    calories=130.0, protein=2.0, carbs=30.0, fat=0.0, fiber=1.0, sugar=24.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=25.0, potassium=69.2, vitamin_A=10.0, vitamin_C=110.0, calcium=8.0
)

country_scramble_517 = create_food(
    food_name="Country Scramble - 4oz",
    serving_size="108g",
    brand="Generic",
    calories=250.0, protein=12.0, carbs=6.0, fat=20.0, fiber=0.0, sugar=0.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=195.0, sodium=240.0, potassium=55.5, vitamin_A=15.0, vitamin_C=25.0, calcium=15.0
)

scrambled_eggs_518 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

tofu_scramble_519 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_520 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

hash_brown_patty_521 = create_food(
    food_name="Hash Brown Patty - Each",
    serving_size="54g",
    brand="Generic",
    calories=90.0, protein=2.0, carbs=11.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=2.0
)

veggie_sausage_patties_522 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_523 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_524 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chicken_sausage_link_525 = create_food(
    food_name="Chicken Sausage Link - Each",
    serving_size="40g",
    brand="Generic",
    calories=80.0, protein=6.0, carbs=2.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=35.0, sodium=240.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_526 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

beef_hot_dog_with_bun_527 = create_food(
    food_name="Beef Hot Dog with Bun - Each",
    serving_size="99g",
    brand="Generic",
    calories=240.0, protein=15.0, carbs=18.0, fat=13.0, fiber=0.0, sugar=2.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=610.0, potassium=190.6, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

corn_dog_528 = create_food(
    food_name="Corn Dog - Each",
    serving_size="113g",
    brand="Generic",
    calories=320.0, protein=9.0, carbs=28.0, fat=19.0, fiber=0.0, sugar=9.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=670.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cajun_fries_529 = create_food(
    food_name="Cajun Fries - 3oz",
    serving_size="86g",
    brand="Generic",
    calories=130.0, protein=1.0, carbs=20.0, fat=5.0, fiber=1.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=420.0, potassium=232.9, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

beanless_chili_530 = create_food(
    food_name="Beanless Chili - Cup",
    serving_size="236g",
    brand="Generic",
    calories=320.0, protein=16.0, carbs=33.0, fat=19.0, fiber=9.0, sugar=3.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=35.0, sodium=1170.0, potassium=0.0, vitamin_A=15.0, vitamin_C=0.0, calcium=8.0
)

vegan_hot_dog_531 = create_food(
    food_name="Vegan Hot Dog - Each",
    serving_size="82g",
    brand="Generic",
    calories=110.0, protein=7.0, carbs=6.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=600.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

onion_532 = create_food(
    food_name="Onion - Cup",
    serving_size="160g",
    brand="Generic",
    calories=60.0, protein=2.0, carbs=15.0, fat=0.0, fiber=3.0, sugar=7.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=5.0, potassium=273.6, vitamin_A=0.0, vitamin_C=20.0, calcium=4.0
)

dill_relish_533 = create_food(
    food_name="Dill Relish - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=4.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=140.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheese_sauce_534 = create_food(
    food_name="Cheese Sauce - Cup",
    serving_size="255g",
    brand="Generic",
    calories=320.0, protein=4.0, carbs=24.0, fat=24.0, fiber=0.0, sugar=0.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=1820.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=15.0
)

al_pastor_pork_tacos_535 = create_food(
    food_name="Al Pastor Pork Tacos - Each",
    serving_size="78g",
    brand="Generic",
    calories=200.0, protein=10.0, carbs=16.0, fat=10.0, fiber=0.0, sugar=1.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=330.0, potassium=2.5, vitamin_A=0.0, vitamin_C=6.0, calcium=4.0
)

cilantro_lime_rice_536 = create_food(
    food_name="Cilantro Lime Rice - 4oz",
    serving_size="99g",
    brand="Generic",
    calories=150.0, protein=3.0, carbs=35.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=35.0, potassium=49.3, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

refried_beans_537 = create_food(
    food_name="Refried Beans - 3oz",
    serving_size="83g",
    brand="Generic",
    calories=70.0, protein=4.0, carbs=12.0, fat=0.5, fiber=4.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=260.0, potassium=190.1, vitamin_A=2.0, vitamin_C=8.0, calcium=15.0
)

tortilla_chips_538 = create_food(
    food_name="Tortilla Chips - 15 Chips",
    serving_size="41g",
    brand="Generic",
    calories=200.0, protein=3.0, carbs=27.0, fat=9.0, fiber=3.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=90.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

fire_roasted_tomato_salsa_539 = create_food(
    food_name="Fire Roasted Tomato Salsa - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=50.0, potassium=2.1, vitamin_A=0.0, vitamin_C=4.0, calcium=0.0
)

msu_bakers_dinner_roll_540 = create_food(
    food_name="MSU Bakers Dinner Roll - Each",
    serving_size="43g",
    brand="MSU",
    calories=110.0, protein=3.0, carbs=20.0, fat=2.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=190.0, potassium=0.0, vitamin_A=0.0, vitamin_C=8.0, calcium=2.0
)

country_fried_steak_541 = create_food(
    food_name="Country Fried Steak - Each",
    serving_size="135g",
    brand="Generic",
    calories=450.0, protein=17.0, carbs=59.0, fat=18.0, fiber=3.0, sugar=5.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=1040.0, potassium=0.0, vitamin_A=10.0, vitamin_C=6.0, calcium=15.0
)

steamed_green_beans_542 = create_food(
    food_name="Steamed Green Beans - 3oz",
    serving_size="86g",
    brand="Generic",
    calories=35.0, protein=1.0, carbs=6.0, fat=1.5, fiber=2.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=5.0, potassium=179.5, vitamin_A=10.0, vitamin_C=15.0, calcium=2.0
)

yukon_mashed_potatoes_543 = create_food(
    food_name="Yukon Mashed Potatoes - 4oz",
    serving_size="101g",
    brand="Generic",
    calories=170.0, protein=3.0, carbs=17.0, fat=10.0, fiber=2.0, sugar=1.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=160.0, potassium=29.1, vitamin_A=10.0, vitamin_C=15.0, calcium=4.0
)

honey_butter_544 = create_food(
    food_name="Honey Butter - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=2.0, fat=10.0, fiber=0.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=8.0, vitamin_C=0.0, calcium=0.0
)

country_gravy_545 = create_food(
    food_name="Country Gravy - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=1.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=35.0, potassium=20.0, vitamin_A=0.0, vitamin_C=2.0, calcium=2.0
)

queso_fresco_crumbles_546 = create_food(
    food_name="Queso Fresco Crumbles - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=25.0, protein=1.0, carbs=0.0, fat=2.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=50.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

pickled_red_onions_547 = create_food(
    food_name="Pickled Red Onions - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=4.0, calcium=0.0
)

fire_roasted_tomato_salsa_548 = create_food(
    food_name="Fire Roasted Tomato Salsa - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=50.0, potassium=2.1, vitamin_A=0.0, vitamin_C=4.0, calcium=0.0
)

salsa_verde_549 = create_food(
    food_name="Salsa Verde - Gallon",
    serving_size="4551g",
    brand="Generic",
    calories=1760.0, protein=82.0, carbs=354.0, fat=72.0, fiber=81.0, sugar=154.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=135.0, potassium=6319.5, vitamin_A=170.0, vitamin_C=520.0, calcium=60.0
)

cheese_pizza_550 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

hawaiian_pizza_551 = create_food(
    food_name="Hawaiian Pizza - Slice",
    serving_size="69g",
    brand="Generic",
    calories=150.0, protein=8.0, carbs=19.0, fat=5.0, fiber=1.0, sugar=3.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=450.0, potassium=54.0, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

halal_pepperoni_pizza_552 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

cheese_pizza_553 = create_food(
    food_name="Cheese Pizza - Slice",
    serving_size="83g",
    brand="Generic",
    calories=210.0, protein=9.0, carbs=30.0, fat=7.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=490.0, potassium=83.1, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

hawaiian_pizza_554 = create_food(
    food_name="Hawaiian Pizza - Slice",
    serving_size="69g",
    brand="Generic",
    calories=150.0, protein=8.0, carbs=19.0, fat=5.0, fiber=1.0, sugar=3.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=450.0, potassium=54.0, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

halal_pepperoni_pizza_555 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

grilled_vegetable_chili_556 = create_food(
    food_name="Grilled Vegetable Chili - 4oz",
    serving_size="128g",
    brand="Generic",
    calories=120.0, protein=3.0, carbs=12.0, fat=7.0, fiber=3.0, sugar=3.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=260.0, potassium=200.7, vitamin_A=6.0, vitamin_C=45.0, calcium=2.0
)

tomato_tortellini_soup_557 = create_food(
    food_name="Tomato Tortellini Soup - 4oz",
    serving_size="123g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=16.0, fat=6.0, fiber=1.0, sugar=5.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=420.0, potassium=114.8, vitamin_A=8.0, vitamin_C=10.0, calcium=4.0
)

chocolate_chip_cookie_558 = create_food(
    food_name="Chocolate Chip Cookie - Each",
    serving_size="29g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=17.0, fat=6.0, fiber=0.0, sugar=10.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=160.0, potassium=37.8, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

special_event_iced_cookie_559 = create_food(
    food_name="Special Event Iced Cookie - Each",
    serving_size="58g",
    brand="Generic",
    calories=240.0, protein=4.0, carbs=32.0, fat=11.0, fiber=0.0, sugar=12.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=170.0, potassium=10.0, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

french_toast_crunch_bars_560 = create_food(
    food_name="French Toast Crunch Bars - 3 oz",
    serving_size="64g",
    brand="Generic",
    calories=260.0, protein=2.0, carbs=48.0, fat=7.0, fiber=2.0, sugar=27.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=15.0, vitamin_C=10.0, calcium=10.0
)

vegan_chocolate_cake_561 = create_food(
    food_name="Vegan Chocolate Cake - 2 oz",
    serving_size="67g",
    brand="Generic",
    calories=200.0, protein=2.0, carbs=38.0, fat=5.0, fiber=1.0, sugar=15.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

creamsicle_sheet_cake_562 = create_food(
    food_name="Creamsicle Sheet Cake - 3 oz",
    serving_size="76g",
    brand="Generic",
    calories=180.0, protein=2.0, carbs=26.0, fat=8.0, fiber=0.0, sugar=7.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

pink_lemonade_cake_563 = create_food(
    food_name="Pink Lemonade Cake - 3 oz",
    serving_size="118g",
    brand="Generic",
    calories=460.0, protein=1.0, carbs=57.0, fat=25.0, fiber=0.0, sugar=35.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=300.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

up_pound_cake_564 = create_food(
    food_name="7 Up Pound Cake - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=110.0, protein=1.0, carbs=16.0, fat=4.5, fiber=0.0, sugar=10.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=10.0, potassium=4.7, vitamin_A=4.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_cheesecake_565 = create_food(
    food_name="Sour Cream Cheesecake - Ounce",
    serving_size="29g",
    brand="Generic",
    calories=100.0, protein=1.0, carbs=10.0, fat=6.0, fiber=0.0, sugar=5.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=90.0, potassium=9.3, vitamin_A=4.0, vitamin_C=0.0, calcium=2.0
)

tropical_cheese_pie_566 = create_food(
    food_name="Tropical Cheese Pie - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=100.0, protein=1.0, carbs=12.0, fat=6.0, fiber=0.0, sugar=7.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=70.0, potassium=7.5, vitamin_A=4.0, vitamin_C=0.0, calcium=0.0
)

vegan_vanilla_cupcake_567 = create_food(
    food_name="Vegan Vanilla Cupcake - Each",
    serving_size="90g",
    brand="Generic",
    calories=320.0, protein=1.0, carbs=54.0, fat=11.0, fiber=0.0, sugar=40.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=17.2, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

special_event_iced_cupcake_568 = create_food(
    food_name="Special Event Iced Cupcake - Each",
    serving_size="111g",
    brand="Generic",
    calories=300.0, protein=2.0, carbs=40.0, fat=15.0, fiber=0.0, sugar=32.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=270.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chocolate_raspberry_flourless_torte_569 = create_food(
    food_name="Chocolate Raspberry Flourless Torte - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=110.0, protein=1.0, carbs=9.0, fat=9.0, fiber=1.0, sugar=5.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=15.0, potassium=69.2, vitamin_A=4.0, vitamin_C=0.0, calcium=0.0
)

apple_pie_570 = create_food(
    food_name="Apple Pie - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=80.0, protein=0.0, carbs=10.0, fat=5.0, fiber=0.0, sugar=4.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=90.0, potassium=6.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheddar_cheese_571 = create_food(
    food_name="Cheddar Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=90.0, protein=5.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=140.0, potassium=22.4, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

cucumbers_572 = create_food(
    food_name="Cucumbers - Cup",
    serving_size="113g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=166.7, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

mayonnaise_573 = create_food(
    food_name="Mayonnaise - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=90.0, protein=0.0, carbs=0.0, fat=10.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=85.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dijon_mustard_574 = create_food(
    food_name="Dijon Mustard - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

red_onions_575 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

banana_peppers_576 = create_food(
    food_name="Banana Peppers - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dill_pickle_chips_577 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

ham_578 = create_food(
    food_name="Ham - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=35.0, protein=6.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

tomatoes_579 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

turkey_breast_580 = create_food(
    food_name="Turkey Breast - Slice",
    serving_size="28g",
    brand="Generic",
    calories=25.0, protein=5.0, carbs=1.0, fat=1.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=78.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheddar_cheese_581 = create_food(
    food_name="Cheddar Cheese - Each",
    serving_size="21g",
    brand="Generic",
    calories=90.0, protein=5.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=140.0, potassium=22.4, vitamin_A=4.0, vitamin_C=0.0, calcium=15.0
)

cucumbers_582 = create_food(
    food_name="Cucumbers - Cup",
    serving_size="113g",
    brand="Generic",
    calories=20.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=166.7, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

mayonnaise_583 = create_food(
    food_name="Mayonnaise - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=90.0, protein=0.0, carbs=0.0, fat=10.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=85.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dijon_mustard_584 = create_food(
    food_name="Dijon Mustard - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

red_onions_585 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

banana_peppers_586 = create_food(
    food_name="Banana Peppers - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dill_pickle_chips_587 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

ham_588 = create_food(
    food_name="Ham - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=35.0, protein=6.0, carbs=0.0, fat=1.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=330.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

tomatoes_589 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

turkey_breast_590 = create_food(
    food_name="Turkey Breast - Slice",
    serving_size="28g",
    brand="Generic",
    calories=25.0, protein=5.0, carbs=1.0, fat=1.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=78.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

omelet_bar_591 = create_food(
    food_name="Omelet Bar - Each",
    serving_size="196g",
    brand="Generic",
    calories=270.0, protein=20.0, carbs=6.0, fat=19.0, fiber=0.0, sugar=2.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=390.0, sodium=570.0, potassium=116.5, vitamin_A=25.0, vitamin_C=50.0, calcium=10.0
)

belgian_waffle_592 = create_food(
    food_name="Belgian Waffle - Each",
    serving_size="71g",
    brand="Generic",
    calories=320.0, protein=4.0, carbs=37.0, fat=17.0, fiber=2.0, sugar=19.0,
    saturated_fat=9.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=280.0, potassium=78.7, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

whipped_butter_593 = create_food(
    food_name="Whipped Butter - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=0.0, fat=11.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=10.0, vitamin_C=0.0, calcium=0.0
)

chicken_594 = create_food(
    food_name="Chicken - 3oz",
    serving_size="85g",
    brand="Generic",
    calories=90.0, protein=16.0, carbs=1.0, fat=2.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=50.0, sodium=490.0, potassium=245.1, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

strawberry_sauce_595 = create_food(
    food_name="Strawberry Sauce - Tablespoon",
    serving_size="11g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.1, vitamin_A=0.0, vitamin_C=6.0, calcium=0.0
)

spinach_596 = create_food(
    food_name="Spinach - Cup",
    serving_size="224g",
    brand="Generic",
    calories=50.0, protein=6.0, carbs=8.0, fat=1.0, fiber=5.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=1246.7, vitamin_A=420.0, vitamin_C=100.0, calcium=20.0
)

chocolate_syrup_597 = create_food(
    food_name="Chocolate Syrup - Tablespoon",
    serving_size="19g",
    brand="Generic",
    calories=50.0, protein=0.0, carbs=12.0, fat=0.0, fiber=0.0, sugar=10.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

vanilla_whipped_topping_598 = create_food(
    food_name="Vanilla Whipped Topping - Tablespoon",
    serving_size="8g",
    brand="Generic",
    calories=25.0, protein=0.0, carbs=2.0, fat=2.0, fiber=0.0, sugar=2.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

beef_barbacoa_599 = create_food(
    food_name="Beef Barbacoa - 2.5oz",
    serving_size="73g",
    brand="Generic",
    calories=110.0, protein=16.0, carbs=2.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=55.0, sodium=150.0, potassium=205.9, vitamin_A=10.0, vitamin_C=2.0, calcium=2.0
)

cilantro_600 = create_food(
    food_name="Cilantro - Tablespoon",
    serving_size="1g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=5.2, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

lime_wedge_601 = create_food(
    food_name="Lime Wedge - Wedge",
    serving_size="15g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=8.0, calcium=0.0
)

ramen_noodles_602 = create_food(
    food_name="Ramen Noodles - Ounce",
    serving_size="28g",
    brand="Generic",
    calories=80.0, protein=3.0, carbs=15.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=160.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

jalapeno_peppers_603 = create_food(
    food_name="Jalapeno Peppers - Tablespoon",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=2.0, vitamin_C=10.0, calcium=0.0
)

roasted_corn_and_poblano_pepper_salsa_604 = create_food(
    food_name="Roasted Corn and Poblano Pepper Salsa - 2oz",
    serving_size="60g",
    brand="Generic",
    calories=120.0, protein=3.0, carbs=16.0, fat=6.0, fiber=5.0, sugar=0.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=20.0, potassium=34.4, vitamin_A=80.0, vitamin_C=10.0, calcium=2.0
)

mexican_asian_broth_w_hoisin_605 = create_food(
    food_name="Mexican Asian Broth w/ Hoisin - Cup",
    serving_size="233g",
    brand="Generic",
    calories=60.0, protein=0.0, carbs=14.0, fat=0.5, fiber=1.0, sugar=9.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=1260.0, potassium=34.3, vitamin_A=6.0, vitamin_C=70.0, calcium=2.0
)

garlic_naan_606 = create_food(
    food_name="Garlic Naan - 2 Slices",
    serving_size="46g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=20.0, fat=5.0, fiber=0.0, sugar=1.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=330.0, potassium=0.8, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

halal_chicken_tikka_masala_607 = create_food(
    food_name="Halal Chicken Tikka Masala - 6oz",
    serving_size="160g",
    brand="Generic",
    calories=270.0, protein=11.0, carbs=11.0, fat=22.0, fiber=2.0, sugar=1.0,
    saturated_fat=10.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=320.0, potassium=102.7, vitamin_A=6.0, vitamin_C=30.0, calcium=4.0
)

lentil_and_garbanzo_curry_608 = create_food(
    food_name="Lentil and Garbanzo Curry - 5oz",
    serving_size="126g",
    brand="Generic",
    calories=180.0, protein=11.0, carbs=33.0, fat=5.0, fiber=9.0, sugar=1.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=290.0, potassium=407.1, vitamin_A=20.0, vitamin_C=25.0, calcium=2.0
)

basmati_rice_609 = create_food(
    food_name="Basmati Rice - 4oz",
    serving_size="121g",
    brand="Generic",
    calories=160.0, protein=4.0, carbs=35.0, fat=0.5, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=47.3, vitamin_A=0.0, vitamin_C=50.0, calcium=2.0
)

vegetable_samosas_610 = create_food(
    food_name="Vegetable Samosas - 2 Each",
    serving_size="90g",
    brand="Generic",
    calories=200.0, protein=4.0, carbs=32.0, fat=6.0, fiber=2.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=480.0, potassium=180.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

green_chutney_611 = create_food(
    food_name="Green Chutney - 2oz",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=50.0, potassium=63.8, vitamin_A=20.0, vitamin_C=10.0, calcium=2.0
)

cucumber_raita_612 = create_food(
    food_name="Cucumber Raita - 2oz",
    serving_size="59g",
    brand="Generic",
    calories=25.0, protein=4.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=60.0, potassium=76.3, vitamin_A=2.0, vitamin_C=2.0, calcium=4.0
)

naan_bread_613 = create_food(
    food_name="Naan Bread - Each",
    serving_size="43g",
    brand="Generic",
    calories=120.0, protein=4.0, carbs=20.0, fat=3.0, fiber=0.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=320.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

sriracha_honey__sesame_halal_chicken_614 = create_food(
    food_name="Sriracha Honey & Sesame Halal Chicken - 4oz",
    serving_size="119g",
    brand="Generic",
    calories=170.0, protein=18.0, carbs=5.0, fat=10.0, fiber=0.0, sugar=5.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=85.0, sodium=610.0, potassium=4.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

ginger_and_garlic_sauteed_snow_peas_615 = create_food(
    food_name="Ginger and Garlic Sauteed Snow Peas - 2oz",
    serving_size="53g",
    brand="Generic",
    calories=40.0, protein=2.0, carbs=5.0, fat=1.5, fiber=1.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=290.0, potassium=4.6, vitamin_A=10.0, vitamin_C=45.0, calcium=2.0
)

basmati_rice_616 = create_food(
    food_name="Basmati Rice - 4oz",
    serving_size="121g",
    brand="Generic",
    calories=160.0, protein=4.0, carbs=35.0, fat=0.5, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=47.3, vitamin_A=0.0, vitamin_C=50.0, calcium=2.0
)

red_thai_tofu_617 = create_food(
    food_name="Red Thai Tofu - 8oz",
    serving_size="225g",
    brand="Generic",
    calories=130.0, protein=9.0, carbs=11.0, fat=6.0, fiber=4.0, sugar=3.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=370.0, potassium=170.1, vitamin_A=25.0, vitamin_C=80.0, calcium=20.0
)

pineapple_pepper_relish_618 = create_food(
    food_name="Pineapple Pepper Relish - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.2, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

woodys_tabbouleh_salad_619 = create_food(
    food_name="Woody's Tabbouleh Salad - Cup",
    serving_size="57g",
    brand="Generic",
    calories=60.0, protein=1.0, carbs=4.0, fat=4.0, fiber=1.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=25.0, potassium=0.0, vitamin_A=30.0, vitamin_C=35.0, calcium=6.0
)

pita_chips_620 = create_food(
    food_name="Pita Chips - 6 Chips",
    serving_size="28g",
    brand="Generic",
    calories=70.0, protein=2.0, carbs=13.0, fat=0.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=55.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

woodys_original_hummus_621 = create_food(
    food_name="Woody's Original Hummus - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=40.0, protein=1.0, carbs=2.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=70.0, potassium=37.5, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

pineapple_pepper_relish_622 = create_food(
    food_name="Pineapple Pepper Relish - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.2, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

scrambled_eggs_623 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

breakfast_tacos_624 = create_food(
    food_name="Breakfast Tacos - Each",
    serving_size="220g",
    brand="Generic",
    calories=310.0, protein=13.0, carbs=25.0, fat=17.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=275.0, sodium=620.0, potassium=90.2, vitamin_A=15.0, vitamin_C=25.0, calcium=6.0
)

tofu_scramble_625 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_626 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

bacon_627 = create_food(
    food_name="Bacon - 2 Slices",
    serving_size="18g",
    brand="Generic",
    calories=90.0, protein=6.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=250.0, potassium=101.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

hash_brown_patty_628 = create_food(
    food_name="Hash Brown Patty - Each",
    serving_size="54g",
    brand="Generic",
    calories=90.0, protein=2.0, carbs=11.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=2.0
)

veggie_sausage_patties_629 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_630 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_631 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_632 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

scrambled_eggs_633 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

breakfast_tacos_634 = create_food(
    food_name="Breakfast Tacos - Each",
    serving_size="220g",
    brand="Generic",
    calories=310.0, protein=13.0, carbs=25.0, fat=17.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=275.0, sodium=620.0, potassium=90.2, vitamin_A=15.0, vitamin_C=25.0, calcium=6.0
)

tofu_scramble_635 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_636 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

bacon_637 = create_food(
    food_name="Bacon - 2 Slices",
    serving_size="18g",
    brand="Generic",
    calories=90.0, protein=6.0, carbs=0.0, fat=7.0, fiber=0.0, sugar=0.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=250.0, potassium=101.3, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

hash_brown_patty_638 = create_food(
    food_name="Hash Brown Patty - Each",
    serving_size="54g",
    brand="Generic",
    calories=90.0, protein=2.0, carbs=11.0, fat=5.0, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=2.0, calcium=2.0
)

veggie_sausage_patties_639 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_640 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_641 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_642 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

black_bean_burger_643 = create_food(
    food_name="Black Bean Burger - Each",
    serving_size="132g",
    brand="Generic",
    calories=250.0, protein=10.0, carbs=37.0, fat=8.0, fiber=7.0, sugar=5.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=650.0, potassium=385.6, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

cheeseburger_644 = create_food(
    food_name="Cheeseburger - Each",
    serving_size="122g",
    brand="Generic",
    calories=300.0, protein=23.0, carbs=19.0, fat=14.0, fiber=0.0, sugar=3.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=65.0, sodium=450.0, potassium=271.9, vitamin_A=6.0, vitamin_C=0.0, calcium=15.0
)

burger_645 = create_food(
    food_name="Burger - Each",
    serving_size="120g",
    brand="Generic",
    calories=290.0, protein=24.0, carbs=17.0, fat=13.0, fiber=0.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=70.0, sodium=240.0, potassium=331.3, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

crinkle_fries_646 = create_food(
    food_name="Crinkle Fries - 3oz",
    serving_size="85g",
    brand="Generic",
    calories=260.0, protein=3.0, carbs=35.0, fat=13.0, fiber=3.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=492.4, vitamin_A=0.0, vitamin_C=6.0, calcium=0.0
)

iceberg_lettuce_647 = create_food(
    food_name="Iceberg Lettuce - Cup",
    serving_size="80g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=8.0, vitamin_C=4.0, calcium=0.0
)

red_onions_648 = create_food(
    food_name="Red Onions - Each",
    serving_size="6g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

dill_pickle_chips_649 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tomatoes_650 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

msu_bakers_dinner_roll_651 = create_food(
    food_name="MSU Bakers Dinner Roll - Each",
    serving_size="43g",
    brand="MSU",
    calories=110.0, protein=3.0, carbs=20.0, fat=2.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=190.0, potassium=0.0, vitamin_A=0.0, vitamin_C=8.0, calcium=2.0
)

green_beans_with_shallots_652 = create_food(
    food_name="Green Beans with Shallots - 4oz",
    serving_size="122g",
    brand="Generic",
    calories=80.0, protein=2.0, carbs=10.0, fat=3.5, fiber=3.0, sugar=3.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=212.3, vitamin_A=15.0, vitamin_C=25.0, calcium=4.0
)

candied_sweet_potatoes_653 = create_food(
    food_name="Candied Sweet Potatoes - 3oz",
    serving_size="102g",
    brand="Generic",
    calories=150.0, protein=1.0, carbs=30.0, fat=3.0, fiber=4.0, sugar=6.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=721.0, vitamin_A=4.0, vitamin_C=25.0, calcium=0.0
)

smoked_bbq_turkey_654 = create_food(
    food_name="Smoked BBQ Turkey - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=90.0, protein=16.0, carbs=5.0, fat=1.5, fiber=0.0, sugar=4.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=45.0, sodium=630.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

whipped_butter_655 = create_food(
    food_name="Whipped Butter - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=0.0, fat=11.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=10.0, vitamin_C=0.0, calcium=0.0
)

turkey_gravy_656 = create_food(
    food_name="Turkey Gravy - Tablespoon",
    serving_size="13g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=0.0, fat=1.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=45.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tennessee_bbq_sauce_657 = create_food(
    food_name="Tennessee BBQ Sauce - Tablespoon",
    serving_size="16g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=0.0, vitamin_A=2.0, vitamin_C=2.0, calcium=0.0
)

cornbread_658 = create_food(
    food_name="Cornbread - Each",
    serving_size="59g",
    brand="Generic",
    calories=190.0, protein=3.0, carbs=30.0, fat=6.0, fiber=1.0, sugar=8.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=35.0, sodium=370.0, potassium=63.0, vitamin_A=0.0, vitamin_C=0.0, calcium=8.0
)

steamed_peas_659 = create_food(
    food_name="Steamed Peas - 3oz",
    serving_size="86g",
    brand="Generic",
    calories=70.0, protein=4.0, carbs=12.0, fat=0.0, fiber=4.0, sugar=4.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=60.0, potassium=0.0, vitamin_A=35.0, vitamin_C=15.0, calcium=2.0
)

cheesy_grits_660 = create_food(
    food_name="Cheesy Grits - 5oz",
    serving_size="139g",
    brand="Generic",
    calories=150.0, protein=2.0, carbs=13.0, fat=11.0, fiber=0.0, sugar=2.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=70.0, potassium=10.5, vitamin_A=10.0, vitamin_C=0.0, calcium=2.0
)

maple_cured_bacon_661 = create_food(
    food_name="Maple Cured Bacon - 3oz",
    serving_size="93g",
    brand="Generic",
    calories=440.0, protein=7.0, carbs=2.0, fat=44.0, fiber=0.0, sugar=2.0,
    saturated_fat=16.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=60.0, sodium=2380.0, potassium=0.3, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

seasoned_diced_potatoes_662 = create_food(
    food_name="Seasoned Diced Potatoes - 3.5oz",
    serving_size="109g",
    brand="Generic",
    calories=170.0, protein=3.0, carbs=22.0, fat=8.0, fiber=3.0, sugar=1.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=430.0, potassium=311.3, vitamin_A=0.0, vitamin_C=20.0, calcium=0.0
)

green_onions_663 = create_food(
    food_name="Green Onions - Cup",
    serving_size="85g",
    brand="Generic",
    calories=25.0, protein=2.0, carbs=6.0, fat=0.0, fiber=3.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=15.0, potassium=232.2, vitamin_A=15.0, vitamin_C=25.0, calcium=6.0
)

cajun_pizza_664 = create_food(
    food_name="Cajun Pizza - Slice",
    serving_size="93g",
    brand="Generic",
    calories=220.0, protein=12.0, carbs=19.0, fat=11.0, fiber=1.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=35.0, sodium=660.0, potassium=84.9, vitamin_A=6.0, vitamin_C=6.0, calcium=10.0
)

cheese_pizza_665 = create_food(
    food_name="3 Cheese Pizza - Slice",
    serving_size="54g",
    brand="Generic",
    calories=150.0, protein=7.0, carbs=18.0, fat=6.0, fiber=0.0, sugar=1.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=340.0, potassium=38.6, vitamin_A=2.0, vitamin_C=0.0, calcium=10.0
)

halal_pepperoni_pizza_666 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

cajun_pizza_667 = create_food(
    food_name="Cajun Pizza - Slice",
    serving_size="93g",
    brand="Generic",
    calories=220.0, protein=12.0, carbs=19.0, fat=11.0, fiber=1.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=35.0, sodium=660.0, potassium=84.9, vitamin_A=6.0, vitamin_C=6.0, calcium=10.0
)

cheese_pizza_668 = create_food(
    food_name="3 Cheese Pizza - Slice",
    serving_size="54g",
    brand="Generic",
    calories=150.0, protein=7.0, carbs=18.0, fat=6.0, fiber=0.0, sugar=1.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=340.0, potassium=38.6, vitamin_A=2.0, vitamin_C=0.0, calcium=10.0
)

halal_pepperoni_pizza_669 = create_food(
    food_name="Halal Pepperoni Pizza - Slice",
    serving_size="85g",
    brand="Generic",
    calories=240.0, protein=10.0, carbs=28.0, fat=10.0, fiber=2.0, sugar=2.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=600.0, potassium=78.8, vitamin_A=0.0, vitamin_C=0.0, calcium=10.0
)

spicy_chicken_soup_670 = create_food(
    food_name="Spicy Chicken Soup - 4oz",
    serving_size="106g",
    brand="Generic",
    calories=30.0, protein=3.0, carbs=2.0, fat=1.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=320.0, potassium=80.4, vitamin_A=2.0, vitamin_C=8.0, calcium=4.0
)

fresh_mushroom_soup_671 = create_food(
    food_name="Fresh Mushroom Soup - 4oz",
    serving_size="112g",
    brand="Generic",
    calories=60.0, protein=1.0, carbs=9.0, fat=2.5, fiber=2.0, sugar=3.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=1280.0, potassium=63.0, vitamin_A=4.0, vitamin_C=8.0, calcium=2.0
)

chocolate_chip_cookie_672 = create_food(
    food_name="Chocolate Chip Cookie - Each",
    serving_size="29g",
    brand="Generic",
    calories=120.0, protein=1.0, carbs=17.0, fat=6.0, fiber=0.0, sugar=10.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=160.0, potassium=37.8, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

special_event_iced_cookie_673 = create_food(
    food_name="Special Event Iced Cookie - Each",
    serving_size="58g",
    brand="Generic",
    calories=240.0, protein=4.0, carbs=32.0, fat=11.0, fiber=0.0, sugar=12.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=170.0, potassium=10.0, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

french_toast_crunch_bars_674 = create_food(
    food_name="French Toast Crunch Bars - 3 oz",
    serving_size="64g",
    brand="Generic",
    calories=260.0, protein=2.0, carbs=48.0, fat=7.0, fiber=2.0, sugar=27.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=0.0, vitamin_A=15.0, vitamin_C=10.0, calcium=10.0
)

vegan_chocolate_cake_675 = create_food(
    food_name="Vegan Chocolate Cake - 2 oz",
    serving_size="67g",
    brand="Generic",
    calories=200.0, protein=2.0, carbs=38.0, fat=5.0, fiber=1.0, sugar=15.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=210.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

creamsicle_sheet_cake_676 = create_food(
    food_name="Creamsicle Sheet Cake - 3 oz",
    serving_size="76g",
    brand="Generic",
    calories=180.0, protein=2.0, carbs=26.0, fat=8.0, fiber=0.0, sugar=7.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=190.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

pink_lemonade_cake_677 = create_food(
    food_name="Pink Lemonade Cake - 3 oz",
    serving_size="118g",
    brand="Generic",
    calories=460.0, protein=1.0, carbs=57.0, fat=25.0, fiber=0.0, sugar=35.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=300.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cream_cheese_iced_cherry_cake_678 = create_food(
    food_name="Cream Cheese Iced Cherry Cake - Ounce",
    serving_size="26g",
    brand="Generic",
    calories=80.0, protein=0.0, carbs=13.0, fat=3.5, fiber=0.0, sugar=7.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=60.0, potassium=0.2, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

cheesecake_with_fruit_679 = create_food(
    food_name="Cheesecake with Fruit - Ounce",
    serving_size="18g",
    brand="Generic",
    calories=60.0, protein=0.0, carbs=6.0, fat=3.5, fiber=0.0, sugar=3.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=55.0, potassium=5.7, vitamin_A=2.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_cheesecake_680 = create_food(
    food_name="Sour Cream Cheesecake - Ounce",
    serving_size="29g",
    brand="Generic",
    calories=100.0, protein=1.0, carbs=10.0, fat=6.0, fiber=0.0, sugar=5.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=90.0, potassium=9.3, vitamin_A=4.0, vitamin_C=0.0, calcium=2.0
)

vegan_vanilla_cupcake_681 = create_food(
    food_name="Vegan Vanilla Cupcake - Each",
    serving_size="90g",
    brand="Generic",
    calories=320.0, protein=1.0, carbs=54.0, fat=11.0, fiber=0.0, sugar=40.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=180.0, potassium=17.2, vitamin_A=0.0, vitamin_C=0.0, calcium=6.0
)

special_event_iced_cupcake_682 = create_food(
    food_name="Special Event Iced Cupcake - Each",
    serving_size="111g",
    brand="Generic",
    calories=300.0, protein=2.0, carbs=40.0, fat=15.0, fiber=0.0, sugar=32.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=270.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

chocolate_raspberry_flourless_torte_683 = create_food(
    food_name="Chocolate Raspberry Flourless Torte - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=110.0, protein=1.0, carbs=9.0, fat=9.0, fiber=1.0, sugar=5.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=15.0, potassium=69.2, vitamin_A=4.0, vitamin_C=0.0, calcium=0.0
)

apple_pie_684 = create_food(
    food_name="Apple Pie - Ounce",
    serving_size="30g",
    brand="Generic",
    calories=80.0, protein=0.0, carbs=10.0, fat=5.0, fiber=0.0, sugar=4.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=90.0, potassium=6.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

strawberry_topping_685 = create_food(
    food_name="Strawberry Topping - Tablespoon",
    serving_size="20g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=7.0, fat=0.0, fiber=0.0, sugar=7.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

cheese_blintz_686 = create_food(
    food_name="Cheese Blintz - Each",
    serving_size="85g",
    brand="Generic",
    calories=200.0, protein=7.0, carbs=28.0, fat=7.0, fiber=0.0, sugar=18.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=250.0, potassium=80.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

omelet_bar_687 = create_food(
    food_name="Omelet Bar - Each",
    serving_size="196g",
    brand="Generic",
    calories=270.0, protein=20.0, carbs=6.0, fat=19.0, fiber=0.0, sugar=2.0,
    saturated_fat=8.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=390.0, sodium=570.0, potassium=116.5, vitamin_A=25.0, vitamin_C=50.0, calcium=10.0
)

chicken_688 = create_food(
    food_name="Chicken - 3oz",
    serving_size="85g",
    brand="Generic",
    calories=90.0, protein=16.0, carbs=1.0, fat=2.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=50.0, sodium=490.0, potassium=245.1, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

spinach_689 = create_food(
    food_name="Spinach - Cup",
    serving_size="224g",
    brand="Generic",
    calories=50.0, protein=6.0, carbs=8.0, fat=1.0, fiber=5.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=1246.7, vitamin_A=420.0, vitamin_C=100.0, calcium=20.0
)

strawberry_topping_690 = create_food(
    food_name="Strawberry Topping - Tablespoon",
    serving_size="20g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=7.0, fat=0.0, fiber=0.0, sugar=7.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=0.0, vitamin_A=0.0, vitamin_C=10.0, calcium=0.0
)

cheese_blintz_691 = create_food(
    food_name="Cheese Blintz - Each",
    serving_size="85g",
    brand="Generic",
    calories=200.0, protein=7.0, carbs=28.0, fat=7.0, fiber=0.0, sugar=18.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=15.0, sodium=250.0, potassium=80.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

hot_pepper_sesame_coleslaw_692 = create_food(
    food_name="Hot Pepper Sesame Coleslaw - 3oz",
    serving_size="84g",
    brand="Generic",
    calories=35.0, protein=0.0, carbs=3.0, fat=2.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=60.0, potassium=56.0, vitamin_A=15.0, vitamin_C=25.0, calcium=2.0
)

pork_tacos_with_slaw__hoisin_bbq_sauce_693 = create_food(
    food_name="Pork Tacos with Slaw & Hoisin BBQ Sauce - Each",
    serving_size="129g",
    brand="Generic",
    calories=210.0, protein=14.0, carbs=17.0, fat=10.0, fiber=1.0, sugar=5.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=45.0, sodium=1570.0, potassium=12.1, vitamin_A=6.0, vitamin_C=6.0, calcium=4.0
)

orange_mango_salsa_694 = create_food(
    food_name="Orange Mango Salsa - Tablespoon",
    serving_size="9g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=10.1, vitamin_A=0.0, vitamin_C=2.0, calcium=0.0
)

hoisin_bbq_sauce_695 = create_food(
    food_name="Hoisin BBQ Sauce - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=25.0, protein=0.0, carbs=5.0, fat=0.0, fiber=0.0, sugar=4.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=320.0, potassium=5.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

taco_flour_tortilla_696 = create_food(
    food_name="Taco Flour Tortilla - Each",
    serving_size="29g",
    brand="Generic",
    calories=80.0, protein=2.0, carbs=14.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=170.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

garlic_naan_697 = create_food(
    food_name="Garlic Naan - 2 Slices",
    serving_size="46g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=20.0, fat=5.0, fiber=0.0, sugar=1.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=330.0, potassium=0.8, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

cauliflower_and_chickpea_coconut_curry_698 = create_food(
    food_name="Cauliflower and Chickpea Coconut Curry - 4oz",
    serving_size="99g",
    brand="Generic",
    calories=80.0, protein=2.0, carbs=7.0, fat=6.0, fiber=2.0, sugar=2.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=35.0, potassium=118.0, vitamin_A=4.0, vitamin_C=30.0, calcium=2.0
)

spicy_green_beans_699 = create_food(
    food_name="Spicy Green Beans - 3oz",
    serving_size="92g",
    brand="Generic",
    calories=45.0, protein=2.0, carbs=7.0, fat=1.5, fiber=2.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=140.0, potassium=190.3, vitamin_A=15.0, vitamin_C=20.0, calcium=2.0
)

basmati_rice_700 = create_food(
    food_name="Basmati Rice - 4oz",
    serving_size="121g",
    brand="Generic",
    calories=160.0, protein=4.0, carbs=35.0, fat=0.5, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=810.0, potassium=47.3, vitamin_A=0.0, vitamin_C=50.0, calcium=2.0
)

grilled_herb_halal_chicken_thigh_701 = create_food(
    food_name="Grilled Herb Halal Chicken Thigh - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=130.0, protein=15.0, carbs=0.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=70.0, sodium=70.0, potassium=3.4, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

naan_bread_702 = create_food(
    food_name="Naan Bread - Each",
    serving_size="43g",
    brand="Generic",
    calories=120.0, protein=4.0, carbs=20.0, fat=3.0, fiber=0.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=320.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

halal_jerk_chicken_703 = create_food(
    food_name="Halal Jerk Chicken - 4oz",
    serving_size="113g",
    brand="Generic",
    calories=170.0, protein=16.0, carbs=7.0, fat=9.0, fiber=0.0, sugar=6.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=80.0, sodium=140.0, potassium=15.2, vitamin_A=2.0, vitamin_C=2.0, calcium=2.0
)

curried_caribbean_chickpeas_704 = create_food(
    food_name="Curried Caribbean Chickpeas - 8oz",
    serving_size="228g",
    brand="Generic",
    calories=190.0, protein=7.0, carbs=25.0, fat=10.0, fiber=5.0, sugar=2.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=130.0, potassium=229.5, vitamin_A=15.0, vitamin_C=50.0, calcium=6.0
)

caribbean_peas_and_rice_705 = create_food(
    food_name="Caribbean Peas and Rice - 4oz",
    serving_size="111g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=32.0, fat=0.0, fiber=2.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=260.0, potassium=19.0, vitamin_A=2.0, vitamin_C=4.0, calcium=2.0
)

caribbean_roasted_vegetables_706 = create_food(
    food_name="Caribbean Roasted Vegetables - 3oz",
    serving_size="78g",
    brand="Generic",
    calories=50.0, protein=1.0, carbs=5.0, fat=3.0, fiber=1.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=100.0, potassium=70.6, vitamin_A=15.0, vitamin_C=70.0, calcium=2.0
)

grilled_pineapple_salsa_707 = create_food(
    food_name="Grilled Pineapple Salsa - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=45.0, potassium=1.3, vitamin_A=2.0, vitamin_C=15.0, calcium=0.0
)

woodys_tabbouleh_salad_708 = create_food(
    food_name="Woody's Tabbouleh Salad - Cup",
    serving_size="57g",
    brand="Generic",
    calories=60.0, protein=1.0, carbs=4.0, fat=4.0, fiber=1.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=25.0, potassium=0.0, vitamin_A=30.0, vitamin_C=35.0, calcium=6.0
)

pita_chips_709 = create_food(
    food_name="Pita Chips - 6 Chips",
    serving_size="28g",
    brand="Generic",
    calories=70.0, protein=2.0, carbs=13.0, fat=0.5, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=55.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

woodys_red_pepper_hummus_710 = create_food(
    food_name="Woody's Red Pepper Hummus - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=40.0, protein=0.0, carbs=2.0, fat=3.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=37.5, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

scrambled_eggs_711 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

tofu_scramble_712 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_713 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

seasoned_diced_potatoes_714 = create_food(
    food_name="Seasoned Diced Potatoes - 3.5oz",
    serving_size="109g",
    brand="Generic",
    calories=170.0, protein=3.0, carbs=22.0, fat=8.0, fiber=3.0, sugar=1.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=430.0, potassium=311.3, vitamin_A=0.0, vitamin_C=20.0, calcium=0.0
)

sausage_patties_715 = create_food(
    food_name="Sausage Patties - Each",
    serving_size="57g",
    brand="Generic",
    calories=210.0, protein=7.0, carbs=0.0, fat=21.0, fiber=0.0, sugar=0.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=45.0, sodium=380.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties_716 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_717 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_718 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_719 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

blueberry_cream_cheese_bread_pudding_720 = create_food(
    food_name="Blueberry Cream Cheese Bread Pudding - 3.5oz",
    serving_size="102g",
    brand="Generic",
    calories=220.0, protein=5.0, carbs=25.0, fat=11.0, fiber=0.0, sugar=14.0,
    saturated_fat=5.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=55.0, sodium=300.0, potassium=72.6, vitamin_A=8.0, vitamin_C=2.0, calcium=10.0
)

scrambled_eggs_721 = create_food(
    food_name="Scrambled Eggs - 4oz",
    serving_size="117g",
    brand="Generic",
    calories=190.0, protein=14.0, carbs=2.0, fat=14.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=475.0, sodium=220.0, potassium=155.4, vitamin_A=15.0, vitamin_C=0.0, calcium=4.0
)

tofu_scramble_722 = create_food(
    food_name="Tofu Scramble - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=80.0, protein=4.0, carbs=3.0, fat=6.0, fiber=2.0, sugar=1.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=150.0, potassium=99.1, vitamin_A=2.0, vitamin_C=4.0, calcium=8.0
)

hard_cooked_eggs_723 = create_food(
    food_name="Hard Cooked Eggs - Each",
    serving_size="57g",
    brand="Generic",
    calories=90.0, protein=7.0, carbs=0.0, fat=6.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=210.0, sodium=70.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

seasoned_diced_potatoes_724 = create_food(
    food_name="Seasoned Diced Potatoes - 3.5oz",
    serving_size="109g",
    brand="Generic",
    calories=170.0, protein=3.0, carbs=22.0, fat=8.0, fiber=3.0, sugar=1.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=430.0, potassium=311.3, vitamin_A=0.0, vitamin_C=20.0, calcium=0.0
)

sausage_patties_725 = create_food(
    food_name="Sausage Patties - Each",
    serving_size="57g",
    brand="Generic",
    calories=210.0, protein=7.0, carbs=0.0, fat=21.0, fiber=0.0, sugar=0.0,
    saturated_fat=7.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=45.0, sodium=380.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

veggie_sausage_patties_726 = create_food(
    food_name="Veggie Sausage Patties - 2 Patties",
    serving_size="70g",
    brand="Generic",
    calories=100.0, protein=5.0, carbs=2.0, fat=8.0, fiber=0.0, sugar=0.0,
    saturated_fat=2.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=61.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

shredded_mild_cheddar_cheese_727 = create_food(
    food_name="Shredded Mild Cheddar Cheese - Tablespoon",
    serving_size="7g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=5.0, sodium=45.0, potassium=0.0, vitamin_A=2.0, vitamin_C=0.0, calcium=4.0
)

salsa_728 = create_food(
    food_name="Salsa - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=65.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

sour_cream_729 = create_food(
    food_name="Sour Cream - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=30.0, protein=0.0, carbs=0.0, fat=2.5, fiber=0.0, sugar=0.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=25.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

broccoli_bacon__smoked_cheddar_salad_730 = create_food(
    food_name="Broccoli, Bacon & Smoked Cheddar Salad - 3oz",
    serving_size="86g",
    brand="Generic",
    calories=300.0, protein=5.0, carbs=17.0, fat=24.0, fiber=3.0, sugar=12.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=30.0, sodium=250.0, potassium=83.0, vitamin_A=10.0, vitamin_C=25.0, calcium=8.0
)

spicy_chicken_sandwich_731 = create_food(
    food_name="Spicy Chicken Sandwich - Each",
    serving_size="149g",
    brand="Generic",
    calories=290.0, protein=20.0, carbs=34.0, fat=9.0, fiber=0.0, sugar=2.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=40.0, sodium=1250.0, potassium=295.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

nashville_hot_tofu_sandwich_732 = create_food(
    food_name="Nashville Hot Tofu Sandwich - Sandwich",
    serving_size="164g",
    brand="Generic",
    calories=300.0, protein=9.0, carbs=36.0, fat=15.0, fiber=3.0, sugar=4.0,
    saturated_fat=2.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=1050.0, potassium=118.2, vitamin_A=20.0, vitamin_C=4.0, calcium=15.0
)

sweet_potato_fries_733 = create_food(
    food_name="Sweet Potato Fries - 4oz",
    serving_size="113g",
    brand="Generic",
    calories=240.0, protein=3.0, carbs=34.0, fat=11.0, fiber=4.0, sugar=9.0,
    saturated_fat=1.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=230.0, potassium=324.0, vitamin_A=0.0, vitamin_C=0.0, calcium=2.0
)

iceberg_lettuce_734 = create_food(
    food_name="Iceberg Lettuce - Cup",
    serving_size="80g",
    brand="Generic",
    calories=10.0, protein=0.0, carbs=2.0, fat=0.0, fiber=0.0, sugar=2.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=10.0, potassium=0.0, vitamin_A=8.0, vitamin_C=4.0, calcium=0.0
)

dill_pickle_chips_735 = create_food(
    food_name="Dill Pickle Chips - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=0.0, protein=0.0, carbs=0.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=125.0, potassium=0.0, vitamin_A=0.0, vitamin_C=0.0, calcium=0.0
)

tomatoes_736 = create_food(
    food_name="Tomatoes - Each",
    serving_size="28g",
    brand="Generic",
    calories=5.0, protein=0.0, carbs=1.0, fat=0.0, fiber=0.0, sugar=0.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=0.0, potassium=67.3, vitamin_A=4.0, vitamin_C=6.0, calcium=0.0
)

hawaiian_roll_737 = create_food(
    food_name="Hawaiian Roll - Each",
    serving_size="49g",
    brand="Generic",
    calories=140.0, protein=4.0, carbs=25.0, fat=2.5, fiber=0.0, sugar=5.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=115.0, potassium=0.0, vitamin_A=0.0, vitamin_C=20.0, calcium=2.0
)

coleslaw_738 = create_food(
    food_name="Coleslaw - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=8.0, fat=8.0, fiber=2.0, sugar=5.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=190.0, potassium=136.6, vitamin_A=50.0, vitamin_C=2.0, calcium=60.0
)

macaroni_and_cheese_cheese_cheese_739 = create_food(
    food_name="Macaroni and Cheese, Cheese, Cheese - 6oz",
    serving_size="173g",
    brand="Generic",
    calories=360.0, protein=17.0, carbs=27.0, fat=21.0, fiber=1.0, sugar=4.0,
    saturated_fat=13.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=90.0, sodium=600.0, potassium=40.3, vitamin_A=15.0, vitamin_C=0.0, calcium=25.0
)

memphis_pork_ribs_740 = create_food(
    food_name="Memphis Pork Ribs - 4oz",
    serving_size="140g",
    brand="Generic",
    calories=390.0, protein=21.0, carbs=10.0, fat=29.0, fiber=1.0, sugar=8.0,
    saturated_fat=11.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=95.0, sodium=1080.0, potassium=0.1, vitamin_A=8.0, vitamin_C=0.0, calcium=2.0
)

pit_baked_beans_741 = create_food(
    food_name="Pit Baked Beans - 2oz",
    serving_size="58g",
    brand="Generic",
    calories=70.0, protein=2.0, carbs=16.0, fat=0.0, fiber=2.0, sugar=11.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=240.0, potassium=4.4, vitamin_A=2.0, vitamin_C=6.0, calcium=2.0
)

whipped_butter_742 = create_food(
    food_name="Whipped Butter - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=0.0, fat=11.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=10.0, vitamin_C=0.0, calcium=0.0
)

tennessee_bbq_sauce_743 = create_food(
    food_name="Tennessee BBQ Sauce - Tablespoon",
    serving_size="16g",
    brand="Generic",
    calories=15.0, protein=0.0, carbs=4.0, fat=0.0, fiber=0.0, sugar=3.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=220.0, potassium=0.0, vitamin_A=2.0, vitamin_C=2.0, calcium=0.0
)

buttermilk_biscuits_744 = create_food(
    food_name="Buttermilk Biscuits - Each",
    serving_size="72g",
    brand="Generic",
    calories=300.0, protein=5.0, carbs=27.0, fat=19.0, fiber=0.0, sugar=2.0,
    saturated_fat=10.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=600.0, potassium=0.0, vitamin_A=6.0, vitamin_C=0.0, calcium=2.0
)

black_pepper_sirloin_745 = create_food(
    food_name="Black Pepper Sirloin - 3.5oz",
    serving_size="112g",
    brand="Generic",
    calories=230.0, protein=27.0, carbs=2.0, fat=11.0, fiber=0.0, sugar=1.0,
    saturated_fat=3.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=85.0, sodium=470.0, potassium=334.2, vitamin_A=0.0, vitamin_C=0.0, calcium=4.0
)

steamed_broccoli_florets_746 = create_food(
    food_name="Steamed Broccoli Florets - 3oz",
    serving_size="85g",
    brand="Generic",
    calories=30.0, protein=2.0, carbs=6.0, fat=0.0, fiber=2.0, sugar=1.0,
    saturated_fat=0.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=30.0, potassium=0.0, vitamin_A=10.0, vitamin_C=130.0, calcium=4.0
)

parmesan_roasted_potatoes_747 = create_food(
    food_name="Parmesan Roasted Potatoes - 4oz",
    serving_size="120g",
    brand="Generic",
    calories=250.0, protein=5.0, carbs=20.0, fat=17.0, fiber=2.0, sugar=0.0,
    saturated_fat=6.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=20.0, sodium=200.0, potassium=0.0, vitamin_A=15.0, vitamin_C=15.0, calcium=10.0
)

honey_butter_748 = create_food(
    food_name="Honey Butter - Tablespoon",
    serving_size="15g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=2.0, fat=10.0, fiber=0.0, sugar=2.0,
    saturated_fat=3.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=8.0, vitamin_C=0.0, calcium=0.0
)

snappy_horseradish_sauce_749 = create_food(
    food_name="Snappy Horseradish Sauce - 2oz",
    serving_size="62g",
    brand="Generic",
    calories=220.0, protein=0.0, carbs=5.0, fat=22.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.5, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=25.0, sodium=310.0, potassium=0.0, vitamin_A=0.0, vitamin_C=6.0, calcium=2.0
)

coleslaw_750 = create_food(
    food_name="Coleslaw - 3oz",
    serving_size="87g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=8.0, fat=8.0, fiber=2.0, sugar=5.0,
    saturated_fat=1.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=0.0, sodium=190.0, potassium=136.6, vitamin_A=50.0, vitamin_C=2.0, calcium=60.0
)

whipped_butter_751 = create_food(
    food_name="Whipped Butter - Tablespoon",
    serving_size="14g",
    brand="Generic",
    calories=100.0, protein=0.0, carbs=0.0, fat=11.0, fiber=0.0, sugar=0.0,
    saturated_fat=4.0, polyunsaturated_fat=0.0, monounsaturated_fat=0.0, trans_fat=0.0,
    cholesterol=10.0, sodium=0.0, potassium=0.0, vitamin_A=10.0, vitamin_C=0.0, calcium=0.0
)

