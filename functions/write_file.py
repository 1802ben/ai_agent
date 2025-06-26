import os

def write_file(working_directory, file_path, content):
    abs_parent_dir = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(os.path.join(abs_parent_dir, file_path))

    common_prefix = os.path.commonpath([abs_target_file , abs_parent_dir])
    if common_prefix != abs_parent_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_target_file):
        os.makedirs(os.path.dirname(abs_target_file), exist_ok=True)
        with open(abs_target_file, "w", encoding="utf-8") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    with open(abs_target_file, "w", encoding="utf-8") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    

