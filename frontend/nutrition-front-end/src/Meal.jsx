import { useState } from 'react';
import './assets/Meal.css'
import NutritionFacts from './NutritionFacts.jsx';
import { HiOutlineInformationCircle } from "react-icons/hi";
import { LuTrash2 } from "react-icons/lu";
import { deleteFood } from './api/mealApi.js';

function Meal(props){
    const [selectedFood, setSelectedFood] = useState(null);
    const [activeFood, setActiveFood] = useState(null);

    const openNutritionFacts = (food) => {
        setSelectedFood(food);
    };

    const closeNutritionFacts = () => {
        setSelectedFood(null);
    };

    const handleFoodClick = (id) => {
        setActiveFood(activeFood === id ? null : id);
    };

    const totalCalculate = (name) => {
        let total = 0; 
        props.foodData.forEach(value => total += value[name]);
        return total;
    }

    const onDelete = async (id) => {
        const deleteResponse = await deleteFood(id); 
        if(deleteResponse === 'Success'){
            props.setFoodData(prevData => prevData.filter(food => food.id !== id));
        }
    }

    const openAddFoodModal = (name) => {
        props.setMeal(name)
        props.onOpen()
    }

    return(
        <div className="meal">
            <div className={`meal-header ${props.first ? 'first': ''}`}>
                <div className="name-button">
                    <h1 className="meal-title">{props.mealName}</h1>
                    <button onClick={() => openAddFoodModal(props.mealName)} className="add-food-button">+</button>
                </div>
                <div className="food-totals">
                    <span className="total-value">{totalCalculate('calories')}Cals</span>
                    <span className="total-value">{totalCalculate('protein')}P</span> 
                    <span className="total-value">{totalCalculate('carbs')}C</span> 
                    <span className="total-value">{totalCalculate('fat')}F</span>  
                </div>
            </div>
            {props.foodData && props.foodData.length > 0 ? (
                props.foodData.map((element) => (
                element.meal === props.mealName ? (
                        <div
                            key={element.id}
                            className={`food ${activeFood === element.id ? 'active' : ''}`}
                            onClick={() => handleFoodClick(element.id)}
                        >
                            <h3 className="food-name">{element.food_name}</h3>
                            <div className="meal-food-info">
                                <span className="food-value">{element.calories}Cals</span>
                                <span className="food-value">{element.protein}P</span>
                                <span className="food-value">{element.carbs}C</span>
                                <span className="food-value">{element.fat}F</span>
                            </div>
                            <div className="food-hover" onClick={(e) => e.stopPropagation()}>
                                <HiOutlineInformationCircle className="info-icon" size={30} color="blue" onClick={() => openNutritionFacts(element)}/>
                                <LuTrash2 className="trash-icon" size={30} color="red" onClick={() => onDelete(element.id)} />
                            </div>
                        </div>
                ) : null
            ))
            ) : <div className="none-div" style={{height: '50px', marginBottom: '-20px'}}><span className="none">No Foods</span></div>
            }

            <NutritionFacts
                isOpen={selectedFood !== null}
                onClose={closeNutritionFacts}
                foodData={selectedFood}
            />
        </div>
    );
}

export default Meal