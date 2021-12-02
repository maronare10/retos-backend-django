const mysql= require('mysql');

const mysqlConnection = mysql.createConnection({
  host:'localhost',
  user: 'admin',
  password:'M@rone123',
  database:'nodejsusuarios',
  multipleStatements: true
});

mysqlConnection.connect(function (err){
  if(err){
    console.error(err);
    return;
  }else{
    console.log('estas conectado a la base de datos')
  }
});

module.exports = mysqlConnection;