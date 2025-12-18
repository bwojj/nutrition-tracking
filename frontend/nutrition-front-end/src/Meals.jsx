import './assets/Meals.css'
import Meal from './Meal';

function Meals({ onOpen }){
    return(
        <div className="meals">
            <Meal onOpen={onOpen} rounded="True" mealName="Breakfast"/>
            <Meal onOpen={onOpen} mealName="Lunch"/>
            <Meal onOpen={onOpen} mealName="Dinner"/>
        </div>
    );
}

export default Meals