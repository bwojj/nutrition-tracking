import { useState } from 'react';
import './assets/Meal.css';
import NutritionFacts from './NutritionFacts.jsx';
import { HiOutlineInformationCircle } from 'react-icons/hi';
import { LuTrash2 } from 'react-icons/lu';
import { deleteFood } from './api/mealApi.js';

function Meal(props) {
    const [selectedFood, setSelectedFood] = useState(null);
    const [open, setOpen] = useState(true);
    const [activeFood, setActiveFood] = useState(null);

    const totalCalculate = (name) => {
        let total = 0;
        props.foodData.forEach((value) => (total += value[name]));
        return total;
    };

    const onDelete = async (id) => {
        const r = await deleteFood(id);
        if (r === 'Success') {
            props.setFoodData((prev) => prev.filter((f) => f.id !== id));
        }
    };

    const openAddFoodModal = (name) => {
        props.setMeal(name);
        props.onOpen();
    };

    const cals = totalCalculate('calories');
    const p    = totalCalculate('protein');
    const c    = totalCalculate('carbs');
    const f    = totalCalculate('fat');

    const foods = props.foodData
        ? props.foodData.filter((el) => el.meal === props.mealName)
        : [];

    return (
        <div className="meal-row">
            <button
                type="button"
                className="meal-bar"
                onClick={() => setOpen((o) => !o)}
            >
                <div className="meal-bar-left">
                    <span className="meal-bar-name">{props.mealName}</span>
                    <span
                        role="button"
                        tabIndex={0}
                        className="meal-add-chip"
                        onClick={(e) => {
                            e.stopPropagation();
                            openAddFoodModal(props.mealName);
                        }}
                        onKeyDown={(e) => {
                            if (e.key === 'Enter' || e.key === ' ') {
                                e.preventDefault();
                                e.stopPropagation();
                                openAddFoodModal(props.mealName);
                            }
                        }}
                        aria-label={`Add food to ${props.mealName}`}
                    >
                        +
                    </span>
                </div>

                <div className="meal-bar-right">
                    <span className="meal-bar-stat">
                        <span className="num">{cals}</span>
                        <span className="unit">Cals</span>
                    </span>
                    <span className="meal-bar-stat">
                        <span className="num">{p}</span>
                        <span className="unit">P</span>
                    </span>
                    <span className="meal-bar-stat">
                        <span className="num">{c}</span>
                        <span className="unit">C</span>
                    </span>
                    <span className="meal-bar-stat">
                        <span className="num">{f}</span>
                        <span className="unit">F</span>
                    </span>
                </div>
            </button>

            {open && (
                <div className="meal-drawer">
                    {foods.length > 0 ? (
                        <ul className="food-list">
                            {foods.map((element) => (
                                <li
                                    key={element.id}
                                    tabIndex={0}
                                    className={`food-line ${activeFood === element.id ? 'active' : ''}`}
                                    onClick={() =>
                                        setActiveFood(
                                            activeFood === element.id ? null : element.id
                                        )
                                    }
                                >
                                    <span className="food-line-name">{element.food_name}</span>
                                    <div className="food-line-right">
                                        <div className="food-line-stats">
                                            <span className="food-line-stat">
                                                <span className="num">{element.calories}</span>
                                                <span className="unit">Cals</span>
                                            </span>
                                            <span className="food-line-stat">
                                                <span className="num">{element.protein}</span>
                                                <span className="unit">P</span>
                                            </span>
                                            <span className="food-line-stat">
                                                <span className="num">{element.carbs}</span>
                                                <span className="unit">C</span>
                                            </span>
                                            <span className="food-line-stat">
                                                <span className="num">{element.fat}</span>
                                                <span className="unit">F</span>
                                            </span>
                                        </div>
                                        <div
                                            className="food-line-actions"
                                            onClick={(e) => e.stopPropagation()}
                                        >
                                            <button
                                                type="button"
                                                className="icon-btn"
                                                aria-label="Nutrition facts"
                                                onClick={() => setSelectedFood(element)}
                                            >
                                                <HiOutlineInformationCircle size={18} />
                                            </button>
                                            <button
                                                type="button"
                                                className="icon-btn icon-btn-danger"
                                                aria-label="Delete"
                                                onClick={() => onDelete(element.id)}
                                            >
                                                <LuTrash2 size={16} />
                                            </button>
                                        </div>
                                    </div>
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <div className="meal-empty">No foods</div>
                    )}
                </div>
            )}

            <NutritionFacts
                isOpen={selectedFood !== null}
                onClose={() => setSelectedFood(null)}
                foodData={selectedFood}
            />
        </div>
    );
}

export default Meal;
