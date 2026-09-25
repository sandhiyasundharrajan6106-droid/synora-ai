import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || (import.meta.env.PROD ? '' : 'http://localhost:7985');

const api = axios.create({
  baseURL: API_URL,
  timeout: 20000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export async function postJson(endpoint, payload) {
  const response = await api.post(endpoint, payload);
  return response.data;
}

export async function getJson(endpoint) {
  const response = await api.get(endpoint);
  return response.data;
}

export const backendUrl = API_URL;
