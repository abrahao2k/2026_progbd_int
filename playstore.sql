create database playstore;

use playstore;

create table apps(
codigo int primary key auto_increment,
nome varchar(100) not null,
versao varchar(100),
preco float default 0
);

insert into apps values
(null, "WhatsApp", "2026", 0);

insert into apps values
(null, "Minecraft", "1.5", 40);

insert into apps values
(null, "Google Chrome", "125", 0);

insert into apps values
(null, "Globoplay", "10.3", 29);






