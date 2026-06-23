# RedRank AI - Intelligent Candidate Discovery

## Overview

RedRank AI is an intelligent candidate ranking system built for the Redrob India Runs Hackathon.

Traditional hiring systems rely heavily on keyword matching, often missing highly relevant candidates whose skills and experience are expressed differently.

RedRank AI combines semantic retrieval, behavioral signals, experience analysis, and recruiter-focused ranking to identify the best candidates for a given job description.

---

## Problem Statement

Recruiters review thousands of profiles and often miss high-quality candidates because keyword-based systems cannot understand context, relevance, or behavioral indicators.

The goal is to build an AI-powered ranking system that understands both job requirements and candidate profiles.

---

## Solution Architecture

### Stage 1: Candidate Understanding

Each candidate profile is transformed into a unified textual representation using:

* Headline
* Summary
* Skills
* Career History

### Stage 2: Semantic Embedding

Model:

sentence-transformers/all-MiniLM-L6-v2

Embeddings generated:

* 100,000 candidates
* 384-dimensional vectors

### Stage 3: Vector Retrieval

FAISS IndexFlatIP is used for high-speed semantic search.

Process:

Job Description → Embedding → FAISS Search → Top Candidates

### Stage 4: Hybrid Ranking

Features:

* Semantic Similarity
* Keyword Relevance
* Experience Match
* Behavioral Signals
* Title Relevance

Final ranking combines all signals into a unified score.

---

## Technologies Used

* Python
* Sentence Transformers
* FAISS
* Pandas
* NumPy
* Scikit-Learn

---

## Results

* 100,000 profiles processed
* Semantic retrieval implemented
* Hybrid ranking system developed
* Top 100 candidate shortlist generated

---

## Future Improvements

* Cross-encoder reranking
* Learning-to-rank models
* Graph-based candidate similarity
* Recruiter feedback loop
* LLM-powered candidate explanations
