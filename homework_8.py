'''
Задание 1
Создайте сервис для сбора обращения абонентов на основе FastAPI.
Эндпойнт должен принимать следующие атрибуты:

фамилия – с заглавной буквы, содержит только кирилицу;
имя – с заглавной буквы, содержит только кирилицу;
дату рождения;
номер телефона;
e-mail.
Все переданные атрибуты должны валидироваться с помощью модели Pydantic.
Результат сохраняется на диске в виде json-файла, содержащего переданные атрибуты.

Задание 2* (выполнение необязательно, сложность повышенная)
Добавьте в сервис следующие атрибуты:

причина обращения – нет доступа к сети, не работает телефон, не приходят письма;
дата и время обнаружения проблемы.
Все переданные атрибуты должны валидироваться с помощью модели Pydantic.

Задание 3** (выполнение необязательно, сложность высокая)
Допишите сервис так, чтобы в одном запросе могло быть несколько причин обращения.
Все переданные атрибуты должны валидироваться с помощью модели Pydantic.
'''
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date, datetime
from typing import List, Optional
import json
import os
import re

app = FastAPI(title="Сервис обращений абонентов")

DATA_FILE = "requests_data.json"

# ======== Модель данных ========
class Subscriber(BaseModel):
    last_name: str = Field(..., description="Фамилия: с заглавной буквы, только кириллица")
    first_name: str = Field(..., description="Имя: с заглавной буквы, только кириллица")
    birth_date: date
    phone_number: str = Field(..., description="Формат: +7XXXXXXXXXX")
    email: EmailStr
    reasons: Optional[List[str]] = Field(default=None, description="Список причин обращения")
    problem_detected_at: Optional[datetime] = Field(default=None, description="Дата и время обнаружения проблемы")

    @validator("last_name", "first_name")
    def validate_cyrillic(cls, value):
        if not re.match(r"^[А-ЯЁ][а-яё]+(-[А-ЯЁ][а-яё]+)?$", value):
            raise ValueError("Должно начинаться с заглавной буквы, кириллица, допускается дефис")
        return value

    @validator("phone_number")
    def validate_phone(cls, value):
        if not re.match(r"^\+7\d{10}$", value):
            raise ValueError("Неверный формат номера. Пример: +79991234567")
        return value

    @validator("reasons")
    def validate_reasons(cls, reasons):
        allowed = ["нет доступа к сети", "не работает телефон", "не приходят письма"]
        if reasons is None:
            return []
        for r in reasons:
            if r not in allowed:
                raise ValueError(f"Недопустимая причина: {r}. Разрешено: {', '.join(allowed)}")
        return reasons


# ======== Эндпоинты ========
@app.post("/add_request")
def add_request(subscriber: Subscriber):
    data = subscriber.dict()

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []

    existing_data.append(data)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4, default=str)

    return {"status": "ok", "message": "Обращение успешно сохранено", "data": data}


@app.get("/get_all_requests")
def get_all_requests():
    if not os.path.exists(DATA_FILE):
        return {"status": "ok", "message": "Файл с обращениями ещё не создан"}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Ошибка чтения данных")

    if not data:
        return {"status": "ok", "message": "Пока нет ни одного обращения"}

    return {"status": "ok", "count": len(data), "requests": data}


@app.delete("/clear_requests")
def clear_requests():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)
    return {"status": "ok", "message": "Все обращения удалены"}


if __name__ == "__main__":
    uvicorn.run(
        "homework_8:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
>>>>>>> 1873813 (Домашнее задание 7 - 101555)
