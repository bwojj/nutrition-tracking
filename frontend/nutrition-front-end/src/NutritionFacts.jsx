import './assets/NutritionFacts.css'
import { createPortal } from 'react-dom'
import { useState, useEffect, useRef } from 'react'
import { updateFoodData, getFoodByID } from './api/mealApi.js'

function NutritionFacts({ isOpen, onClose, foodData, onUpdate }) {
    const [servings, setServings] = useState('1');
    const [baseFood, setBaseFood] = useState(null);
    const prevFoodId = useRef(null);

    const currentId = foodData?.id ?? null;
    if (currentId !== prevFoodId.current) {
        prevFoodId.current = currentId;
        setServings('1');
        setBaseFood(null);
    }

    useEffect(() => {
        if (!isOpen || !foodData) return;
        getFoodByID(foodData.food_from).then(data => {
            if (data && data.length > 0) setBaseFood(data[0]);
        });
    }, [isOpen, foodData]);

    if (!isOpen || !foodData) return null;

    const base = baseFood || foodData;
    const s = parseFloat(servings) || 1;

    const handleSave = async () => {
        await updateFoodData(s, foodData.id);
        if (onUpdate) await onUpdate();
        onClose();
    };

    const micros = [
        { label: 'Fiber',       value: Math.round(base.fiber * s),                unit: 'g'  },
        { label: 'Sugar',       value: Math.round(base.sugar * s),                unit: 'g'  },
        { label: 'Sat. Fat',    value: Math.round(base.saturated_fat * s),        unit: 'g'  },
        { label: 'Trans Fat',   value: Math.round(base.trans_fat * s),            unit: 'g'  },
        { label: 'Poly Fat',    value: Math.round(base.polyunsaturated_fat * s),  unit: 'g'  },
        { label: 'Mono Fat',    value: Math.round(base.monounsaturated_fat * s),  unit: 'g'  },
        { label: 'Cholesterol', value: Math.round(base.cholesterol * s),          unit: 'mg' },
        { label: 'Sodium',      value: Math.round(base.sodium * s),               unit: 'mg' },
        { label: 'Potassium',   value: Math.round(base.potassium * s),            unit: 'mg' },
        { label: 'Calcium',     value: Math.round(base.calcium * s),              unit: '%'  },
        { label: 'Vitamin A',   value: Math.round(base.vitamin_A * s),            unit: '%'  },
        { label: 'Vitamin C',   value: Math.round(base.vitamin_C * s),            unit: '%'  },
    ];

    return createPortal(
        <div className="nf-overlay" onClick={onClose}>
            <div className="nf-modal" onClick={(e) => e.stopPropagation()}>
                <button className="nf-close" onClick={onClose}>✕</button>

                <div className="nf-header">
                    <div className="nf-eyebrow">Nutrition Facts</div>
                    <div className="nf-food-name">{foodData.food_name}</div>
                    {base.brand && <div className="nf-brand">{base.brand}</div>}
                    <div className="nf-serving-row">
                        <span className="nf-serving-size">{base.serving_size} per serving</span>
                        <div className="nf-servings-control">
                            <label className="nf-servings-label" htmlFor="nf-servings">Servings</label>
                            <input
                                id="nf-servings"
                                className="nf-servings-input"
                                type="number"
                                min="0.25"
                                step="0.25"
                                value={servings}
                                onChange={(e) => setServings(e.target.value)}
                            />
                        </div>
                    </div>
                </div>

                <div className="nf-body">
                    <div className="nf-main-macros">
                        <div className="nf-tile nf-tile--calories">
                            <span className="nf-tile-label">Calories</span>
                            <span className="nf-tile-value">{Math.round(base.calories * s)}</span>
                            <span className="nf-tile-unit">kcal</span>
                        </div>
                        <div className="nf-tile nf-tile--protein">
                            <span className="nf-tile-label">Protein</span>
                            <span className="nf-tile-value">{Math.round(base.protein * s)}</span>
                            <span className="nf-tile-unit">g</span>
                        </div>
                        <div className="nf-tile nf-tile--carbs">
                            <span className="nf-tile-label">Carbs</span>
                            <span className="nf-tile-value">{Math.round(base.carbs * s)}</span>
                            <span className="nf-tile-unit">g</span>
                        </div>
                        <div className="nf-tile nf-tile--fat">
                            <span className="nf-tile-label">Fat</span>
                            <span className="nf-tile-value">{Math.round(base.fat * s)}</span>
                            <span className="nf-tile-unit">g</span>
                        </div>
                    </div>

                    <div className="nf-grid">
                        {micros.map(({ label, value, unit }) => (
                            <div className="nf-micro-tile" key={label}>
                                <span className="nf-micro-label">{label}</span>
                                <span className="nf-micro-value">
                                    {value}<span className="nf-micro-unit">{unit}</span>
                                </span>
                            </div>
                        ))}
                    </div>
                </div>

                <div className="nf-footer">
                    <button className="nf-save-btn" onClick={handleSave}>Update Serving</button>
                </div>
            </div>
        </div>,
        document.body
    );
}

export default NutritionFacts
