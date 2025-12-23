import './assets/Meals.css'
import Meal from './Meal';

function Meals({ foodData, onOpen, onDelete }){
    const meals = ["Breakfast", "Lunch", "Dinner", "Snacks"];


    return(
        <div className="meals">
            {meals.map((element, index) => (
                index === 0 ? (<Meal key={index} first={true} onOpen={onOpen} mealName={element}
                                foodData={foodData.filter(f => f.meal === element)} onDelete={onDelete}/>)
                : <Meal key={index} onOpen={onOpen} mealName={element} 
                foodData={foodData.filter(f => f.meal === element)} onDelete={onDelete}/> 
            ))}
        </div>
    );
}

export default Meals