import './assets/Micronutrients.css'
import { FaPills } from "react-icons/fa";
import { TbPill } from "react-icons/tb";
import { MdMedication } from "react-icons/md";

function Micronutrients(){
    return(
        <div className="micronutrient-box">
            <h1 className="micro-title">Micronutrients</h1>
            <div className="micronutrient-icons">
                <div className="icon-name">
                    <div className="micronutrient-icon-box" style={{backgroundColor: '#add9ea'}}>
                        <FaPills size={45}/>
                    </div>
                    <span>Vitamins</span>
                    <span>0%</span>
                </div>
                <div className="icon-name">
                    <div className="micronutrient-icon-box" style={{backgroundColor: '#d7b696'}}>
                        <TbPill size={45}/>
                    </div>
                    <span>Minerals</span>
                    <span>0%</span>
                </div>
                <div className="icon-name">
                    <div className="micronutrient-icon-box" style={{backgroundColor: '#abc699'}}>
                        <MdMedication size={45}/>
                    </div>
                    <span>Fiber</span>
                    <span>0%</span>
                </div>
            </div>
        </div>
    );
}

export default Micronutrients