import { refresh } from "./authApi.js";

const BASE_URL = import.meta.env.VITE_API_URL;

export const getUserData = async () => {
    try {
        const response = await fetch(`${BASE_URL}api/user/`, {
            credentials: 'include',
        })
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const response = await fetch(`${BASE_URL}api/user/`, {
                    credentials: 'include',
                })
                if (response.ok) {
                    const data = await response.json();
                    return data[0].username
                }
            }
        }
        if (response.ok) {
            const data = await response.json();
            return data[0].username
        }
    } catch (error) {
        console.log("Failed to fetch", error)
    }
}

export const getProgress = async () => {
    try {
        const response = await fetch(`${BASE_URL}api/progress/`, {
            credentials: 'include',
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const response = await fetch(`${BASE_URL}api/progress/`, {
                    credentials: 'include',
                });
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
    } catch (error) {
        console.log('Failed to Fetch', error)
    }
};

export const getDays = async () => {
    try {
        const response = await fetch(`${BASE_URL}api/days/`, {
            credentials: 'include',
        })
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const response = await fetch(`${BASE_URL}api/days/`, {
                    credentials: 'include',
                })
                if (response.ok) {
                    const data = await response.json();
                    return data
                }
            }
        }
        if (response.ok) {
            const data = await response.json();
            return data
        } else {
            return false
        }
    } catch (error) {
        console.log("Failed", error);
    }
};

export const saveProgress = async (progressInfo) => {
    try {
        const response = await fetch(`${BASE_URL}api/update-progress/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify(progressInfo),
        });
        if (response.status === 401) {
            const refreshResponse = await refresh();
            if (refreshResponse.ok) {
                const response = await fetch(`${BASE_URL}api/update-progress/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    credentials: 'include',
                    body: JSON.stringify(progressInfo),
                });
                if (response.ok) {
                    const result = await response.json();
                    console.log("Saved", result);
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