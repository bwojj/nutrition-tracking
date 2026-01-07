import { useState } from 'react';

function Login({ onLoginSuccess, onSwitch }) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        try {
            const response = await fetch('http://127.0.0.1:8000/api/login/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                const data = await response.json();
                
                // Save both access and refresh tokens
                localStorage.setItem('access_token', data.access);
                localStorage.setItem('refresh_token', data.refresh);

                // Pass access token to parent
                onLoginSuccess(data.access);

            } else {
                setError('Invalid username or password');
            }
        } catch (err) {
            setError('Connection failed. Is the backend running?');
            console.error(err);
        }
    };

    return (
        <div className="auth-box">
            <h2>Login</h2>
            {error && <p className="error-msg">{error}</p>}
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Username" required 
                       onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" required 
                       onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Enter</button>
            </form>
            <p>New user? <span className="toggle-link" onClick={onSwitch}>Create account</span></p>
        </div>
    );
}

export default Login;
