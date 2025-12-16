import './assets/Calories.css'
import Macro from './Macros';
import { useEffect, useState } from 'react';

function Calories() {
  const r = window.innerWidth >= 1378 ? 190 : 130;
  const cx = 200;
  const cy = 210;

  const x1 = cx - r;
  const x2 = cx + r;
  const y  = cy;

  let currentCalories = 1000; 
  const targetCalories = 1620; 

  const circumfrence = Math.PI * r; 
  let progress = 0; 
  const targetProgress = (currentCalories / targetCalories) * 100;

  const [offset, setOffset] = useState(circumfrence); 
  const [percentage, setPercentage] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
        if(progress >= targetProgress){
            return(clearInterval(intervalId));
        }
        else{
            // eslint-disable-next-line react-hooks/exhaustive-deps
            progress += 1; 
            setOffset(circumfrence - (circumfrence * progress) / 100);
            setPercentage(progress);
        }
    }, 30);
  }, [])


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
                <Macro color="#7231bd" name="Protein" amount="110" goal="150"/>
                <Macro color="#31bd98" name="Carbs" amount="150" goal="200"/>
                <Macro color="#ffad21ff" name="Fat" amount="50" goal="80"/>
            </div>
        </div>
    </>
  );
}

export default Calories 