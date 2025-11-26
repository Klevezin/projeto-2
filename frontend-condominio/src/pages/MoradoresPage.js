// src/pages/MoradoresPage.js
import React, { useState, useEffect } from 'react';
import api from '../api';
import { useNavigate } from 'react-router-dom';

function MoradoresPage() {
    // ... (States existentes: moradores, loading, error)

    const handleDelete = async (moradorId) => {
        if (!window.confirm(`Tem certeza que deseja excluir o morador ${moradorId}?`)) {
            return;
        }

        try {
            // Chamada DELETE para o endpoint /api/moradores/{id}/
            await api.delete(`moradores/${moradorId}/`);
            
            // Se o DELETE for bem-sucedido, removemos o morador da lista local (sem recarregar a página)
            setMoradores(moradores.filter(morador => morador.id !== moradorId));
            alert("Morador excluído com sucesso!");
        } catch (err) {
            console.error("Delete Error:", err);
            setError("Erro ao excluir. Verifique suas permissões (Admin).");
        }
    };

    // ... (fetchMoradores existente)

    // ... (Renderização loading/error)

    return (
        <div>
            <h2>🏠 Lista de Moradores ({moradores.length})</h2>
            {/* ... (renderização da lista) */}
            {moradores.length === 0 ? (
                <p>Nenhum morador cadastrado.</p>
            ) : (
                <ul>
                    {moradores.map(morador => (
                        <li key={morador.id}>
                            <strong>{morador.nome_completo}</strong> (CPF: {morador.cpf}) - Apto ID: {morador.apartamento}
                            
                            {/* Botão para DELETE */}
                            <button onClick={() => handleDelete(morador.id)} style={{ marginLeft: '10px', color: 'red' }}>
                                Excluir (DELETE)
                            </button>
                            
                            {/* Botão para PUT (A ser implementado abaixo) */}
                            <button onClick={() => { /* Iniciar edição */ }} style={{ marginLeft: '5px' }}>
                                Editar (PUT)
                            </button>
                        </li>
                    ))}
                </ul>
            )}
            
            {/* ... (Botão Voltar) */}
        </div>
    );
}

export default MoradoresPage;