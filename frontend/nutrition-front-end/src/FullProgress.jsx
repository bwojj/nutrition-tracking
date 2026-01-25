import './assets/FullProgress.css'
import { createPortal } from "react-dom";
import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import LoadingScreen from "./LoadingScreen.jsx";
import { saveProgress } from './api/userApi.js';

function FullProgress({ isOpen, onClose, progressData, isLoading }){

    const [advanced, setAdvanced] = useState(false);
 
    const [formData, setFormData] = useState({
        currentWeight: progressData[0].current_weight || 0, 
        goalWeight: progressData[0].goal_weight || 0, 
        goal: progressData[0].goal || "", 
        goalCalories: progressData[0].goal_calories || 0, 
        goalProtein: progressData[0].goal_protein || 0, 
        goalCarbs: progressData[0].goal_carbs || 0, 
        goalFat: progressData[0].goal_fat || 0,
    });

    useEffect(() => {
        const data = progressData[0];
        setFormData({
            currentWeight: data.current_weight,
            goalWeight: data.goal_weight, 
            goal: data.goal, 
            goalCalories: data.goal_calories, 
            goalProtein: data.goal_protein, 
            goalCarbs: data.goal_carbs, 
            goalFat: data.goal_fat, 
        })
    }, [progressData])

    function handleChange(event){
        const { name, value, type} = event.target; 

        const finalType = type === "number" ? parseFloat(value) : value;
        setFormData(prev => ({
            ...prev,
            [name]: finalType, 
        }))

    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(formData);
        await saveProgress(formData);
        window.location.reload();
        

        onClose();
    }

    if (!isOpen) return null; 

    if (isLoading) {
        return <LoadingScreen/>
    }

    return createPortal(
        <div className="full-screen-overlay" onClick={onClose}>
            <div className="full-progress-box" onClick={(e) => e.stopPropagation()}>
                <h1 className="full-progress-title">Manage Progress</h1>
                <div className="progress-input">
                    <div className="label-input">
                        <label for="currentWeight">Current Weight</label>
                        <input onChange={handleChange} name="currentWeight" id="currentWeight" type="number"/>
                    </div>
                    <div className="label-input">
                        <label for="goalWeight">Goal Weight</label>
                        <input onChange={handleChange} name="goalWeight" id="goalWeight" type="number"/>
                    </div>
                    <div className="label-input">
                        <label for="goal">Goal</label>
                        <select onChange={handleChange} name="goal" id="goal">
            
                        </select>
                    </div>
                    <div className="label-input">
                        <label for="actiivty">Activity</label>
                        <select onChange={handleChange} name="activity" id="activity">

                        </select>
                    </div>
                </div>
                <div className="advanced-options">
                    <button onClick={() => setAdvanced(!advanced)} id="advanced">
                        Advanced Options 
                        <motion.span 
                            animate={{ rotate: advanced ? 180 : 0, marginTop: advanced ? '15px' : 0 }}
                            transition={{ duration: 0.3 }}
                            style={{ display: 'inline-block', marginLeft: '5px', marginBottom: '8px'}}
                        >
                            {'\u2304'}
                        </motion.span>
                    </button>
                </div>
                <AnimatePresence>
                {advanced ? 
                    <motion.div className="advanced-options-box"
                    layout
                            initial={{ height: 0, opacity: 0 }}
                            animate={{ height: 'auto', opacity: 1 }}
                            exit={{ height: 0, opacity: 0 }}      
                            transition={{ duration: 0.4, ease: "easeInOut" }}
                    >  
                        <div className="advanced-label-input">
                            <label for="goalCalories">Calories</label>
                            <input onChange={handleChange} type="number" name="goalCalories" id="goalCalories"/>
                        </div>
                        <div className="advanced-label-input">
                            <label for="goalProtein">Protein</label>
                            <input onChange={handleChange} type="number" name="goalProtein" id="goalProtein"/>
                        </div>
                        <div className="advanced-label-input">
                            <label for="goalCarbs">Carbohydrates</label>
                            <input onChange={handleChange} type="number" name="goalCarbs" id="goalCarbs"/>
                        </div>
                        <div className="advanced-label-input">
                            <label for="goalFat">Fat</label>
                            <input onChange={handleChange} type="number" name="goalFat" id="goalFat"/>
                        </div>
                    </motion.div>
                : null}
                </AnimatePresence>
               <motion.button id="saveBtn"
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}      
                    transition={{ duration: 0.4, ease: "easeInOut" }}
                    onClick={handleSubmit}
               >Save</motion.button>
            </div>
        </div>,
        document.body
    );
}

export default FullProgress