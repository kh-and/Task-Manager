# Task-Manager

**Task-Manager** — это backend приложение на **FastAPI + PostgreSQL**, позволяющее создавать, редактировать, удалять и фильтровать задачи с авторизацией через JWT.  

Видео показывающее работу: https://youtu.be/spaOtEX4pK0
---

## Стек

- Python 3.11  
- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- Pydantic  
- Docker & docker-compose  
- JWT авторизация  
- Soft delete для задач  

---

## Функционал

1. Регистрация и логин пользователей (JWT)  
2. CRUD задач (Create, Read, Update, Delete)  
3. Фильтрация и поиск по задачам  
4. Пагинация и сортировка  
5. Soft delete (удалённые задачи не показываются)  
6. Swagger/OpenAPI документация для тестирования API  
