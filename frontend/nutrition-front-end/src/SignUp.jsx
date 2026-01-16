import './assets/Signup.css'
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Signup({ }) {
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        "username": "",
        "email": "", 
        "password": "", 
        "confirmPassword": "", 
    }); 
    const [message, setMessage] = useState("");

    function handleChange(event){
        const { name, value } = event.target;  
        
        setFormData(prev => ({
            ...prev, 
            [name]: value,
        }))
    }

    const signup = async (username, email, password) => {
        try {
            const response = await fetch('http://127.0.0.1:8000/register/', {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                }, 
                credentials: 'include',
                body: JSON.stringify({ username, email, password })
            });
        } catch(error){
            setMessage(error);
        }
    }

    function handleSignUp(){
        if(formData.password === formData.confirmPassword){
            signup(formData.username, formData.email, formData.password)
            setMessage("Success!")
            navigate('/onboarding');
        } else {
            console.log("Failed to login");
        }
    }

    return (
            <div className="signup-box">
                <h1 className="signup-title">Create Account</h1>
                
                <div className="label-input">
                    <label htmlFor="username">Username</label>
                    <input onChange={handleChange} id="username" type="text" name="username" placeholder="Username"/>
                </div>

                <div className="label-input">
                    <label htmlFor="email">Email</label>
                    <input onChange={handleChange} id="email" type="email" name="email" placeholder="Email"/>
                </div>

                <div className="label-input">
                    <label htmlFor="password">Password</label>
                    <input onChange={handleChange} id="password" type="password" name="password" placeholder="Password"/>
                </div>

                <div className="label-input">
                    <label htmlFor="confirmPassword">Confirm Password</label>
                    <input onChange={handleChange} id="confirmPassword" type="password" name="confirmPassword" placeholder="Confirm Password"/>
                </div>

                <button onClick={handleSignUp} id="signupBtn">Sign Up</button>
                <p>{message}</p>
            </div>
    );
}

export default Signup;