import './assets/Meal.css'

function Meal(props){
    
    return(
        <div className="meal">
            <div className={`meal-header ${props.first ? 'first': ''}`}>
                <div className="name-button">
                    <h1 className="meal-title">{props.mealName}</h1>
                    <button onClick={props.onOpen} className="add-food-button">+</button>
                </div>
                <div className="food-totals">
                    <span className="total-value">Cals</span>
                    <span className="total-value">P</span> 
                    <span className="total-value">C</span> 
                    <span className="total-value">F</span>  
                </div>
            </div>
            {props.foodData && props.foodData.length > 0 ? (
                props.foodData.map((element, index) => (
                element.meal === props.mealName ? (
                    <div key={index} className="food">
                    <h3 className="food-name">{element.food_name}</h3>
                    <div className="meal-food-info">
                        <span className="food-value">{element.calories}Cals</span>
                        <span className="food-value">{element.protein}P</span> 
                        <span className="food-value">{element.carbs}C</span> 
                        <span className="food-value">{element.fat}F</span>  
                    </div>
                    </div>
                ) : null
            ))
            ) : <div style={{height: '50px'}}>No Foods</div>
            }

        </div>
    );
}

export default Meal