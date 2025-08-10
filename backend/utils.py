from config import constants
from backend.utils_helper import upload_files_openAI, delete_files_openAI, upload_files_temp_file, create_contents_list

def load_system_settings_template():
    with open(constants.PROMPT_TEMPLATE_PATH, "r") as f:
        prompt_template = f.read()
    return prompt_template



def generate_response_with_files(openAI_client, tier_level, files_dict):
    print("Loading the System Instruction")
    system_instruction_template = load_system_settings_template()

    print("Uploading the files to OpenAI")
    file_id_list = upload_files_openAI(openAI_client, files_dict)


    user_prompt = """
    Based on the uploaded files, please provide a resilience architecture assessment.
    Use the following categories to guide your analysis:

    - **Architecture & HLD (High-Level Design)**: Includes detailed design documents and architecture diagrams that outline the overall system structure and components.

    - **DR Plan & Procedures / Runbooks**: Contains disaster recovery plans, procedures, and runbooks detailing how to handle outages or disruptions.

    - **DR Test Results & TTX (Tabletop Exercise) Minutes**: Post-incident reviews, including results from disaster recovery testing and documentation from simulation exercises.

    - **RCA Reports (P1/P2 incidents from the last 12–18 months)**: Root cause analysis reports for priority 1 and 2 incidents, showing past failures and their causes.

    - **Monitoring Dashboards & Synthetic Definitions**: Observability evidence including monitoring dashboards, synthetic transaction definitions, and alerting configurations.

    - **Backup / Restore Settings & Reports**: Details about backup configurations, restore procedures, and reports validating backup integrity and immutability.

    - **Prior Patterns & Standards**: Any previously established standards, patterns, or best practices relevant to resilience and architecture.

    Analyze across these domains and correlate issues if seen in RCA with lack of monitoring or DR.

    Please provide an output as requested in the system instruction.
    """

    print("Getting the response from OpenAI")
    # response = openAI_client.chat.completions.create(
    #         model="gpt-4-1106-preview",  # Use the latest GPT-4 model that supports tools
    #         messages=[
    #             {"role": "system", "content": system_instruction_template.format(TierLevel=tier_level)},
    #             {"role": "user", "content": user_prompt}
    #         ],
    #         tools=[],
    #         tool_choice="none",
    #         temperature=0.3,
    #         files=file_id_list
    #     )

    response = openAI_client.files.list()
    for file in response.data:
        print(f"ID: {file.id}, Filename: {file.filename}, Status: {file.status}")
    print("Deleting the files from OpenAI")
    delete_files_openAI(openAI_client=openAI_client, file_id_list=file_id_list)
    response = openAI_client.files.list()
    print("Delete done")
    for file in response.data:
        print(f"ID: {file.id}, Filename: {file.filename}, Status: {file.status}")
    print("Returning the response")
    return "ASd"






def generate_response(openAI_client, tier_level, files_dict):


    system_instruction_template = load_system_settings_template()
    system_instruction = system_instruction_template.format(TierLevel=tier_level)
    print("Uploading the files to OpenAII")
    file_id_dict = upload_files_temp_file(openAI_client, files_dict)
    print("Making the contents list")
    contents_list = create_contents_list(file_id_dict=file_id_dict)
    
    response_v = openAI_client.responses.create(
    model="gpt-4o-mini",  # or "gpt-3.5-turbo"
    tools=[{"type": "web_search_preview"}],
    instructions=system_instruction + "\nIdentify the respective files automatically.",
    input=[
        {
            "role": "user",
            "content": contents_list
        }
    ]
    )


    response = openAI_client.files.list()
    for file in response.data:
        openAI_client.files.delete(file.id)

    
    response = openAI_client.files.list()

    print("Delete done")
    print("files after deleting")
    for file in response.data:
        print(f"ID: {file.id}, Filename: {file.filename}, Status: {file.status}")

    return response_v.output_text