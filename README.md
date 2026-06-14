# RAG-Based Contact Search System

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline to perform semantic search over B2B contact data.

It includes a modular data preprocessing pipeline and exposes it as a FastAPI service, enabling reusable and scalable data processing.

---

## Features

* Data preprocessing and cleaning (modular pipeline)
* Email resolution using scoring and validation logic
* Semantic document generation
* Embedding using Sentence Transformers
* Vector search using PostgreSQL + pgvector
* FastAPI-based preprocessing service for reusable data ingestion

---

## Tech Stack

* Python (pandas, numpy, sentence-transformers)
* FastAPI
* PostgreSQL
* pgvector

---

## System Architecture

```text
Raw Dataset → FastAPI Preprocessing API → Clean Data → Embeddings → PostgreSQL (pgvector) → Semantic Search
```

---

## Workflow

1. Upload raw dataset via FastAPI endpoint
2. Preprocess and clean data (null removal, column normalization, email scoring)
3. Generate structured RAG documents
4. Create embeddings using Sentence Transformers
5. Store embeddings in PostgreSQL with pgvector
6. Perform semantic search using vector similarity

---

## API Usage

### Endpoint

`POST /process/`

### Description

Accepts a CSV file and returns cleaned and processed data.

### Example Flow

1. Go to `/docs`
2. Upload dataset
3. Receive processed output (JSON)

---

## Example Query

"CTOs in fintech security India"

---

## Output

Returns most relevant contacts based on semantic similarity.

---

## Future Improvements

* Return downloadable cleaned CSV
* Integrate with web scraping pipelines (Scrapy/Playwright)
* Containerization using Docker
* Deployment as a microservice
