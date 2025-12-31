import { createPortal } from "react-dom";
import './assets/FullMicronutrients.css'

function FullMicronutrients({ isOpen, onClose }){

    if (!isOpen) return null; 

    return createPortal(
        <div className="full-screen-overlay" onClick={onClose}>
            <div className="full-micronutrient-box">

            </div>
        </div>,
        document.body
    );
}

export default FullMicronutrients 