import json
import boto3
import uuid  # Import UUID to generate unique task IDs

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TodoList")

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))  # Debugging

    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",  # Allow all origins
        "Access-Control-Allow-Methods": "OPTIONS, POST, GET, DELETE",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    try:
        if "httpMethod" not in event:
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({"message": "Invalid request format", "received_event": event})
            }

        http_method = event["httpMethod"]

        if http_method == "OPTIONS":  # ✅ Handle CORS preflight request
            return {
                "statusCode": 200,
                "headers": headers,
                "body": json.dumps({"message": "CORS preflight successful"})
            }

        if http_method == "POST":
            body_str = event.get("body", "{}")  
            body = json.loads(body_str) if isinstance(body_str, str) else body_str  # Handle double encoding
            
            task = body.get("task")
            if not task:
                return {"statusCode": 400, "headers": headers, "body": json.dumps({"message": "Task is required"})}

            task_id = str(uuid.uuid4())
            table.put_item(Item={"taskId": task_id, "task": task})

            return {
                "statusCode": 201,
                "headers": headers,
                "body": json.dumps({"message": "Task added successfully", "taskId": task_id, "task": task})
            }

        elif http_method == "GET":
            response = table.scan()
            tasks = [{"taskId": item["taskId"], "task": item["task"]} for item in response.get("Items", [])]

            return {"statusCode": 200, "headers": headers, "body": json.dumps(tasks)}

        elif http_method == "DELETE":
            body_str = event.get("body", "{}")  
            body = json.loads(body_str) if isinstance(body_str, str) else body_str  # Handle double encoding
            
            task_id = body.get("taskId")
            if not task_id:
                return {"statusCode": 400, "headers": headers, "body": json.dumps({"message": "taskId is required for deletion"})}

            table.delete_item(Key={"taskId": task_id})

            return {"statusCode": 200, "headers": headers, "body": json.dumps({"message": "Task deleted successfully", "taskId": task_id})}

        else:
            return {"statusCode": 405, "headers": headers, "body": json.dumps({"message": "Method Not Allowed"})}

    except Exception as e:
        return {"statusCode": 500, "headers": headers, "body": json.dumps({"message": "Internal Server Error", "error": str(e)})}
