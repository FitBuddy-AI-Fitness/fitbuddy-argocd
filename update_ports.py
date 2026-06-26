import glob
import re

port_map = {
    'auth-service': 5001,
    'user-service': 5002,
    'diet-service': 5003,
    'workout-service': 5004,
    'chatbot-service': 5005,
    'progress-service': 5006,
    'yolo-exercise-service': 8001
}

for service, port in port_map.items():
    files = glob.glob(f'charts/{service}/values-dev.yaml') + glob.glob(f'charts/{service}/values-prod.yaml')
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
        
        # Replace service.port
        content = re.sub(r'port:\s*\d+', f'port: {port}', content)
        
        with open(file, 'w', newline='\n') as f:
            f.write(content)
