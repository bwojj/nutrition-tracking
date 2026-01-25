
const BASE_URL = import.meta.env.VITE_API_URL; 

export const is_authenticated = async () => {
    try{
        const response = await fetch(`${BASE_URL}authenticated/`, {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            credentials: "include", 
        })
        if(response.ok){
            const data = await response.json();
            return data;
        }
    } catch(error){
        console.log("Failed to fetch", error);
    } 
}