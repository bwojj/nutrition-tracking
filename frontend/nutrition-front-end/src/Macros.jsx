import './assets/Macro.css'
import {useEffect, useState } from 'react';

function Macro(props){

    const circumfrence = 2 * Math.PI * 60; 
    let progress = 0;
    const targetProgress = (Number(props.amount) / Number(props.goal)) * 100;

    const [offset, setOffset] = useState(circumfrence);
    const [percentage, setPercentage] = useState(0); 
    
    useEffect(() => {
        const intervalId = setInterval(() => {
            if (progress >= targetProgress){
                return (
                    clearInterval(intervalId)
                );
            }
            else{
                // eslint-disable-next-line react-hooks/exhaustive-deps
                progress += 2; 
                setOffset((circumfrence - (circumfrence * progress) / 100));
                setPercentage(progress); 
            };
            }, 60);
        }, []);
    


    return(
        <div className="macro-container">
            <svg>
                <circle className="circle" r="60" cx="37%" cy="50%" fill="none" stroke="#c6c8bb" strokeWidth={20}/>
                <circle className="progress-circle" r="60" cx="37%" cy="50%" fill="none" stroke={props.color} strokeWidth={20}
                style={{
                    strokeDasharray: circumfrence,
                    strokeDashoffset: offset, 
                    strokeLinecap: 'round',
                    transform: 'rotate(-180deg)',
                    transformOrigin: '37% 50%',
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