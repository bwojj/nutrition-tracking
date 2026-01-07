import AddFood from './AddFood';
import './assets/MainBox.css'
import Calories from './Calories';
import Meals from './Meals';
import Micronutrients from './Micronutrients';
import Progress from './Progress';
import FullMicronutrients from './FullMicronutrients';
import FullProgress from './FullProgress';
import { useState, useEffect } from 'react';
import LoadingScreen from './LoadingScreen';

function MainBox({ isMicroModalOpen, isProgressModalOpen, setIsMicroModalOpen, setIsProgressModalOpen}){
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isDataModalOpen, setIsDataModalOpen] = useState(false);
    const [meal, setMeal] = useState("");

    const [foodData, setFoodData] = useState([]);
    const [progressData, setProgressData] = useState([]);
    const [selectedDate, setSelectedDate] = useState(new Date().toISOString().split('T')[0]);

    const [daysData, setDaysData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const today = new Date().toISOString().split('T')[0]; 


    const refreshData = async () => {
        setIsLoading(true);
        try{
            const response = await fetch(`http://127.0.0.1:8000/api/food-data/?date=${selectedDate}`);
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
    const deleteFood = async (id) => {
        setIsLoading(true);
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/food-data/${id}/`, {
                method: 'DELETE',
            });

            if (response.ok) {
                setFoodData(prevData => prevData.filter(food => food.id !== id));
            } else {
                console.error("Failed to delete item");
            }
        } catch (error) {
            console.error("Error deleting food:", error);
        } finally {
            setIsLoading(false);
        }
    };
    const getProgress = async () => {
        setIsLoading(true);
        try {
            const response = await fetch('http://127.0.0.1:8000/api/progress/');
            if (response.ok){
                const data = await response.json();
                setProgressData(data); 
            }
        } catch(error) {
            console.log('Failed to Fetch', error)
        } finally {
            setIsLoading(false); 
        }
    };
    const getDays = async () => {
        setIsLoading(true);
        try {
            const response = await fetch("http://127.0.0.1:8000/api/days/")
            if (response.ok){
                const data = await response.json(); 
                setDaysData(data);
            } 
        } catch(error){
            console.log('Failed to fetch', error)
        } finally{
            setIsLoading(false);
        }
    }

    useEffect(() => { refreshData(); }, [selectedDate]);
    useEffect(() => { getProgress(); }, []);
    useEffect(() => { getDays(); }, []);
    
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
    if (isLoading) {
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
                onDataClose={() => setIsDataModalOpen(false)} refreshData={refreshData}
                setMeal={setMeal} meal={meal} searchFoods={searchFoods} setIsLoading={setIsLoading} date={selectedDate}/>
            <FullMicronutrients foodData={foodData} isOpen={isMicroModalOpen} onClose={() => setIsMicroModalOpen(false)}/>
            <FullProgress isLoading={isLoading} refreshData={getProgress} progressData={progressData} isOpen={isProgressModalOpen} onClose={() => setIsProgressModalOpen(false)}/>
            <div className="top-main">
                <Calories foodData={foodData} progressData={progressData}/>
                <Meals onDelete={deleteFood} setMeal={setMeal} foodData={foodData} onOpen={() => setIsModalOpen(true)}/>
            </div>
            <div className="bottom-main">
                <Micronutrients foodData={foodData} onOpen={() => setIsMicroModalOpen(true)}/>
                <Progress progressData={progressData[0]} onOpen={() => setIsProgressModalOpen(true)}/>
            </div>
        </div>
    );
}

export default MainBox