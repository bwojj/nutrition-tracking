import './assets/Signup.css'
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signup, login } from './api/authApi';

function Signup({ setIsLoggedIn, setIsLoading }) {
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        "username": "",
        "email": "", 
        "password": "", 
        "confirmPassword": "", 
    }); 

    function handleChange(event){
        const { name, value } = event.target;  
        
        setFormData(prev => ({
            ...prev, 
            [name]: value,
        }))
    }

async function handleSignUp(){
    if(formData.password === formData.confirmPassword){
        setIsLoading(true);
        const response = await signup(formData.username, formData.email, formData.password)
        if(response === 'Success'){
            setIsLoggedIn(true);
            setIsLoading(false);
            navigate('/onboarding');
        }
        } else {
            console.log("Failed to login");
        }
    }

    return (
            <div className="signup-box">
                <h1 className="signup-title">Create Account</h1>
                
                <div className="signup-label-input">
                    <label htmlFor="username">Username</label>
                    <input onChange={handleChange} id="username" type="text" name="username" placeholder="Username"/>
                </div>

                <div className="signup-label-input">
                    <label htmlFor="email">Email</label>
                    <input onChange={handleChange} id="email" type="email" name="email" placeholder="Email"/>
                </div>

                <div className="signup-label-input">
                    <label htmlFor="password">Password</label>
                    <input onChange={handleChange} id="password" type="password" name="password" placeholder="Password"/>
                </div>

                <div className="signup-label-input">
                    <label htmlFor="confirmPassword">Confirm Password</label>
                    <input onChange={handleChange} id="confirmPassword" type="password" name="confirmPassword" placeholder="Confirm Password"/>
                </div>

                <button onClick={handleSignUp} id="signupBtn">Sign Up</button>
            </div>
    );
}

export default Signup;