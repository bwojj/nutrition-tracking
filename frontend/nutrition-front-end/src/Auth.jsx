import { useState } from "react";
import Login from "./Login";
import Signup from "./Signup";

function Auth({ setIsLoggedIn}) {
    const [isLogin, setIsLogin] = useState(true);

    return (
        <div className="login-screen">
            <div className="auth-card">
                {isLogin ? <Login setIsLoggedIn={setIsLoggedIn} /> : <Signup setIsLogin={setIsLogin} />}
                
                <div className="toggle-container">
                    <button 
                        className="toggle-auth-btn" 
                        onClick={() => setIsLogin(!isLogin)}
                    >
                        {isLogin ? "Need an account? Sign Up" : "Have an account? Login"}
                    </button>
                </div>
            </div>
        </div>
    );
}

export default Auth;