const express = require('express');
const { config } = require('./config/index');
const usuariosApi = require('./routes/usuarios.js');

const app = express();

// // const port = 5000;

// app.get('/',(req,res)=> {
//   res.send('HOLA MUNDO EXPRESS')
// })

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ mensaje: 'bienvenido a mi API usuarios' })
})

usuariosApi(app)

// app.get('/usuarios',(req,res) =>{
//   res.json({mensaje:'hola estas en el enpoint usuarios'})
// })

app.listen(config.port, () => {
  console.log(`servidor en http://localhost:${config.port}`)
})