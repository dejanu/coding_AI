# Prompt Engineering Cheat Sheet: Domain Knowledge as a Force Multiplier

💡 The more you specify the domain, stack, and real-world context, the more useful and production-ready the output will be!

| Domain      | Use this Prompt                                      | Instead of This Prompt                        | Why (Force Multiplier)                                                                 |
|-------------|------------------------------------------------------|-----------------------------------------------|----------------------------------------------------------------------------------------|
| Frontend    | `Generate a React component for a login form with email validation and Material UI styling.` | `Create a login form` | Ensures production-ready, styled, and framework-aligned code. |
| Layout      | `Use Flexbox or CSS Grid to align and distribute elements in a responsive layout.` | `Put things next to each other` | Gives precise control over alignment and responsiveness. |
| Style       | `Apply Tailwind utility classes for styling components inline.` | `Use specific CSS files` | Enables rapid, consistent, and maintainable inline styling. |
| Feedback    | `Show skeleton screens for loading states instead of spinners.` | `Show loading spinners` | Provides a modern, premium user experience. |
| Backend     | `Write a Flask route that handles file uploads, saves to S3, and returns a presigned URL.` | `Write a file upload endpoint` | Incorporates real-world backend patterns and cloud integration. |
| Data Science| `Create a pandas pipeline to clean, normalize, and one-hot encode a DataFrame for ML.` | `Clean this dataset` | Produces code ready for ML workflows using best practices. |
| DevOps      | `Write a GitHub Actions workflow for CI/CD on a Node.js app, including lint, test, and deploy to Heroku.` | `Write a CI/CD pipeline` | Leverages platform and stack knowledge for robust automation. |
| Security    | `Write a Django authentication view with JWT and CSRF protection.` | `Write a login view` | Adds security best practices and reduces vulnerabilities. |
| Validation  | `Implement input sanitization to prevent SQL injection and XSS attacks.` | `Checking the data` | Prevents code injection and security breaches. |
| Auth        | `Use OAuth or JWT for authentication and authorization flows.` | `Login system` | Specifies the security protocol for robust authentication. |
| API Design  | `Design a RESTful API for a bookstore with endpoints for books, authors, and orders, using OpenAPI spec.` | `Design an API for a bookstore` | Produces standardized, documented, and scalable APIs. |
| Cloud       | `Write Terraform code to provision an AWS Lambda with API Gateway and DynamoDB integration.` | `Provision a serverless function` | Delivers production-ready infrastructure-as-code for cloud deployments. |
| Database    | `Write a PostgreSQL migration to add a users table with email, hashed password, and created_at.` | `Add a users table` | Ensures production-ready migrations and best schema practices. |
| Efficiency  | `Add database indexing to optimize query performance for frequent searches.` | `Fast searching` | Optimizes how the database finds records and improves performance. |
| State       | `Implement state management (e.g., Redux, Zustand, Context API) to handle app data flow and updates.` | `The app's memory` | Enables robust handling of data changes over time. |
