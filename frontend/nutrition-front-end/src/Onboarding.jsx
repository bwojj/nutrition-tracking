import React, { useState } from 'react';
import './assets/Onboarding.css';

const Onboarding = () => {
  const [formData, setFormData] = useState({
    goal_calories: '',
    goal_protein: '',
    goal_carbs: '',
    goal_fat: '',
    current_weight: '',
    goal_weight: '',
    goal: 'Weight Loss'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Submitted Onboarding Data:', formData);
  };

  return (
    <div className="onboarding-scope-wrapper">
      <div className="onboarding-scope-card">
        <h2 className="onboarding-scope-title">Setup Your Profile</h2>
        <form onSubmit={handleSubmit} className="onboarding-scope-form">
          
          <div className="onboarding-scope-group">
            <label className="onboarding-scope-label">Primary Goal</label>
            <select 
                className="onboarding-scope-input" 
                name="goal" 
                value={formData.goal} 
                onChange={handleChange}
            >
              <option value="Weight Loss">Weight Loss</option>
              <option value="Maintenance">Maintenance</option>
              <option value="Muscle Gain">Muscle Gain</option>
            </select>
          </div>

          <div className="onboarding-scope-row">
            <div className="onboarding-scope-group">
              <label className="onboarding-scope-label">Current Weight (lbs)</label>
              <input 
                className="onboarding-scope-input"
                type="number" 
                name="current_weight" 
                placeholder="175.0" 
                onChange={handleChange} 
              />
            </div>
            <div className="onboarding-scope-group">
              <label className="onboarding-scope-label">Goal Weight (lbs)</label>
              <input 
                className="onboarding-scope-input"
                type="number" 
                name="goal_weight" 
                placeholder="127.0" 
                onChange={handleChange} 
              />
            </div>
          </div>

          <div className="onboarding-scope-divider"></div>

          <div className="onboarding-scope-group">
            <label className="onboarding-scope-label">Daily Calorie Goal</label>
            <input 
              className="onboarding-scope-input"
              type="number" 
              name="goal_calories" 
              placeholder="2200" 
              onChange={handleChange} 
            />
          </div>

          <div className="onboarding-scope-macro-grid">
            <div className="onboarding-scope-group">
              <label className="onboarding-scope-label">Protein (g)</label>
              <input className="onboarding-scope-input" type="number" name="goal_protein" onChange={handleChange} />
            </div>
            <div className="onboarding-scope-group">
              <label className="onboarding-scope-label">Carbs (g)</label>
              <input className="onboarding-scope-input" type="number" name="goal_carbs" onChange={handleChange} />
            </div>
            <div className="onboarding-scope-group">
              <label className="onboarding-scope-label">Fat (g)</label>
              <input className="onboarding-scope-input" type="number" name="goal_fat" onChange={handleChange} />
            </div>
          </div>

          <button type="submit" className="onboarding-scope-submit-btn">Save Progress</button>
        </form>
      </div>
    </div>
  );
};

export default Onboarding;