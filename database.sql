drop database if exists BrainNote;
create database BrainNote;
use BrainNote;

create table user
(
    idUser int(5) auto_increment not null,
    lastname varchar(25) not null,
    firstname varchar(25) not null,
    email varchar(25) not null,
    userpassword varchar(25) not null,
    primary key(idUser)
);

create table categorie
(
    idUser int(5) not null,
    idCategorie int(5) auto_increment not null,
    name varchar(25) not null,
    primary key(idCategorie),
    foreign key(idUser) references user(idUser)
);

create table note
(
    idCategorie int(5) not null,
    idNote int(5) auto_increment not null,
    title varchar(25) not null,
    primary key(idNote),
    foreign key(idCategorie) references categorie(idCategorie)
);