import os
import json
import uuid
from typing import List, Optional
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- Настройки ---
NOTES_DIR = "notes_storage"  # Папка, где будут лежать JSON файлы

# Создаем папку, если её нет
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Note Taking API")

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Схемы данных (Pydantic) ---
class NoteCreate(BaseModel):
    title: str
    content: str

class Note(BaseModel):
    id: str
    title: str
    content: str
    created_at: str

# --- Вспомогательные функции ---
def get_note_path(note_id: str) -> str:
    return os.path.join(NOTES_DIR, f"{note_id}.json")

# --- Эндпоинты (Маршруты) ---

@app.post("/notes/", response_model=Note)
def create_note(note_data: NoteCreate):
    """Создать новую заметку и сохранить в JSON файл."""
    note_id = str(uuid.uuid4())
    new_note = Note(
        id=note_id,
        title=note_data.title,
        content=note_data.content,
        created_at=datetime.now().isoformat()
    )
    
    file_path = get_note_path(note_id)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(new_note.dict(), f, ensure_ascii=False, indent=4)
    
    return new_note

@app.get("/notes/", response_model=List[Note])
def list_notes():
    """Получить список всех заметок."""
    notes = []
    for filename in os.listdir(NOTES_DIR):
        if filename.endswith(".json"):
            file_path = os.path.join(NOTES_DIR, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                notes.append(json.load(f))
    return notes

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: str):
    """Получить одну заметку по ID."""
    file_path = get_note_path(note_id)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: str, note_data: NoteCreate):
    """Обновить существующую заметку."""
    file_path = get_note_path(note_id)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    
    # Читаем старую, чтобы сохранить дату создания
    with open(file_path, "r", encoding="utf-8") as f:
        old_data = json.load(f)
    
    updated_note = Note(
        id=note_id,
        title=note_data.title,
        content=note_data.content,
        created_at=old_data["created_at"]
    )
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(updated_note.dict(), f, ensure_ascii=False, indent=4)
    
    return updated_note

@app.delete("/notes/{note_id}")
def delete_note(note_id: str):
    """Удалить заметку."""
    file_path = get_note_path(note_id)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    
    os.remove(file_path)
    return {"message": f"Заметка {note_id} удалена"}

# --- Запуск ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)