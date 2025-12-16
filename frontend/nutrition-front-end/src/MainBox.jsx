import './assets/MainBox.css'
import Calories from './Calories';
import Meals from './Meals';
import Micronutrients from './Micronutrients';
import Progress from './Progress';

function MainBox(){
    return(
        <div className="main">
            <div className="top-main">
                <Calories/>
                <Meals/>
            </div>
            <div className="bottom-main">
                <Micronutrients/>
                <Progress/>
            </div>
        </div>
    );
}

export default MainBox