# Sprint_7 — API-тесты Яндекс Самокат

## Установка
```powershell
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install -r requirements.txt
```

## Запуск тестов и сбор результатов Allure
```powershell
pytest --alluredir=allure-results
```

## Генерация HTML-отчёта
```powershell
allure generate allure-results -o allure-report --clean
```

## Открыть отчёт
```powershell
allure open allure-report
```

## Ручная проверка
Открой Swagger: https://qa-scooter.praktikum-services.ru/docs/
Проверь POST /api/v1/courier, POST /api/v1/courier/login,
POST /api/v1/orders и GET /api/v1/orders в Postman.
Сверь фактические коды и тела ответов с документацией.

Тесты автоматически создают уникальных курьеров, а фикстура удаляет
курьера после авторизационных тестов. Заказы создаются в учебном API.
