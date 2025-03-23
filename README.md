# AWS Serverless Todo App

This project is a **serverless TODO application** built using AWS services. It allows users to create, retrieve, and delete tasks via a REST API.

## 🚀 Tech Stack
The project utilizes the following AWS services:

- **AWS Amplify** – Frontend hosting & deployment
- **API Gateway** – Exposes RESTful APIs
- **AWS Lambda** – Handles business logic
- **DynamoDB** – Stores tasks
- **IAM** – Provides necessary permissions

---

## 📌 Architecture
The application follows a **serverless architecture**:

1. **Frontend (Amplify)** hosts the UI and interacts with the backend via API Gateway.
2. **API Gateway** routes HTTP requests to Lambda functions.
3. **Lambda** processes requests and interacts with DynamoDB.
4. **DynamoDB** stores and retrieves task data.
5. **IAM Roles** ensure secure access control between AWS services.

---

## 📌 API Endpoints

| Method  | Endpoint         | Description            |
|---------|----------------|------------------------|
| `POST`  | `/tasks`       | Create a new task      |
| `GET`   | `/tasks`       | Retrieve all tasks     |
| `DELETE`| `/tasks`       | Delete a task by ID    |

### Request & Response Examples

#### 1️⃣ **Create a Task**
**Request:**
```json
{
  "task": "Buy groceries"
}
```
**Response:**
```json
{
  "message": "Task added successfully",
  "taskId": "12345",
  "task": "Buy groceries"
}
```

#### 2️⃣ **Get All Tasks**
**Response:**
```json
[
  { "taskId": "12345", "task": "Buy groceries" },
  { "taskId": "67890", "task": "Read a book" }
]
```

#### 3️⃣ **Delete a Task**
**Request:**
```json
{
  "taskId": "12345"
}
```
**Response:**
```json
{
  "message": "Task deleted successfully",
  "taskId": "12345"
}
```

---

## 📌 How to Deploy

### Step 1️⃣: Deploy the Backend
1. Create a **DynamoDB table** named `TodoList` with `taskId` as the primary key.
2. Create a **Lambda function** with the provided `lambda_handler.py` code.
3. Attach an **IAM Role** with `AmazonDynamoDBFullAccess` to Lambda.
4. Set up **API Gateway** to trigger the Lambda function.
5. Enable **CORS headers** in API Gateway.

### Step 2️⃣: Deploy the Frontend with Amplify
1. Push your frontend code to a GitHub repository.
2. Connect the repo to **AWS Amplify** and deploy.
3. Set the API URL in the frontend config.

---

## 📌 CORS Configuration
Ensure that **CORS headers** are included in Lambda responses:
```python
return {
    "statusCode": 200,
    "headers": {"Access-Control-Allow-Origin": "*"},
    "body": json.dumps(response)
}
```

---

## 🎯 Future Enhancements
- ✅ Add authentication with **Cognito**
- ✅ Implement **update task** API
- ✅ UI improvements with React/Tailwind

---

## 🔥 Conclusion
This project showcases **AWS serverless architecture** by integrating Amplify, API Gateway, Lambda, DynamoDB, and IAM. 🚀
