import './assets/Login.css'
import { useState } from 'react';
import { useNavigate } from "react-router-dom";



function Login({ setIsLoggedIn }) {
    const navigate = useNavigate(); 

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const login = async (username, password) => {
        try {
            const response = await fetch('http://localhost:8000/token/', {
                method: "POST", 
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
                credentials: 'include',
            });

            if(response.ok){
                const data = await response.json(); 
                localStorage.setItem('userToken', data.token);
                setIsLoggedIn(true);
                navigate("/");
            }
        } catch(error){
            console.log('Failed to Post', error); 
        }
    }

    function onUsernameChange(event){
        setUsername(event.target.value);
    }
    function onPasswordChange(event){
        setPassword(event.target.value);
    }

    function handleLogin(){
        try{
            login(username, password); 
        } catch(error) {
            console.log("Failed to login", error);
        }
        
    }
     
    return (
            <div className="login-box">
                <h1 className="login-title">Login</h1>
                
                <div className="label-input">
                    <label htmlFor="username">Username</label>
                    <input onChange={onUsernameChange} id="username" value={username} type="text" name="username" placeholder="Enter username"/>
                </div>

                <div className="label-input">
                    <label htmlFor="password">Password</label>
                    <input  onChange={onPasswordChange} id="password" type="password" name="password" placeholder="Enter password"/>
                </div>

                <button onClick={handleLogin} id="loginBtn">Login</button>
            </div>
    );
}

export default Login;