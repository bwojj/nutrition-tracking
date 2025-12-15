import './assets/Meal.css'

function Meal(props){
    const dummyMeals = [{
        foodName: 'Chicken',
        calories: 167,
        protein: 63,
        carbs: 30, 
        fat: 1,
    }]; 

    
    return(
        <div className="meal">
            <div className="meal-header" style={{
                borderTopRightRadius: props.rounded ? '10px' : '0px',
                borderTopLeftRadius: props.rounded ? '10px' : '0px',
            }}>
                <h1 className="meal-title">{props.mealName}</h1>
                <div className="food-totals">
                    <span className="total-value">{dummyMeals[0].calories}Cals</span>
                    <span className="total-value">{dummyMeals[0].protein}P</span> 
                    <span className="total-value">{dummyMeals[0].carbs}C</span> 
                    <span className="total-value">{dummyMeals[0].fat}F</span>  
                </div>
            </div>
            <div className="food">
                <h3 className="food-name">{dummyMeals[0].foodName}</h3>
                <div className="food-info">
                    <span className="food-value">{dummyMeals[0].calories}Cals</span>
                    <span className="food-value">{dummyMeals[0].protein}P</span> 
                    <span className="food-value">{dummyMeals[0].carbs}C</span> 
                    <span className="food-value">{dummyMeals[0].fat}F</span>  
                </div>
            </div>

        </div>
    );
}

export default Meal