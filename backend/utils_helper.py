import os
import tempfile


def upload_files_openAI(openAI_client, files_dict):
    file_ids = []

    for section, files in files_dict.items():
        for f in files:
            # Rename file for clarity
            filename = f"{section}_{f.name}"
            uploaded = openAI_client.files.create(file=(filename, f), purpose="user_data")
            file_ids.append(uploaded.id)

    return file_ids


def delete_files_openAI(openAI_client, file_id_list):
    for fid in file_id_list:
        openAI_client.files.delete(id=fid)


def upload_files_temp_file(openAI_client, files_dict):
    return_dict = {}
    for section, files in files_dict.items():
        return_dict[section] = []
        with tempfile.TemporaryDirectory() as temp_dir:

            for uploaded_file in files: # Iterate through each uploaded file

                temp_file_path = os.path.join(temp_dir, f"{section}_"+uploaded_file.name)
                try:
                    # 1. Save the uploaded file to a temporary local file
                    with open(temp_file_path, "wb") as f:
                        f.write(uploaded_file.read())
                    file = openAI_client.files.create(
                        file=open(temp_file_path, "rb"),
                        purpose="user_data" # Or "assistants" for the Assistants API
                    )
                    return_dict[section].append(file.id)

                except Exception as e:
                    print(f"An error occurred during processing file '{uploaded_file.name}': {e}")

                finally:
                    if temp_file_path and os.path.exists(temp_file_path):
                        os.remove(temp_file_path)
                        print(f"Temporary file '{temp_file_path}' deleted for '{uploaded_file.name}'.")

    return return_dict



def create_contents_list(file_id_dict):

    content_list = [] # TODO add more context for individual file groups
    for category, file_ids_list in file_id_dict.items():
        if len(file_ids_list) == 0:
            continue
        current_category={"type": "input_text", "text": f"The following contains files related to {category}"}
        content_list.append(current_category)
        for file_id in file_ids_list: 
            content_list.append({"type":"input_file", "file_id":file_id})

    
    return content_list
