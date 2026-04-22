import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Any

def search_courses(query: str = None, category: str = None, current_date: str = None) -> str:
    """
    Search for courses in the knowledge base by category or query.
    Filters courses starting within the next 30 days from current_date.
    current_date format: YYYY-MM-DD
    """
    kb_path = os.getenv("KNOWLEDGE_BASE_PATH", "knowledge_base.json")
    
    try:
        with open(kb_path, 'r', encoding='utf-8') as f:
            kb = json.load(f)
    except FileNotFoundError:
        return "Knowledge base not found."
    except json.JSONDecodeError:
        return "Error reading knowledge base."

    if not current_date:
        current_date_dt = datetime.now()
    else:
        try:
            current_date_dt = datetime.strptime(current_date, "%Y-%m-%d")
        except ValueError:
            current_date_dt = datetime.now()

    end_date_dt = current_date_dt + timedelta(days=30)

    results = []

    if category and category in kb:
        candidates = kb[category]
    else:
        candidates = []
        for cat_courses in kb.values():
            candidates.extend(cat_courses)

    query = query.lower() if query else None

    for course in candidates:
        # Check date constraint
        try:
            course_start_dt = datetime.strptime(course['start_date'], "%Y-%m-%d")
            # Only include if start_date is between current_date and next 30 days
            if not (current_date_dt <= course_start_dt <= end_date_dt):
                continue
        except (KeyError, ValueError):
            continue

        # Check search terms if query exists
        if query:
            if query in course['name'].lower() or query in course['description'].lower():
                results.append(course)
        elif category: # If no query but category matched
            results.append(course)
        else: # If no query and no category, but we are in candidates from all categories
            results.append(course)

    if not results:
        return f"No courses found starting between {current_date_dt.strftime('%Y-%m-%d')} and {end_date_dt.strftime('%Y-%m-%d')}."

    response = f"Found the following courses starting within the next 30 days ({current_date_dt.strftime('%Y-%m-%d')} to {end_date_dt.strftime('%Y-%m-%d')}):\n"
    for course in results:
        response += f"- {course['name']} (Starts: {course['start_date']}, Duration: {course['duration']}, Price: {course['price']}): {course['description']}\n"
    
    return response

if __name__ == "__main__":
    # Test with current date as 2026-01-15
    print(search_courses(current_date="2026-01-15"))
    print("-" * 20)
    print(search_courses(category="IT", current_date="2026-01-15"))
