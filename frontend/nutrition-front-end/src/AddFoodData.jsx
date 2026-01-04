import './assets/AddFoodData.css'
import { MealsContext } from './Context/Context';
import { useContext, useState } from 'react';

function AddFoodData({ refreshData, isOpen, onClose, onModalClose, info, setIsLoading }){
    const { meals } = useContext(MealsContext);
    

    const saveFood = async (foodData) => {
        try {
            const response = await fetch("http://127.0.0.1:8000/api/add-food/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(foodData),
            });
            
            if(response.ok) {
                const result = await response.json();
                console.log("Saved", result);
            } else {
                console.log("Server Error", response.statusText);
            }
        } catch(error){
            console.log('Network Error', error); 
        }
    };

    console.log(info.meal);
    const [formData, setFormData] = useState({
        meal_name: info.meal,
        food_name: info.food_name,
        calories: info.calories, 
        protein: info.protein, 
        carbs: info.carbs, 
        fat: info.fat, 
        fiber: info.fiber,
        sugar: info.sugar,
        saturated_fat: info.saturated_fat,
        polyunsaturated_fat: info.polyunsaturated_fat,
        monounsaturated_fat: info.monounsaturated_fat,
        trans_fat: info.trans_fat,
        cholesterol: info.cholesterol,
        sodium: info.sodium,
        potassium: info.potassium,
        vitamin_a: info.vitamin_a,
        vitamin_c: info.vitamin_c,
        calcium: info.calcium
    });

    function handleNumServingsChange(e){

        const value = Number(e.target.value);
        setFormData({
            meal_name: info.meal, 
            food_name: info.food_name,
            calories: (info.calories * value),
            protein: (info.protein * value),
            carbs: (info.carbs * value),
            fat: (info.fat * value),
            fiber: (info.fiber * value),
            sugar: (info.sugar * value),
            saturated_fat: (info.saturated_fat * value),
            polyunsaturated_fat: (info.polyunsaturated_fat * value),
            monounsaturated_fat: (info.monounsaturated_fat * value),
            trans_fat: (info.trans_fat * value),
            cholesterol: (info.cholesterol * value),
            sodium: (info.sodium * value),
            potassium: (info.potassium * value),
            vitamin_a: (info.vitamin_a * value),
            vitamin_c: (info.vitamin_c * value),
            calcium: (info.calcium * value)
        });
    }
    function handleChange(e){
        const { id, value } = e.target; 

        setFormData({
            ...formData,
            [id]: value
        })
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(formData);
        setIsLoading(true);
        await saveFood(formData);

        if (refreshData){
            await refreshData();
        }
        onClose();
        onModalClose();
    }

    if (!isOpen) return null;

    return(
        <div className="add-food-data-container">
            <div className="add-food-data-header">
                <button onClick={handleSubmit} className="add-food">+</button>
                <h2 className="food-info">{info.food_name}</h2>
                <div className="x-data-wrapper">
                    <span onClick={onClose} className="x-data">{"\u00D7"}</span>
                </div>
            </div>
            <div className="serving-size">
                <label for="serve-size">Serving Size</label>
                <select id="serve-size" onChange={handleChange}>
                    <option value="1oz" selected>1oz</option>
                </select>
            </div>
            <div className="serving-num">
                <label for="num-serving">Number of Servings</label>
                <input onChange={handleNumServingsChange} id="num-servings" type="number"/>
            </div>
            <div className="serving-num">
                <label for="meal">Meal</label>
                <select defaultValue={info.meal} id="meal_name" onChange={handleChange}>
                    {meals.map((element) => (
                        <option value={element}>{element}</option>
                    ))};
                </select>
            </div>
            <div className="food-add-data">
                <div className="label-data">
                    <span className="cals">Calories</span>
                    <span className="cal-value">{formData.calories}</span>
                </div>
                <div className="macro-data">
                    <div className="label-data" style={{border: '2px solid #7231bd'}}>
                        <span className="macro-data-name" style={{color: '#7231bd', fontWeight: 'bold'}}>Protein</span>
                        <span>{formData.protein}</span>
                    </div>
                    <div className="label-data" style={{border: '2px solid #31bd98'}}>
                        <span className="macro-data-name" style={{color: '#31bd98', fontWeight: 'bold'}}>Carbs</span>
                        <span>{formData.carbs}</span>
                    </div>
                    <div className="label-data" style={{border: '2px solid #ffad21ff'}}>
                        <span className="macro-data-name" style={{color: '#ffad21ff', fontWeight: 'bold'}}>Fat</span>
                        <span>{formData.fat}</span>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default AddFoodData; 