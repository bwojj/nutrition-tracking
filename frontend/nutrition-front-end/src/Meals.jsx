import './assets/Meals.css'
import { MealsContext } from './Context/Context';
import Meal from './Meal';
import { useContext } from 'react';

function Meals({ meal, setMeal, foodData, onOpen, onDelete }){
    const { meals } = useContext(MealsContext);


    return(
        <div className="meals">
            {meals.map((element, index) => (
                index === 0 ? (<Meal key={index} first={true} onOpen={onOpen} mealName={element}
                                foodData={foodData.filter(f => f.meal === element)} onDelete={onDelete}
                                setMeal={setMeal}/>)
                : <Meal key={index} onOpen={onOpen} mealName={element} 
                foodData={foodData.filter(f => f.meal === element)} onDelete={onDelete}
                 setMeal={setMeal} meal={meal}/> 
            ))}
        </div>
    );
}

export default Meals