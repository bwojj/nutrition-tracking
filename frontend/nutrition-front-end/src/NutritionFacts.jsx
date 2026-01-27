import './assets/NutritionFacts.css'
import { createPortal } from 'react-dom'

function NutritionFacts({ isOpen, onClose, foodData }) {
    if (!isOpen || !foodData) return null;

    return createPortal(
        <div className="nutrition-label-modal__overlay" onClick={onClose}>
            <div className="nutrition-label-modal__container" onClick={(e) => e.stopPropagation()}>
                <div className="nutrition-label-modal__label">
                    <button className="nutrition-label-modal__close-btn" onClick={onClose}>
                        {"\u00D7"}
                    </button>
                    <div className="nutrition-label-modal__header">
                        <h1 className="nutrition-label-modal__title">Nutrition Facts</h1>
                    </div>

                    <div className="nutrition-label-modal__divider-thick"></div>

                    <div className="nutrition-label-modal__serving-section">
                        <div className="nutrition-label-modal__food-name">{foodData.food_name}</div>
                        {foodData.brand && (
                            <div className="nutrition-label-modal__brand">{foodData.brand}</div>
                        )}
                        <div className="nutrition-label-modal__serving-size">
                            <span className="nutrition-label-modal__serving-label">Serving Size</span>
                            <span className="nutrition-label-modal__serving-value">{foodData.serving_size}</span>
                        </div>
                    </div>

                    <div className="nutrition-label-modal__divider-extra-thick"></div>

                    <div className="nutrition-label-modal__amount-header">
                        <span className="nutrition-label-modal__amount-label">Amount Per Serving</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__calories-section">
                        <div className="nutrition-label-modal__calories-main">
                            <span className="nutrition-label-modal__calories-label">Calories</span>
                            <span className="nutrition-label-modal__calories-value">{Math.round(foodData.calories)}</span>
                        </div>
                        <div className="nutrition-label-modal__calories-fat">
                            Calories from Fat {Math.round(foodData.fat * 9)}
                        </div>
                    </div>

                    <div className="nutrition-label-modal__divider-medium"></div>

                    <div className="nutrition-label-modal__daily-value-header">
                        <span>% Daily Value*</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row">
                        <span><strong>Total Fat</strong> {foodData.fat}g</span>
                        <span>{Math.round((foodData.fat / 78) * 100)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row nutrition-label-modal__nutrient-row--indented">
                        <span>Saturated Fat {foodData.saturated_fat}g</span>
                        <span>{Math.round((foodData.saturated_fat / 20) * 100)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row nutrition-label-modal__nutrient-row--indented">
                        <span>Trans Fat {foodData.trans_fat}g</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row nutrition-label-modal__nutrient-row--indented">
                        <span>Polyunsaturated Fat {foodData.polyunsaturated_fat}g</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row nutrition-label-modal__nutrient-row--indented">
                        <span>Monounsaturated Fat {foodData.monounsaturated_fat}g</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row">
                        <span><strong>Cholesterol</strong> {foodData.cholesterol}mg</span>
                        <span>{Math.round((foodData.cholesterol / 300) * 100)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row">
                        <span><strong>Sodium</strong> {foodData.sodium}mg</span>
                        <span>{Math.round((foodData.sodium / 2300) * 100)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row">
                        <span><strong>Total Carbohydrate</strong> {foodData.carbs}g</span>
                        <span>{Math.round((foodData.carbs / 275) * 100)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row nutrition-label-modal__nutrient-row--indented">
                        <span>Dietary Fiber {foodData.fiber}g</span>
                        <span>{Math.round((foodData.fiber / 28) * 100)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row nutrition-label-modal__nutrient-row--indented">
                        <span>Total Sugars {foodData.sugar}g</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__nutrient-row">
                        <span><strong>Protein</strong> {foodData.protein}g</span>
                    </div>

                    <div className="nutrition-label-modal__divider-extra-thick"></div>

                    <div className="nutrition-label-modal__vitamin-row">
                        <span>Vitamin A</span>
                        <span>{Math.round(foodData.vitamin_A)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__vitamin-row">
                        <span>Vitamin C</span>
                        <span>{Math.round(foodData.vitamin_C)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__vitamin-row">
                        <span>Calcium</span>
                        <span>{Math.round(foodData.calcium)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-thin"></div>

                    <div className="nutrition-label-modal__vitamin-row">
                        <span>Potassium</span>
                        <span>{Math.round((foodData.potassium / 4700) * 100)}%</span>
                    </div>

                    <div className="nutrition-label-modal__divider-medium"></div>

                    <div className="nutrition-label-modal__footnote">
                        * The % Daily Value (DV) tells you how much a nutrient in a serving of food contributes to a daily diet. 2,000 calories a day is used for general nutrition advice.
                    </div>
                </div>
            </div>
        </div>,
        document.body
    );
}

export default NutritionFacts
