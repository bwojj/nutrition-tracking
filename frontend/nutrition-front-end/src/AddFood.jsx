import AddFoodData from './AddFoodData.jsx';
import './assets/AddFood.css'
import { useState } from 'react';
import { createPortal } from 'react-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { Search, X, Clock, Star, Utensils, Apple } from 'lucide-react';
import { saveFavorite } from './api/mealApi.js';

const MEAL_TABS = ['Breakfast', 'Lunch', 'Dinner', 'Snacks'];

const CATEGORY_CHIPS = [
    { icon: <Clock size={14} />, label: 'Recent' },
    { icon: <Star size={14} />, label: 'Favorites' },
    { icon: <Utensils size={14} />, label: 'My Meals' },
    { icon: <Apple size={14} />, label: 'Foods' },
];

function AddFood({ meal, date, setIsLoading, isOpen, setIsModalOpen, onDataOpen, isDataModalOpen, onDataClose, foodDatabaseFavorites, searchFoodsDB, getRefresh, foodDatabase, foodDatabasebyID}){

    const [search, setSearch] = useState("");
    const [searchResults, setSearchResults] = useState([]);
    const [isSearching, setIsSearching] = useState(false);
    const [hasSearched, setHasSearched] = useState(false);
    const [activeMeal, setActiveMeal] = useState(meal);
    const [activeChip, setActiveChip] = useState('Recent');
    const [localFavoriteIds, setLocalFavoriteIds] = useState(new Set());

    const favoriteIdSet = new Set(foodDatabaseFavorites.map(f => f.id));
    const isFavorited = (food) => favoriteIdSet.has(food.id) || localFavoriteIds.has(food.id);

    const defaultFiltered = search.length > 0
        ? foodDatabase.filter((food) =>
            food.food_name.toLowerCase().includes(search.toLowerCase())
          )
        : foodDatabase;

    const foodsByID20 = search.length > 0
        ? foodDatabasebyID.slice(0, 20).filter((food) =>
            food.food_name.toLowerCase().includes(search.toLowerCase())
          )
        : foodDatabasebyID.slice(0, 20);
    
    const favorites = search.length > 0
        ? foodDatabaseFavorites.slice(0, 20).filter((food) =>
            food.food_name.toLowerCase().includes(search.toLowerCase())
          )
        : foodDatabaseFavorites.slice(0, 20);

    function handleChange(event){
        setSearch(event.target.value);
        setSearchResults([]);
        setHasSearched(false);
    }

    function onClose(){
        setIsModalOpen(false);
        setSearch("");
        setSearchResults([]);
        setHasSearched(false);
    }

    const handleSearch = async () => {
        if (!search.length) return;
        setIsSearching(true);
        setHasSearched(true);
        const results = await searchFoodsDB(search);
        setSearchResults(results || []);
        setIsSearching(false);
    };

    const handleKeyDown = async (event) => {
        if (event.key === 'Enter') {
            await handleSearch();
        }
    };

    const chipFoods = activeChip === 'Foods' ? foodsByID20 : activeChip == 'Favorites' ? favorites : defaultFiltered;
    const displayFoods = hasSearched ? searchResults : chipFoods;

    console.log(displayFoods);
    console.log(foodDatabaseFavorites);

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

    async function handleFavorite(food) {
        setLocalFavoriteIds(prev => new Set([...prev, food.id]));
        await saveFavorite(food.id);
    }

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
            meal: activeMeal,
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
                    <div className="add-food-header-left">
                        <span className="add-food-eyebrow">Add to log</span>
                        <h1 className="add-food-title">Search Foods</h1>
                    </div>
                    <button className="add-food-close" onClick={onClose}><X size={16} /></button>
                </div>

                <div className="meal-tabs">
                    {MEAL_TABS.map(m => (
                        <button key={m} className={`meal-tab${m === activeMeal ? ' meal-tab--active' : ''}`} onClick={() => setActiveMeal(m)}>{m}</button>
                    ))}
                </div>

                <div className="search-area">
                    <div className="searchBox">
                        <Search className="search-icon" size={18} />
                        <input
                            className="search"
                            value={search}
                            onKeyDown={handleKeyDown}
                            onChange={handleChange}
                            placeholder="Search foods, brands, meals…"
                        />
                        <button className="search-cmdk-chip" onClick={handleSearch}>⌘K</button>
                    </div>
                    <div className="category-chips">
                        {CATEGORY_CHIPS.map(({ icon, label }) => (
                            <button key={label} className={`category-chip${label === activeChip ? ' category-chip--active' : ''}`} onClick={() => setActiveChip(label)}>
                                {icon}
                                {label}
                            </button>
                        ))}
                    </div>
                </div>

                <div className="foods">
                    {isSearching ? (
                        <div className="search-loading">
                            <div className="spinner"></div>
                        </div>
                    ) : (
                        <AnimatePresence>
                            {displayFoods.length === 0 ? (
                                <motion.p
                                    className="no-results"
                                    key="no-results"
                                    initial={{ opacity: 0 }}
                                    animate={{ opacity: 1 }}
                                    exit={{ opacity: 0 }}
                                >No foods found</motion.p>
                            ) : (
                                displayFoods.map((element, index) => (
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
                                            <div className="food-meta">
                                                <span className="brand-name">{element.brand}</span>
                                                {element.serving_size && (
                                                    <><span className="food-meta-sep">·</span><span className="brand-name">{element.serving_size}</span></>
                                                )}
                                            </div>
                                        </div>
                                        <div className="food-macros">
                                            <span><span className="macro-p">P</span> {element.protein}</span>
                                            <span><span className="macro-c">C</span> {element.carbs}</span>
                                            <span><span className="macro-f">F</span> {element.fat}</span>
                                            <span className="macro-cal">{element.calories} cal</span>
                                        </div>
                                        <div className="food-actions">
                                            <button
                                                className="food-favorite-btn"
                                                onClick={(e) => { e.stopPropagation(); handleFavorite(element); }}
                                            ><Star size={14} fill={isFavorited(element) ? 'currentColor' : 'none'} /></button>
                                            <button
                                                className="food-add-btn"
                                                onClick={(e) => { e.stopPropagation(); dataOpen(element); }}
                                            >+</button>
                                        </div>
                                    </motion.div>
                                ))
                            )}
                        </AnimatePresence>
                    )}
                </div>

                <AddFoodData date={date} onFoodAdded={getRefresh} setIsLoading={setIsLoading} info={dataSent} onModalClose={onClose} isOpen={isDataModalOpen} onClose={onDataClose}/>
            </div>
        </div>,
        document.body
    );
}

export default AddFood;
