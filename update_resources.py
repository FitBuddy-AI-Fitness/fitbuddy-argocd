import glob
import re

files = glob.glob('charts/*/values-dev.yaml') + glob.glob('charts/*/values-prod.yaml')

new_resources = """resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "250m"
    memory: "256Mi\""""

# Regex matches the entire resources block up to the limits memory
pattern = re.compile(r'resources:\s*requests:\s*cpu:\s*"[^"]+"\s*memory:\s*"[^"]+"\s*limits:\s*cpu:\s*"[^"]+"\s*memory:\s*"[^"]+"')

for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace resources
    content = pattern.sub(new_resources, content)
    
    with open(file, 'w', newline='\n') as f:
        f.write(content)
