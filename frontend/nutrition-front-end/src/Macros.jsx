import './assets/Macro.css'
import { useEffect, useState } from 'react';

function Macro(props) {
    const [windowWidth, setWindowWidth] = useState(window.innerWidth);
    const [percentage, setPercentage] = useState(0);
    const [isResizing, setIsResizing] = useState(false);

    useEffect(() => {
        let timeoutId;
        const handleResize = () => {
            setIsResizing(true);
            setWindowWidth(window.innerWidth);
            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => setIsResizing(false), 200);
        };
        window.addEventListener('resize', handleResize);
        return () => {
            window.removeEventListener('resize', handleResize);
            clearTimeout(timeoutId);
        };
    }, []);

    const radius   = windowWidth >= 1385 ? 48 : (windowWidth <= 600 ? 34 : 42);
    const strokeW  = windowWidth >= 1385 ? 16 : (windowWidth <= 600 ? 11 : 13);
    const circumfrence = 2 * Math.PI * radius;

    const visualPercentage = Math.min(percentage, 100);
    const currentOffset = circumfrence - (circumfrence * visualPercentage) / 100;

    useEffect(() => {
        const targetProgress = Math.round((Number(props.amount) / Number(props.goal)) * 100) || 0;
        const duration = 1000; 
        const frameRate = 20;  
        const totalSteps = duration / frameRate;

        const intervalId = setInterval(() => {
            setPercentage((prev) => {
                const distance = targetProgress - prev;

                if (Math.abs(distance) < 1) {
                    clearInterval(intervalId);
                    return targetProgress;
                }

                const step = distance / (totalSteps / 2);
                return prev + (step > 0 ? Math.ceil(step) : Math.floor(step));
            });
        }, frameRate);

        return () => clearInterval(intervalId);
    }, [props.amount, props.goal]);

    return (
        <div className="macro-container">
            <svg className="macro-circles">
                <circle
                    className="circle"
                    r={radius}
                    cx="50%"
                    cy="50%"
                    fill="none"
                    stroke="#1e3028"
                    strokeWidth={strokeW}
                />
                <circle
                    className="progress-circle"
                    r={radius}
                    cx="50%"
                    cy="50%"
                    fill="none"
                    stroke={props.color}
                    strokeWidth={strokeW}
                    style={{
                        strokeDasharray: circumfrence,
                        strokeDashoffset: currentOffset,
                        strokeLinecap: 'round',
                        transform: 'rotate(-90deg)',
                        transformOrigin: '50% 50%',
                        transition: isResizing ? "none" : "stroke-dashoffset 0.1s linear",
                        filter: `drop-shadow(0 0 3px ${props.color}90)`,
                    }}
                />
            </svg>
            <div className="macro-name-amount">
                <span className="macro-name">{props.name}</span>
                <span className="macro-amount">{props.amount}g</span>
            </div>
            <span className="macro-percentage">{percentage}%</span>
        </div>
    );
}

export default Macro;