import ollama

MODEL = "gemma3:4b"


# PROMPT = """Look at this photo from someone's outdoor walk. Write ONE short,
# dreamy or witty caption (max 12 words). Only mention what you can
# actually see. Do not name species or make guesses about what
# plants or animals are."""

# PROMPT = """Describe this photo in one short sentence. Write a short, poetic caption for this photo."""

PROMPT = """- Look at this photo from someone's outdoor walk.
            - Generate short, impactful caption that combine aesthetic imagery, poetic depth, and a touch of witty subtext. 
            - Do not explain the captions; provide only the text.
            - Max 12 words
            - Do not name species or make guesses about what plants or animals are
"""

def clean(text):
    """Keep the first line, strip quotes, cap the length."""
    text = text.strip().split("\n")[0]
    text = text.strip(" \"'“”")
    words = text.split()
    if len(words) > 20:  # small models sometimes ignore the word limit
        text = " ".join(words[:20])
    
    return text


def make_caption(image_path):
    """Return a caption string, or None if the model fails."""
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[{
                "role": "user",
                "content": PROMPT,
                "images": [image_path]
            }]
        )
        print
        return clean(response["message"]["content"]) or None

    except Exception as e:
        print("Caption failed", e)
        return None

if __name__ == "__main__":
    print(make_caption("test.jpg"))
    # r = ollama.chat(
    #     model=MODEL,
    #     messages=[{"role": "user", "content": PROMPT, "images": ["test.jpg"]}],
    # )
    # print(repr(r["message"]["content"]))