create database restaurante;

use restaurante;

create table cardapio(
codigo int primary key auto_increment,
prato varchar(100),
valor decimal(10,2) );

select * from cardapio;