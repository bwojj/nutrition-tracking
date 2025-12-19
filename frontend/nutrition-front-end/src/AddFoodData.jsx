import './assets/AddFoodData.css'
import { useState } from 'react';

function AddFoodData({ isOpen, onClose, info }){
    const saveFood = async (foodData) => {
        try {
            const foodItem = {
            meal_name: "Breakfast",
            food_name: "Oatmeal",
            calories: 150,
            protein: 5,
            carbs: 27,
            fat: 3
            };
            const response = await fetch("http://127.0.0.1:8000/api/add-food/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(foodItem),
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

    const [formData, setFormData] = useState({
        meal_name: "",
        food_name: info.food_name,
        calories: info.calories, 
        protein: info.protein, 
        carbs: info.carbs, 
        fat: info.fat, 
    });

    function handleNumServingsChange(e){

        const value = Number(e.target.value);

        setFormData({
            ...formData, 
            calories: (info.calories * value),
            protein: (info.protein * value),
            carbs: (info.carbs * value),
            fat: (info.fat * value)
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
        await saveFood(formData);
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
                <select id="meal" onChange={handleChange}>
                    <option value="Breakfast">Breakfast</option>
                    <option value="Lunch">Lunch</option>
                    <option value="Dinner">Dinner</option>
                </select>
            </div>
            <div className="food-add-data">
                <div className="label-data">
                    <span className="cals">Calories</span>
                    <span className="cal-value">{formData.calories}</span>
                </div>
                <div className="macro-data">
                    <div className="label-data" style={{border: '2px solid #7231bd'}}>
                        <span style={{color: '#7231bd', fontWeight: 'bold'}}>Protein</span>
                        <span>{formData.protein}</span>
                    </div>
                    <div className="label-data" style={{border: '2px solid #31bd98'}}>
                        <span style={{color: '#31bd98', fontWeight: 'bold'}}>Carbs</span>
                        <span>{formData.carbs}</span>
                    </div>
                    <div className="label-data" style={{border: '2px solid #ffad21ff'}}>
                        <span style={{color: '#ffad21ff', fontWeight: 'bold'}}>Fat</span>
                        <span>{formData.fat}</span>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default AddFoodData; 