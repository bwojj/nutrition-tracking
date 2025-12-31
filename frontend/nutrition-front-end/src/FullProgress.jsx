import { createPortal } from "react-dom";
import './assets/FullProgress.css'

function FullProgress({ isOpen, onClose }){

    if (!isOpen) return null; 

    return createPortal(
        <div className="full-screen-overlay" onClick={onClose}>
            <div className="full-progress-box">

            </div>
        </div>,
        document.body
    );
}

export default FullProgress