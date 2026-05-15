const BASE_URL = import.meta.env.VITE_API_URL;

// Get stored access token
export const getAccessToken = () => localStorage.getItem('accessToken');

// Get auth headers for API requests (Safari fallback for ITP blocking cookies)
export const getAuthHeaders = (additionalHeaders = {}) => {
    const token = getAccessToken();
    return {
        ...additionalHeaders,
        ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    };
};

export const login = async (username, password) => {
    const response = await fetch(`${BASE_URL}token/`, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
        credentials: 'include',
    });

    if (response.ok) {
        const data = await response.json();
        // Store tokens for Safari (cookies may be blocked by ITP)
        if (data.access) localStorage.setItem('accessToken', data.access);
        if (data.refresh) localStorage.setItem('refreshToken', data.refresh);
        return "Success";
    }

    if (response.status === 401) throw new Error('Incorrect username or password.');
    throw new Error('Login failed. Please try again.');
};

export const signup = async (username, email, password) => {
    const response = await fetch(`${BASE_URL}register/`, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ username, email, password }),
    });

    if (response.ok) return login(username, password);

    if (response.status === 409) {
        const data = await response.json().catch(() => ({}));
        const field = data.username ? 'username' : data.email ? 'email' : null;
        const msg = field === 'username' ? 'Username already taken.'
                  : field === 'email'    ? 'Email already registered.'
                  : 'Account already exists.';
        const err = new Error(msg);
        if (field) err.field = field;
        throw err;
    }

    throw new Error('Sign up failed. Please try again.');
};

export const refresh = async () => {
    // Try cookie-based refresh first, with localStorage fallback for Safari
    const refreshToken = localStorage.getItem('refreshToken');

    const response = await fetch(`${BASE_URL}token/refresh/`, {
        credentials: 'include',
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        // Send refresh token in body as fallback for Safari
        body: JSON.stringify({ refresh: refreshToken }),
    });

    if (response.ok) {
        const data = await response.json();
        // Store new access token for Safari
        if (data.access) {
            localStorage.setItem('accessToken', data.access);
        }
    }

    return response;
};

export const clearTokens = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
};