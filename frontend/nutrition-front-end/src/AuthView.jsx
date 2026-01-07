import { useState } from "react";
import Login from "./Login.jsx"
import SignUp from "./SignUp.jsx"

function AuthView({ onLoginSuccess }){
    const [isLogin, setIsLogin] = useState(true);
    return(
        <div className="auth-screen">
            {isLogin ? (
                <Login onLoginSuccess={onLoginSuccess} onSwitch={() => setIsLogin(false)} />
            ) : (
                <SignUp onSwitch={() => setIsLogin(true)} />
            )}
        </div>
    );
}

export default AuthView