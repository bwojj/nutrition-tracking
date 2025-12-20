import './assets/Meals.css'
import { useState, useEffect } from 'react';
import Meal from './Meal';

function Meals({ onOpen }){
        const [mealData, setMealData] = useState([]); 
        const [isLoading, setIsLoading] = useState(true);
    
        useEffect(() => {
            const fetchMealData = async () => {
                try{
                    const response = await fetch("http://127.0.0.1:8000/api/meals/");
                    if(response.ok){
                        const data = await response.json();
                        setMealData(data);
                    } 
                } catch(error){
                    console.log("Failed to fetch", error)
                } finally {
                    setIsLoading(false); 
                }
            }
    
            fetchMealData()
        }, []);


    return(
        <div className="meals">
            {mealData.map((element, index) => (
                <Meal key={index} onOpen={onOpen} mealName={element.meal_name}/> 
            ))}
        </div>
    );
}

export default Meals