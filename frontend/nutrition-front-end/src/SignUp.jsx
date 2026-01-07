import { useState } from 'react';

function SignUp({ onSwitch }) {
    const [formData, setFormData] = useState({
        username: '', email: '', password: '', password_confirm: ''
    });
    const [errors, setErrors] = useState({});

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:8000/api/register/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                alert("Account created! Please log in.");
                onSwitch(); // Send them back to Login view
            } else {
                const data = await response.json();
                setErrors(data); // Displays field-specific errors from Django
            }
        } catch (err) {
            console.error("Signup error:", err);
        }
    };

    return (
        <div className="auth-box">
            <h2>Sign Up</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Username" required
                       onChange={(e) => setFormData({...formData, username: e.target.value})} />
                {errors.username && <span className="error-text">{errors.username[0]}</span>}

                <input type="email" placeholder="Email" required
                       onChange={(e) => setFormData({...formData, email: e.target.value})} />

                <input type="password" placeholder="Password" required
                       onChange={(e) => setFormData({...formData, password: e.target.value})} />

                <input type="password" placeholder="Confirm Password" required
                       onChange={(e) => setFormData({...formData, password_confirm: e.target.value})} />
                {errors.password && <span className="error-text">{errors.password[0]}</span>}

                <button type="submit">Register</button>
            </form>
            <p>Already have an account? <span className="toggle-link" onClick={onSwitch}>Login</span></p>
        </div>
    );
}

export default SignUp 