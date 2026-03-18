# Agentic AI Course: Материалы лекций 🚀

Этот репозиторий содержит материалы курса по **Agentic AI**, охватывающего все этапы от работы с LLM до построения автономных систем.

## 📌 Проект и философия
Этот курс — модульная образовательная программа, созданная для вывода студентов на уровень специалистов, способных самостоятельно внедрять ИИ-решения корпоративного уровня.
- **"Fishing rod, not fish"**: Models change rapidly, but principles remain. Focus on fundamental understanding of LLM logic.
- **"Technological Transformation"**: Transitioning from a regular chatbot user to a specialist capable of designing and implementing **AI-first solutions**.
- **Business Focus**: Created by Nikolay Sekachev. Focus on ROI, business efficiency, and solving real-world corporate tasks.

## 📂 Repository Structure
- `Module_01/`: AI Evolution & Foundations. Includes neural network basics, information revolutions, and slides.
- `Module_02/`: LLM deeply. Architecture, API (OpenRouter), JSON/Markdown, Quantization, and Prompt Engineering.
- `Module_03/`: AI Agents. Anatomy, Design Patterns (ReAct, CoT), n8n (no-code), and Professional Coding. Now includes v2 based on the "Agentic Design Patterns" book.
- `Module_04/`: Cohort-specific materials. `group_01/` contains the earlier "Real World Architecture" module (frontend/backend, data storage, MVP construction, deployment basics, homework). `group_02/` now contains "Автономные мультиагентные системы" focused on multi-agent architecture, OpenClaw internals, skills, and VPS practice. The root `Модуль 4.md` acts as a cohort index.
- `Module_05/`: Deployment & DevOps. Structured learning path: Ubuntu Terminal basics → Networking fundamentals (IP, DNS, Nginx reverse proxy, SSL) → Frontend deployment via Cockpit → Complete FastAPI tutorial.
- `Module_06/`: Visual AI & Content Generation. Covers Vision LLMs (OCR, Transformer vision), Image Generation theory (CLIP, VAE, Diffusion), and practical tools (Midjourney, Nano Banana, FLUX, LoRA).
- `slides_docs/`: Source documents and assets for presentations.
- `LICENSE`: CC BY-NC-SA 4.0 License.
- `README.md`: SEO-optimized main entry point with course philosophy and viewing instructions.
- `Программы курсов.md`: Full curriculum (Note: actual file contents may evolve faster than the program).

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
- **Interoperability (MCP)**: Use of Model Context Protocol for standardized access to data and tools.

### 3. Agentic Design Patterns
- **ReAct Pattern**: `Thought -> Action -> Observation` cycle.
- **Perceive-Reason-Act**: The core loop of any agent.
- **Methodology**: Hierarchical planning (PRD -> Roadmap -> Todo list).
- **Strategies**: CoT (Chain of Thought), Reflection (self-critique), Multi-agent orchestration.
- **Collaboration (a2a)**: Agent-to-Agent communication and delegation patterns.
- **Reliability**: Exception Handling, Human-in-the-Loop (HITL), and RAG (Knowledge Retrieval).

### 4. Format & Tooling
- **No-Code**: Focus on **n8n** (workflows as JSON). LLMs can often generate these JSON structures.
- **Code**: Python (PydanticAI, LangGraph) and TypeScript (Vercel AI SDK).
- **Format**: The lecturer uses **Obsidian** with the **Advanced Slides** plugin. Slides are written in Markdown.
- **Workflow**: Before creating a new presentation or slide, examine existing ones in the modules (e.g., `Module_03/`) to align with the lecturer's style and Advanced Slides formatting (e.g., slide separators, animation fragments).
- **Ecosystem**: Google AI Studio, Hugging Face (Model Hub), OpenRouter (API Aggregator), VPS (hosting automation).


---

*This file serves as a context provider for AI agents working on the TETkool project. Keep it updated as the course evolves.*
