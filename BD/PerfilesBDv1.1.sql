-- Este será el código SQL para poder crear la base de datos. 
-- Version 1.1 del 12/05/2025

create database PerfilesDB;
use PerfilesDB;

-- Crear la tabla de los perfiles

CREATE TABLE Perfiles (
    id SERIAL PRIMARY KEY,  -- SERIAL es el equivalente a auto_increment en PostgreSQL
    -- Acerca de la vacante
    tipoContratacion VARCHAR(50) NOT NULL, -- Becario, tiempo indeterminado, temporal, por proyecto.
    horarioTrabajo VARCHAR(50) NOT NULL, -- Tiempo completo y medio tiempo.
    modalidadTrabajo VARCHAR(50) NOT NULL, -- Presencial, remoto e híbrido.
    sueldoMensualMinimo DOUBLE PRECISION NOT NULL, -- Sueldo mensual mínimo.
    sueldoMensualMaximo DOUBLE PRECISION NOT NULL, -- Sueldo mensual máximo.
    escolaridad VARCHAR(50) NOT NULL, -- Escolaridad mínima.
    area VARCHAR(50) NOT NULL, -- Área de la vacante.
    puesto VARCHAR(50) NOT NULL, -- Puesto de la vacante.
    ubicacion VARCHAR(50) NOT NULL, -- Ubicación de la vacante (Estados de la república mexicana).
    -- Destrezas y habilidades
    idioma VARCHAR(50) NOT NULL, -- Idioma requerido.
    nivelIdioma VARCHAR(50) NOT NULL, -- Nivel del idioma requerido.
    licenciaConducir BOOLEAN NOT NULL, -- Licencia de conducir requerida (TRUE/FALSE).
    añosExperiencia INTEGER NOT NULL -- Años de experiencia requeridos.
);



