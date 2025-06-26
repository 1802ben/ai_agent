import os


def get_files_info(working_directory, directory=None):
    abs_parent_dir = os.path.abspath(working_directory)

    # Resolve `directory` relative to the working directory
    abs_potential_subdir = os.path.abspath(
        os.path.join(abs_parent_dir, directory if directory else "")
    )

    if not os.path.isdir(abs_potential_subdir) or not os.path.isdir(abs_parent_dir):
        return f'Error: "{directory}" is not a directory'

    # Ensure the subdir is within the working directory
    common_prefix = os.path.commonpath([abs_potential_subdir, abs_parent_dir])
    if common_prefix != abs_parent_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    contents = describe_directory(abs_potential_subdir)
    return contents

def describe_directory(path):
    entries = []
    with os.scandir(path) as it:
        for entry in it:
            file_size = entry.stat().st_size
            is_dir = entry.is_dir()
            entries.append(f"- {entry.name}: file_size={file_size} bytes, is_dir={is_dir}")
    return "\n".join(entries)