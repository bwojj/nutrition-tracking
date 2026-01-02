import { createPortal } from "react-dom";
import './assets/FullProgress.css'

function FullProgress({ isOpen, onClose }){

    if (!isOpen) return null; 

    return createPortal(
        <div className="full-screen-overlay" onClick={onClose}>
            <div className="full-progress-box">
                <h1 className="full-progress-title">Manage Progress</h1>
                <div className="progress-input">
                    <label for="currentWeight">Current Weight</label>
                    <input id="currentWeight" type="number"/>

                    <label for="goalWeight">Goal Weight</label>
                    <input id="goalWeight" type="number"/>

                    <label for="goal">Goal</label>
                    <select id="goal">
                    </select>

                    <label for="activity">Activity</label>
                    <select id="activity">
                    </select>
                </div>
            </div>
        </div>,
        document.body
    );
}

export default FullProgress