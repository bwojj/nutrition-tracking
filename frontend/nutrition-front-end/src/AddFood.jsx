import AddFoodData from './AddFoodData';
import './assets/AddFood.css'
import { useState } from 'react';
import { createPortal } from 'react-dom'
import { motion, AnimatePresence } from 'framer-motion'

function AddFood({ meal, isOpen, onClose, onDataOpen, isDataModalOpen, onDataClose, refreshData, searchFoods}){

    const [apiFoods, setApiFoods] = useState([]);

    let foodDatabase = [
    {
        id: 1,
        name: "Grilled Chicken Breast",
        calories: 165,
        protein: 31,
        carbs: 0,
        fat: 3.6,
        brand: "Default"
    },
    {
        id: 2,
        name: "Brown Rice (1 cup)",
        calories: 218,
        protein: 4.5,
        carbs: 45,
        fat: 1.6,
         brand: "Default"
    },
    {
        id: 3,
        name: "Avocado (Medium)",
        calories: 240,
        protein: 3,
        carbs: 12,
        fat: 22,
         brand: "Default"
    },
    {
        id: 4,
        name: "Greek Yogurt (Non-fat)",
        calories: 100,
        protein: 17,
        carbs: 6,
        fat: 0.4,
         brand: "Default"
    },
    {
        id: 5,
        name: "Almonds (1 oz)",
        calories: 164,
        protein: 6,
        carbs: 6,
        fat: 14,
        brand: "Default"
    },
    {
        id: 6,
        name: "Sweet Potato (Medium)",
        calories: 103,
        protein: 2,
        carbs: 24,
        fat: 0.2,
        brand: "Default"
    },
    {
        id: 7,
        name: "Atlantic Salmon",
        calories: 208,
        protein: 20,
        carbs: 0,
        fat: 13,
        brand: "Default"
    }
    ];

    const [search, setSearch] = useState("");

    function handleChange(event){
        setSearch(event.target.value);
    }

    let searchFilteredFoods = foodDatabase.filter((food) => (
        food.name.toLowerCase().includes(search.toLowerCase())
    ));

    async function handleSearch(){
        if(search.length <= 0){
            setApiFoods([]);
        }
        else if(searchFilteredFoods.length <= 0){
            const results = await searchFoods(search.toLowerCase());
            setApiFoods(results || []); 
        }
    }
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
                <div className="searchBox">
                    <input className="search" onChange={handleChange} placeholder="Search Foods"/>
                    <button className="searchBTN" onClick={handleSearch}>Search</button>
                </div>
                <div className="foods">
                    <AnimatePresence>
                        {(searchFilteredFoods.length <= 0 ? apiFoods : searchFilteredFoods).map((element, index) => (
                            <motion.div 
                                onClick={() => dataOpen(element)} 
                                className="food-items-inner" 
                                key={index}
                                layout 
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                exit={{ opacity: 0, scale: 0.95 }}
                                transition={{ duration: 0.2 }}
                            >
                                <div className="name">
                                    <span className="food-name">{element.name}</span>
                                    <span className="brand-name">{element.brand}</span>
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
                            </motion.div>
                            ))}
                        </AnimatePresence>
                </div>
                <AddFoodData info={dataSent} onModalClose={onClose} refreshData={refreshData} isOpen={isDataModalOpen} onClose={onDataClose}/>
            </div>
        </div>,
        document.body
    );
}

export default AddFood; 