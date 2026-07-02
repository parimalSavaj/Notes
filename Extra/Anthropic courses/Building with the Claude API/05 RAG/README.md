## 1. Chunking (Splitting the Data)

Chunking is how you divide your documents into smaller pieces before converting them to vectors.

- **Recursive Character Chunking (The Baseline):** Splits text using a hierarchy of natural breaks (paragraphs `\n\n`, then sentences `\n`, then spaces). Used to prevent cutting sentences in half.
- **Structural Chunking (The Standard):** Uses parsers to split documents based on their actual format (Markdown headers, HTML tags, or PDF sections). Ensures a table or a specific legal clause stays together as one chunk.
- **Semantic Chunking (Advanced):** Uses an AI model to detect when the author changes the topic, making the split exactly at the point the meaning shifts.
- **Contextual Chunking (State-of-the-Art):** Before saving a chunk, an LLM writes a one-sentence summary of the whole document and attaches it to the chunk. This prevents the vector database from losing track of what the chunk is actually referring to.
- **Chunk Overlap:** A universal best practice. Always overlap chunks by 10% to 20% so that concepts spanning across a split are not lost.

---

## 2. Embedding & Metadata (Storing the Data)

Embeddings turn text into math so the computer can understand the meaning. But in production, vectors alone are not enough.

- **Metadata Injection:** Attaching structured tags to your chunks (e.g., `Author: John`, `Date: 2026`, `DocType: API_Docs`).
- **Pre-Filtering:** The industry standard for speed and security. Before running a heavy vector search, you use a standard database query to filter out irrelevant rows using the metadata (e.g., `WHERE tenant_id = '123'`). This ensures users only search data they have permission to see.

---

## 3. Searching (Retrieving the Data)

Production systems never just do a simple vector search and send the first result to the LLM. They use multi-stage pipelines.

- **Hybrid Search (Stage 1):** Combines two search methods at the exact same time:
- **Vector Search:** Finds the "vibe" or semantic meaning of the question.
- **Keyword Search (BM25):** Finds exact word matches (like specific error codes or names).
- _Result:_ These two lists are mathematically merged using an algorithm called **Reciprocal Rank Fusion (RRF)**.

- **Parent Document Retriever (Small-to-Big):** You embed tiny chunks (1-2 sentences) so the search is highly accurate. But when a match is found, you swap it out and send the massive "Parent" chunk (the whole page) to the LLM so it has full context to read.
- **Cross-Encoder Reranking (Stage 2):** The most important upgrade. After Hybrid Search grabs the top 100 messy results, a specialized AI model (the Reranker) reads the user's question and every single chunk, scores their actual relevance, and sends only the top 5 perfect chunks to the final LLM.
