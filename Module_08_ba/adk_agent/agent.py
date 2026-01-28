import sqlite3
from google.adk.agents.llm_agent import Agent

DB_PATH = '/Users/sekachev/test-sql/students.db'

def run_sql(query: str, params: list = None) -> list | dict:
    """
    Executes a SQL query against the database and returns the results.
    For SELECT queries, returns a list of dictionaries (rows).
    For INSERT, UPDATE, DELETE, returns a dictionary with 'affected_rows' and 'last_row_id'.
    If an error occurs, returns a dictionary with an 'error' message.
    """
    if params is None:
        params = []
    
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            if query.strip().upper().startswith('SELECT'):
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
            else:
                conn.commit()
                return {"affected_rows": cursor.rowcount, "last_row_id": cursor.lastrowid}
    except Exception as e:
        return {"error": str(e)}

def get_schema() -> str:
    """Returns the database schema (list of tables and their CREATE statements)."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
            schemas = cursor.fetchall()
            return "\n\n".join([s[0] for s in schemas if s[0]])
    except Exception as e:
        return f"Error fetching schema: {str(e)}"

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='sql_agent',
    description='An agent that can manage a student database using SQL.',
    instruction=(
        "You are a database administrator for a student management system. "
        "You can perform CRUD operations on the 'students.db' database using SQL.\n\n"
        "CRITICAL RULES:\n"
        "1. Start by calling 'get_schema' if you are unsure about the database structure.\n"
        "2. Use 'run_sql' to execute SQL queries (SQLite syntax).\n"
        "3. AFTER EVERY TOOL CALL, you MUST provide a human-readable summary of the results to the user. "
        "Do not just stop after the tool returns. Explain what you found or confirmed.\n"
        "4. If the user asks for data (SELECT), format it nicely as a list or table.\n"
        "5. If you performed a change (INSERT/UPDATE/DELETE), confirm how many rows were affected."
    ),
    tools=[run_sql, get_schema],
)
