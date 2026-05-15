import msuLogo from './assets/msuWhite1.png'
import './assets/Header.css'
import { Calendar, LogOut } from "lucide-react";
import { useState, useEffect, useRef } from 'react';
import { createPortal } from 'react-dom'
import { getAuthHeaders, clearTokens } from './api/authApi.js';
import { getDays } from './api/userApi.js';
import { useDaysContext } from './Context/DayContext.jsx';

const BASE_URL = import.meta.env.VITE_API_URL;

const getLocalDateString = () => {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
};

function Header({ setIsLoggedIn, username }){

    const { selectedDate, setSelectedDate } = useDaysContext();
    const [daysData, setDaysData] = useState([]);
    const [isOpen, setIsOpen] = useState(false);
    const profileRef = useRef(null);

    const today = getLocalDateString(); 

    const logout = async () => {
        try {
            const response = await fetch(`${BASE_URL}logout/`, {
                method: "POST",
                headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
                credentials: 'include',
            });
            // Clear tokens regardless of response (for Safari)
            clearTokens();
            if (response.ok) {
                setIsLoggedIn(false);
            } else {
                // Still log out locally even if server call fails
                setIsLoggedIn(false);
            }
        } catch (error) {
            console.log("Failed", error);
            // Clear tokens and log out even on network error
            clearTokens();
            setIsLoggedIn(false);
        }
    }

    useEffect(() => {
        const handleClickOutside = (e) => {
            if (profileRef.current && !profileRef.current.contains(e.target)) {
                setIsOpen(false);
            }
        };
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

    // Loads days into select
    useEffect(() => {

    let cancelled = false;

    const loadDays = async () => {
        try {
        const dayResponse = await getDays(); 

        if (cancelled) return;

        setDaysData(dayResponse || []);
        } catch (err) {
        console.error("Days load error:", err);
        }
    };

    loadDays();

    return () => {
        cancelled = true; 
    };
    }, []);


    return createPortal(
        <div className="header">
            <img src={msuLogo} alt="image"/>
            <h1 className="title">MSUtrition</h1>
            <div className="empty"></div>

            <div className={selectedDate === today ? 'daysSelectToday' : 'daysSelect'}>
                <Calendar size={20} color="#e8f5ec" />
                <select value={selectedDate} id="selected-date-header" className={selectedDate === today ? 'today' : ''}onChange={(event) => setSelectedDate(event.target.value)}>
                    {daysData.map((element) => (
                        <option className="option" value={element.date}>{element.date === today ? 'Today' : element.date}</option>
                    ))}; 
                </select>
            </div>

            {username && (
                <div className="profile-wrapper" ref={profileRef}>
                    <div className="profile" onClick={() => setIsOpen(o => !o)}>
                        <div className="pfp">{username.substr(0, 2).toUpperCase()}</div>
                        <p className="username">{username}</p>
                    </div>
                    {isOpen && (
                        <div className="profile-dropdown">
                            <p className="dropdown-username">{username}</p>
                            <div className="dropdown-divider" />
                            <button className="dropdown-logout" onClick={logout}>
                                <LogOut size={14} />
                                Log Out
                            </button>
                        </div>
                    )}
                </div>
            )}

        </div>,
        document.getElementById('header')
    );
}

export default Header