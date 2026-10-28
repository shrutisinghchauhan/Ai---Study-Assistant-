import re
import fitz
import numpy as np
from ollama import embed

EMBED_MODEL = 'all-minilm'


def extract_pdf_text(pdf_bytes):
    pages = []
    with fitz.open(stream=pdf_bytes, filetype='pdf') as document:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text('text')
            text = re.sub(r'\s+', ' ', text).strip()
            if text:
                pages.append((page_number, text))
    return pages


def split_text(pages, chunk_size=900, overlap=150):
    if chunk_size <= 0 or not 0 <= overlap < chunk_size:
        raise ValueError('chunk_size must be positive and overlap smaller than chunk_size')
    chunks = []
    for page_number, text in pages:
        sentences = re.split(r'(?<=[.!?])\s+', text)
        current = ''
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            # Long sentences are split with overlap as a fallback.
            if len(sentence) > chunk_size:
                if current:
                    chunks.append({'page': page_number, 'text': current})
                    current = ''
                start = 0
                while start < len(sentence):
                    end = min(start + chunk_size, len(sentence))
                    chunks.append({'page': page_number, 'text': sentence[start:end]})
                    if end == len(sentence):
                        break
                    start = end - overlap
                continue
            candidate = (current + ' ' + sentence).strip()
            if len(candidate) <= chunk_size:
                current = candidate
            else:
                if current:
                    chunks.append({'page': page_number, 'text': current})
                # Carry the tail into the next chunk for continuity.
                tail = current[-overlap:] if current else ''
                current = (tail + ' ' + sentence).strip()
                if len(current) > chunk_size:
                    current = sentence
        if current:
            chunks.append({'page': page_number, 'text': current})
    return chunks


def create_embeddings(chunks, batch_size=16):
    if not chunks:
        return np.empty((0, 0), dtype=np.float32)
    vectors = []
    texts = [chunk['text'] for chunk in chunks]
    for start in range(0, len(texts), batch_size):
        result = embed(model=EMBED_MODEL, input=texts[start:start + batch_size])
        vectors.extend(result.embeddings)
    matrix = np.asarray(vectors, dtype=np.float32)
    if matrix.shape[0] != len(chunks):
        raise RuntimeError('Embedding count does not match chunk count')
    return matrix


def retrieve_context(question, chunks, embeddings, top_k=3):
    if not chunks or embeddings is None or embeddings.size == 0:
        return []
    query = np.asarray(embed(model=EMBED_MODEL, input=question).embeddings[0], dtype=np.float32)
    scores = embeddings @ query / np.maximum(
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query), 1e-8
    )
    indices = np.argsort(scores)[::-1][:max(1, min(top_k, len(chunks))) ]
    return [
        {'page': chunks[int(i)]['page'], 'text': chunks[int(i)]['text'], 'score': float(scores[int(i)])}
        for i in indices
    ]
