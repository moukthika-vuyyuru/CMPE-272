package com.rea.time.chatroomapplication.model;

public class User {
    private String name;
    private String messageContent;

    public User(String name, String content) {
        this.name = name;
        this.messageContent = content;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getMessageContent() {
        return messageContent;
    }

    public void setMessageContent(String messageContent) {
        this.messageContent = messageContent;
    }
}
