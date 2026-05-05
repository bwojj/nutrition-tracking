import './assets/Calories.css';
import Macro from './Macros.jsx';
import LoadingScreen from './LoadingScreen.jsx';
import { useEffect, useState } from 'react';

function Calories({ foodData, progressData, isLoading }) {
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

    const r = windowWidth >= 1471 ? 138 : 94;
    const cx = 200;
    const cy = 210;
    const x1 = cx - r;
    const x2 = cx + r;
    const y  = cy;
    const circumfrence = Math.PI * r; 

    let currentCalories = 0; 
    foodData.forEach(value => { currentCalories += value.calories; });
    const targetCalories = progressData?.[0]?.goal_calories || 2000;

    const currentOffset = circumfrence - (circumfrence * percentage) / 100;

    useEffect(() => {
        const targetProgress = Math.round((currentCalories / targetCalories) * 100) || 0;
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
    }, [currentCalories, targetCalories]);

    const macroData = (macroName) => {
        let currentMacros = 0; 
        foodData.forEach(value => { currentMacros += value[macroName]; }); 
        return currentMacros; 
    };

    if (isLoading || !progressData || progressData.length === 0) {
        return <LoadingScreen />;
    }

    return (
        <div className="calories">
            <h1 className="calorie-title">Total Calories</h1>
            <svg width="500" height="260" viewBox="0 0 400 240" className="calorie-progress">
                <path d={`M ${x1} ${y} A ${r} ${r} 0 0 1 ${x2} ${y}`} fill="none" stroke="#1e3028" strokeWidth="24" strokeLinecap="round" />
                <path
                    d={`M ${x1} ${y} A ${r} ${r} 0 0 1 ${x2} ${y}`}
                    fill="none"
                    stroke="#22c55e"
                    strokeWidth="24"
                    strokeLinecap="round"
                    style={{
                        strokeDasharray: circumfrence,
                        strokeDashoffset: currentOffset,
                        transition: isResizing ? "none" : "stroke-dashoffset 0.1s linear",
                        filter: "drop-shadow(0 0 3px #22c55e90)",
                    }}
                />
            </svg>
            <div className="calorie-number-ratio">
                <span className="calorie-number">{percentage}%</span>
                <span className="calorie-ratio">{currentCalories} / {targetCalories}</span>
            </div>
            <div className="macros">
                <Macro color="#3b82f6" name="Protein" amount={macroData("protein")} goal={progressData[0].goal_protein}/>
                <Macro color="#ef4444" name="Carbs" amount={macroData("carbs")} goal={progressData[0].goal_carbs}/>
                <Macro color="#eab308" name="Fat" amount={macroData("fat")} goal={progressData[0].goal_fat}/>
            </div>
        </div>
    );
}

export default Calories;