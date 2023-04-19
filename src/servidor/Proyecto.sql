DROP DATABASE IF EXISTS PYBUYS;
CREATE DATABASE PYBUYS;
USE PYBUYS;

CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    precio DOUBLE,
    foto VARCHAR(50),
    rebaja DOUBLE,
    cantidad INT,
    categoria INT
);

CREATE TABLE categorias (
    id INT PRIMARY KEY,
    nombre VARCHAR(40),
    grupo INT
);

CREATE TABLE caracteristicas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(50) UNIQUE
);
    
CREATE TABLE caracteristicaPorProducto (
    caracteristica_id INT,
    producto_id INT,
    PRIMARY KEY (caracteristica_id , producto_id),
    FOREIGN KEY (producto_id)
        REFERENCES productos (id),
    FOREIGN KEY (caracteristica_id)
        REFERENCES caracteristicas (id)
);

CREATE TABLE cuentas (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(64) NOT NULL
);

CREATE TABLE sesiones (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    clave_encriptada VARCHAR(64) NOT NULL,
    usuario_id INT NOT NULL,
    fecha_inicio TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id)
        REFERENCES cuentas (id)
);

CREATE TABLE carrito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    usuario_id INT,
    cantidad INT,
    FOREIGN KEY (usuario_id)
        REFERENCES cuentas (id),
    FOREIGN KEY (producto_id)
        REFERENCES productos (id)
);

ALTER TABLE productos
	ADD	FOREIGN KEY (categoria)
	REFERENCES categorias(id);

ALTER TABLE categorias
	ADD FOREIGN KEY (grupo)
	REFERENCES categorias(id);
    
#Elimina las sesiones que han "caducado"
delimiter //
CREATE PROCEDURE borrar_sesiones_antiguas()
BEGIN
    DELETE FROM sesiones WHERE TIMESTAMPDIFF(HOUR, fecha_inicio, NOW()) > 12;
END //
DELIMITER ;

delimiter $$
CREATE FUNCTION iniciar_sesion (email VARCHAR(100), contraseña VARCHAR(64))
RETURNS TEXT
DETERMINISTIC
BEGIN
    DECLARE usuario_id INT;
    DECLARE nueva_clave VARCHAR(64);
    DECLARE respuesta JSON;
	SET usuario_id = (SELECT id FROM cuentas WHERE cuentas.email = email AND cuentas.contraseña = SHA2(contraseña, 256));
    IF usuario_id IS NOT NULL THEN
        SET nueva_clave = SHA2(CONCAT(email, NOW()), 256);
        INSERT INTO sesiones (clave_encriptada, usuario_id, fecha_inicio) VALUES (nueva_clave, usuario_id, NOW());
    ELSE
        SET nueva_clave = NULL;
    END IF;
    RETURN nueva_clave;
END $$
DELIMITER ;


#Inserta datos de prueba en la tabla de usuarios
INSERT INTO cuentas (nombre, email, contraseña) VALUES ('admin', 'a@gmail.com', SHA2('1234', 256));

SELECT iniciar_sesion('a@gmail.com','1234');