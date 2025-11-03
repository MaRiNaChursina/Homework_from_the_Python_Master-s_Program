'''
Создайте FastAPI-приложение, реализующее работу простого калькулятора.
Приложение должно реализовывать следующие методы:

Методы сложения, вычитания, умножения, деления.
Методы создания выражения, возможность добавления сложных выражений, таких как, (а+b)* c + (d - e)/(f-g). Пример: отдельный метод, который принимает аргументы a, op и b; где a, b — атрибуты. op — операция над ними.
Нужно так же реализовать возможность использования выражения в составе более сложного выражения. Пример: метод принимает строку вида (а+b)* c + (d - e)/(f-g). Бизнес-логика парсит строку, расставляет правильным образом порядок выполнения операций, производит вычисление и возвращает ответ. В этом случае потребность в выполнение пунктов 3 и 4 отпадает.
Метод просмотра текущего выражения. Метод возвращает состояние выражения сформированное на текущий момент.
Метод выполнения выражения. Метод возвращает результат выполнения выражения.
'''

import uvicorn
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import math

app = FastAPI()

# Хранилище текущего выражения
current_expression = ""

@app.get("/sum")
def sum(a: float, b: float):
    return {"result": a + b}

@app.get("/difference")
def difference(a: float, b: float):
    return {"result": a - b}

@app.get("/multiplication")
def multiplication(a: float, b: float):
    return {"result": a * b}

@app.get("/division")
def division(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Деление на ноль запрещено")
    return {"result": a / b}


@app.get("/create_expression")
def create_expression(a: float, op: str = Query(..., description="Операция: +, -, *, /"), b: float = None):
    global current_expression
    if op not in {"+", "-", "*", "/"}:
        raise HTTPException(status_code=400, detail="Некорректная операция. Разрешены: +, -, *, /")
    current_expression = f"({a}{op}{b})"
    return {"expression": current_expression}


@app.post("/set_expression")
def set_expression(expr: str):
    global current_expression
    current_expression = expr
    return {"message": "Выражение сохранено", "expression": current_expression}


@app.get("/get_expression")
def get_expression():
    if not current_expression:
        return {"message": "Выражение еще не задано"}
    return {"current_expression": current_expression}


@app.get("/execute_expression")
def execute_expression():
    global current_expression
    if not current_expression:
        raise HTTPException(status_code=400, detail="Нет сохраненного выражения")

    try:
        result = eval(current_expression, {"__builtins__": None}, {"math": math})
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Ошибка: деление на ноль")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка вычисления: {str(e)}")

    return {"expression": current_expression, "result": result}


if __name__ == "__main__":
    uvicorn.run(
        "homework_6:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
