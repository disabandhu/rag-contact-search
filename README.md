# RAG-Based Contact Search System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline to perform semantic search over B2B contact data.

## Features
- Data preprocessing and cleaning
- Email and phone resolution
- Semantic document generation
- Embedding using Sentence Transformers
- Vector search using PostgreSQL + pgvector

## Tech Stack
- Python (pandas, sentence-transformers)
- PostgreSQL
- pgvector

## Workflow
1. Clean dataset
2. Generate RAG documents
3. Create embeddings
4. Store in PostgreSQL
5. Perform semantic search using vector similarity

## Example Query
"CTOs in fintech security India"

## Output
Returns most relevant contacts based on semantic similarity.