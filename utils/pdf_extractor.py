import fitz  # PyMuPDF
import re

def extract_clauses_from_text(text: str, page_number: int = 1):
    clause_pattern = re.compile(
        r'(Clause\s*(\d+)\s*-\s*[^:]+:\s*(.*?))(?=\nClause\s*\d+\s*-|$)',
        re.DOTALL
    )

    clauses = []
    for match in clause_pattern.finditer(text):
        full_text = match.group(1).strip()
        clause_id = int(match.group(2))
        clauses.append({
            "id": clause_id,
            "text": full_text,
            "page": page_number
        })

    return clauses


def extract_clauses_from_pdf(pdf_path: str):
    doc = fitz.open(pdf_path)
    all_clauses = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        clauses = extract_clauses_from_text(text, page_number=page_num + 1)
        all_clauses.extend(clauses)

    return all_clauses



