import './assets/MainBox.css'
import Calories from './Calories';
import Meals from './Meals';

function MainBox(){
    return(
        <div className="main">
            <Calories/>
            <Meals/>
        </div>
    );
}

export default MainBox