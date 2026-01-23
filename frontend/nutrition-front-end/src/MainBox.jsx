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
import { getFoodData, getFoods } from './api/mealApi';
import { getDays, getProgress } from './api/userApi';

function MainBox({ isLoggedIn, isLoading, setIsLoading, isMicroModalOpen, setIsMicroModalOpen, isProgressModalOpen, setIsProgressModalOpen}){
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isDataModalOpen, setIsDataModalOpen] = useState(false);
    const [meal, setMeal] = useState("");
    const [foodData, setFoodData] = useState([]);
    const [progressData, setProgressData] = useState([]);
    const [selectedDate, setSelectedDate] = useState(new Date().toISOString().split('T')[0]);
    const [daysData, setDaysData] = useState([]);
    const [foodDatabase, setFoodDatabase] = useState([]);

    const today = new Date().toISOString().split('T')[0]; 

    const getRefresh = async () => {
        const [dataResponse, dayResponse] = await Promise.all([
            getFoodData(selectedDate),
            getDays()
        ]);
        if(dataResponse){
            setFoodData(dataResponse);
        }
        if(dayResponse){
            setDaysData(dayResponse);
        }
    }
    useEffect(() => {
  if (!isLoggedIn) return;

  let cancelled = false;

  const loadAll = async () => {
    try {
      const [progressResponse, dayResponse, foodResponse, itemsResponse] =
        await Promise.all([
          getProgress(),
          getDays(),
          getFoodData(selectedDate),
          getFoods(),
        ]);

      if (cancelled) return;

      setProgressData(progressResponse || []);
      setDaysData(dayResponse || []);
      setFoodData(foodResponse || []);
      setFoodDatabase(itemsResponse || [])
    } catch (err) {
      console.error("MainBox load error:", err);
    }
  };

  loadAll();

  return () => {
    cancelled = true; 
  };
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
                    food_name: product.product_name.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' '), 
                    calories: n['energy-kcal_serving'],
                    protein: n['proteins_serving'],
                    carbs: n['carbohydrates_serving'],
                    fat: n['fat_serving'],
                    brand: product.brands,
                    serving_size: product.serving_size,
                }
            });
            
        } catch(error){
            console.log("Search Failed", error); 
        }

    }
    console.log(foodDatabase);

    if (!progressData.length || !daysData.length) {
        return <LoadingScreen/>
    }
    return(
        <div className="main">
            <select value={selectedDate} id="selected-date" className={selectedDate === today ? 'today' : ''}onChange={(event) => setSelectedDate(event.target.value)}>
                {daysData.map((element) => (
                    <option className="option" value={element.date}>{element.date === today ? 'Today' : element.date}</option>
                ))}; 
            </select>
            <AddFood 
                isOpen={isModalOpen} setIsModalOpen={setIsModalOpen}
                isDataModalOpen={isDataModalOpen} onDataOpen={() => setIsDataModalOpen(true)}
                onDataClose={() => setIsDataModalOpen(false)}
                setIsLoading={setIsLoading}
                setMeal={setMeal} 
                meal={meal} 
                searchFoods={searchFoods} 
                date={selectedDate}
                getRefresh={getRefresh} 
                foodDatabase={foodDatabase}
            />
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