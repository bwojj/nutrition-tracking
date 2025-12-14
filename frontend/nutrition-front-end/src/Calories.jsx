import './assets/Calories.css'

function Calories(){
    return(
        <div className="calories">
            <h1 className="calorie-title">Total Calories</h1>
            <svg width="100" height="50">
                <circle r="45" cx="50" cy="50" fill="red"/> 
            </svg>
        </div>
    );
}

export default Calories 