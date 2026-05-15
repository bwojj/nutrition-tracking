import AddFoodData from './AddFoodData.jsx';
import SavedMealForm from './SavedMealForm.jsx';
import './assets/AddFood.css'
import { useState, useEffect } from 'react';
import { createPortal } from 'react-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { Search, X, Clock, Star, Utensils, Apple, ListChecks, Trash2 } from 'lucide-react';
import { saveFavorite, removeFavorite, getFoods, getSavedMeals, addSaveMealData, addMultipleFoods, deleteSavedMeal } from './api/mealApi.js';

const MEAL_TABS = ['Breakfast', 'Lunch', 'Dinner', 'Snacks'];

const CATEGORY_CHIPS = [
    { icon: <Clock size={14} />, label: 'Recent' },
    { icon: <Star size={14} />, label: 'Favorites' },
    { icon: <Utensils size={14} />, label: 'My Meals' },
    { icon: <Apple size={14} />, label: 'Foods' },
];

function AddFood({ meal, setMeal, date, setIsLoading, isOpen, setIsModalOpen, onDataOpen, isDataModalOpen, onDataClose, searchFoodsDB, getRefresh, foodDatabase, foodDatabasebyID}){

    const [search, setSearch] = useState("");
    const [searchResults, setSearchResults] = useState([]);
    const [isSearching, setIsSearching] = useState(false);
    const [hasSearched, setHasSearched] = useState(false);
    const [activeChip, setActiveChip] = useState('Recent');
    const [favorites, setFavorites] = useState([]);
    const [foodKey, setFoodKey] = useState(0);
    const [smOpen, setSmOpen] = useState(false);
    const [isSelectMode, setIsSelectMode] = useState(false);
    const [selectedIndices, setSelectedIndices] = useState(new Set());
    const [servings, setServings] = useState({});
    const [savedMeals, setSavedMeals] = useState([]);

    useEffect(() => {
        if (!isOpen) return;
        document.body.style.overflow = 'hidden';
        return () => { document.body.style.overflow = ''; };
    }, [isOpen]);

    useEffect(() => {
        if (!isOpen) return;
        getFoods('favorite').then(data => setFavorites(data || []));
    }, [isOpen]);

    useEffect(() => {
        if (!isOpen || activeChip !== 'My Meals') return;
        getSavedMeals().then(data => setSavedMeals(data || []));
    }, [isOpen, activeChip]);

    async function handleAddMultipleFoods() {
        if (selectedIndices.size === 0) return;
        setIsLoading(true);
        const foods = [...selectedIndices].map(index => {
            const food = displayFoods[index];
            const scale = getScale(food, index);
            const servNum = servings[index];
            const unit = food.serving_size?.match(/^[\d.]+\s*(.*)/)?.[1] || 'g';
            const serving_size = servNum !== undefined
                ? `${servNum} ${unit}`
                : food.serving_size;
            return {
                food_name: food.food_name,
                serving_size,
                calories: Math.round(food.calories * scale),
                protein: Math.round(food.protein * scale),
                carbs: Math.round(food.carbs * scale),
                fat: Math.round(food.fat * scale),
                fiber: Math.round((food.fiber || 0) * scale),
                sugar: Math.round((food.sugar || 0) * scale),
                saturated_fat: Math.round((food.saturated_fat || 0) * scale),
                polyunsaturated_fat: Math.round((food.polyunsaturated_fat || 0) * scale),
                monounsaturated_fat: Math.round((food.monounsaturated_fat || 0) * scale),
                trans_fat: Math.round((food.trans_fat || 0) * scale),
                cholesterol: Math.round((food.cholesterol || 0) * scale),
                sodium: Math.round((food.sodium || 0) * scale),
                potassium: Math.round((food.potassium || 0) * scale),
                vitamin_a: Math.round((food.vitamin_A || 0) * scale),
                vitamin_c: Math.round((food.vitamin_C || 0) * scale),
                calcium: Math.round((food.calcium || 0) * scale),
            };
        });
        await addMultipleFoods(foods, date, meal);
        await getRefresh();
        setIsLoading(false);
        onClose();
    }

    async function handleAddSavedMeal(savedMealId) {
        setIsLoading(true);
        await addSaveMealData(savedMealId, date, meal);
        await getRefresh();
        setIsLoading(false);
        onClose();
    }

    async function handleDeleteSavedMeal(savedMealId) {
        await deleteSavedMeal(savedMealId);
        setSavedMeals(prev => prev.filter(m => m.id !== savedMealId));
    }

    const favoriteIdSet = new Set(favorites.map(f => f.id));
    const isFavorited = (food) => favoriteIdSet.has(food.id);

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

    const favoritesChip = search.length > 0
        ? favorites.slice(0, 20).filter((food) =>
            food.food_name.toLowerCase().includes(search.toLowerCase())
          )
        : favorites.slice(0, 20);

    useEffect(() => {
        if (!search.trim()) {
            setSearchResults([]);
            setHasSearched(false);
            setIsSearching(false);
            return;
        }
        setIsSearching(true);
        const timer = setTimeout(async () => {
            const results = await searchFoodsDB(search);
            setSearchResults(results || []);
            setHasSearched(true);
            setIsSearching(false);
        }, 300);
        return () => clearTimeout(timer);
    }, [search, searchFoodsDB]);

    function handleChange(event){
        setSearch(event.target.value);
    }

    function resetSelectMode() {
        setIsSelectMode(false);
        setSelectedIndices(new Set());
        setServings({});
    }

    function toggleSelectMode() {
        setIsSelectMode(prev => !prev);
        setSelectedIndices(new Set());
        setServings({});
    }

    function toggleFoodSelection(index) {
        setSelectedIndices(prev => {
            const next = new Set(prev);
            if (next.has(index)) next.delete(index);
            else next.add(index);
            return next;
        });
    }

    function handleServingChange(index, val) {
        setServings(prev => ({ ...prev, [index]: val }));
    }

    function getScale(food, index) {
        const m = food.serving_size?.match(/^([\d.]+)/);
        const origNum = parseFloat(m?.[1]) || 1;
        const raw = servings[index];
        const current = raw !== undefined ? (parseFloat(raw) || 0) : origNum;
        return origNum > 0 ? current / origNum : 1;
    }

    function onClose(){
        setIsModalOpen(false);
        setSearch("");
        resetSelectMode();
    }

    const chipFoods = activeChip === 'My Meals' ? [] : activeChip === 'Foods' ? foodsByID20 : activeChip === 'Favorites' ? favoritesChip : defaultFiltered;
    const displayFoods = hasSearched ? searchResults : chipFoods;


    const [dataSent, setDataSent] = useState({
        food_id: null,
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
        if (isFavorited(food)) {
            setFavorites(prev => prev.filter(f => f.id !== food.id));
            await removeFavorite(food.id);
        } else {
            setFavorites(prev => [...prev, food]);
            await saveFavorite(food.id);
        }
        const [favData] = await Promise.all([
            getFoods('favorite'),
            getRefresh(),
        ]);
        setFavorites(favData || []);
    }
    function dataOpen(data){
        setFoodKey(k => k + 1);
        setDataSent({
            food_id: data.id,
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
                    <div className="add-food-header-left">
                        <span className="add-food-eyebrow">Add to log</span>
                        <h1 className="add-food-title">Search Foods</h1>
                    </div>
                    <button className="add-food-close" onClick={onClose}><X size={16} /></button>
                </div>

                <div className="meal-tabs">
                    {MEAL_TABS.map(m => (
                        <button key={m} className={`meal-tab${m === meal ? ' meal-tab--active' : ''}`} onClick={() => setMeal(m)}>{m}</button>
                    ))}
                </div>

                <div className="search-area">
                    <div className="searchBox">
                        <Search className="search-icon" size={18} />
                        <input
                            className="search"
                            value={search}
                            onChange={handleChange}
                            placeholder="Search foods, brands, meals…"
                        />
                    </div>
                    <div className="category-chips">
                        {CATEGORY_CHIPS.map(({ icon, label }) => (
                            <button key={label} className={`category-chip${label === activeChip ? ' category-chip--active' : ''}`} onClick={() => { setActiveChip(label); resetSelectMode(); }}>
                                {icon}
                                {label}
                            </button>
                        ))}
                    </div>
                    {activeChip !== 'My Meals' && (
                        <div className="select-foods-row">
                            <button
                                className={`category-chip select-foods-chip${isSelectMode ? ' select-foods-chip--active' : ''}`}
                                onClick={toggleSelectMode}
                            >
                                <ListChecks size={14} />
                                Select Foods
                            </button>
                            <AnimatePresence>
                                {isSelectMode && (
                                    <motion.button
                                        key="add-foods-to-meal"
                                        className="select-save-btn"
                                        initial={{ opacity: 0 }}
                                        animate={{ opacity: 1 }}
                                        exit={{ opacity: 0 }}
                                        transition={{ duration: 0.15 }}
                                        onClick={handleAddMultipleFoods}
                                    >
                                        Add Foods to Meal
                                    </motion.button>
                                )}
                            </AnimatePresence>
                        </div>
                    )}
                    {activeChip === 'My Meals' && (
                        <button className="add-saved-meal-btn" onClick={() => setSmOpen(true)}>
                            + Add a Saved Meal
                        </button>
                    )}
                </div>

                <div className="foods">
                    {activeChip === 'My Meals' ? (
                        savedMeals.length === 0 ? (
                            <p className="no-results">No saved meals yet — create one above.</p>
                        ) : (
                            savedMeals.map((meal) => (
                                <div key={meal.id} className="saved-meal-card">
                                    <div className="saved-meal-card-header">
                                        <span className="saved-meal-card-name">{meal.meal_name}</span>
                                        <div className="saved-meal-card-header-right">
                                            <span className="saved-meal-card-count">{meal.foods.length} item{meal.foods.length !== 1 ? 's' : ''}</span>
                                            <button
                                                className="icon-btn icon-btn-danger"
                                                aria-label="Delete saved meal"
                                                onClick={(e) => { e.stopPropagation(); handleDeleteSavedMeal(meal.id); }}
                                            ><Trash2 size={15} /></button>
                                            <button
                                                className="saved-meal-add-btn"
                                                onClick={() => handleAddSavedMeal(meal.id)}
                                            >+</button>
                                        </div>
                                    </div>
                                    <div className="saved-meal-card-foods">
                                        {meal.foods.map((food) => {
                                            const f = typeof food === 'object' ? food : foodDatabase.find(d => d.id === food);
                                            if (!f) return null;
                                            return (
                                                <div key={f.id} className="saved-meal-food-row">
                                                    <div className="saved-meal-food-info">
                                                        <span className="saved-meal-food-name">{f.food_name}</span>
                                                        <span className="saved-meal-food-serving">{f.serving_size}</span>
                                                    </div>
                                                    <div className="saved-meal-food-macros">
                                                        <span><span className="macro-p">P</span> {f.protein}</span>
                                                        <span><span className="macro-c">C</span> {f.carbs}</span>
                                                        <span><span className="macro-f">F</span> {f.fat}</span>
                                                        <span className="macro-cal">{f.calories} cal</span>
                                                    </div>
                                                </div>
                                            );
                                        })}
                                    </div>
                                </div>
                            ))
                        )
                    ) : isSearching ? (
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
                                displayFoods.map((element, index) => {
                                    const isSel = isSelectMode && selectedIndices.has(index);
                                    const servMatch = isSelectMode ? element.serving_size?.match(/^([\d.]+)\s*(.*)/) : null;
                                    const servNum = servMatch ? servMatch[1] : '1';
                                    const servUnit = servMatch ? (servMatch[2] || 'g') : 'g';
                                    const scale = isSelectMode ? getScale(element, index) : 1;
                                    return (
                                        <motion.div
                                            onClick={() => isSelectMode ? toggleFoodSelection(index) : dataOpen(element)}
                                            className={`food-items-inner${isSelectMode ? ' food-items-inner--select-mode' : ''}${isSel ? ' food-items-inner--selected' : ''}`}
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
                                                {isSel && (
                                                    <div className="food-inline-macros">
                                                        <span><span className="macro-p">P</span> {Math.round(element.protein * scale)}</span>
                                                        <span><span className="macro-c">C</span> {Math.round(element.carbs * scale)}</span>
                                                        <span><span className="macro-f">F</span> {Math.round(element.fat * scale)}</span>
                                                        <span className="macro-cal">{Math.round(element.calories * scale)} cal</span>
                                                    </div>
                                                )}
                                            </div>
                                            <div className="food-macros">
                                                <span><span className="macro-p">P</span> {isSelectMode ? Math.round(element.protein * scale) : element.protein}</span>
                                                <span><span className="macro-c">C</span> {isSelectMode ? Math.round(element.carbs * scale) : element.carbs}</span>
                                                <span><span className="macro-f">F</span> {isSelectMode ? Math.round(element.fat * scale) : element.fat}</span>
                                                <span className="macro-cal">{isSelectMode ? Math.round(element.calories * scale) : element.calories} cal</span>
                                            </div>
                                            {!isSelectMode && (
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
                                            )}
                                            {isSelectMode && (
                                                <div className="food-row-serving" onClick={(e) => e.stopPropagation()}>
                                                    <span className="food-serving-label">Serving</span>
                                                    <div className="food-serving-input-wrap">
                                                        <input
                                                            type="number"
                                                            className="food-serving-input"
                                                            value={servings[index] !== undefined ? servings[index] : servNum}
                                                            onChange={(e) => handleServingChange(index, e.target.value)}
                                                        />
                                                        <span className="food-serving-unit">{servUnit}</span>
                                                    </div>
                                                </div>
                                            )}
                                        </motion.div>
                                    );
                                })
                            )}
                        </AnimatePresence>
                    )}
                </div>


                <AddFoodData key={foodKey} date={date} onFoodAdded={getRefresh} setIsLoading={setIsLoading} info={dataSent} onModalClose={onClose} isOpen={isDataModalOpen} onClose={onDataClose}/>
                <SavedMealForm
                    isOpen={smOpen}
                    onClose={() => setSmOpen(false)}
                    recentFoods={foodDatabase.slice(0, 20)}
                    setIsLoading={setIsLoading}
                    searchFoodsDB={searchFoodsDB}
                />
            </div>
        </div>,
        document.body
    );
}

export default AddFood;
