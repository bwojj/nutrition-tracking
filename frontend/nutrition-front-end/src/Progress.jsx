import './assets/Progress.css'
import { Dumbbell, Target, Utensils } from 'lucide-react';

function Progress({ onOpen, progressData }){
    return(
        <div className="progress-container" onClick={onOpen}>
            <h1 className="progress-title">Progress Tracker</h1>
            <div className="tracking-icons">
                <div className="icon-info">
                    <Dumbbell size={40} color={'#22c55e'}/>
                    <h2 className="tracking-title">Current Weight:</h2>
                    <span className="progress-data">{progressData.current_weight} lbs</span>
                </div>
                <div className="icon-info">
                    <Target size={40} color={'#22c55e'}/>
                    <h2 className="tracking-title">Goal Weight:</h2>
                    <span className="progress-data">{progressData.goal_weight} lbs</span>
                </div>
                <div className="icon-info">
                    <Utensils size={40} color={'#22c55e'}/>
                    <h2 className="tracking-title">Eating Plan:</h2>
                    <span className="progress-data">Weight Loss</span>
                </div>
            </div>
        </div>
    );
}

export default Progress; 