import { createPortal } from "react-dom";
import './assets/FullMicronutrients.css'
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
                    <div className="column">
                        <h2 className="col-title">Vitamins</h2>
                        <ul className="col-info">
                            <div className="name-data">
                                <li>Vitamin A</li>
                                <li className="count">{microTotals.vitamin_A}</li>
                            </div>
                            <div className="name-data">
                                <li>Vitamin C</li>
                                <li className="count">{microTotals.vitamin_C}</li>
                            </div>
                            <div className="name-data">
                                <li>Fiber</li>
                                <li className="count">{microTotals.fiber}</li>
                            </div>
                            <div className="name-data">
                                <li>Sugar</li>
                                <li className="count">{microTotals.sugar}</li>
                            </div>
                        </ul>
                    </div>
                    <div className="column">
                        <h2 className="col-title">Minerals</h2>
                        <ul className="col-info">
                            <div className="name-data">
                                <li>Sodium</li>
                                <li className="count">{microTotals.sodium}</li>
                            </div>
                            <div className="name-data">
                                <li>Potassium</li>
                                <li className="count">{microTotals.potassium}</li>
                            </div>
                            <div className="name-data">
                                <li>Cholesterol</li>
                                <li className="count">{microTotals.cholesterol}</li>
                            </div>
                            <div className="name-data">
                                <li>Calcium</li>
                                <li className="count">{microTotals.calcium}</li>
                            </div>
                        </ul>
                    </div>
                    <div className="column">
                        <h2 className="col-title">Fats</h2>
                        <ul className="col-info">
                            <div className="name-data">
                                <li>Saturated Fat</li>
                                <li className="count">{microTotals.saturated_fat}</li>
                            </div>
                            <div className="name-data">
                                <li>Polyunsaturated Fat</li>
                                <li className="count">{microTotals.polyunsaturated_fat}</li>
                            </div>
                            <div className="name-data">
                                <li>Monounsaturated Fat</li>
                                <li className="count">{microTotals.monounsaturated_fat}</li>
                            </div>
                            <div className="name-data">
                                <li>Trans Fat</li>
                                <li className="count">{microTotals.trans_fat}</li>
                            </div>
                        </ul>
                    </div>
                </div>
            </div>
        </div>,
        document.body
    );
}

export default FullMicronutrients 