from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import os

app = FastAPI(title="FreshIQ Backend")

DB_PATH = os.path.join(os.path.dirname(__file__), "freshiq.db")

# Initialize database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        expiry_date TEXT,
        note TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

class Item(BaseModel):
    name: str
    category: Optional[str] = None
    expiry_date: Optional[str] = None
    note: Optional[str] = None

@app.post("/items", status_code=201)
def create_item(item: Item):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO items (name, category, expiry_date, note) VALUES (?, ?, ?, ?)",
              (item.name, item.category, item.expiry_date, item.note))
    conn.commit()
    item_id = c.lastrowid
    conn.close()
    return {"id": item_id, "message": "Item created"}

@app.get("/items", response_model=List[Item])
def read_items():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, category, expiry_date, note FROM items")
    rows = c.fetchall()
    conn.close()
    return [{"name": r[0], "category": r[1], "expiry_date": r[2], "note": r[3]} for r in rows]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, name, category, expiry_date, note FROM items WHERE id=?", (item_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": row[0], "name": row[1], "category": row[2], "expiry_date": row[3], "note": row[4]}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE items SET name=?, category=?, expiry_date=?, note=? WHERE id=?",
              (item.name, item.category, item.expiry_date, item.note, item_id))
    conn.commit()
    updated = c.rowcount
    conn.close()
    if updated == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated"}

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()
    deleted = c.rowcount
    conn.close()
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return

@app.get("/")
def root():
    return {"message": "Hello FreshIQ! Backend is up."}
