import { refresh, getAuthHeaders } from "./authApi.js";

const BASE_URL = import.meta.env.VITE_API_URL;

export const getMealId = async (mealName, date) => {
    try {
        const response = await fetch(
            `${BASE_URL}api/meals/?meal_name=${encodeURIComponent(mealName)}&date=${date}`,
            { headers: getAuthHeaders(), credentials: 'include' }
        );
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(
                    `${BASE_URL}api/meals/?meal_name=${encodeURIComponent(mealName)}&date=${date}`,
                    { headers: getAuthHeaders(), credentials: 'include' }
                );
                if (retryResponse.ok) {
                    const data = await retryResponse.json();
                    return data[0]?.id ?? null;
                }
            }
        }
        if (response.ok) {
            const data = await response.json();
            return data[0]?.id ?? null;
        }
    } catch {
        return null;
    }
};

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

export const deleteWholeMeal = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}api/meals/${id}/`, {
            method: 'DELETE',
            credentials: 'include',
            headers: getAuthHeaders(),
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/meals/${id}/`, {
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
            console.error("Failed to delete meal");
        }
    } catch (error) {
        console.error("Error deleting meal:", error);
    }
};

export const deleteSavedMeal = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}api/saved-meals/${id}/`, {
            method: 'DELETE',
            credentials: 'include',
            headers: getAuthHeaders(),
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/saved-meals/${id}/`, {
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
            console.error("Failed to delete meal");
        }
    } catch (error) {
        console.error("Error deleting meal:", error);
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

export const getFoodByID = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}api/foods/?id=${id}`, {
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
            credentials: 'include',
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/foods/?id=${id}`, {
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
        console.log("Failed to get food by ID", error);
    }
};

export const removeFavorite = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}api/remove-favorite/`, {
            method: 'POST',
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
            credentials: 'include',
            body: JSON.stringify({ id }),
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/remove-favorite/`, {
                    method: 'POST',
                    headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
                    credentials: 'include',
                    body: JSON.stringify({ id }),
                });
                if (retryResponse.ok) {
                    return true;
                }
            }
        }
        if (response.ok) {
            return true;
        }
    } catch (_) {
        return false;
    }
};

export const addSavedMeal = async (custom_meal_name, foods) => {
    try {
        const response = await fetch(`${BASE_URL}api/add-saved-meal/`, {
            method: 'POST',
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
            credentials: 'include',
            body: JSON.stringify({ custom_meal_name, foods }),
        });
        if (response.status === 401) {
            const retryResponse = await refresh();
            if (retryResponse.ok) {
                return true;
            }
        }
        if (response.ok) {
            return true;
        }
    } catch (_) {
        return false;
    }
}
export const updateFoodData = async (new_serving_size, food_id) => {
    try {
        const response = await fetch(`${BASE_URL}api/update-food/`, {
            method: 'POST', 
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }), 
            credentials: 'include', 
            body: JSON.stringify({ new_serving_size, food_id }), 
        }); 
        if(response.status === 401) {
            const retryResponse = await refresh(); 
            if(retryResponse.ok) {
                return true
            }
        } 
        if(response.ok){
            return true; 
        }

    } catch (_) {
        return false; 
    }
}

export const addSaveMealData = async (id, date, meal_name) => {
    try{
        const response = await fetch(`${BASE_URL}api/add-saved-meal-to-meal/`, {
            method: 'POST',
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
            credentials: 'include',
            body: JSON.stringify({ id, date, meal_name }),
        });
        if(response.status === 401){
            const retryResponse = await refresh(); 
            if(retryResponse.ok){
                return true; 
            }
        }
        if(response.ok){
            return true
        }
    } catch(_){
        return false; 
    }
}

export const addMultipleFoods = async (foods, date, meal_name) => {
    try{
        const response = await fetch(`${BASE_URL}api/add-multiple-foods/`, {
            method: 'POST',
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
            credentials: 'include',
            body: JSON.stringify({ foods, date, meal_name }),
        });
        if(response.status === 401){
            const retryResponse = await refresh(); 
            if(retryResponse.ok){
                return true; 
            }
        }
        if(response.ok){
            return true
        }
    } catch(_){
        return false; 
    }
}

export const saveFavorite = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}api/add-favorite/`, {
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
export const getSavedMeals = async () => {
    try {
        const response = await fetch(`${BASE_URL}api/saved-meals/`, {
            headers: getAuthHeaders({ 'Content-Type': 'application/json' }),
            credentials: 'include',
        });

        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const retryResponse = await fetch(`${BASE_URL}api/saved-meals/`, {
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