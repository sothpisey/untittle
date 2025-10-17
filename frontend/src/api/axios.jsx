import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_BASE_URL || 'http://localhost:8000',
});


api.interceptors.request.use((config) => {
  const token = sessionStorage.getItem('access_token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;
