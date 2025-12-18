import AddFood from './AddFood';
import './assets/MainBox.css'
import Calories from './Calories';
import Meals from './Meals';
import Micronutrients from './Micronutrients';
import Progress from './Progress';
import AddFoodData from './AddFoodData';
import { useState } from 'react';

function MainBox(){

    const [isModalOpen, setIsModalOpen] = useState(false);

    // const toggleModal = () => setIsModalOpen(!isModalOpen);

    return(
        <div className="main">
            <AddFood isOpen={isModalOpen}/>
            <div className="top-main">
                <Calories/>
                <Meals onOpen={() => setIsModalOpen(true)}/>
            </div>
            <div className="bottom-main">
                <Micronutrients/>
                <Progress/>
            </div>
        </div>
    );
}

export default MainBox