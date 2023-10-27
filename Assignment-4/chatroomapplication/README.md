# Chat Room Application

This project is a simple chat room application implemented using Spring Boot for the backend and basic HTML/CSS/JavaScript for the frontend.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Java 11 or later.
- You have a basic understanding of Spring framework concepts.
- (Optional) You have installed an IDE (like IntelliJ IDEA, Eclipse, or any preferred one).

## Running the Chat Room Application

To run the Chat Room Application, follow these steps:

1. Clone the repository to your local machine or download the source code.
2. Open a terminal and navigate to the project directory.
3. Run the following command to start the Spring Boot application:
```./mvnw spring-boot:run```
or if you are using Maven directly,
```mvn spring-boot:run```

Alternatively, you can run the application from your IDE by importing the project and running it directly.

4. Open a web browser and navigate to `http://localhost:8080` (assuming the default port is 8080, otherwise replace with the correct port number).

5. The application should now be running, and you can interact with the UI to test its functionalities.

## Using the Chat Room Application

1. Enter your name in the provided text box and click "Enter" to join the chat room.
2. To send a message, type your message in the 'Enter Your Message:' box and click "Send".
3. Your message will be broadcasted to everyone connected to the chat room.
4. To leave the chat, click the "Logout" button.

## Project Structure

- `MessageConfig` class: Configures the WebSocket message broker and registers the STOMP endpoints.
- `MessageController` class: Handles the mapping of incoming messages and broadcasts them to subscribed clients.
- `User` class: Represents the user entity in the application.
- `ChatroomapplicationApplication` class: Contains the main method to run the Spring Boot application.
- Frontend files: The `index.html`, `script.js`, and `style.css` files make up the basic frontend of the application.