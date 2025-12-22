import './assets/Macro.css'
import {useEffect, useState } from 'react';

function Macro(props){

    const [windowWidth, setWindowWidth] = useState(window.innerWidth);

    useEffect(() => {
        const handleResize = () => setWindowWidth(window.innerWidth);

        window.addEventListener('resize', handleResize); 

        return () => window.removeEventListener('resize', handleResize); 
    }, []);
    
    const radius = windowWidth >= 1471 ? 60 : (windowWidth <= 400 ? 35 : 40); 
    

    const circumfrence = 2 * Math.PI * radius; 

    const [offset, setOffset] = useState(circumfrence);
    const [percentage, setPercentage] = useState(0); 
    
    useEffect(() => {
        const targetProgress = (Number(props.amount) / Number(props.goal)) * 100;

        const intervalId = setInterval(() => {
            setPercentage((prev) => {
                if (prev >= targetProgress){
                    clearInterval(intervalId);
                    return prev; 
                }

                const nextValue = prev + 1; 

                setOffset(circumfrence - (circumfrence * nextValue) / 100);

                return nextValue; 
            })
        }, 30);

        return () => clearInterval(intervalId);
        }, [circumfrence, props.amount]);
    


    return(
        <div className="macro-container">
            <svg className="macro-circles">
                <circle className="circle" r={radius} cx="50%" cy="50%" fill="none" stroke="#c6c8bb" strokeWidth={20}/>
                <circle className="progress-circle" r={radius} cx="50%" cy="50%" fill="none" stroke={props.color} strokeWidth={20}
                style={{
                    strokeDasharray: circumfrence,
                    strokeDashoffset: offset, 
                    strokeLinecap: 'round',
                    transform: 'rotate(-180deg)',
                    transformOrigin: '50% 50%',
                    transition: "stroke-dash-offset 0.5s ease",
                }}/>
            </svg>
            <div className="macro-name-amount">
                <span className="macro-name">{props.name}</span>
                <span className="macro-amount">{props.amount}g</span>
            </div>
            <span className="macro-percentage">{percentage}%</span>
        </div>
    );
}

export default Macro 