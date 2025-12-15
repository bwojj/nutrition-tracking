import './assets/Macro.css'
import { useEffect, useState } from 'react';

function Macro(props){

    const circumfrence = 2 * Math.PI * 60; 

    const progress = (Number(props.amount) / Number(props.goal)) * 100;

    const [offset, setOffset] = useState(Number(circumfrence - (circumfrence * progress) / 100));
    console.log(offset);


    return(
        <div className="macro-container">
            <svg>
                <circle className="circle" r="60" cx="37%" cy="50%" fill="none" stroke="#c6c8bb" strokeWidth={20}/>
                <circle className="progress-circle" r="60" cx="37%" cy="50%" fill="none" stroke={props.color} strokeWidth={20}
                style={{
                    strokeDasharray: circumfrence,
                    strokeDashoffset: offset, 
                    transform: 'rotate(-180deg)',
                    transformOrigin: '37% 50%',
                }}/>
            </svg>
            <div className="macro-name-amount">
                <span className="macro-name">{props.name}</span>
                <span className="macro-amount">{props.amount}</span>
            </div>
            <span className="macro-percentage">0%</span>
        </div>
    );
}

export default Macro 