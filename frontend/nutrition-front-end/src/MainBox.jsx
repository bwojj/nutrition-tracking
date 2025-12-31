import AddFood from './AddFood';
import './assets/MainBox.css'
import Calories from './Calories';
import Meals from './Meals';
import Micronutrients from './Micronutrients';
import Progress from './Progress';
import FullMicronutrients from './FullMicronutrients';
import FullProgress from './FullProgress';
import { useState, useEffect } from 'react';

function MainBox(){

    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isDataModalOpen, setIsDataModalOpen] = useState(false);
    const [isMicroModalOpen, setIsMicroModalOpen] = useState(false);
    const [isProgressModalOpen, setIsProgressModalOpen] = useState(false);
    const [meal, setMeal] = useState("");

    const [foodData, setFoodData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const refreshData = async () => {
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
    const deleteFood = async (id) => {
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
        }
    };
    useEffect(() => { refreshData(); }, []);

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


    return(
        <div className="main">
            <AddFood isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}
                isDataModalOpen={isDataModalOpen} onDataOpen={() => setIsDataModalOpen(true)}
                onDataClose={() => setIsDataModalOpen(false)} refreshData={refreshData}
                setMeal={setMeal} meal={meal} searchFoods={searchFoods}/>
            <FullMicronutrients isOpen={isMicroModalOpen} onClose={() => setIsMicroModalOpen(false)}/>
            <FullProgress isOpen={isProgressModalOpen} onClose={() => setIsProgressModalOpen(false)}/>
            <div className="top-main">
                <Calories foodData={foodData}/>
                <Meals onDelete={deleteFood} setMeal={setMeal} foodData={foodData} onOpen={() => setIsModalOpen(true)}/>
            </div>
            <div className="bottom-main">
                <Micronutrients foodData={foodData} onOpen={() => setIsMicroModalOpen(true)}/>
                <Progress onOpen={() => setIsProgressModalOpen(true)}/>
            </div>
        </div>
    );
}

export default MainBox