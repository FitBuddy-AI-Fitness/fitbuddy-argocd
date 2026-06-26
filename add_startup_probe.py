import glob

startup_probe_block = """          startupProbe:
            httpGet:
              path: /healthz
              port: {{ .Values.service.port }}
            failureThreshold: 30
            periodSeconds: 10
"""

files = glob.glob('charts/*/templates/deployment.yaml')
for file in files:
    with open(file, 'r') as f:
        content = f.read()
        
    if 'startupProbe:' not in content:
        content = content.replace('          livenessProbe:', startup_probe_block + '          livenessProbe:')
        with open(file, 'w', newline='\n') as f:
            f.write(content)
