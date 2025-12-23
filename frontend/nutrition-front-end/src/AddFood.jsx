import AddFoodData from './AddFoodData';
import './assets/AddFood.css'
import { useState } from 'react';
import { createPortal } from 'react-dom'

function AddFood({ meal, isOpen, onClose, onDataOpen, isDataModalOpen, onDataClose, refreshData}){


    let foodDatabase = [
    {
        id: 1,
        name: "Grilled Chicken Breast",
        calories: 165,
        protein: 31,
        carbs: 0,
        fat: 3.6
    },
    {
        id: 2,
        name: "Brown Rice (1 cup)",
        calories: 218,
        protein: 4.5,
        carbs: 45,
        fat: 1.6
    },
    {
        id: 3,
        name: "Avocado (Medium)",
        calories: 240,
        protein: 3,
        carbs: 12,
        fat: 22
    },
    {
        id: 4,
        name: "Greek Yogurt (Non-fat)",
        calories: 100,
        protein: 17,
        carbs: 6,
        fat: 0.4
    },
    {
        id: 5,
        name: "Almonds (1 oz)",
        calories: 164,
        protein: 6,
        carbs: 6,
        fat: 14
    },
    {
        id: 6,
        name: "Sweet Potato (Medium)",
        calories: 103,
        protein: 2,
        carbs: 24,
        fat: 0.2
    },
    {
        id: 7,
        name: "Atlantic Salmon",
        calories: 208,
        protein: 20,
        carbs: 0,
        fat: 13
    }
    ];

    const [search, setSearch] = useState("");

    function handleChange(event){
        setSearch(event.target.value);
    }

    const searchFilteredFoods = foodDatabase.filter((food) => (
        food.name.toLowerCase().includes(search.toLowerCase())
    ));

    const [dataSent, setDataSent] = useState({
        food_name: "", 
        calories: 0, 
        protein: 0, 
        carbs: 0, 
        fat: 0, 
        meal: "",
    });
        

    function dataOpen(data){
        setDataSent({
            food_name: data.name, 
            calories: data.calories, 
            protein: data.protein, 
            carbs: data.carbs, 
            fat: data.fat, 
            meal: meal, 
        })
        onDataOpen();
    }

    if (!isOpen) return null; 

    return createPortal(
        <div className="full-screen-overlay" onClick={onClose}>
            <div className="add-food-container" onClick={(e) => e.stopPropagation()}>
                {isDataModalOpen && (
                    <div className="inner-modal-overlay" onClick={onDataClose} />
                )}
                <div className="add-food-header">
                    <div style={{flex: 1}}></div>
                    <h1 className="add-food-title">Add Food</h1>
                    <div className="x-wrapper">
                        <span onClick={onClose} className="x">{"\u00D7"}</span>
                    </div>
                </div>
                <input className="search" onChange={handleChange} placeholder="Search Foods"/>
                <div className="foods">
                    {searchFilteredFoods.map((element, index) => (
                        <div onClick={() => dataOpen(element)} className="food-items-inner" key={index}>
                            <div className="name">
                                <span className="food-name">{element.name}</span>
                            </div>
                            <div className="data">
                                <div className="data-top">
                                    <span className="food-data">{element.calories}Cals</span>
                                    <span className="food-data">{element.protein}P</span>
                                </div>
                                <div className="data-bottom">
                                    <span className="food-data">{element.carbs}C</span>
                                    <span className="food-data">{element.fat}F</span>
                                </div>
                            </div>
                        </div>
                        ))}
                </div>
                <AddFoodData info={dataSent} onModalClose={onClose} refreshData={refreshData} isOpen={isDataModalOpen} onClose={onDataClose}/>
            </div>
        </div>,
        document.body
    );
}

export default AddFood; 