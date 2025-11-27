-- CREACION TABLA HISTORIAL --
CREATE TABLE historico(
	id_historico INT AUTO_INCREMENT PRIMARY KEY,
    max_intentos INT,
	victoria BOOLEAN,
    tiempo DATETIME DEFAULT NOW(),
    puntuacion INT,
    dificult INT
    
    
    
    
    );