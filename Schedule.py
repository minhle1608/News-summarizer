import os
import datetime
import schedule
import time
import subprocess

NOTEBOOK_PATH = '/Users/lebinhminh/Desktop/Jupytercall/Agent.ipynb'
OUTPUT_DIR = '/Users/lebinhminh/Desktop/Jupytercall/Agentcall.ipynb'

def execute_notebook():
    try:
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Get current date
        now = datetime.datetime.now()
        output_notebook_name = f'executed_notebook_{now.strftime("%Y-%m-%d_%H-%M-%S")}.ipynb'
        output_path = os.path.join(OUTPUT_DIR, output_notebook_name)

        command = [
            'jupyter', 'nbconvert',
            '--execute', NOTEBOOK_PATH,
            '--to', 'notebook',
            '--output', output_path
        ]
        
        print(f"Executing command: {' '.join(command)}")
        subprocess.run(command, check=True, capture_output=True, text=True)
        
        print(f"SUCCESS: Notebook '{NOTEBOOK_PATH}' executed at {now}")
        print(f"Output saved to '{output_path}'")

    except subprocess.CalledProcessError as e:
        print(f"ERROR: Notebook execution failed.")
        print(f"Return Code: {e.returncode}")
        print(f"Output (stdout):\n{e.stdout}")
        print(f"Error (stderr):\n{e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print(f"[{datetime.datetime.now()}] --- JOB FINISHED ---")


# --- Scheduling ---
print("Script started")

schedule.every().day.at("08:00").do(execute_notebook)
schedule.every().day.at("12:00").do(execute_notebook)
schedule.every().day.at("17:00").do(execute_notebook)
schedule.every().day.at("21:00").do(execute_notebook)

while True:
    schedule.run_pending()
    time.sleep(1) 
