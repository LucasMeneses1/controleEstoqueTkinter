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
	
	
	
	
	
SELECT * FROM Itens
WHERE cod_item = '{cod}' AND lote_item = '{lote}';

SELECT * FROM Itens
WHERE cod_item = '{cod}';

SELECT * FROM Itens

INSERT INTO Historico 
                        Values(
                        '{data}', 
                        '{hora}', 
                        '{usuario}', 
                        '{acao}',
                        '{fk}', 
                        '-',
                        '{cod}',
                        '-',
                        '{nome}',
                        '-',
                        '{lote}',
                        '',  
                        '{qtd}' )
						

select id_item, nome_item, quantidade_item from Itens
where cod_item = '{cod}' and lote_item = '{lote}'


INSERT INTO Historico 
                        Values(
                        '{data}', 
                        '{hora}', 
                        '{usuario}', 
                        '{acao}',
                        '{fk}', 
                        '{cod}',
                        '-',
                        '{nome}',
                        '-',
                        '{lote}',
                        '-',
                        '{qtd}',
                        '0') 
						
						
INSERT INTO Historico 
                        Values(
                        '{data}', 
                        '{hora}', 
                        '{usuario}', 
                        '{acao}',
                        '{fk}', 
                        '{cod}',
                        '-',
                        '{nome}',
                        '-',
                        '{lote}', 
                        '-',
                        '{qtd}', 
                        '{qtda}')
						
						
select id_item, nome_item, quantidade_item from Itens
where cod_item = '{cod}' and lote_item = '{lote}'

INSERT INTO Historico 
                        Values(
                        '{data}', 
                        '{hora}', 
                        '{usuario}', 
                        '{acao}',
                        '{fk}', 
                        '{cod}',
                        '-',
                        '{nome}',
                        '-',
                        '{lote}', 
                        '-',
                        '{qtd}', 
                        '{qtda}')
						
						
select cod_item from Itens
where id_item = '{fk}'

INSERT INTO Historico 
                            Values(
                            '{data}', 
                            '{hora}', 
                            '{usuario}', 
                            '{acao}',
                            '{fk}', 
                            '{cod}', 
                            '{cod_n}',
                            '{nome}', 
                            '-',
                            '{lote}', 
                            '-',
                            '{qtd}',
                            '')
							
select nome_item from Itens
where id_item = '{fk}'

INSERT INTO Historico 
                            Values(
                            '{data}', 
                            '{hora}', 
                            '{usuario}', 
                            '{acao}',
                            '{fk}', 
                            '{cod}',
                            '-',
                            '{nome}',
                            '{nome_n}',
                            '{lote}',
                            '-',
                            '{qtd}',
                            '')
							
							
select lote_item from Itens
where id_item = '{fk}'

INSERT INTO Historico 
                            Values(
                            '{data}', 
                            '{hora}', 
                            '{usuario}', 
                            '{acao}',
                            '{fk}', 
                            '{cod}',
                            '-',
                            '{nome}',
                            '-',
                            '{lote}',
                            '{lote_n}',
                            '{qtd}',
                            '') 
							
							
SELECT quantidade_item FROM Itens
WHERE cod_item = '{cod}' AND lote_item = '{lote}';

UPDATE Itens
SET quantidade_item = quantidade_item - {qtd}
WHERE cod_item = '{cod}' AND lote_item = '{lote}';

SELECT * FROM Usuarios
WHERE login_usuario = '{lg}';

SELECT senha_usuario FROM Usuarios
WHERE login_usuario = '{lg}';


