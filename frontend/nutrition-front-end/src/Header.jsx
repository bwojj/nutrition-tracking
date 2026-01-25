import msuLogo from './assets/msuWhite1.png'
import './assets/Header.css'
import { useState } from 'react';
import { createPortal } from 'react-dom'

const BASE_URL = import.meta.env.VITE_API_URL;

function Header({ setIsMicroModalOpen, setIsProgressModalOpen, setIsLoggedIn, username }){

    const [animate, setAnimate] = useState(false); 

    

    const logout = async () => {
        try{
            const response = await fetch(`${BASE_URL}logout/`, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
            });
            if(response.ok){
                setIsLoggedIn(false);
            }

        } catch(error){
            console.log("Failed", error);
        }
    }

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
                        <li onClick={() => setIsMicroModalOpen(true)} className="menu-item">Micronutrients</li>
                        <li onClick={() => setIsProgressModalOpen(true)} className="menu-item">Progress</li>
                        <li onClick={logout} className="menu-item">Log-Out</li>
                        <li></li>
                        <li className="menu-item">Signed in as: <span style={{fontWeight: 'bold', marginLeft: 5}}>{username}</span></li>
                    </ul>
                </div>
            </div>
        </div>,
        document.getElementById('header')
    );
}

export default Header 