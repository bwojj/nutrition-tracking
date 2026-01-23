from ..models import Foods

basmati_rice = Foods.objects.create(
    food_name="Basmati Rice",
    serving_size="4oz (121g)",
    brand="MSU", # Defaulting to MSU per your model's design
    calories=161.0,
    protein=4.0,
    carbs=35.0,
    fat=0.5,
    fiber=0.0,
    sugar=1.0,
    saturated_fat=0.0,
    polyunsaturated_fat=0.0, # Not explicitly listed in screenshot
    monounsaturated_fat=0.0, # Not explicitly listed in screenshot
    trans_fat=0.0,
    cholesterol=0.0,
    sodium=810.0,
    potassium=47.3,
    vitamin_A=0.0,
    vitamin_C=50.0, # Values from the screenshot
    calcium=2.0
)