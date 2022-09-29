drop DATABASE ProjetoCrud

USE ProjetoCrud
USE ContosoRetailDW


CREATE TABLE Itens(
	id_item int IDENTITY(1,1) NOT NULL,
		constraint PKitem primary key (id_item),
	cod_item varchar(50),
	nome_item varchar(50),
	lote_item varchar(50),
	quantidade_item int,
	)

CREATE TABLE Usuarios(
	id_usuario int IDENTITY(1,1) NOT NULL,
		constraint PKusuario primary key (id_usuario),
	login_usuario varchar(50),
	senha_usuario varchar(50),
	)


CREATE TABLE Historico(
	id_registro int IDENTITY(1,1) NOT NULL,
		constraint PKregistro primary key (id_registro),
	data_mod datetime,
	hora_mod varchar(10),
	usuario_mod varchar(50),
	acao varchar(20),
	id_item int,
		constraint FKitem foreign key (id_item)
		references Itens(id_item),
	cod_item_ori varchar(50),
	cod_item_mod varchar(50),
	nome_item_ori varchar(50),
	nome_item_mod varchar(50),
	lote_item_ori varchar(50),
	lote_item_mod varchar(50),
	quantidade_item_ori int,
	quantidade_item_mod int
	)

	
	insert into Usuarios values('usuario1', 'senha1')
	insert into Usuarios values('usuario2', 'senha2')
	insert into Usuarios values('usuario3', 'senha3')
	
	
	select * from Usuarios

	select * from Itens
	
	select * from Historico
