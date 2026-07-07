import base64
import urllib.parse
import re

svg_one_hot = '''<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#202122"/>
  <rect x="50" y="50" width="300" height="200" fill="none" stroke="#79a1ff" stroke-width="4"/>
  <text x="60" y="90" fill="#fff" font-family="sans-serif" font-size="20">Dog  | 1 | 0 | 0 |</text>
  <text x="60" y="140" fill="#fff" font-family="sans-serif" font-size="20">Cat  | 0 | 1 | 0 |</text>
  <text x="60" y="190" fill="#fff" font-family="sans-serif" font-size="20">Bird | 0 | 0 | 1 |</text>
</svg>'''

svg_embeddings = '''<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#202122"/>
  <line x1="50" y1="250" x2="350" y2="250" stroke="#79a1ff" stroke-width="2"/>
  <line x1="50" y1="250" x2="50" y2="50" stroke="#79a1ff" stroke-width="2"/>
  <text x="100" y="120" fill="#447ff5" font-family="sans-serif" font-size="20">King</text>
  <text x="100" y="200" fill="#447ff5" font-family="sans-serif" font-size="20">Man</text>
  <text x="250" y="120" fill="#f5447f" font-family="sans-serif" font-size="20">Queen</text>
  <text x="250" y="200" fill="#f5447f" font-family="sans-serif" font-size="20">Woman</text>
  <path d="M110,130 L110,180" stroke="#fff" stroke-dasharray="4" stroke-width="2"/>
  <path d="M260,130 L260,180" stroke="#fff" stroke-dasharray="4" stroke-width="2"/>
  <path d="M120,115 L240,115" stroke="#fff" stroke-dasharray="4" stroke-width="2"/>
</svg>'''

svg_bow = '''<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#202122"/>
  <text x="130" y="100" fill="#79a1ff" font-family="sans-serif" font-size="24" font-weight="bold">"The quick brown fox"</text>
  <rect x="50" y="130" width="90" height="50" fill="#1b1e22" stroke="#447ff5"/>
  <text x="65" y="160" fill="#fff" font-family="sans-serif">The: 1</text>
  <rect x="150" y="130" width="90" height="50" fill="#1b1e22" stroke="#447ff5"/>
  <text x="160" y="160" fill="#fff" font-family="sans-serif">Quick: 1</text>
  <rect x="250" y="130" width="100" height="50" fill="#1b1e22" stroke="#447ff5"/>
  <text x="255" y="160" fill="#fff" font-family="sans-serif">Brown: 1</text>
</svg>'''

svg_attention = '''<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#202122"/>
  <text x="150" y="150" fill="#fff" font-family="sans-serif" font-size="24">Bank</text>
  <text x="50" y="70" fill="#79a1ff" font-family="sans-serif" font-size="18">River</text>
  <text x="250" y="70" fill="#f5447f" font-family="sans-serif" font-size="18">Money</text>
  <path d="M80,80 Q120,110 150,130" stroke="#79a1ff" stroke-width="6" fill="none"/>
  <path d="M260,80 Q210,110 180,130" stroke="#f5447f" stroke-width="2" fill="none"/>
</svg>'''

b64_one_hot = "data:image/svg+xml;base64," + base64.b64encode(svg_one_hot.encode()).decode()
b64_embeddings = "data:image/svg+xml;base64," + base64.b64encode(svg_embeddings.encode()).decode()
b64_bow = "data:image/svg+xml;base64," + base64.b64encode(svg_bow.encode()).decode()
b64_attention = "data:image/svg+xml;base64," + base64.b64encode(svg_attention.encode()).decode()

with open('html.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Wikimedia URLs with SVGs
text = text.replace("https://upload.wikimedia.org/wikipedia/commons/4/46/One-hot_Encoder_%2851342016761%29.jpg", b64_one_hot)
text = text.replace("https://upload.wikimedia.org/wikipedia/commons/3/3b/Word_vector_illustration.jpg", b64_embeddings)
text = text.replace("https://upload.wikimedia.org/wikipedia/commons/f/ff/TFIDF_score_example.png", b64_bow)
text = text.replace("https://upload.wikimedia.org/wikipedia/commons/d/d4/Encoder_self-attention%2C_block_diagram.png", b64_attention)

with open('html.html', 'w', encoding='utf-8') as f:
    f.write(text)
