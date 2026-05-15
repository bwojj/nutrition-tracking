import './assets/AddFoodData.css';
import { MealsContext } from './Context/Context.js';
import { useContext, useState } from 'react';
import { saveFood } from './api/mealApi.js';

function AddFoodData({ isOpen, onClose, onModalClose, info, setIsLoading, date, onFoodAdded, selectedDate }) {
    const { meals } = useContext(MealsContext);

    const [formData, setFormData] = useState({
        food_id: info.food_id,
        meal_name: info.meal,
        food_name: info.food_name,
        serving_size: info.serving_size,
        calories: info.calories,
        protein: info.protein,
        carbs: info.carbs,
        fat: info.fat,
        fiber: info.fiber,
        sugar: info.sugar,
        saturated_fat: info.saturated_fat,
        polyunsaturated_fat: info.polyunsaturated_fat,
        monounsaturated_fat: info.monounsaturated_fat,
        trans_fat: info.trans_fat,
        cholesterol: info.cholesterol,
        sodium: info.sodium,
        potassium: info.potassium,
        vitamin_a: info.vitamin_a,
        vitamin_c: info.vitamin_c,
        calcium: info.calcium,
    });

    function handleNumServingsChange(e) {
        const value = Number(e.target.value);
        const servingSize = value > 1 ? `${value} x ${info.serving_size}` : info.serving_size;
        setFormData({
            food_id: info.food_id,
            meal_name: formData.meal_name,
            food_name: info.food_name,
            serving_size: servingSize,
            calories: Math.round(info.calories * value),
            protein: Math.round(info.protein * value),
            carbs: Math.round(info.carbs * value),
            fat: Math.round(info.fat * value),
            fiber: Math.round(info.fiber * value),
            sugar: Math.round(info.sugar * value),
            saturated_fat: Math.round(info.saturated_fat * value),
            polyunsaturated_fat: Math.round(info.polyunsaturated_fat * value),
            monounsaturated_fat: Math.round(info.monounsaturated_fat * value),
            trans_fat: Math.round(info.trans_fat * value),
            cholesterol: Math.round(info.cholesterol * value),
            sodium: Math.round(info.sodium * value),
            potassium: Math.round(info.potassium * value),
            vitamin_a: Math.round(info.vitamin_a * value),
            vitamin_c: Math.round(info.vitamin_c * value),
            calcium: Math.round(info.calcium * value),
        });
    }

    function handleChange(e) {
        const { id, value } = e.target;
        setFormData({ ...formData, [id]: value });
    }

    const handleSubmit = async (e) => {
        setIsLoading(true);
        e.preventDefault();
        console.log(formData);
        await saveFood(formData, date);
        if (onFoodAdded) await onFoodAdded();
        onClose();
        onModalClose();
        setIsLoading(false);
    };

    if (!isOpen) return null;

    return (
        <div className="afd-overlay" onClick={onClose}>
            <div
                className="afd-card"
                role="dialog"
                aria-labelledby="afd-title"
                onClick={(e) => e.stopPropagation()}
            >
                {/* HEADER */}
                <div className="afd-header">
                    <div className="afd-header-text">
                        <div className="afd-eyebrow">Add to log</div>
                        <h2 className="afd-title" id="afd-title">{info.food_name}</h2>
                        <div className="afd-subtitle">per {info.serving_size}</div>
                    </div>
                    <button type="button" className="afd-close" aria-label="Close" onClick={onClose}>✕</button>
                </div>

                {/* BODY */}
                <div className="afd-body">
                    <div className="afd-form-grid">
                        <label className="afd-field">
                            <span className="afd-field-label">Serving size</span>
                            <select id="serve-size" defaultValue={info.serving_size} onChange={handleChange}>
                                <option value={info.serving_size}>{info.serving_size}</option>
                            </select>
                        </label>

                        <label className="afd-field">
                            <span className="afd-field-label">Servings</span>
                            <input
                                id="num-servings"
                                type="number"
                                min="0"
                                step="0.25"
                                defaultValue={1}
                                onChange={handleNumServingsChange}
                            />
                        </label>

                        <label className="afd-field">
                            <span className="afd-field-label">Meal</span>
                            <select id="meal_name" defaultValue={info.meal} onChange={handleChange}>
                                {meals.map((element) => (
                                    <option key={element} value={element}>{element}</option>
                                ))}
                            </select>
                        </label>
                    </div>

                    <div className="afd-totals">
                        <div className="afd-total-tile calories">
                            <span className="afd-total-label">Calories</span>
                            <span className="afd-total-value">
                                <span className="afd-calories">{formData.calories}</span>
                                <span className="afd-total-unit">kcal</span>
                            </span>
                        </div>
                        <div className="afd-total-tile protein">
                            <span className="afd-total-label">Protein</span>
                            <span className="afd-total-value">
                                <span className="afd-macro">{formData.protein}</span>
                                <span className="afd-total-unit">g</span>
                            </span>
                        </div>
                        <div className="afd-total-tile carbs">
                            <span className="afd-total-label">Carbs</span>
                            <span className="afd-total-value">
                                <span className="afd-macro">{formData.carbs}</span>
                                <span className="afd-total-unit">g</span>
                            </span>
                        </div>
                        <div className="afd-total-tile fat">
                            <span className="afd-total-label">Fat</span>
                            <span className="afd-total-value">
                                <span className="afd-macro">{formData.fat}</span>
                                <span className="afd-total-unit">g</span>
                            </span>
                        </div>
                    </div>
                </div>

                {/* FOOTER */}
                <div className="afd-footer">
                    <button type="button" className="afd-btn afd-btn-ghost" onClick={onClose}>Cancel</button>
                    <button type="button" className="afd-btn afd-btn-primary" onClick={handleSubmit}>
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M12 5v14" /><path d="M5 12h14" />
                        </svg>
                        Add to {formData.meal_name}
                    </button>
                </div>
            </div>
        </div>
    );
}

export default AddFoodData;
