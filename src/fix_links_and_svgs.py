import os
import re

src_dir = "/Users/hojin/dev/jinysite/l01.linux/src"

def get_svg_template(theme, title):
    # Terminal Theme
    if theme == "terminal":
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
  <rect width="100%" height="100%" fill="#f8f9fa" rx="15"/>
  <rect x="50" y="50" width="700" height="300" fill="#282a36" rx="10"/>
  <rect x="50" y="50" width="700" height="40" fill="#44475a" rx="10"/>
  <circle cx="75" cy="70" r="6" fill="#ff5555"/>
  <circle cx="95" cy="70" r="6" fill="#f1fa8c"/>
  <circle cx="115" cy="70" r="6" fill="#50fa7b"/>
  <text x="400" y="76" font-family="monospace" font-size="16" fill="#f8f8f2" text-anchor="middle">{title}</text>
  <text x="70" y="130" font-family="monospace" font-size="18" fill="#50fa7b">root@linux:~# </text>
  <text x="215" y="130" font-family="monospace" font-size="18" fill="#f8f8f2">systemctl start service</text>
  <text x="70" y="160" font-family="monospace" font-size="16" fill="#6272a4">[ OK ] Started Linux Target Service.</text>
  <text x="70" y="200" font-family="monospace" font-size="18" fill="#50fa7b">root@linux:~# </text>
  <rect x="215" y="185" width="12" height="20" fill="#f8f8f2"><animate attributeName="opacity" values="0;1;0" dur="1s" repeatCount="indefinite"/></rect>
</svg>'''

    # Network / Cloud Theme
    elif theme == "network":
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
  <rect width="100%" height="100%" fill="#f8f9fa" rx="15"/>
  <rect x="50" y="50" width="700" height="300" fill="#ffffff" rx="10" stroke="#ced4da" stroke-width="2"/>
  <text x="400" y="90" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#343a40" text-anchor="middle">{title}</text>
  <path d="M 230 200 L 580 200" stroke="#adb5bd" stroke-width="3" stroke-dasharray="8,4"/>
  <path d="M 400 130 L 400 280" stroke="#adb5bd" stroke-width="3" stroke-dasharray="8,4"/>
  <circle cx="400" cy="200" r="45" fill="#e2edff" stroke="#4d8aff" stroke-width="4"/>
  <text x="400" y="205" font-family="sans-serif" font-size="14" font-weight="bold" fill="#4d8aff" text-anchor="middle">ROUTER</text>
  <rect x="150" y="165" width="80" height="70" rx="8" fill="#ffe3e3" stroke="#ff6b6b" stroke-width="2"/>
  <text x="190" y="205" font-family="sans-serif" font-size="14" fill="#ff6b6b" text-anchor="middle">Client</text>
  <rect x="580" y="165" width="80" height="70" rx="8" fill="#d3f9d8" stroke="#37b24d" stroke-width="2"/>
  <text x="620" y="205" font-family="sans-serif" font-size="14" fill="#37b24d" text-anchor="middle">Server</text>
  <rect x="360" y="80" width="80" height="50" rx="8" fill="#f3f0ff" stroke="#845ef7" stroke-width="2"/>
  <text x="400" y="110" font-family="sans-serif" font-size="13" fill="#845ef7" text-anchor="middle">Internet</text>
</svg>'''

    # Database & Storage Theme
    elif theme == "database":
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
  <rect width="100%" height="100%" fill="#f8f9fa" rx="15"/>
  <rect x="50" y="50" width="700" height="300" fill="#ffffff" rx="10" stroke="#ced4da" stroke-width="2"/>
  <text x="400" y="90" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#343a40" text-anchor="middle">{title}</text>
  <!-- Cylinder -->
  <path d="M 500 150 C 500 130, 600 130, 600 150 L 600 250 C 600 270, 500 270, 500 250 Z" fill="#e2edff" stroke="#4d8aff" stroke-width="3"/>
  <ellipse cx="550" cy="150" rx="50" ry="20" fill="#fff" stroke="#4d8aff" stroke-width="3"/>
  <ellipse cx="550" cy="200" rx="50" ry="20" fill="none" stroke="#4d8aff" stroke-width="3"/>
  <text x="550" y="155" fill="#4d8aff" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">STORAGE</text>
  <!-- App Block -->
  <rect x="200" y="160" width="120" height="80" rx="10" fill="#ffe3e3" stroke="#ff6b6b" stroke-width="3"/>
  <text x="260" y="205" fill="#ff6b6b" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Engine</text>
  <!-- Data flow arrows -->
  <path d="M 330 190 L 480 190" stroke="#495057" stroke-width="4" fill="none"/>
  <polygon points="480,190 470,183 470,197" fill="#495057"/>
  <path d="M 480 210 L 330 210" stroke="#495057" stroke-width="4" fill="none"/>
  <polygon points="330,210 340,203 340,217" fill="#495057"/>
