import './assets/MainBox.css';
import AddFood from './AddFood';
import Calories from './Calories';
import Meals from './Meals';
import Micronutrients from './Micronutrients';
import Progress from './Progress';
import FullMicronutrients from './FullMicronutrients';
import FullProgress from './FullProgress';
import LoadingScreen from './LoadingScreen';
import { useState, useEffect } from 'react';
import { getFoodData } from './api/mealApi';
import { getDays, getProgress } from './api/userApi';

function MainBox({ isLoggedIn, isMicroModalOpen, setIsMicroModalOpen, isProgressModalOpen, setIsProgressModalOpen}){
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isDataModalOpen, setIsDataModalOpen] = useState(false);
    const [meal, setMeal] = useState("");
    const [foodData, setFoodData] = useState([]);
    const [progressData, setProgressData] = useState([]);
    const [selectedDate, setSelectedDate] = useState(new Date().toISOString().split('T')[0]);
    const [daysData, setDaysData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const today = new Date().toISOString().split('T')[0]; 

    useEffect(() => {
    if (isLoggedIn) {
        setIsLoading(true);
        const getRefresh = async () => {
            const dataResponse = await getFoodData(selectedDate);
            if(dataResponse){
                setFoodData(dataResponse); 
            }
        }
        const userProgress = async () => {
            const progressResponse = await getProgress();
            if(progressResponse){
                setProgressData(progressResponse);
            }
        }
        const userDays = async () => {
            const dayResponse = await getDays();
            if(dayResponse){
                setDaysData(dayResponse); 
            }
        }
        userDays();
        userProgress();
        getRefresh();
        setIsLoading(false);
    }
}, [isLoggedIn, selectedDate]);
    
    const searchFoods = async (query) => {

        const url = new URL("https://world.openfoodfacts.org/cgi/search.pl"); 

        const selectedFields = [
            "product_name",
            "brands",
            "nutriments",
            "code",
            "serving_size",
        ].join(",");

        const params = {
            search_terms: query,
            search_simple: 1, 
            action: "process",
            json: 1,
            page_size: 5,
            fields: selectedFields
        };

        url.search = new URLSearchParams(params).toString();

        try {
            const response = await fetch(url, {
                method: "GET",
                headers: {
                    "User-Agent": "MSUTracking/1.0 (wojobeemer@gmail.com)"
                }
            });

            if(!response.ok) throw new Error("Network response failed");

            const data = await response.json();
            const products = data.products; 

            return products.filter(product => {
                const n = product.nutriments;

                return (
                    product.code && 
                    product.product_name &&
                    n['energy-kcal_serving'] !== undefined &&
                    n['proteins_serving'] !== undefined &&
                    n['carbohydrates_serving'] !== undefined &&
                    n['fat_serving'] !== undefined 
                );
            }).map(product => {
                const n = product.nutriments;

                return {
                    id: product.code,
                    name: product.product_name.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' '), 
                    calories: n['energy-kcal_serving'],
                    protein: n['proteins_serving'],
                    carbs: n['carbohydrates_serving'],
                    fat: n['fat_serving'],
                    brand: product.brands,
                }
            });
            
        } catch(error){
            console.log("Search Failed", error); 
        }

    }

    if(isLoading || !progressData?.length){
        return <LoadingScreen/>
    }
    return(
        <div className="main">
            <select value={selectedDate} id="selected-date" className={selectedDate === today ? 'today' : ''}onChange={(event) => setSelectedDate(event.target.value)}>
                {daysData.map((element) => (
                    <option className="option" value={element.date}>{element.date === today ? 'Today' : element.date}</option>
                ))}; 
            </select>
            <AddFood isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}
                isDataModalOpen={isDataModalOpen} onDataOpen={() => setIsDataModalOpen(true)}
                onDataClose={() => setIsDataModalOpen(false)} refreshData={getFoodData}
                setMeal={setMeal} meal={meal} searchFoods={searchFoods} setIsLoading={setIsLoading} date={selectedDate}/>
            <FullMicronutrients foodData={foodData} isOpen={isMicroModalOpen} onClose={() => setIsMicroModalOpen(false)}/>
            <FullProgress isOpen={isProgressModalOpen} onClose={() => setIsProgressModalOpen(false)} progressData={progressData}/>
            
            
            <div className="top-main">
                {progressData.length > 0 ? <Calories foodData={foodData} progressData={progressData} isLoading={isLoading}/> : null }
                <Meals setFoodData={setFoodData} setMeal={setMeal} foodData={foodData} onOpen={() => setIsModalOpen(true)}/>
            </div>
            <div className="bottom-main">
                <Micronutrients foodData={foodData} onOpen={() => setIsMicroModalOpen(true)}/>
                {progressData.length > 0 ? <Progress progressData={progressData[0]} onOpen={() => setIsProgressModalOpen(true)}/> : null}
            </div>
        </div>
    );
}

export default MainBox