
import api from './api';

export const login = async (username, password) => {
    try {
        const response = await api.post('token/', { username, password });
        
        
        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        
        return response.data;
        
    } catch (error) {
       
        throw new Error("Credenciais inválidas ou erro no servidor.");
    }
};