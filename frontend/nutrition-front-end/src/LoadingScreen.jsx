import { createPortal } from "react-dom"
import './assets/LoadingScreen.css'


function LoadingScreen(){
    return createPortal(
        <div className="loading-div">
            <div className="spinner"/>
            <p>Loading...</p>
        </div>, document.body
    )
}

export default LoadingScreen