import './assets/Progress.css'
import { FaWeight } from "react-icons/fa";
import { FaBullseye } from "react-icons/fa";
import { FaUtensils } from "react-icons/fa";

function Progress({ onOpen, progressData }){
    return(
        <div className="progress-container" onClick={onOpen}>
            <h1 className="progress-title">Progress Tracker</h1>
            <div className="tracking-icons">
                <div className="icon-info">
                    <FaWeight size={45} color={'#22c55e'}/>
                    <h2 className="tracking-title">Current Weight:</h2>
                    <span className="progress-data">{progressData.current_weight} lbs</span>
                </div>
                <div className="icon-info">
                    <FaBullseye size={45} color={'#22c55e'}/>
                    <h2 className="tracking-title">Goal Weight:</h2>
                    <span className="progress-data">{progressData.goal_weight} lbs</span>
                </div>
                <div className="icon-info">
                    <FaUtensils size={45} color={'#22c55e'}/>
                    <h2 className="tracking-title">Eating Plan:</h2>
                    <span className="progress-data">Weight Loss</span>
                </div>
            </div>
        </div>
    );
}

export default Progress; 