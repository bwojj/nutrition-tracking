import './assets/Meals.css'
import { MealsContext } from './Context/Context.js';
import Meal from './Meal.jsx';
import { useContext } from 'react';

function Meals({ meal, setMeal, setFoodData, foodData, onOpen, onDelete }){
    const { meals } = useContext(MealsContext);


    return(
        <div className="meals">
            {meals.map((element, index) => (
                index === 0 ? (<Meal key={index} first={true} onOpen={onOpen} mealName={element}
                                foodData={foodData.filter(f => f.meal === element)} onDelete={onDelete}
                                setMeal={setMeal} setFoodData={setFoodData} />)
                : <Meal key={index} onOpen={onOpen} mealName={element} 
                foodData={foodData.filter(f => f.meal === element)} onDelete={onDelete}
                 setMeal={setMeal} meal={meal} setFoodData={setFoodData}/> 
            ))}
        </div>
    );
}

export default Meals