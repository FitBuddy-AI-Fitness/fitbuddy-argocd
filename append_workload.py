import glob
import os

workload_identity_block = '''
workloadIdentity:
  enabled: true
  clientId: "YOUR-AZURE-MANAGED-IDENTITY-CLIENT-ID"
'''

files = glob.glob('charts/*/values-dev.yaml') + glob.glob('charts/*/values-prod.yaml')
for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    if 'workloadIdentity:' not in content:
        with open(file, 'a') as f:
            if not content.endswith('\n'):
                f.write('\n')
            f.write(workload_identity_block)
