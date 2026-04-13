def summarize_text(text: str) -> str:
    text = text.strip()

    if not text:
        return "No text provided."

    if len(text) <= 150:
        return f"Summary: {text}"

    return f"Summary: {text[:150]}..."