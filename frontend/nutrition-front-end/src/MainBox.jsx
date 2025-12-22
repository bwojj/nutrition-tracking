import AddFood from './AddFood';
import './assets/MainBox.css'
import Calories from './Calories';
import Meals from './Meals';
import Micronutrients from './Micronutrients';
import Progress from './Progress';
import { useState, useEffect } from 'react';

function MainBox(){

    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isDataModalOpen, setIsDataModalOpen] = useState(false);

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

    useEffect(() => { refreshData(); }, []);


    return(
        <div className="main">
            <AddFood isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}
                isDataModalOpen={isDataModalOpen} onDataOpen={() => setIsDataModalOpen(true)}
                onDataClose={() => setIsDataModalOpen(false)} refreshData={refreshData}/>
            <div className="top-main">
                <Calories foodData={foodData}/>
                <Meals foodData={foodData} onOpen={() => setIsModalOpen(true)}/>
            </div>
            <div className="bottom-main">
                <Micronutrients foodData={foodData}/>
                <Progress/>
            </div>
        </div>
    );
}

export default MainBox