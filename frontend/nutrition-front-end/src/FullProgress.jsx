import './assets/RefinedModal.css'
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

    const delta = Math.abs(formData.currentWeight - formData.goalWeight);

    return createPortal(
        <div className="refined-overlay" onClick={onClose}>
            <div className="refined-modal" onClick={(e) => e.stopPropagation()}>

                <div className="refined-modal-header">
                    <div>
                        <div className="refined-eyebrow">Manage</div>
                        <h2 className="refined-title">Progress &amp; Goals</h2>
                    </div>
                    <button className="refined-close" onClick={onClose}>✕</button>
                </div>

                <div className="progress-stat-strip">
                    <div className="progress-stat-card">
                        <div className="progress-stat-label">Current</div>
                        <div className="progress-stat-value">
                            {formData.currentWeight}<span className="progress-stat-unit">lbs</span>
                        </div>
                    </div>
                    <div className="progress-stat-card">
                        <div className="progress-stat-label">Goal</div>
                        <div className="progress-stat-value">
                            {formData.goalWeight}<span className="progress-stat-unit">lbs</span>
                        </div>
                    </div>
                    <div className="progress-stat-card">
                        <div className="progress-stat-label">Delta</div>
                        <div className="progress-stat-value progress-stat-value--accent">
                            −{delta}<span className="progress-stat-unit">lbs</span>
                        </div>
                    </div>
                </div>

                <div className="progress-form-grid">
                    <label className="progress-field">
                        <span className="progress-field-label">Current Weight</span>
                        <div className="progress-field-row">
                            <input
                                className="progress-field-input progress-field-input--mono"
                                onChange={handleChange}
                                name="currentWeight"
                                type="number"
                                value={formData.currentWeight}
                            />
                            <span className="progress-field-unit">lbs</span>
                        </div>
                    </label>
                    <label className="progress-field">
                        <span className="progress-field-label">Goal Weight</span>
                        <div className="progress-field-row">
                            <input
                                className="progress-field-input progress-field-input--mono"
                                onChange={handleChange}
                                name="goalWeight"
                                type="number"
                                value={formData.goalWeight}
                            />
                            <span className="progress-field-unit">lbs</span>
                        </div>
                    </label>
                    <label className="progress-field">
                        <span className="progress-field-label">Goal</span>
                        <div className="progress-field-row">
                            <select
                                className="progress-field-input"
                                onChange={handleChange}
                                name="goal"
                                value={formData.goal}
                            >
                                <option value="Weight Loss">Weight Loss</option>
                                <option value="Maintain">Maintain</option>
                                <option value="Muscle Gain">Muscle Gain</option>
                            </select>
                        </div>
                    </label>
                    <label className="progress-field">
                        <span className="progress-field-label">Activity Level</span>
                        <div className="progress-field-row">
                            <select
                                className="progress-field-input"
                                onChange={handleChange}
                                name="activity"
                            >
                                <option value="Sedentary">Sedentary</option>
                                <option value="Light">Light</option>
                                <option value="Moderate">Moderate</option>
                                <option value="Active">Active</option>
                                <option value="Very Active">Very Active</option>
                            </select>
                        </div>
                    </label>
                </div>

                <div className="advanced-toggle-wrap">
                    <button className="advanced-toggle" onClick={() => setAdvanced(a => !a)}>
                        <span>Advanced — macro targets</span>
                        <motion.span
                            className="advanced-toggle-chevron"
                            animate={{ rotate: advanced ? 180 : 0 }}
                            transition={{ duration: 0.3 }}
                        >
                            {'⌄'}
                        </motion.span>
                    </button>
                </div>

                <AnimatePresence>
                {advanced &&
                    <motion.div
                        className="advanced-grid"
                        layout
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: 'auto', opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.4, ease: "easeInOut" }}
                    >
                        <label className="progress-field progress-field--compact">
                            <span className="progress-field-label">Calories</span>
                            <div className="progress-field-row">
                                <input
                                    className="progress-field-input progress-field-input--mono"
                                    onChange={handleChange}
                                    type="number"
                                    name="goalCalories"
                                    value={formData.goalCalories}
                                />
                                <span className="progress-field-unit">kcal</span>
                            </div>
                        </label>
                        <label className="progress-field progress-field--compact progress-field--protein">
                            <span className="progress-field-label">Protein</span>
                            <div className="progress-field-row">
                                <input
                                    className="progress-field-input progress-field-input--mono"
                                    onChange={handleChange}
                                    type="number"
                                    name="goalProtein"
                                    value={formData.goalProtein}
                                />
                                <span className="progress-field-unit">g</span>
                            </div>
                        </label>
                        <label className="progress-field progress-field--compact progress-field--carbs">
                            <span className="progress-field-label">Carbs</span>
                            <div className="progress-field-row">
                                <input
                                    className="progress-field-input progress-field-input--mono"
                                    onChange={handleChange}
                                    type="number"
                                    name="goalCarbs"
                                    value={formData.goalCarbs}
                                />
                                <span className="progress-field-unit">g</span>
                            </div>
                        </label>
                        <label className="progress-field progress-field--compact progress-field--fat">
                            <span className="progress-field-label">Fat</span>
                            <div className="progress-field-row">
                                <input
                                    className="progress-field-input progress-field-input--mono"
                                    onChange={handleChange}
                                    type="number"
                                    name="goalFat"
                                    value={formData.goalFat}
                                />
                                <span className="progress-field-unit">g</span>
                            </div>
                        </label>
                    </motion.div>
                }
                </AnimatePresence>

                <div className="progress-footer">
                    <button className="progress-btn-cancel" onClick={onClose}>Cancel</button>
                    <button className="progress-btn-save" onClick={handleSubmit}>Save Changes</button>
                </div>

            </div>
        </div>,
        document.body
    );
}

export default FullProgress
