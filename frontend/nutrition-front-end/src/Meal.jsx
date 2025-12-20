import { useEffect, useState } from 'react';
import './assets/Meal.css'

function Meal(props){
    const [foodData, setFoodData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const fetchFoodData = async () => {
            try{
                const response = await fetch("http://127.0.0.1:8000/api/food-data/");
                if(response.ok){
                    const data = await response.json();
                    setFoodData(data);
                } 
            } catch(error){
                console.log("Failed to fetch", error)
            } finally {
                setIsLoading(false); 
            }
        }

        fetchFoodData()
    }, []);
    
    return(
        <div className="meal">
            <div className="meal-header" style={{
                borderTopRightRadius: props.rounded ? '10px' : '0px',
                borderTopLeftRadius: props.rounded ? '10px' : '0px',
            }}>
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
            {foodData.map((element, index) => (
                <div key={index} className="food">
                    <h3 className="food-name">{element.food_name}</h3>
                    <div className="meal-food-info">
                        <span className="food-value">{element.calories}Cals</span>
                        <span className="food-value">{element.protein}P</span> 
                        <span className="food-value">{element.carbs}C</span> 
                        <span className="food-value">{element.fat}F</span>  
                    </div>
                </div>
            ))}

        </div>
    );
}

export default Meal