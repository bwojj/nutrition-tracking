import './assets/AddFoodData.css'
import { MealsContext } from './Context/Context.js';
import { useContext, useState} from 'react';
import { saveFood } from './api/mealApi.js';

function AddFoodData({ isOpen, onClose, onModalClose, info, setIsLoading, date, onFoodAdded, selectedDate}){
    const { meals } = useContext(MealsContext);

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
            calories: Math.round(info.calories * value),
            protein: Math.round(info.protein * value),
            carbs: Math.round(info.carbs * value),
            fat: Math.round(info.fat * value),
            fiber: Math.round(info.fiber * value),
            sugar: Math.round(info.sugar * value),
            saturated_fat: Math.round(info.saturated_fat * value),
            polyunsaturated_fat: Math.round(info.polyunsaturated_fat * value),
            monounsaturated_fat: Math.round(info.monounsaturated_fat * value),
            trans_fat: Math.round(info.trans_fat * value),
            cholesterol: Math.round(info.cholesterol * value),
            sodium: Math.round(info.sodium * value),
            potassium: Math.round(info.potassium * value),
            vitamin_a: Math.round(info.vitamin_a * value),
            vitamin_c: Math.round(info.vitamin_c * value),
            calcium: Math.round(info.calcium * value)
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
        setIsLoading(true);
        e.preventDefault();
        await saveFood(formData, date);
        if (onFoodAdded) await onFoodAdded();
        onClose();
        onModalClose();
        setIsLoading(false);
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
                    <option value="1oz" selected>{info.serving_size}</option>
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