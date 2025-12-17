import AddFoodData from './AddFoodData';
import './assets/AddFood.css'
import { useState } from 'react';

function AddFood(){
    let foodDatabase = [
    {
        id: 1,
        name: "Grilled Chicken Breast",
        calories: 165,
        protein: 31,
        carbs: 0,
        fat: 3.6
    },
    {
        id: 2,
        name: "Brown Rice (1 cup)",
        calories: 218,
        protein: 4.5,
        carbs: 45,
        fat: 1.6
    },
    {
        id: 3,
        name: "Avocado (Medium)",
        calories: 240,
        protein: 3,
        carbs: 12,
        fat: 22
    },
    {
        id: 4,
        name: "Greek Yogurt (Non-fat)",
        calories: 100,
        protein: 17,
        carbs: 6,
        fat: 0.4
    },
    {
        id: 5,
        name: "Almonds (1 oz)",
        calories: 164,
        protein: 6,
        carbs: 6,
        fat: 14
    },
    {
        id: 6,
        name: "Sweet Potato (Medium)",
        calories: 103,
        protein: 2,
        carbs: 24,
        fat: 0.2
    },
    {
        id: 7,
        name: "Atlantic Salmon",
        calories: 208,
        protein: 20,
        carbs: 0,
        fat: 13
    }
    ];

    const [search, setSearch] = useState("");

    function handleChange(event){
        setSearch(event.target.value);
    }

    const searchFilteredFoods = foodDatabase.filter((food) => (
        food.name.toLowerCase().includes(search.toLowerCase())
    ));

    return(
        <div className="add-food-container">
            <h1 className="add-food-title">Add Food</h1>
            <input className="search" onChange={handleChange} placeholder="Search Foods"/>
            <div className="foods">
                {searchFilteredFoods.map((element, index) => (
                    <div className="food-items-inner" key={index}>
                        <div className="name">
                            <span className="food-name">{element.name}</span>
                        </div>
                        <div className="data">
                            <span className="food-data">{element.calories}Cals</span>
                            <span className="food-data">{element.protein}P</span>
                            <span className="food-data">{element.carbs}C</span>
                            <span className="food-data">{element.fat}F</span>
                        </div>
                    </div>
                    ))}
            </div>
            <AddFoodData/>
        </div>
    );
}

export default AddFood; 