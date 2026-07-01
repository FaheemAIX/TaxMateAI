# Product Requirements Document (PRD)

# Project Name

TaxMate AI - FBR Income Tax Assistant

---

# Version

0.1.0

---

## 1. Project Vision
To simplify tax compliance in Pakistan by transforming complex, fragmented FBR legal documentation into an interactive, accessible, and AI-powered knowledge assistant.

## 2. Target Users
* **Primary:** Individuals (freelancers, salaried employees) seeking to become tax filers.
* **Secondary:** Small business owners, students, and tax consultants requiring simplified explanations of tax law.

## 3. Problem Statement
Pakistan’s tax regulations change frequently. Taxpayers struggle to find accurate, up-to-date information because FBR documentation is spread across hundreds of disconnected notifications, circulars, SROs, and Finance Acts. Manual searching is time-consuming, error-prone, and leads to outdated interpretations.

## 4. Core Features (Version 1)
* **Official RAG Pipeline:** Ingestion of verified FBR documents (PDFs).
* **Context-Aware Chat:** Intelligent responses grounded only in provided legal documents.
* **Source Citations:** Displaying specific section/page references for every claim.
* **Simple Language Toggle:** Translating legal jargon into plain, understandable English/Urdu.

## 5. Future feature (Version 2)
* **Tax Calculator:** User enters Income -> AI estimates tax.

## 6. System Architecture
Our backend follows a modular "Clean Architecture" pattern:
* **API Layer:** [FastAPI](https://fastapi.tiangolo.com/) for asynchronous request handling.
* **Data Ingestion:** LangChain PDF loaders with optimized chunking strategies.
* **Vector Database:** [FAISS/ChromaDB](https://www.trychroma.com/) for high-speed semantic search.
* **Orchestration:** LangChain/LangGraph for managing retrieval logic and memory.
* **LLM Integration:** OpenAI (or Groq/Gemini) for high-reasoning capabilities.
* **Containerization:** Docker for consistent environment management.

## 7. Development Milestones
* **Milestone 1 (Days 1–3):** Project setup, GitHub initialization, and functional FastAPI health/upload endpoints.
* **Milestone 2 (Days 4–8):** Complete the RAG pipeline (document loading, embedding, and vector storage).
* **Milestone 3 (Days 9–12):** Implement chat logic, source citations, and conversation history.
* **Milestone 4 (Days 13–15):** Dockerization, documentation, demo video creation, and final deployment.

## 8. Definition of Done (DoD)
A feature or milestone is considered "Done" only when:
1. **Code Quality:** The code is modular, type-hinted, and adheres to PEP 8 standards.
2. **Testing:** All API endpoints pass basic sanity checks (via Swagger/manual testing).
3. **Documentation:** The specific feature is updated in the README and docstrings are added.
4. **Version Control:** The code is committed and pushed to the relevant GitHub branch.
5. **Deployment Ready:** The feature functions within a Docker container.

## 9. Tech Stack
| Component | Technology |
| :--- | :--- |
| Backend | Python, FastAPI |
| Frontend | React | 
| Orchestration | LangChain |
| LLM | OpenAI or Groq |
| Embedding | OpenAI or Groq |
| Vector Store | FAISS/ChromaDB |
| Container | Docker |