from typing import List

import boto3
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent

load_dotenv()


class MWAA_task_id_info(BaseModel):
    dag: str
    task: str
    run_id: str
    attempt: int = 1
    aws_region: str = "eu-central-1"


def get_cloudwatch_log_from_mwaa_task_id(
    task_id_info: MWAA_task_id_info,
) -> List[str]:
    print(f"Récupération des logs pour la task MWAA: {task_id_info}")
    """
    Récupère les logs CloudWatch pour une task MWAA spécifique.

    Args:
        task_id_info (MWAA_task_id_info): infos de la task
    Returns:
        List[str]: liste des lignes de logs
    """
    session = boto3.Session(profile_name="production")
    logs_client = session.client("logs", region_name=task_id_info.aws_region)

    log_group = "airflow-AirflowData-Task"

    # Construire le prefix pour filtrer les log streams
    prefix = f"dag_id={task_id_info.dag}/run_id={task_id_info.run_id}/task_id={task_id_info.task}/attempt={task_id_info.attempt}.log"

    # Chercher le log stream correspondant
    streams_resp = logs_client.describe_log_streams(
        logGroupName=log_group,
        logStreamNamePrefix=prefix,
        limit=1,
    )

    if not streams_resp["logStreams"]:
        print(f"Aucun log stream trouvé pour {prefix}")
        return []

    log_stream_name = streams_resp["logStreams"][0]["logStreamName"]

    # Récupérer les événements
    events = logs_client.get_log_events(
        logGroupName=log_group, logStreamName=log_stream_name, startFromHead=True
    )

    # Retourner les messages comme liste
    logs = [event["message"] for event in events["events"]]
    return logs


class AgentResponse(BaseModel):
    python_exception: str | None = None
    logs: List[str] | None = None
    explication: str | None = None


system_prompt = """
Tu es un expert en Airflow et AWS MWAA.
Ton role est de détecter et d'expliquer brièvement les erreurs d'un task run MWAA depuis ces logs sur Cloudwatch.
Tu vas récupérer les warning des logs cloudwatch et analyser les erreurs.
Ne rappel pas le nom de la task, dag ou run_id.
"""

# --- Agent utilisant un modèle GitHub ---
agent = Agent(
    model="openai:gpt-3.5-turbo",  # ou "github:gpt-4.1-mini" selon dispo
    tools=[get_cloudwatch_log_from_mwaa_task_id],
    output_type=AgentResponse,
    system_prompt=system_prompt,
)

# --- Exemple d'utilisation de l'agent ---
task_info = MWAA_task_id_info(
    dag="dbt_daily_run_dag",
    task="widely.widely_sensors.external_sensors_task_group.sensor_for_meta_dag",
    run_id="scheduled__2025-12-07T04_00_00+00_00",
    attempt=1,
)

result = agent.run_sync(
    f"{task_info}",
)


agent_result = result.output

print("=== Résultat de l'agent ===")
print(agent_result.explication)
if agent_result.python_exception:
    print("=== Exception Python détectée ===")
    print(agent_result.python_exception)
if agent_result.logs:
    print("=== Logs pertinents ===")
    for log_line in agent_result.logs:
        print(log_line)
