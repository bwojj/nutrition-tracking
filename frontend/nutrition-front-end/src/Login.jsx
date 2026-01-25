import './assets/Login.css'
import { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { login } from './api/authApi.js';



function Login({ setIsLoggedIn }) {
    const navigate = useNavigate(); 

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function onUsernameChange(event){
        setUsername(event.target.value);
    }
    function onPasswordChange(event){
        setPassword(event.target.value);
    }

    async function handleLogin(){
        try{
            const response = await login(username, password); 
            if(response === 'Success'){
                setIsLoggedIn(true);
                navigate('/');
            }
        } catch(error) {
            console.log("Failed to login", error);
        }
        
    }
     
    return (
            <div className="login-box">
                <h1 className="login-title">Login</h1>
                
                <div className="login-label-input">
                    <label htmlFor="username">Username</label>
                    <input onChange={onUsernameChange} id="username" value={username} type="text" name="username" placeholder="Enter username"/>
                </div>

                <div className="login-label-input">
                    <label htmlFor="password">Password</label>
                    <input  onChange={onPasswordChange} id="password" type="password" name="password" placeholder="Enter password"/>
                </div>

                <button onClick={handleLogin} id="loginBtn">Login</button>
            </div>
    );
}

export default Login;