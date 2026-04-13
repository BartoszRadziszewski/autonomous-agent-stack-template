import logging
import json
from datetime import datetime

class AntiGravityLogger:
    def __init__(self, project_name):
        self.log_file = f"stack/logs/{project_name}_audit.jsonl"
        logging.basicConfig(level=logging.INFO, format='%(message)s')

    def log_event(self, agent_role, action, status, metadata=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_role,
            "action": action,
            "status": status,
            "metadata": metadata or {}
        }
        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
        logging.info(f"🛡️ [{agent_role}] {action} -> {status}")