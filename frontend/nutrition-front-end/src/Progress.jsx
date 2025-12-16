import './assets/Progress.css'
import { FaWeight } from "react-icons/fa";
import { FaBullseye } from "react-icons/fa";
import { FaUtensils } from "react-icons/fa";

function Progress(){
    return(
        <div className="progress-container">
            <h1 className="progress-title">Progress Tracker</h1>
            <div className="tracking-icons">
                <div className="icon-info">
                    <FaWeight size={45} color={'#1d693d'}/>
                    <h2 className="tracking-title">Current Weight:</h2>
                    <span className="progress-data">163 lbs</span>
                </div>
                <div className="icon-info">
                    <FaBullseye size={45} color={'#1d693d'}/>
                    <h2 className="tracking-title">Goal Weight:</h2>
                    <span className="progress-data">155 lbs</span>
                </div>
                <div className="icon-info">
                    <FaUtensils size={45} color={'#1d693d'}/>
                    <h2 className="tracking-title">Eating Plan:</h2>
                    <span className="progress-data">Weight Loss</span>
                </div>
            </div>
        </div>
    );
}

export default Progress; 