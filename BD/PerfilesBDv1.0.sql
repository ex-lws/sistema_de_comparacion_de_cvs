-- Este será el código SQL para poder crear la base de datos. 
-- Version 1.0 del 12/05/2025

create database PerfilesDB;
use PerfilesDB;

-- Crear la tabla de los perfiles

create table Pefiles(
    id int auto_increment primary key,
    -- Acerca de la vacante
    tipoContratacion varchar(50) not null, -- Becario, tiempo indeterminado, termporal, por poryecto.
    horarioTrabajo varchar(50) not null, -- Tiempo completo y medio tiempo.
    modalidadTrabajo varchar(50) not null, -- Presencial, remoto e hibrido.
    sueldoMensualMinimo DOUBLE PRECISION not null, -- Sueldo mensual mínimo.
    sueldoMensualMaximo DOUBLE PRECISION not null, -- Sueldo mensual máximo.
    escolaridad varchar(50) not null, -- Escolaridad minima.
    area varchar(50) not null, -- Area de la vacante.
    puesto varchar(50) not null, -- Puesto de la vacante.
    ubicación varchar(50) not null, -- Ubicación de la vacante. -- Estados de la república mexicana.
    -- Destrezas y habilidades
    idioma varchar(50) not null, -- Idioma requerido.
    nivelIdioma varchar(50) not null, -- Nivel del idioma requerido.
    licenciaConducir boolean not null, -- Licencia de conducir requerida, si o no.
    añosExperiencia integer not null, -- Años de experiencia requeridos.
);



