import './assets/Meal.css'

function Meal(props){
    const totalCalculate = (name) => {
        let total = 0; 
        props.foodData.forEach(value => total += value[name]);

        return total;
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
                    <div onClick={() => props.onDelete(element.id)} key={element.id} className="food">
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
            ) : <div className="none-div" style={{height: '50px', marginBottom: '-20px'}}><span className="none">No Foods</span></div>
            }

        </div>
    );
}

export default Meal