-- TP 15 - Inventario de Gorras
-- Ejecutar este archivo en MySQL para crear la base de datos y cargar datos de prueba.

CREATE DATABASE IF NOT EXISTS inventario_gorras
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE inventario_gorras;

CREATE TABLE IF NOT EXISTS gorras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    color VARCHAR(30) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Datos de prueba (se insertan solamente si la tabla está vacía).
INSERT INTO gorras (modelo, marca, color, precio, stock)
SELECT * FROM (
    SELECT 'Classic LA', 'CBA CAPS CO', 'Negro', 25000.00, 8
    UNION ALL SELECT 'Spider Edition', 'CBA CAPS CO', 'Negro y rojo', 32000.00, 5
    UNION ALL SELECT 'Vintage NY', 'Urban Caps', 'Azul', 22000.00, 12
    UNION ALL SELECT 'Basic Trucker', 'Street Wear', 'Beige', 18000.00, 10
    UNION ALL SELECT 'Premium Black', 'CBA CAPS CO', 'Negro', 28000.00, 6
) AS datos
WHERE NOT EXISTS (SELECT 1 FROM gorras LIMIT 1);
