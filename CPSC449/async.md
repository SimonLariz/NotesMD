## Asynchronous Programming
- No need to wait for the result of a function before moving on to the next one.
- The program can continue to run.

Coroutine - A function that can pause and resume its execution.

Task - in FASTApi, a task is unit of work that can be execute asynchronously in the background either immediately or at some point in the future.

Event loop - responsible for managing and coordinating the tasks or coroutines in an application, based on priority and available resources.

## Asyncio 
- A library to write concurrent code using the async/await syntax.

Snippet: 
```python
import asyncio
async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
```

## FastAPI
- A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

Snippet:
```python
app = FastAPI()

def send_email(email: str, message: str):
    print(f"email to {email} with message {message}")

@app.post("/send-email/")
async def send_email_route(email: str, message: str):
    await asyncio.get_event_loop().run_in_executor(None, send_email, email, message)
    return {"message": "Email sent successfully"}
```

## Microservices
- A software development technique that structures an application as a collection of loosely coupled services.

## Monolithic Architecture
- A single unified model that combines the user interface, business logic, and data access layers of an application.
- All the components are interconnected and interdependent.
- Difficult to scale and maintain.

## Microservices Architecture
- An architectural style that structures an application as a collection of services that are:
  - Highly maintainable and testable.
  - Loosely coupled.
  - Independently deployable.
  - Organized around business capabilities.
  - Owned by a small team.

## Broker
- Broker means a third party/middleMan that helps to perform or achieve our goal. In this case, its service as we are talking about microservices.
- So, Broker which helps services to do inter-communication via messaging is Message Broker.



