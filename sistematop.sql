create database sistematop;
use sistematop;

create table usuarios(
codigo int primary key auto_increment,
usuario varchar(255),
senha varchar(255));

insert into usuarios values (1,'ana','miau');

select * from usuarios;

## TIPO DE DADO BLOB #########################
insert into usuarios values
(2, 'beto',aes_encrypt('1234','bola'));

select usuario, cast(aes_decrypt(senha,'bola')
as char) from usuarios;

#############################################

insert into usuarios values
(3,'carlos', MD5('ninja'));
