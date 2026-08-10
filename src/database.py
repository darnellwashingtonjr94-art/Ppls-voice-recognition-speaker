import sqlite3
import numpy as np
import json

class VoiceprintDatabase:
    def __init__(self, db_path="data/voiceprints.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._initialize_schema()

    def _initialize_schema(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS speakers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                category TEXT NOT NULL, -- 'star', 'athlete', 'public'
                embedding JSON NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_speaker(self, name, category, embedding):
        """Stores the 192-d numpy vector as a JSON string."""
        emb_json = json.dumps(embedding.tolist())
        try:
            self.cursor.execute(
                "INSERT INTO speakers (name, category, embedding) VALUES (?, ?, ?)",
                (name, category, emb_json)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Speaker {name} already exists. Update logic required.")

    def get_all_embeddings(self):
        self.cursor.execute("SELECT name, category, embedding FROM speakers")
        rows = self.cursor.fetchall()
        
        vectors = []
        metadata = []
        for row in rows:
            metadata.append({"name": row[0], "category": row[1]})
            vectors.append(np.array(json.loads(row[2])))
            
        return metadata, np.array(vectors)
