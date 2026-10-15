   #!/bin/bash

   echo "🚀 Начинаем автоматическое развертывание..."

   # Обновляем систему
   sudo apt update -y

   # Устанавливаем Nginx
   sudo apt install nginx -y

   # Создаем кастомную страничку
   echo "<h1>Deployed by My Bash Script!</h1>" | sudo tee /var/www/html/index.html

   # Перезапускаем веб-сервер, чтобы он точно подхватил изменения
   sudo systemctl restart nginx

   echo "✅ Сервер успешно развернут! Открой IP в браузере."
