import './assets/MainBox.css';
import AddFood from './AddFood.jsx';
import Calories from './Calories.jsx';
import Meals from './Meals.jsx';
import Micronutrients from './Micronutrients.jsx';
import Progress from './Progress.jsx';
import FullMicronutrients from './FullMicronutrients.jsx';
import FullProgress from './FullProgress.jsx';
import LoadingScreen from './LoadingScreen.jsx';
import { useState, useEffect } from 'react';
import { getFoodData, getFoods, searchFoodsDB } from './api/mealApi.js';
import { getProgress } from './api/userApi.js';
import { useDaysContext } from './Context/DayContext.jsx';


function MainBox({ isLoggedIn, isLoading, setIsLoading, isMicroModalOpen, setIsMicroModalOpen, isProgressModalOpen, setIsProgressModalOpen}){
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isDataModalOpen, setIsDataModalOpen] = useState(false);
    const [meal, setMeal] = useState("");
    const [foodData, setFoodData] = useState([]);
    const [progressData, setProgressData] = useState([]);
    const [foodDatabase, setFoodDatabase] = useState([]);
    const [foodDatabasebyID, setFoodDatabasebyID] = useState([]); 
    const [foodDatabaseFavorites, setFoodDatabaseFavorites] = useState([]); 

    const { selectedDate } = useDaysContext();


    const getRefresh = async () => {
        const dataResponse = await getFoodData(selectedDate)

        if(dataResponse){
            setFoodData(dataResponse);
        }
    }
    useEffect(() => {
  if (!isLoggedIn) return;

  let cancelled = false;

  const loadAll = async () => {
    try {
      const [progressResponse, foodResponse, itemsResponse, itemsIdResponse, itemsFavoriteResponse] =
        await Promise.all([
          getProgress(),
          getFoodData(selectedDate),
          getFoods('date'),
          getFoods('id'), 
          getFoods('favorite'), 
        ]);

      if (cancelled) return;

      setProgressData(progressResponse || []);
      setFoodData(foodResponse || []);
      setFoodDatabase(itemsResponse || []);
      setFoodDatabasebyID(itemsIdResponse || []);
      setFoodDatabaseFavorites(itemsFavoriteResponse || []); 
    } catch (err) {
      console.error("MainBox load error:", err);
    }
  };

  loadAll();

  return () => {
    cancelled = true; 
  };
}, [isLoggedIn, selectedDate]);

    
    if (!progressData.length) {
        return <LoadingScreen/>
    }
    return(
        <div className="main">
            <AddFood 
                isOpen={isModalOpen} setIsModalOpen={setIsModalOpen}
                isDataModalOpen={isDataModalOpen} onDataOpen={() => setIsDataModalOpen(true)}
                onDataClose={() => setIsDataModalOpen(false)}
                setIsLoading={setIsLoading}
                setMeal={setMeal} 
                meal={meal} 
                searchFoodsDB={searchFoodsDB}
                date={selectedDate}
                getRefresh={getRefresh} 
                foodDatabase={foodDatabase}
                foodDatabasebyID={foodDatabasebyID}
                foodDatabaseFavorites={foodDatabaseFavorites}
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