</svg>'''

    # Security Theme
    elif theme == "security":
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
  <rect width="100%" height="100%" fill="#f8f9fa" rx="15"/>
  <rect x="50" y="50" width="700" height="300" fill="#ffffff" rx="10" stroke="#ced4da" stroke-width="2"/>
  <text x="400" y="90" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#343a40" text-anchor="middle">{title}</text>
  <path d="M 400 120 L 480 150 L 480 230 C 480 280 400 320 400 320 C 400 320 320 280 320 230 L 320 150 Z" fill="#fff4e6" stroke="#fd7e14" stroke-width="5"/>
  <circle cx="400" cy="210" r="25" fill="#fd7e14"/>
  <path d="M 390 205 L 400 220 L 420 190" stroke="#fff" stroke-width="4" fill="none"/>
  <rect x="150" y="180" width="100" height="60" rx="8" fill="#e9ecef" stroke="#adb5bd" stroke-width="2"/>
  <text x="200" y="215" font-family="sans-serif" font-size="14" fill="#495057" text-anchor="middle">Traffic</text>
  <path d="M 260 210 L 305 210" stroke="#adb5bd" stroke-width="4" stroke-dasharray="5,5"/>
  <polygon points="305,210 295,200 295,220" fill="#adb5bd"/>
  <rect x="550" y="180" width="100" height="60" rx="8" fill="#d3f9d8" stroke="#37b24d" stroke-width="2"/>
  <text x="600" y="215" font-family="sans-serif" font-size="14" fill="#37b24d" text-anchor="middle">Trusted</text>
</svg>'''

    # Default Theme
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
  <rect width="100%" height="100%" fill="#f8f9fa" rx="15"/>
  <rect x="50" y="50" width="700" height="300" fill="#ffffff" rx="10" stroke="#ced4da" stroke-width="2"/>
  <text x="400" y="90" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#343a40" text-anchor="middle">{title}</text>
  <rect x="180" y="150" width="140" height="100" rx="15" fill="#e2edff" stroke="#4d8aff" stroke-width="2"/>
  <text x="250" y="205" font-family="sans-serif" font-size="16" font-weight="bold" fill="#4d8aff" text-anchor="middle">Input Task</text>
  <path d="M 330 200 L 470 200" stroke="#ced4da" stroke-width="4" fill="none" stroke-dasharray="8,4"/>
  <polygon points="470,200 455,190 455,210" fill="#ced4da"/>
  <rect x="480" y="150" width="140" height="100" rx="15" fill="#d3f9d8" stroke="#37b24d" stroke-width="2"/>
  <text x="550" y="205" font-family="sans-serif" font-size="16" font-weight="bold" fill="#37b24d" text-anchor="middle">Execution</text>
</svg>'''

def get_theme_category(text):
    text = text.lower()
    if any(k in text for k in ["명령어", "쉘", "shell", "command", "cli", "terminal"]):
        return "terminal"
    if any(k in text for k in ["네트워크", "network", "라우터", "클라우드", "route"]):
        return "network"
    if any(k in text for k in ["데이터베이스", "db", "sql", "storage", "스토리지", "디스크"]):
        return "database"
    if any(k in text for k in ["보안", "방화벽", "백업", "security", "firewall"]):
        return "security"
    return "default"

pages = []
for root, dirs, files in os.walk(src_dir):
    if "index.md" in files:
        pages.append(os.path.join(root, "index.md"))

# 링크 정규식: [TEXT](TARGET)
link_pattern = re.compile(r'\[([^\]]+)\]\(([a-zA-Z0-9_\-]+)\)')

for path in pages:
    curr_dir = os.path.dirname(path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 엑스박스 링크(하드코딩 인라인 링크) 수정
    def link_replacer(match):
        text = match.group(1)
        target = match.group(2)
        
        if target.startswith("http") or target.startswith("/") or target.startswith("."):
            return match.group(0) # 정상 링크 건너뜀
            
        # target 단어(예: unix)가 들어간 제일 가까운 진짜 폴더 찾기
        subdirs = [d for d in os.listdir(curr_dir) if os.path.isdir(os.path.join(curr_dir, d)) and d != 'img']
        matched_folder = None
        for d in subdirs:
            if target in d: # e.g. "unix" in "01_1_13_unix"
                matched_folder = d
                break
                
        if matched_folder:
            return f"[{text}](./{matched_folder}/index.md)"
        else:
            # 못 찾으면 원본유지 (혹은 제거). 일단 원본유지.
            return match.group(0)
            
    content = link_pattern.sub(link_replacer, content)

    # 2. 문맥 기반 스마트 SVG 다시 그리기
    # title 구하기
    title_match = re.search(r"title:\s*['\"]?(.*?)['\"]?\s*\n", content)
    title = title_match.group(1).strip() if title_match else os.path.basename(curr_dir).capitalize()
    
    # SVG 그려서 덮어쓰기
    theme = get_theme_category(content)
    svg_code = get_svg_template(theme, title.upper())
    
    img_dir = os.path.join(curr_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    svg_path = os.path.join(img_dir, "concept_architecture.svg")
    
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_code)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Smart SVGs regenerated and inline links completely healed!")
