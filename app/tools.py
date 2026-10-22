
from typing import Literal

import requests
from langchain.tools import tool


API_BASE_URL = "http://127.0.0.1:8000"

TaskStatus = Literal["Pending", "InProgress", "Completed"]


def call_api(
    method: str,
    endpoint: str,
    **kwargs,
):
    """Call the FastAPI backend and handle API errors consistently."""
    url = f"{API_BASE_URL}{endpoint}"

    try:
        response = requests.request(
            method=method,
            url=url,
            timeout=15,
            **kwargs,
        )

        response.raise_for_status()

        # DELETE returns HTTP 204 with no response body.
        if response.status_code == 204 or not response.content:
            return {"success": True, "message": "Operation completed successfully."}

        return response.json()

    except requests.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "unknown"
        detail = (
            exc.response.text
            if exc.response is not None
            else str(exc)
        )

        return {
            "success": False,
            "statusCode": status_code,
            "error": detail,
        }

    except requests.RequestException as exc:
        return {
            "success": False,
            "error": f"Unable to connect to the Task API: {exc}",
        }


@tool
def get_all_tasks() -> dict | list:
    """Retrieve all tasks, including their IDs, titles, descriptions,
    due dates, statuses, and creation or update timestamps.
    Use this when the user asks to list, show, or review tasks.
    """
    return call_api("GET", "/api/tasks")

@tool
def create_task(
    title: str,
    description: str | None = None,
    due_date_utc: str | None = None,
    status: TaskStatus = "Pending",
) -> dict:
    """Create a new task in the database.
    A title is required. Provide due_date_utc as an ISO 8601 date-time
    string when a due date is specified. Valid statuses are Pending,
    InProgress, and Completed.
    """
    payload = {
        "title": title,
        "description": description,
        "dueDateUtc": due_date_utc,
        "status": status,
    }

    return call_api("POST", "/api/tasks", json=payload)

@tool
def update_task(
    task_id: int,
    title: str | None = None,
    description: str | None = None,
    due_date_utc: str | None = None,
    status: TaskStatus | None = None,
) -> dict:
    """Partially update a task using PATCH.
    Supply the task ID and only the fields the user wants to change.
    Valid statuses are Pending, InProgress, and Completed.
    Do not use this tool to replace the entire task.
    """
    payload = {}

    if title is not None:
        payload["title"] = title

    if description is not None:
        payload["description"] = description

    if due_date_utc is not None:
        payload["dueDateUtc"] = due_date_utc

    if status is not None:
        payload["status"] = status

    if not payload:
        return {
            "success": False,
            "error": "Provide at least one field to update.",
        }

    return call_api("PATCH", f"/api/tasks/{task_id}", json=payload)


@tool
def delete_task(task_id: int) -> dict:
    """Permanently delete a task using its numeric task ID.
    Only use this when the user explicitly requests deletion.
    Confirm the intended task ID before deleting if it is ambiguous.
    """
    result = call_api("DELETE", f"/api/tasks/{task_id}")

    if isinstance(result, dict) and result.get("success") is True:
        return {
            "success": True,
            "message": f"Task {task_id} was deleted successfully.",
        }

    return result
