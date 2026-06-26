import glob
import re

files = glob.glob('charts/*/templates/deployment.yaml')
for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace /healthz with /health
    content = content.replace('path: /healthz', 'path: /health')
    # Replace /ready with /health
    content = content.replace('path: /ready', 'path: /health')
    
    with open(file, 'w', newline='\n') as f:
        f.write(content)
