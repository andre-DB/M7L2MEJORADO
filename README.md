Discord Bot - Detector de Imágenes IA
¿Qué hace?
Recibe una imagen
La analiza con un modelo de IA
Indica si es real o generada por IA

Este bot de Discord permite que el usuario envíe una imagen y automáticamente la clasifica utilizando un modelo de inteligencia artificial. El resultado indica si la imagen fue creada por un humano o generada por IA, junto con un porcentaje de probabilidad.

¿Cómo funciona?
El usuario ejecuta el comando $check
Adjunta una imagen
El bot guarda la imagen en una carpeta local
La imagen se procesa con un modelo .h5
El bot envía el resultado al chat
Ejemplo de salida

Si la imagen es real:

Tu imagen ha sido analizada y es 87.5% real!

Si la imagen es generada por IA:

Tu imagen ha sido analizada y es 92.3% hecha por IA!
Archivos importantes
bot.py: código principal del bot
model.py: función que clasifica la imagen
keras_model.h5: modelo de inteligencia artificial
labels.txt: etiquetas del modelo
Requisitos

Instalar dependencias:

pip install discord.py tensorflow pillow
