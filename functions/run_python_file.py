import os    
import subprocess

def run_python_file(working_directory, file_path):
    abs_parent_dir = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(os.path.join(abs_parent_dir, file_path))

    common_prefix = os.path.commonpath([abs_target_file , abs_parent_dir])
    if common_prefix != abs_parent_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_target_file):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        results = subprocess.run(["python3", abs_target_file], timeout=30,
                                capture_output=True, text=True, 
                                cwd = abs_parent_dir)
        stdout = results.stdout.strip()
        stderr = results.stderr.strip()
        output_lines = []

        if stdout:
            output_lines.append(f"STDOUT: {stdout}")
        if stderr:
            output_lines.append(f"STDERR: {stderr}")
        if results.returncode != 0:
            output_lines.append(f"Process exited with code {results.returncode}")
        if not output_lines:
            return "No output produced."

        return "\n".join(output_lines)
 
    except Exception as e:
        return f"Error: executing Python file: {e}"
