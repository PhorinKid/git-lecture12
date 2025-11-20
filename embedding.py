def embed_api(text):
    vec = embed(text)
    return {'vector': vec, 'dim': len(vec)}

def embed(text):
    return f'embedded {text}'