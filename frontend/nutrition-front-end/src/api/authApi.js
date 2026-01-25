

const BASE_URL = import.meta.env.VITE_API_URL;

export const login = async (username, password) => {
    try {
        const response = await fetch(`${BASE_URL}token/`, {
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
            return "Success"
        }
    } catch(error){
        console.log('Failed to Post', error); 
    }
}

export const signup = async (username, email, password) => {
    try {
        const response = await fetch(`${BASE_URL}register/`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            }, 
            credentials: 'include',
            body: JSON.stringify({ username, email, password })
        });
        if(response.ok){
            const loginResponse = await login(username, password); 
            if(loginResponse === 'Success'){
                return "Success"
            }
        }
        } catch(error){
            console.log('Failed to sign-up', error);
        }
    }
export const refresh = async () => {
    const response = await fetch(`${BASE_URL}token/refresh/`, {
        credentials: 'include',
        method: "POST",
    }); 
    return response; 
}