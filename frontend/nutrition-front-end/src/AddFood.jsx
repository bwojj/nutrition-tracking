import AddFoodData from './AddFoodData';
import './assets/AddFood.css'
import { useState } from 'react';
import { createPortal } from 'react-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { Search } from 'lucide-react';

function AddFood({ meal, date, setIsLoading, isOpen, setIsModalOpen, onDataOpen, isDataModalOpen, onDataClose, selectedDate, searchFoods, getRefresh, foodDatabase}){

    const [apiFoods, setApiFoods] = useState([]);

    
    const [search, setSearch] = useState("");

    function handleChange(event){
        setSearch(event.target.value);
    }

    let searchFilteredFoods = foodDatabase.filter((food) => (
        food.food_name.toLowerCase().includes(search.toLowerCase())
    ));

    function onClose(){
        setIsModalOpen(false);
        setSearch("");
        setApiFoods([]);
    }

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };

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
        serving_size: "",
        calories: 0, 
        protein: 0, 
        carbs: 0, 
        fat: 0,
        fiber: 0,
        sugar: 0,
        saturated_fat: 0,
        polyunsaturated_fat: 0,
        monounsaturated_fat: 0,
        trans_fat: 0,
        cholesterol: 0,
        sodium: 0,
        potassium: 0,
        vitamin_a: 0,
        vitamin_c: 0,
        calcium: 0,
        meal: meal,
    });
        

    function dataOpen(data){
        setDataSent({
            food_name: data.food_name, 
            serving_size: data.serving_size,
            calories: data.calories, 
            protein: data.protein, 
            carbs: data.carbs, 
            fat: data.fat, 
            fiber: data.fiber,
            sugar: data.sugar,
            saturated_fat: data.saturated_fat,
            polyunsaturated_fat: data.polyunsaturated_fat,
            monounsaturated_fat: data.monounsaturated_fat,
            trans_fat: data.trans_fat,
            cholesterol: data.cholesterol,
            sodium: data.sodium,
            potassium: data.potassium,
            vitamin_a: data.vitamin_A,
            vitamin_c: data.vitamin_C,
            calcium: data.calcium,
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
                    <Search className="search-icon" size={20} />
                    <input className="search" onKeyDown={handleKeyDown} onChange={handleChange} placeholder="Search Foods"/>
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
                                    <span className="food-name">{element.food_name}</span>
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
                <AddFoodData date={date} onFoodAdded={getRefresh} setIsLoading={setIsLoading} info={dataSent} onModalClose={onClose} isOpen={isDataModalOpen} onClose={onDataClose}/>
            </div>
        </div>,
        document.body
    );
}

export default AddFood; 