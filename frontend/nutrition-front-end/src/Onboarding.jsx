import React, { useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import './assets/Onboarding.css';
import LoadingScreen from './LoadingScreen';

const BASE_URL = import.meta.env.VITE_API_URL;

const Onboarding = ({ setIsLoggedIn }) => {
  const navigate = useNavigate();

  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setIsLoading(false);
  }, [])

   const [formData, setFormData] = useState({
        currentWeight: 0, 
        goalWeight: 0, 
        goal: "Weight Loss", 
        goalCalories: 0, 
        goalProtein: 0, 
        goalCarbs: 0, 
        goalFat: 0,
    });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    e.stopPropagation();
    await progress(formData); 
    setIsLoggedIn(true);
    console.log('Submitted Onboarding Data:', formData);
    navigate('/');
  };

  const progress = async (formData) => {
    try{
      const response = await fetch(`${BASE_URL}api/update-progress/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(formData), 
      })
      if(response.ok){
        const data = await response.json();
        console.log("Success", data); 
      }
    } catch(error){
      console.log("Failed to post", error);
    }
  }
  if(isLoading){
    return <LoadingScreen/>;
  }

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
                name="currentWeight" 
                placeholder="175.0" 
                onChange={handleChange} 
              />
            </div>
            <div className="onboarding-scope-group">
              <label className="onboarding-scope-label">Goal Weight (lbs)</label>
              <input 
                className="onboarding-scope-input"
                type="number" 
                name="goalWeight" 
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
              name="goalCalories" 
              placeholder="2200" 
              onChange={handleChange} 
            />
          </div>

          <div className="onboarding-scope-macro-grid">
            <div className="onboarding-scope-group">
              <label className="onboarding-scope-label">Protein (g)</label>
              <input className="onboarding-scope-input" type="number" name="goalProtein" onChange={handleChange} />
            </div>
            <div className="onboarding-scope-group">
              <label className="onboarding-scope-label">Carbs (g)</label>
              <input className="onboarding-scope-input" type="number" name="goalCarbs" onChange={handleChange} />
            </div>
            <div className="onboarding-scope-group">
              <label className="onboarding-scope-label">Fat (g)</label>
              <input className="onboarding-scope-input" type="number" name="goalFat" onChange={handleChange} />
            </div>
          </div>

          <button type="submit" className="onboarding-scope-submit-btn">Save Progress</button>
        </form>
      </div>
    </div>
  );
};

export default Onboarding;