import { refresh, getAuthHeaders } from "./authApi.js";

const BASE_URL = import.meta.env.VITE_API_URL;

export const getFoodData = async (selectedDate) => {
    try {
        const response = await fetch(`${BASE_URL}api/food-data/?date=${selectedDate}`, {
            credentials: 'include',
            headers: getAuthHeaders(),
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/food-data/?date=${selectedDate}`, {
                    credentials: 'include',
                    headers: getAuthHeaders(),
                });
                if (retryResponse.ok) {
                    const data = await retryResponse.json();
                    return data;
                }
            }
        }
        if (response.ok) {
            const data = await response.json();
            return data;
        }
    } catch (error) {
        console.log("Failed to fetch", error);
    }
};

export const deleteFood = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}api/food-data/${id}/`, {
            method: 'DELETE',
            credentials: 'include',
            headers: getAuthHeaders(),
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/food-data/${id}/`, {
                    method: 'DELETE',
                    credentials: 'include',
                    headers: getAuthHeaders(),
                });
                if (retryResponse.ok) {
                    return 'Success';
                }
            }
        }
        if (response.ok) {
            return 'Success';
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
        };
        const response = await fetch(`${BASE_URL}api/add-food/`, {
            method: 'POST',
            credentials: 'include',
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
            body: JSON.stringify(payload),
        });

        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/add-food/`, {
                    method: 'POST',
                    credentials: 'include',
                    headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
                    body: JSON.stringify(payload),
                });
                if (retryResponse.ok) {
                    const result = await retryResponse.json();
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

export const getFoods = async (sort) => {
    try {
        const response = await fetch(`${BASE_URL}api/foods/?sort=${sort}`, {
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
            credentials: 'include',
        });

        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/foods/`, {
                    headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
                    credentials: 'include',
                });
                if (retryResponse.ok) {
                    const data = await retryResponse.json();
                    return data;
                }
            }
        }

        if (response.ok) {
            const data = await response.json();
            return data;
        }
    } catch (error) {
        console.log("Failed to fetch Foods", error);
    }
};

export const searchFoodsDB = async (query) => {
    try {
        const response = await fetch(`${BASE_URL}api/foods/?search=${encodeURIComponent(query)}`, {
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
            credentials: 'include',
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/foods/?search=${encodeURIComponent(query)}`, {
                    headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
                    credentials: 'include',
                });
                if (retryResponse.ok) {
                    const data = await retryResponse.json();
                    return data;
                }
            }
        }
        if (response.ok) {
            const data = await response.json();
            return data;
        }
    } catch (error) {
        console.log("Failed to search foods", error);
    }
};

export const saveFavorite = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}api/add-favorite`, {
            method: 'POST', 
            headers: getAuthHeaders({'Content-Type': 'application/json'}),
            credentials: 'include', 
            body: JSON.stringify({'id': id}), 
        })
        if(response.ok){
            return true; 
        }
    } catch (_) {
        return false; 
    }
}