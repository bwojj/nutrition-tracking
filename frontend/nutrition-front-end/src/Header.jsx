import msuLogo from './assets/msuWhite1.png' 
import './assets/Header.css'
import { useState } from 'react';

function Header(){

    const [animate, setAnimate] = useState(false); 

    const handleAnimation = () => {
        setAnimate(prev => !prev); 
    }

    return(
        <div className="header">
            <img src={msuLogo} alt="image"/>
            <h1 className="title">MSUtrition</h1>
            <div onClick={handleAnimation} class="hamburger">
                <span id="line1" className={`line ${animate ? 'active' : ''}`}></span>
                <span id="line2" className={`line ${animate ? 'active' : ''}`}></span>
                <span id="line3" className={`line ${animate ? 'active' : ''}`}></span>
            </div>
            <div className={`menu ${animate ? 'active' : ''}`}>
                <h2 className="menu-title">Menu</h2>
                <ul className="menu-list">
                    <li className="menu-item">Micronutrients</li>
                    <li className="menu-item">Progress</li>
                </ul>
            </div>
        </div>
    );
}

export default Header 