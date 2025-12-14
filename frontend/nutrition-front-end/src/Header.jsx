import msuLogo from './assets/msuWhite1.png' 
import './assets/Header.css'

function Header(){

    return(
        <div className="header">
            <img src={msuLogo} alt="image"/>
            <h1 className="title">MSUtrition</h1>
            <div class="hamburger">
                <span className="line"></span>
                <span className="line"></span>
                <span className="line"></span>
            </div>
        </div>
    );
}

export default Header 