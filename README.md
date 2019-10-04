# Dist1

### Consideraciones generales:

Para cada una de las actividades existe un archivo "docker-compose.yml", por lo que dependiendo de la actividad que se quiera ejecutar, basta con meterse dentro de la carpeta "Actividad n" y ejecutar los comandos "docker-compose build" y "docker-compose up".
Una vez finalizada la ejecución de la actividad, el programa terminará y los cambios realizados en los archivos pasarán a ser persistentes.

***Si se llega a forzar la detención de la ejecución, los cambios a los archivos no se verán reflejados y por lo tanto no habrán cambios (no habrá persistencia).***

Es importante notar que para poder enviar cualquier cosa desde la aplicación cliente (de cualquier actividad) se debe cambiar el archivo "target.txt" que se encuentra dentro de sus carpetas "work", asimismo se pueden realizar otros cambios como el servidor a conectar, etc...

(Tal y como está la tarea funciona, dado que no se debiesen cambiar los input de esta tarea no deberían haber problemas, y si llegasen a ocurrir se hablará en alguna instancia futura)
(Solo se ha probado la tarea en w10)

## Actividad 1

Para la primera actividad existen dos aplicaciones ("servidor" y "cliente") que se encuentran en los directorios "s1" y "c1" respectivamente. Dentro de cada una de estos directorios, existen los archivos "Dockerfile", y el código python de la aplicación correspondiente se encuentra en su carpeta "work".
Para la ejecución de esta actividad, basta con escribir el comando "docker-compose build" y luego "docker-compose up" desde la carpeta "Actividad 1".

Los archivos .txt solicitados se encuentran dentro de las carpetas "work" de cada aplicación. Para el cliente (c1), su archivo de "respuestas.txt", junto con su respectivo "target.txt" se encuentra en la carpeta "Actividad 1/c1/work". Para el servidor, su archivo "log.txt" se encuentra en la carpeta "Actividad 1/s1/work".

## Actividad 2

Para la segunda actividad existen 3 aplicaciones ("headnode", "datanode", y "cliente") que se encuentran en los directorios "s2/head", "s2/data" y "c2" respectivamente. Dentro de cada una de estos directorios, existen los archivos "Dockerfile", y el código python de la aplicación correspondiente se encuentra en su carpeta "work".
Para la ejecución de esta actividad, basta con escribir el comando "docker-compose build" y luego "docker-compose up" desde la carpeta "Actividad 2".

Los archivos .txt solicitados se encuentran dentro de las carpetas "work" de cada aplicación. Para el cliente (c2), su archivo de "registro_cliente.txt", junto con su respectivo "target.txt" se encuentra en la carpeta "Actividad 2/c2/work". Para el headnode, sus archivos "registro_server.txt" y "heartbeat_server.txt" se encuentra en la carpeta "Actividad 2/s2/head/work". Finalmente, para cada datanode existe un archivo "data" distinto, esto significa que los archivos .txt solicitados para los datanodes se encuentran en "Actividad 2/s2/data/work1", donde "data1.txt", "data2.txt", y "data3.txt", son los archivos data de los nodos respectivos.

### Integrantes:

- Sebastián Alvarado A. 201673580-1
- Felipe González G. 201673616-6