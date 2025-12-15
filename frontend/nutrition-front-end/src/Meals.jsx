import './assets/Meals.css'
import Meal from './Meal';

function Meals(){
    return(
        <div className="meals">
            <Meal rounded="True" mealName="Breakfast"/>
            <Meal mealName="Lunch"/>
            <Meal mealName="Dinner"/>
        </div>
    );
}

export default Meals