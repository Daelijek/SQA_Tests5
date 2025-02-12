# SQA Project: API Testing & BDD Framework

Этот проект содержит автоматизированные тесты для API GitHub и JSONPlaceholder, реализованные с использованием:

- **Postman/Newman** для API-тестирования и регрессионного тестового набора
- **Behave (BDD)** для тестов в стиле Gherkin

## Установка и запуск проекта

### 1. Установка зависимостей

Для запуска BDD тестов требуется Python (версия 3.6 или выше). Установите зависимости с помощью pip:
Убедитесь, что у вас установлен Newman (для установки через npm):

```bash
pip install -r requirements.txt
npm install -g newman
```

### 2. Запуск тестов через терминал

API-тестирование с Newman
Для GitHub CRUD коллекции

```bash
newman run api-testing/collections/github-crud-collection.json -e api-testing/environments/github-environment.json
```

Для регрессионного тестового набора

```bash
newman run api-testing/collections/regression-suite.json -e api-testing/environments/github-environment.json
```

BDD-тестирование с Behave
Перейдите в директорию bdd-framework и запустите тесты

```bash
cd bdd-framework
behave
```

### 3. Запуск тестов в Postman (GUI)

Чтобы запускать тесты через графический интерфейс Postman:

Импорт коллекций:

Откройте Postman.
Нажмите на кнопку "Import" и выберите файлы:
api-testing/collections/github-crud-collection.json
api-testing/collections/regression-suite.json (если требуется)
Импорт окружений:

Импортируйте файл api-testing/environments/github-environment.json.
Перейдите в "Manage Environments" и убедитесь, что переменные github_username, github_token и repo_name заданы корректно.
Запуск через Collection Runner:

Нажмите кнопку "Runner" (обычно в правом верхнем углу Postman).
Выберите нужную коллекцию (например, GitHub CRUD Operations).
Выберите соответствующее окружение (например, GitHub Environment).
Нажмите "Run".

# SQA Project: API Testing & BDD Framework

Этот проект содержит автоматизированные тесты для API GitHub и JSONPlaceholder, реализованные с использованием:

- **Postman/Newman** для API-тестирования и регрессионного тестового набора
- **Behave (BDD)** для тестов в стиле Gherkin

## Структура проекта

sqa-project/
├── api-testing/
│ ├── collections/
│ │ ├── github-crud-collection.json # Коллекция Postman для CRUD операций с GitHub
│ │ └── regression-suite.json # Регрессионный тестовый набор (Postman)
│ ├── environments/
│ │ ├── dev-environment.json # Окружение для тестирования JSONPlaceholder
│ │ └── github-environment.json # Окружение для тестирования GitHub API
├── bdd-framework/
│ ├── features/
│ │ ├── steps/
│ │ │ ├── api_steps.py # Шаги для тестов JSONPlaceholder
│ │ │ └── github_steps.py # Шаги для CRUD тестов GitHub
│ │ ├── api_tests.feature # Feature файл для тестов JSONPlaceholder
│ │ └── github_crud.feature # Feature файл для CRUD тестов GitHub
├── behave.ini # Конфигурация Behave
├── requirements.txt # Зависимости проекта
└── README.md # Этот файл

## Установка и запуск проекта

### 1. Установка зависимостей

Для запуска BDD тестов требуется Python (версия 3.6 или выше). Установите зависимости с помощью pip:

```bash
pip install -r requirements.txt
```

### 2. Запуск тестов через терминал

#### a) API-тестирование с Newman

Убедитесь, что у вас установлен Newman (для установки через npm):

```bash
npm install -g newman
```

Примеры запуска:

- Для GitHub CRUD коллекции:

```bash
  newman run api-testing/collections/github-crud-collection.json -e api-testing/environments/github-environment.json
```

```bash
- Для регрессионного тестового набора:
  newman run api-testing/collections/regression-suite.json -e api-testing/environments/github-environment.json
```

#### b) BDD-тестирование с Behave

Перейдите в директорию `bdd-framework` и запустите тесты:

```bash
cd bdd-framework
behave
```

### 3. Запуск тестов в Postman (GUI)

Чтобы запускать тесты через графический интерфейс Postman, выполните следующие шаги:

1. **Импорт коллекций:**

   - Откройте Postman.
   - Нажмите на кнопку "Import" и выберите файлы:
     - `api-testing/collections/github-crud-collection.json`
     - `api-testing/collections/regression-suite.json` (если требуется)

2. **Импорт окружений:**

   - Импортируйте файл `api-testing/environments/github-environment.json`.
   - Перейдите в "Manage Environments" и убедитесь, что переменные `github_username`, `github_token` и `repo_name` заданы корректно.

3. **Запуск через Collection Runner:**
   - Нажмите кнопку "Runner" (обычно в правом верхнем углу Postman).
   - Выберите нужную коллекцию (например, "GitHub CRUD Operations").
   - Выберите соответствующее окружение (например, "GitHub Environment").
   - Нажмите "Run".

## Примечания

- **Безопасность:**  
  Не публикуйте реальные токены или секреты в публичном репозитории. Используйте переменные окружения или секретные менеджеры (например, GitHub Secrets) для CI/CD.

- **BDD-тесты:**  
  Тесты в директории `bdd-framework` используют Gherkin-сценарии, которые запускаются через Behave и не интегрированы в Postman.

- **Расширение регрессионного набора:**  
  Для повышения покрытия тестов можно добавить дополнительные сценарии, например, проверки на коды ошибок (422, 404) и проверки содержимого ответов.