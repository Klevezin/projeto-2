import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';


import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage';
import MoradoresPage from './pages/MoradoresPage';
import NotFound from './pages/NotFound'; // Para rotas inválidas


const isAuthenticated = () => {
    return localStorage.getItem('access_token');
};

const PrivateRoute = ({ children }) => {
    return isAuthenticated() ? children : <Navigate to="/login" />;
};

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    {/* Rota de Login (Pública) */}
                    <Route path="/login" element={<LoginPage />} />

                    {/* Rotas Protegidas (Exigem Login) */}
                    <Route path="/" element={<PrivateRoute><HomePage /></PrivateRoute>} />
                    <Route path="/moradores" element={<PrivateRoute><MoradoresPage /></PrivateRoute>} />
                    
                    {/* Rota 404 */}
                    <Route path="*" element={<NotFound />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;