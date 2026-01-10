# Agentic AI Course: Материалы лекций 🚀

Этот репозиторий содержит материалы курса по **Agentic AI**, охватывающего все этапы от работы с LLM до построения автономных систем.

## 📌 Проект и философия
Этот курс — модульная образовательная программа, созданная для вывода студентов на уровень специалистов по ИИ-автоматизации корпоративного уровня.
- **"Fishing rod, not fish"**: The goal is to teach fundamental understanding, not just how to use specific tools.
- **"From tools to solutions"**: We move from consuming ready-made AI tools to building custom autonomous systems via API.
- **"Technological Transformation"**: Transitioning from an AI user (Web UI) to an AI architect who builds automated "factories" (agentic systems).
- **Business Focus**: Created by Nikolay Sekachev (Visionary of the Year), the course focuses on ROI, business efficiency, and solving real-world tasks. It treats AI as a "combine harvester" for intellectual labor.

## 📂 Repository Structure
- `Module_01/`: AI Evolution & Foundations. Includes slides, `pdf/` and `transcripts/`.
- `Module_02/`: LLM, API, and Tokenomics. Includes `transcripts/` and practical examples.
- `Module_03/`: Sound, Voice, and Agentic Systems. 
- `slides_docs/`: Source documents and assets for presentations.
- `LICENSE`: CC BY-NC-SA 4.0 License.
- `README.md`: Main entry point with contact info and viewing instructions.
- `Программы курсов.md`: The full curriculum.

## 🤖 Instructions for Gemini & AI Agents
When assisting with this project, follow these guidelines:

> **CRITICAL**: After making changes to any files in the repository, you MUST update this `GEMINI.md` file if the changes affect the project structure, logic, or educational materials. This file must always be up-to-date to serve as a reliable source of truth for the agent.


### 1. Tone and Style
- **Educational & Strategic**: Use analogies (LLM as an engine, Agent as a car; Horse vs. Combine harvester).
- **Visionary**: Acknowledge the exponential growth of AI (doubling every ~196 days).
- **Systematic**: Follow the module structures. Relate small tasks to the bigger picture (The MVP).
- **Visual**: Use ASCII art, Mermaid diagrams, or structured lists. Use Markdown/HTML for slides.

### 2. Technical Concepts to Know
- **LLM Parameters**: `Temperature` (creativity/randomness), `Top-P/Top-K` (sampling), `Max Tokens`.
- **Architecture**: Transformers, Self-Attention mechanism, Tokenization vs. Vektorization (Embeddings).
- **Tokenomics**: Knowledge of Input/Output/Cache costs. "Token" as the unit of thought.
- **Efficiency**: Quantization (4-bit, 8-bit) for running models on consumer hardware.
- **Tool Calling**: The bridge between "Reasoning" and "Acting" via external functions.

### 3. Agentic Design Patterns
- **ReAct Pattern**: `Thought -> Action -> Observation` cycle.
- **Perceive-Reason-Act**: The core loop of any agent.
- **Methodology**: Hierarchical planning (PRD -> Roadmap -> Todo list).
- **Strategies**: CoT (Chain of Thought), Reflection (self-critique), Multi-agent orchestration.

### 4. Format & Tooling
- **No-Code**: Focus on **n8n** (workflows as JSON). LLMs can often generate these JSON structures.
- **Code**: Python (PydanticAI, LangGraph) and TypeScript (Vercel AI SDK).
- **Format**: The lecturer uses **Obsidian** with the **Advanced Slides** plugin. Slides are written in Markdown.
- **Workflow**: Before creating a new presentation or slide, examine existing ones in the modules (e.g., `Module_03/`) to align with the lecturer's style and Advanced Slides formatting (e.g., slide separators, animation fragments).
- **Ecosystem**: Google AI Studio, Hugging Face (Model Hub), OpenRouter (API Aggregator), VPS (hosting automation).


---

*This file serves as a context provider for AI agents working on the TETkool project. Keep it updated as the course evolves.*
