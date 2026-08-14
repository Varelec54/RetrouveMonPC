import time, subprocess, os, sys

SCRIPT = os.path.join(os.path.dirname(__file__), "RetrouveMonPC.py")
ATTENTE = 300 # 5 minutes

if __name__ == "__main__":
    while True:
        try:
            subprocess.run([sys.executable, SCRIPT])
        except: pass
        time.sleep(ATTENTE)
