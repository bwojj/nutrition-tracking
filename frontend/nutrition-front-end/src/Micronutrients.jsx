import './assets/Micronutrients.css'
import { Citrus, ExternalLink, Eye, Spline } from 'lucide-react';

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
            <ExternalLink size={18} className="micro-expand-icon" />
            <h1 className="micro-title">Micronutrients</h1>
            <div className="micronutrient-icons">
                <div className="icon-name">
                    <div className="micronutrient-icon-box" style={{backgroundColor: '#1a3a4a', color: '#7dd3fc'}}>
                        <Eye size={32}/>
                    </div>
                    <span>Vitamin A</span>
                    <span>{totals.vitaminA}mg</span>
                </div>
                <div className="icon-name">
                    <div className="micronutrient-icon-box" style={{backgroundColor: '#3a2a1a', color: '#fdba74'}}>
                        <Citrus size={32}/>
                    </div>
                    <span>Vitamin C</span>
                    <span>{totals.vitaminC}mg</span>
                </div>
                <div className="icon-name">
                    <div className="micronutrient-icon-box" style={{backgroundColor: '#2d1f4e', color: '#c084fc'}}>
                        <Spline size={32}/>
                    </div>
                    <span>Sodium</span>
                    <span>{totals.sodium}mg</span>
                </div>
            </div>
        </div>
    );
}

export default Micronutrients