import { refresh } from "./authApi.js";

const BASE_URL = import.meta.env.VITE_API_URL;

export const getFoodData = async (selectedDate) => {
    try{
        const response = await fetch(`${BASE_URL}api/food-data/?date=${selectedDate}`, { 
            credentials: 'include',
        });
        if (response.status === 401){
            const refreshResponse = await refresh();
            if(refreshResponse.ok){
                const response = await fetch(`${BASE_URL}api/food-data/?date=${selectedDate}`, { 
                    credentials: 'include',
                });
                if(response.ok){
                    const data = await response.json();
                    return data; 
                }
            }
        }
        if(response.ok){
            const data = await response.json();
            return data; 
        } 
    } catch(error){
        console.log("Failed to fetch", error)
    }
}

export const deleteFood = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}api/food-data/${id}/`, {
            method: 'DELETE',
            credentials: 'include',
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const response = await fetch(`${BASE_URL}api/food-data/${id}/`, {
                    method: 'DELETE',
                    credentials: 'include',
                });
                if (response.ok) {
                    return 'Success'
                }
            }
        }
        if (response.ok) {
            return 'Success'
        } else {
            console.error("Failed to delete item");
        }
    } catch (error) {
        console.error("Error deleting food:", error);
    }
};

export const saveFood = async (foodData, date) => {
    try {
        const payload = {
            ...foodData,
            date: date,
        }
        const response = await fetch(`${BASE_URL}api/add-food/`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const response = await fetch(`${BASE_URL}api/add-food/`, {
                    method: 'POST',
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(payload),
                });
                if (response.ok) {
                    const result = await response.json();
                    return result;
                }
            }
        }

        if (response.ok) {
            const result = await response.json();
            console.log("Saved", result);
            return result;
        } else {
            console.log("Server Error", response.statusText);
        }
    } catch (error) {
        console.log('Network Error', error);
    }
};

export const getFoods = async () => {
    try {
        const response = await fetch(`${BASE_URL}api/foods`, {
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
        })

        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const response = await fetch(`${BASE_URL}api/foods`, {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    credentials: 'include',
                })
                if (response.ok) {
                    const data = await response.json();
                    return data;
                }
            }
        }

        if (response.ok) {
            const data = await response.json();
            return data;
        }
    }
    catch (error) {
        console.log("Failed to fetch Foods", error);
    }
}