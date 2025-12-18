import './assets/AddFoodData.css'

function AddFoodData({ isOpen, onClose }){
    if (!isOpen) return null;

    return(
        <div className="add-food-data-container">
            <div className="add-food-data-header">
                <h2 className="food-info">Chicken</h2>
                <div className="x-data-wrapper">
                    <span onClick={onClose} className="x-data">{"\u00D7"}</span>
                </div>
            </div>
            <div className="serving-size">
                <label for="serve-size">Serving Size</label>
                <select id="serve-size">
                    <option value="1oz" selected>1oz</option>
                </select>
            </div>
            <div className="serving-num">
                <label for="num-serving">Number of Servings</label>
                <input id="num-servings" type="number"/>
            </div>
            <div className="serving-num">
                <label for="meal">Meal</label>
                <select id="meal">
                    <option value="Breakfast">Breakfast</option>
                    <option value="Lunch">Lunch</option>
                    <option value="Dinner">Dinner</option>
                </select>
            </div>
            <div className="food-add-data">
                <div className="label-data">
                    <span className="cals">Calories</span>
                    <span className="cal-value">100</span>
                </div>
                <div className="macro-data">
                    <div className="label-data" style={{border: '2px solid #7231bd'}}>
                        <span style={{color: '#7231bd', fontWeight: 'bold'}}>Protein</span>
                        <span>100</span>
                    </div>
                    <div className="label-data" style={{border: '2px solid #31bd98'}}>
                        <span style={{color: '#31bd98', fontWeight: 'bold'}}>Carbs</span>
                        <span>100</span>
                    </div>
                    <div className="label-data" style={{border: '2px solid #ffad21ff'}}>
                        <span style={{color: '#ffad21ff', fontWeight: 'bold'}}>Fat</span>
                        <span>100</span>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default AddFoodData; 