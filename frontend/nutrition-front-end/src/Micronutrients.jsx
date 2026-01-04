import './assets/Micronutrients.css'
import { FaPills } from "react-icons/fa";
import { TbPill } from "react-icons/tb";
import { MdMedication } from "react-icons/md";

function Micronutrients({ onOpen, foodData }){

    const totals = {
        vitaminA: 0, 
        vitaminC: 0, 
        sodium: 0, 
    }

    foodData.forEach(food => {
        totals.vitaminA += food.vitamin_A;
        totals.vitaminC += food.vitamin_C;
        totals.sodium += food.sodium;
    }); 

    return(
        <div className="micronutrient-box" onClick={onOpen}>
            <h1 className="micro-title">Micronutrients</h1>
            <div className="micronutrient-icons">
                <div className="icon-name">
                    <div className="micronutrient-icon-box" style={{backgroundColor: '#add9ea'}}>
                        <FaPills size={45}/>
                    </div>
                    <span>Vitamin A</span>
                    <span>{totals.vitaminA}mg</span>
                </div>
                <div className="icon-name">
                    <div className="micronutrient-icon-box" style={{backgroundColor: '#d7b696'}}>
                        <TbPill size={45}/>
                    </div>
                    <span>Vitamin C</span>
                    <span>{totals.vitaminC}mg</span>
                </div>
                <div className="icon-name">
                    <div className="micronutrient-icon-box" style={{backgroundColor: '#abc699'}}>
                        <MdMedication size={45}/>
                    </div>
                    <span>Sodium</span>
                    <span>{totals.sodium}mg</span>
                </div>
            </div>
        </div>
    );
}

export default Micronutrients