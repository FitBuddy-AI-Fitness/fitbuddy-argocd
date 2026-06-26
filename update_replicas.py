import glob
import re

files = glob.glob('charts/*/values-dev.yaml') + glob.glob('charts/*/values-prod.yaml')

for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace replicaCount
    content = re.sub(r'replicaCount:\s*\d+', 'replicaCount: 1', content)
    # Replace minReplicas
    content = re.sub(r'minReplicas:\s*\d+', 'minReplicas: 1', content)
    # Replace maxReplicas
    content = re.sub(r'maxReplicas:\s*\d+', 'maxReplicas: 3', content)
    
    with open(file, 'w', newline='\n') as f:
        f.write(content)
