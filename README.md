# Dist1
## Actividad 1
Para la primera actividad, existen dos aplicaciones ("servidor" y "cliente"), que se encuentran en los directorios "s1" y "c1" respectivamente. Dentro de cada una de estos directorios, existen los archivos "docker-compose.yml", "Dockerfile", y el código python de la aplicación correspondiente.
Para ejectuar cualquiera de estas aplicaciones, basta ejectuar el comando "docker-compose build" y luego "docker-compose up" desde la carpeta contenedora.

### Consideraciones y funcionamiento:
 - Cuando el servidor se inicia, muestra su dirección IP y su puerto. La dirección IP mostrada es virtual, y se usa cuando ambos contenedores (cliente y servidor) se ejecutan en la misma máquina. Si se ejecutan en máquinas distinas, debe usarse la dirección IP de la máquina.
 - El cliente necesita la dirección IP y el puerto abierto del servidor. Estos deben indicarse en el archivo "target.txt" en la carpeta "c1".
 - Si el cliente se inicia y no encuentra el servidor, lanzará un error y se cerrará.
 - Cuando el cliente encuentra el servidor, le envía el mensaje "hello" y espera una respuesta. Al recibir la respuesta, la guarda en un archivo "respuestas.txt" y cierra.
 - Cuando el servidor recibe un mensaje de un cliente conectado, guarda el mensaje recibido en el archivo "log.txt" y le envía la respuesta "received message".
 - Ambos archivos ("log.txt" y "respuestas.txt") se encuentran en el directorio "/app" del contenedor de la apliación correspondiente.
