#NOMBRE Y APPELIDO
nombre = "Axel German"
apellido = "Le Roux"

#IMPRIMIR NOMBRE Y APELLIDO
print(f"mi nombre es: {nombre} y mi apellido es: {apellido}")

#ACTIVIDADES 1: 
 # 1. ¿Qué es GitHub?
 #GITHUB es una plataforma online que permite almacenar, gestionar y colaborar en proyectos. Permite el control de versiones a traves de Git.
 # 2. ¿Cómo crear un repositorio en GitHub?
 #al hacerse un usuario en GitHub, se puede crear un repositorio desde la página principal. Haciendo clic en el botón "New" o "Create repository. Se elige un nombre del repositior, licencia y si es publica o privada.
 # 3. ¿Cómo crear una rama en Git? 
 # usando el comando : git branch <nombre de la rama> o git checkout -m <nombre de la rama> para crear y cambiarse a la rama.
# 4. ¿Cómo cambiar a una rama en Git? 
# Usando el comando: git checkout <nombre de la rama>. 
#5. ¿Cómo fusionar ramas en Git? 
# usando el comando merge : git merge <nombre de la rama>.
#6. ¿Cómo crear un commit en Git? 
# usando el comando: git commit -m "mensaje del comit"

#7. ¿Cómo enviar un commit a GitHub? 
# usando el command: git push origin <nombre de la rama>.
# 8. ¿Qué es un repositorio remoto? 
#  es una copia del repositorio local que se encuentra en un servidor, como GitHub. Permite colaborar con otros usuarios y compartir cambios de manera sencilla.
# 9.¿Cómo agregar un repositorio remoto a Git? 
# usando el comando: git remote add origin <url del repositorio remoto>.
#10. ¿Cómo empujar cambios a un repositorio remoto? 

#11.¿Cómo tirar de cambios de un repositorio remoto? 
#12. ¿Qué es un fork de repositorio? 
#13. ¿Cómo crear un fork de un repositorio?
# 14. ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?
# Luego de hacer un fork y un push a tu rama, vas a GitHub, entrás al repositorio original y hacés clic en "Compare & pull request".
# Completás el título, descripción del cambio y hacés clic en "Create pull request".

# 15. ¿Cómo aceptar una solicitud de extracción?
# El propietario del repositorio revisa el pull request en GitHub y, si está todo correcto, hace clic en "Merge pull request" para aceptar los cambios.

# 16. ¿Qué es una etiqueta en Git?
# Una etiqueta (tag) es una referencia fija a un commit, normalmente utilizada para marcar versiones específicas de un proyecto (como v1.0.0).

# 17. ¿Cómo crear una etiqueta en Git?
# Usás el comando:
# git tag nombre-etiqueta
# También podés agregar un mensaje con:
# git tag -a nombre-etiqueta -m "mensaje"

# 18. ¿Cómo enviar una etiqueta a GitHub?
# Para una etiqueta específica:
# git push origin nombre-etiqueta
# Para enviar todas las etiquetas:
# git push --tags

# 19. ¿Qué es un historial de Git?
# Es el registro cronológico de todos los commits del repositorio, incluyendo autor, fecha y mensaje de cada cambio.

# 20. ¿Cómo ver el historial de Git?
# Usás:
# git log
# También podés ver un resumen con:
# git log --oneline

# 21. ¿Cómo buscar en el historial de Git?
# Para buscar un commit por mensaje:
# git log --grep="palabra clave"
# Para buscar por autor:
# git log --author="nombre"

# 22. ¿Cómo borrar el historial de Git?
# No se recomienda, pero se puede reiniciar con:
# git checkout --orphan nueva-rama
# git add .
# git commit -m "Nuevo comienzo"
# git branch -D main
# git branch -m main
# git push -f origin main

# 23. ¿Qué es un repositorio privado en GitHub?
# Es un repositorio que sólo es visible para vos y las personas que invites. Se usa para proyectos personales o confidenciales.

# 24. ¿Cómo crear un repositorio privado en GitHub?
# Al crear un nuevo repositorio en GitHub, seleccionás la opción "Private" antes de hacer clic en "Create repository".

# 25. ¿Cómo invitar a alguien a un repositorio privado en GitHub?
# En el repositorio, vas a "Settings" > "Collaborators" > escribís el nombre de usuario > clic en "Add collaborator".

# 26. ¿Qué es un repositorio público en GitHub?
# Es un repositorio accesible públicamente, donde cualquier persona puede ver el código, clonarlo o contribuir si se lo permitís.

# 27. ¿Cómo crear un repositorio público en GitHub?
# En el proceso de creación de un nuevo repo, seleccionás "Public" y luego hacés clic en "Create repository".

# 28. ¿Cómo compartir un repositorio público en GitHub?
# Copiás la URL del repositorio desde la barra de direcciones o desde el botón "Code" y se la pasás a quien quieras.
