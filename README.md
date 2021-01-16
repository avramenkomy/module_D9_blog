# module_D9_blog

Маршруты приложения:
https://<app_name>/ - список постов
https://<app_name>/<int:pk> - подробности о конкретном посте
https://<app_name>/categories/ - список категорий и входящих в них постов
https://<app_name>/categories/<int:pk> - подробности о конкретной категории, включая список входящих постов

Поддерживаются post запросы к:
    https://<app_name>/ - для создания новых постов
    https://<app_name>/categories/ - для создания новых категорий

Для post запросов при создании нового поста обязательно указывать: "title", "slug", "status", "content"
