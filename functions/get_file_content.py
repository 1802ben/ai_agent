import os


def get_file_content(working_directory, file_path):
    abs_parent_dir = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(os.path.join(abs_parent_dir, file_path))

    common_prefix = os.path.commonpath([abs_target_file , abs_parent_dir])
    if common_prefix != abs_parent_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000

    with open(abs_target_file, "r") as f:
        file_content_string = f.read(MAX_CHARS)

    if len(file_content_string) == MAX_CHARS:
        file_content_string += f"[...File \"{file_path}\" truncated at 10000 characters]"
    
    return file_content_string