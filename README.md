# Propuesta de Visualización eventtia.com 
Este desarrollo corresponde al proyecto final de la materia 201920_ISIS4822-VISUAL ANALYTICS de la Maestría en Ingeniería de Información (MINE) Ingeniería de Sistemas y Computación.

## Problema

La plataforma Eventtia cuenta con algunas herramientas de visualización actualmente, tanto a nivel de evento como a nivel global por organizador de eventos; pero, se requiere potenciar esos dos tipos de dashboards con visualizaciones interactivas que permitan al organizador entender sus eventos. 

## Objetivos 

- Diferenciar el producto con un valor agregado para análisis de eventos basados en información histórica. 
- Diseñar visualizaciones interactivas para dashboard global que permitan al organizador conocer quién es su audiencia, que factores comunes hay en los asistentes a sus eventos para que pueda tomar decisiones en la configuración de sus eventos futuros. 
- Diseñar visualizaciones interactivas para dashboard de eventos. 
- Encontrar mediante visualización de datos la tasa con la que los usuarios repiten eventos. 

## Metodología 

- Recolección de los datos: Actualmente Eventtia cuenta con un conjunto de datos compuesto principalmente por 13.626 eventos, 5.598 cuentas de usuario, 42.530 grupos de asistentes a eventos, 37.896 tipos de asistentes a eventos, 460.285 asistentes a workshops, y 3.466.326 asistentes a eventos. Es un dataset con disponibilidad dinámica que se encuentra almacenado en base de datos relacional MySQL. Los datos fueron entregados en archivos CSV, uno por cada tabla disponible. Cabe anotar que los datos sensibles que permitirían identificar asistentes, organizadores o tipos de asistentes, fueron enmascarados. 
- Entendimiento del problema: A partir de una serie de reuniones con el cliente, se estableció el problema que se busca solucionar por medio de varias visualizaciones. 
- Procesamiento de los datos:  Los datos fueron procesados utilizando Tableau Prep Buider y Python con el fin de obtener la información necesaria para la construcción de las visualizaciones. Para disponer la información para el prototipo funcional, se utilizó el framework Django para implementar el backend sobre una base de datos SQLite. 
- Visualizaciones: Las visualizaciones se construyeron utilizando D3 v.5. y Vega-lite 4 utilizando como frontend Django 3.0. 
- Despliegue: El despliegue de todas las visualizaciones se realizó sobre la plataforma PAAS Heroku utilizando GitHub como fuente del despliegue. 

## Enlaces del Proyecto 

- Aplicación Web: https://viz201920.herokuapp.com
- Código de la aplicacion: https://github.com/jairocollante/viz 
- Video explicativo 
- Diapositivas 

## Autores
- Jairo Rafael Collante Rivero <jr.collante@uniandes.edu.co>
- Mauricio Alejandro Rendón Moreno <ma.rendon@uniandes.edu.co>
- Omar Rojas García <o.rojasg@uniandes.edu.co>
