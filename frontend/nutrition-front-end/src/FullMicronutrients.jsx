import { createPortal } from "react-dom";
import './assets/FullMicronutrients.css'
import Micro from "./Micro";
import { useState } from "react";

function FullMicronutrients({ isOpen, onClose, foodData }){

    let microTotals = {
        fiber: 0,
        sugar: 0,
        saturated_fat: 0,
        polyunsaturated_fat: 0,
        monounsaturated_fat: 0, 
        trans_fat: 0,
        cholesterol: 0, 
        sodium: 0,
        potassium: 0, 
        vitamin_A: 0,
        vitamin_C: 0, 
        calcium: 0,
    }
    foodData.forEach(food => {
       Object.keys(microTotals).forEach(key => {
            microTotals[key] += food[key]; 
       })
    })

    if (!isOpen) return null; 
    console.log(microTotals)
    return createPortal(
        <div className="full-screen-overlay" onClick={onClose}>
            <div className="full-micronutrient-box">
                <h1 class="full-micro-title">Micronutrients</h1>
                <div className="micro-info">
                    <div className="title-dv">
                        <h2 className="micro-title">Vitamins</h2>
                        <h2 className="dv-label">Goal</h2>
                    </div>
                    <div className="micros">
                        <Micro vitamin="Vitamin A" amount={microTotals.vitamin_A} goal={900}/>
                        <Micro vitamin="Vitamin C" amount={microTotals.vitamin_C} goal={90}/>
                        <Micro vitamin="Fiber" amount={microTotals.fiber} goal={23}/>
                        <Micro vitamin="Sugar" amount={microTotals.sugar} goal={41}/>
                    </div>
                </div>
                <div className="micro-info">
                    <div className="title-dv">
                        <h2 className="micro-title">Minerals</h2>
                        <h2 className="dv-label">Goal</h2>
                    </div>
                    <div className="micros">
                        <Micro vitamin="Sodium" amount={microTotals.sodium} goal={2300}/>
                        <Micro vitamin="Potassium" amount={microTotals.potassium} goal={4700}/>
                        <Micro vitamin="Calcium" amount={microTotals.calcium} goal={1300}/>
                        <Micro vitamin="Cholesterol" amount={microTotals.cholesterol} goal={300}/>
                    </div>
                </div>
                <div className="micro-info">
                    <div className="title-dv">
                        <h2 className="micro-title">Fats</h2>
                        <h2 className="dv-label">Goal</h2>
                    </div>
                    <div className="micros">
                        <Micro vitamin="Saturated Fat" amount={microTotals.saturated_fat} goal={16}/>
                        <Micro vitamin="Monounsaturated Fat" amount={microTotals.monounsaturated_fat} goal={0}/>
                        <Micro vitamin="Polyunsaturated Fat" amount={microTotals.polyunsaturated_fat} goal={0}/>
                        <Micro vitamin="Trans Fat" amount={microTotals.trans_fat} goal={0}/>
                    </div>
                </div>
            </div>
        </div>,
        document.body
    );
}

export default FullMicronutrients 