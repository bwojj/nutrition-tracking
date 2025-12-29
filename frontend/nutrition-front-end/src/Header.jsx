import msuLogo from './assets/msuWhite1.png' 
import './assets/Header.css'
import { useState } from 'react';
import { createPortal } from 'react-dom'

function Header(){

    const [animate, setAnimate] = useState(false); 

    const handleAnimation = () => {
        setAnimate(prev => !prev); 
    }

    return createPortal(
        <div className="header">
            <img src={msuLogo} alt="image"/>
            <h1 className="title">MSUtrition</h1>
            <div onClick={handleAnimation} class={`hamburger ${animate ? 'active' : ''}`}>
                <span id="line1" className={`line ${animate ? 'active' : ''}`}></span>
                <span id="line2" className={`line ${animate ? 'active' : ''}`}></span>
                <span id="line3" className={`line ${animate ? 'active' : ''}`}></span>
            </div>
            <div className={`empty ${animate ? 'active' : ''}`}></div>
            <div className={`header-overlay ${animate ? 'active' : ''}`}>
                <div className={`menu ${animate ? 'active' : ''}`}>
                    <h2 className="menu-title">Menu</h2>
                    <ul className="menu-list">
                        <li className="menu-item">Micronutrients</li>
                        <li className="menu-item">Progress</li>
                    </ul>
                </div>
            </div>
        </div>,
        document.getElementById('header')
    );
}

export default Header 