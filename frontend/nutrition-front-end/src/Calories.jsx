import './assets/Calories.css'
import Macro from './Macros';
import { useEffect, useState } from 'react';

function Calories({ foodData }) {
    const [windowWidth, setWindowWidth] = useState(window.innerWidth);

    useEffect(() => {
        const handleResize = () => setWindowWidth(window.innerWidth);

        window.addEventListener('resize', handleResize);

        return () => window.removeEventListener('resize', handleResize); 
    }, []);

    const r = windowWidth >= 1471 ? 190 : 130;
    const cx = 200;
    const cy = 210;

    const x1 = cx - r;
    const x2 = cx + r;
    const y  = cy;

    let currentCalories = 0; 
    foodData.forEach(value => {
        currentCalories += value.calories;
    })
    const targetCalories = 1620; 


    const circumfrence = Math.PI * r; 

    const [offset, setOffset] = useState(circumfrence); 
    const [percentage, setPercentage] = useState(0);

    useEffect(() => {
        const targetProgress = Math.round((currentCalories / targetCalories) * 100) || 0;

        if (percentage > targetProgress) {
        const intervalId = setInterval(() => {
            setPercentage((prev) => {
                const safePrev = isNaN(prev) ? 0 : prev;
                console.log(safePrev);
                if(safePrev > targetProgress){
                    const prevValue = safePrev - 1; 
                    setOffset(circumfrence - (circumfrence * prevValue) / 100);
                    return prevValue; 
                }
                clearInterval(intervalId);
                return targetProgress;
            });
        }, 30); 
        return () => clearInterval(intervalId);
        }

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
    }, [currentCalories, circumfrence, foodData])

    const macroData = (macroName) => {
        let currentMacros = 0; 
        foodData.forEach(value => {
            currentMacros += value[macroName];
        }); 

        return currentMacros; 
    }

    return (
        <>
            <div className="calories">
                <h1 className="calorie-title">Total Calories</h1>

                <svg width="500" height="325" viewBox="0 0 400 300" className="calorie-progress">
                    <path
                    d={`M ${x1} ${y} A ${r} ${r} 0 0 1 ${x2} ${y}`}
                    fill="none"
                    stroke="#c6c8bb"
                    strokeWidth="30"
                    strokeLinecap="round"
                    />
                    <path
                    d={`M ${x1} ${y} A ${r} ${r} 0 0 1 ${x2} ${y}`}
                    fill="none"
                    stroke="green"
                    strokeWidth="30"
                    strokeLinecap="round"
                    style={{
                        strokeDasharray: circumfrence, 
                        strokeDashoffset: offset, 
                        transition: "stroke-dash-offset 0.5s ease", 
                    }}
                    />
                </svg>
                <div className="calorie-number-ratio">
                    <span className="calorie-number">{percentage}%</span>
                    <span className="calorie-ratio">{currentCalories} / {targetCalories}</span>
                </div>
                <div class="macros">
                    <Macro color="#7231bd" name="Protein" amount={macroData("protein")} goal="150"/>
                    <Macro color="#31bd98" name="Carbs" amount={macroData("carbs")} goal="200"/>
                    <Macro color="#ffad21ff" name="Fat" amount={macroData("fat")} goal="80"/>
                </div>
            </div>
        </>
    );
}

export default Calories 