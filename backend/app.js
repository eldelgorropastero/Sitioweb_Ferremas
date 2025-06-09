// app.js
const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware para permitir peticiones desde el frontend
app.use(cors());
app.use(express.json());

// Ruta de bienvenida
app.get('/', (req, res) => {
  res.send('¡Bienvenido al Web Service de FERREMAS!');
});

// Ruta de ejemplo: productos
app.get('/productos', (req, res) => {
  res.json([
    { id: 1, nombre: 'Martillo', precio: 5000 },
    { id: 2, nombre: 'Destornillador', precio: 3000 },
    { id: 3, nombre: 'Taladro', precio: 25000 }
  ]);
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
