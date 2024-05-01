# PadronRucSunatHttptoDatabase

Este proyecto se centra en la descarga, procesamiento y migración de datos del padrón reducido de RUC de SUNAT a una base de datos.

## Procesos terminados

1. Descarga del archivo ZIP del padrón reducido de RUC desde la página oficial de SUNAT. Este proceso se realiza en el archivo `data_processing.ipynb`.
2. Extracción del archivo ZIP descargado.
3. Limpieza de los datos descargados y preparación para su migración. Este proceso también se realiza en `data_processing.ipynb`.

## Procesos pendientes

1. Análisis de los datos: Actualmente, solo se ha completado un 30% del análisis de los datos. Se necesita realizar un análisis más profundo para entender mejor los datos y cómo se pueden utilizar de manera efectiva.
2. Migración de los datos a la base de datos: Aún no se ha implementado la funcionalidad para migrar los datos procesados a la base de datos. Los detalles de la base de datos se encuentran en el archivo `config.yaml`.
3. Pruebas y validación: Una vez que se haya completado la migración de los datos, será necesario realizar pruebas para asegurarse de que los datos se han migrado correctamente.

## Cómo contribuir

Este proyecto está en desarrollo y cualquier contribución es bienvenida. Si tienes alguna sugerencia o mejora, no dudes en abrir un issue o un pull request.