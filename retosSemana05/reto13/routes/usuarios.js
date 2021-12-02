const { Router, request } = require('express');
const express = require('express');
const { dataUsuarios } = require('../data/usuarios');
const mysqlConnection = require('../lib/mysql');

function usuariosApi(app) {
  const router = express.Router();
  app.use("/usuarios", router);

  router.get("/", async function (req, res, next) {
    try {
      // const usuarios = await Promise.resolve(dataUsuarios);

      // res.status(200).json({
      //   status: 'ok',
      //   data: usuarios
      // })
      mysqlConnection.query('select * from usuarios', (err, rows, fields) => {
        if (!err) {
          res.json(rows);
        } else {
          console.log(err);
        }
      });

    } catch (err) {
      next(err);
    }
  })

  router.get("/:id", (req, res) => {
    const { id } = req.params;
    mysqlConnection.query('select * from usuarios where id = ?', [id], (err, rows, fields) => {
      if (!err) {
        res.json(rows[0]);
      } else {
        console.log(err);
      }
    });
  });

  router.post('/', (req, res) => {
    const { name, email, role } = req.body;
    console.log(name, email, role);
    mysqlConnection.query('insert into usuarios(name,email,role) values(?,?,?)',
      [name, email, role], (err, rows, fields) => {
        if (!err) {
          res.json({ status: 'ok' });
        } else {
          console.log(err);
        }
      })
  });

  router.put('/:id', (req,res) => {
    const { name, email, role } = req.body;
    const { id } = req.params;
    mysqlConnection.query('update usuarios set name=?,email=?,role=? where id =?',
      [name, email, role,id], (err, rows, fields) => {
        if (!err) {
          res.json({status: 'Actualización exitosa' });
        }else {
            console.log(err);
          }
        });
  });

  router.delete('/:id',(req,res)=>{
    const {id} = req.params;
    mysqlConnection.query('delete from usuarios where id = ?', [id],(err,rows,fields)=>{
      if(!err){
        res.json({status:'eliminación exitosa'});
      }else {
        console.log(err);
      }
    })
  })
}

module.exports = usuariosApi