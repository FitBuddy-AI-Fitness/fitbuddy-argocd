import glob
import os

services = [
    'auth-service',
    'user-service',
    'diet-service',
    'workout-service',
    'chatbot-service',
    'progress-service',
    'yolo-exercise-service'
]

for service in services:
    file = f'charts/{service}/templates/service.yaml'
    
    if not os.path.exists(file):
        continue
        
    with open(file, 'r') as f:
        content = f.read()
    
    # 1. Change the exposed port from 80 to the internal application port
    content = content.replace('port: 80', 'port: {{ .Values.service.port }}')
    
    # 2. Fix the service name to drop the `fitbuddy-` prefix so Nginx can resolve it
    content = content.replace(f'name: fitbuddy-{service}', f'name: {service}')
    
    with open(file, 'w', newline='\n') as f:
        f.write(content)
