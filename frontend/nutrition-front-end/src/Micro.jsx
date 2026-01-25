import './assets/Micro.css'
import MicroProgress from './MicroProgress.jsx';

function Micro(props){
    return(
        <div className="micro-div">
            <span className="micro-name">{props.vitamin}</span>
            <div className="progress-dv">
                <MicroProgress current={props.amount} goal={props.goal}/>
                <span className="micro-goal">{props.goal}</span>
            </div>
        </div>
    );
}

export default Micro 