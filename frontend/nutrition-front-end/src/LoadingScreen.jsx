import { createPortal } from "react-dom"
import { useEffect } from "react";
import './assets/LoadingScreen.css'


function LoadingScreen(){
    useEffect(() => {
    let frame;
    const rotate = () => {
      const degrees = (Date.now() % 1000) * 0.36; 
      document.documentElement.style.setProperty('--rotation', `${degrees}deg`);
      frame = requestAnimationFrame(rotate);
    };

    rotate();
    return () => cancelAnimationFrame(frame);
  }, []);
    return createPortal(
        <div className="loading-div">
            <div className="spinner"/>
            <p>Loading...</p>
        </div>, document.body
    )
}

export default LoadingScreen