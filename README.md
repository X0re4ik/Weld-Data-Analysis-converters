# ZIT-ReadWeld-notification-system
Проект является частью системы мониторинга ReadWeldMonitoring


Разработчик: Мочалов Антон Вячеславович, 2023 год

Используемый стек технологий (в порядке частоты использования):
1.	Python 3.6.8 – основной язык программирования
2.	openpyxl для генерации excel-отчетов
3.	SQLAlchemy - ORM для работы с базой данных
4.	Docker – для развертывания приложения на удаленном сервере

Генератор отчетов исследует активные датчики и параллельно с 
работой системы создаёт excel отчеты после рабочего дня. 
Отчеты всегда доступны на web-сайте в разделе «Кладовка».
