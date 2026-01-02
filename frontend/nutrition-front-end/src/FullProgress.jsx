import { createPortal } from "react-dom";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import './assets/FullProgress.css'

function FullProgress({ isOpen, onClose }){

    const [advanced, setAdvanced] = useState(false);

    if (!isOpen) return null; 

    return createPortal(
        <div className="full-screen-overlay" onClick={onClose}>
            <div className="full-progress-box" onClick={(e) => e.stopPropagation()}>
                <h1 className="full-progress-title">Manage Progress</h1>
                <div className="progress-input">
                    <div className="label-input">
                        <label for="currentWeight">Current Weight</label>
                        <input id="currentWeight" type="number"/>
                    </div>
                    <div className="label-input">
                        <label for="goalWeight">Goal Weight</label>
                        <input id="goalWeight" type="number"/>
                    </div>
                    <div className="label-input">
                        <label for="goal">Goal</label>
                        <select id="goal">
            
                        </select>
                    </div>
                    <div className="label-input">
                        <label for="actiivty">Activity</label>
                        <select id="activity">

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
                            <label for="advanced-cals">Calories</label>
                            <input type="number" id="advanced-cals"/>
                        </div>
                        <div className="advanced-label-input">
                            <label for="protein-cals">Protein</label>
                            <input type="number" id="protein"/>
                        </div>
                        <div className="advanced-label-input">
                            <label for="advanced-carbs">Carbohydrates</label>
                            <input type="number" id="advanced-carbs"/>
                        </div>
                        <div className="advanced-label-input">
                            <label for="advanced-fat">Fat</label>
                            <input type="number" id="advanced-fat"/>
                        </div>
                    </motion.div>
                : null}
                </AnimatePresence>
               <motion.button id="saveBtn"
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}      
                    transition={{ duration: 0.4, ease: "easeInOut" }}
               >Save</motion.button>
            </div>
        </div>,
        document.body
    );
}

export default FullProgress