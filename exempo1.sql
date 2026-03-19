create database escola;

use escola;

create table alunos(
codigo int primary key auto_increment,
nome varchar(80) not null,
curso varchar(80),
serie int);

select * from alunos;