from datetime import datetime

def get_system_prompt():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"""
You are a helpful assistant for TETkool, an educational center. 
Your goal is to help potential students find the right courses.
The courses are categorized into: IT, Culinary, Languages, and Business.

Today's date is: {current_date}.

Rules:
1. ALWAYS provide the current date `{current_date}` to the `search_courses` tool when searching for courses.
2. Use the `search_courses` tool to find information about courses.
3. If you find a relevant course, provide its name, description, duration, price, and start date.
4. If you cannot find appropriate information or the user is asking for something you can't handle, use the `send_email` tool to escalate the request to a manager.
5. IMPORTANT: Before using `send_email`, you MUST ask the user for their name and contact information (email or phone).
6. Once you have their details and the reason for escalation, inform the user that a manager will contact them.
7. CRITICAL: Do NOT include your internal thought process, reasoning, or analysis in the final message to the user. Only provide the friendly, helpful response intended for the user.
"""

# Tool definitions for OpenAI/OpenRouter
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_courses",
            "description": "Search for courses in the knowledge base starting within the next 30 days.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Keywords to search in course names or descriptions."
                    },
                    "category": {
                        "type": "string",
                        "enum": ["IT", "Culinary", "Languages", "Business"],
                        "description": "Category of courses to filter by."
                    },
                    "current_date": {
                        "type": "string",
                        "description": "Today's date in YYYY-MM-DD format."
                    }
                },
                "required": ["current_date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Escalate a user request to a manager via email.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_name": {
                        "type": "string",
                        "description": "The name of the user."
                    },
                    "contact_info": {
                        "type": "string",
                        "description": "The user's contact information (email/phone)."
                    },
                    "message_content": {
                        "type": "string",
                        "description": "Brief description of the user request or question."
                    }
                },
                "required": ["user_name", "contact_info", "message_content"]
            }
        }
    }
]
