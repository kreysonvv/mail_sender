#!/usr/bin/env python3
import os
import zipfile
import smtplib
from email.message import EmailMessage
from datetime import datetime
# Проверка наличия папки с текущей датой
today_date = datetime.today().strftime('%Y-%m-%d')
folder_path = f'/test/{today_date}'
if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
    print(f'Папка {folder_path} не существует.')
        exit()
# Архивирование содержимого папки в zip
zip_filename = f'{folder_path}.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, _, files in os.walk(folder_path):
            for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, folder_path))
print(f'Архив {zip_filename} успешно создан.')
# Отправка почты без авторизации
# Настройки SMTP сервера
smtp_server = 'Ваш SMTP-сервер'
smtp_port = 25  # Порт SMTP-сервера (обычно 25)
# Список получателей
recipients = ['Получатель 1', 'Получатель 2','Получатель 3']
# Формирование письма
msg = EmailMessage()
msg['Subject'] = f'Название темы {today_date}'
msg['From'] = 'Адрес отправителя'
msg['To'] = ', '.join(recipients)
msg.set_content(f'Тело письма')
# Прикрепление архива к письму
with open(zip_filename, 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='zip', filename=os.path.basename(zip_filename))
# Отправка письма
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.send_message(msg)
    print('Письмо успешно отправлено.')
except Exception as e:
    print(f'Ошибка отправки письма: {e}')
finally:
    # Удаление временного архива
    os.remove(zip_filename)
    print(f'Архив {zip_filename} удален.')