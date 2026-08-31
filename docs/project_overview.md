# WhatsApp Clone - Project Overview

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#whatsapp-clone---project-overview)

## Project Description

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#project-description)

WhatsApp Clone is a real-time messaging application built using React and FastAPI. The project focuses on implementing the core functionality of a modern messaging platform, including authentication, one-to-one conversations, real-time messaging, message reactions, media sharing, group chats, status updates, and audio/video calls.

The goal is to understand full-stack application architecture, REST APIs, WebSockets, database relationships, authentication, state management with Redux, file uploads, and real-time communication.

---

# Technology Stack

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#technology-stack)

## Backend

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#backend)

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* WebSockets
* JWT Authentication

## Database

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#database)

* PostgreSQL
* Alembic for database migrations

## Frontend

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#frontend)

* React
* Vite
* Redux Toolkit
* React Router
* Tailwind CSS
* JavaScript

## Realtime Communication

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#realtime-communication)

* FastAPI WebSockets
* WebRTC

## Storage

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#storage)

* Cloudinary
* Local storage for development

## Cache

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#cache)

* Redis

## Deployment

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#deployment)

* Render / Railway
* PostgreSQL Cloud Database

## Containerization

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#containerization)

* Docker
* Docker Compose

## Version Control

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#version-control)

* Git
* GitHub

---

# Core Features

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#core-features)

## Authentication

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#authentication)

* User Registration
* User Login
* User Logout
* JWT Authentication
* Token Refresh
* Protected Routes
* Session Management

## Profile Management

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#profile-management)

* View Profile
* Update Profile
* Profile Picture
* About / Bio
* Online Status
* Last Seen

## Users & Contacts

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#users-and-contacts)

* Search Users
* Add Contacts
* Remove Contacts
* View Contact Profiles

## Messaging

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#messaging)

* One-to-One Conversations
* Send Messages
* Receive Messages
* Message History
* Real-Time Messaging
* Reply to Messages
* Forward Messages
* Edit Messages
* Delete Messages
* Message Pagination

## Message Status

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#message-status)

* Sent Status
* Delivered Status
* Read Status
* Read Receipts

## Message Reactions

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#message-reactions)

* Add Reaction
* Remove Reaction
* Multiple Emoji Reactions

## Realtime Features

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#realtime-features)

* WebSocket Connections
* Real-Time Messages
* Online Presence
* Typing Indicators
* Message Delivery Updates
* Read Receipts

## Media & File Sharing

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#media-and-file-sharing)

* Image Sharing
* Video Sharing
* Document Sharing
* Voice Messages
* Media Preview
* File Uploads
* Shared Media View

## Groups

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#groups)

* Create Groups
* Group Profile
* Add Members
* Remove Members
* Leave Group
* Group Administrators
* Group Messages
* Group Media

## Status

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#status)

* Create Status
* Text Status
* Image Status
* Video Status
* View Status
* Status View Tracking
* Delete Status
* Automatic Status Expiration

## Notifications

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#notifications)

* New Message Notifications
* Group Message Notifications
* Message Reaction Notifications
* Call Notifications

## Audio & Video Calls

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#audio-and-video-calls)

* Audio Calls
* Video Calls
* Incoming Calls
* Outgoing Calls
* Call Accept / Reject
* WebRTC Communication

---

# Database Design

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#database-design)

## User

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#user)

Stores authentication, profile, and presence information.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields)

* id
* phone_number
* username
* password_hash
* display_name
* profile_picture
* about
* is_online
* last_seen
* created_at
* updated_at

### Relationship

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationship)

* One User can participate in many Conversations.
* One User can send many Messages.
* One User can create many Statuses.
* One User can belong to many Groups.

---

## Contact

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#contact)

Stores relationships between users and their contacts.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-1)

* id
* user_id
* contact_user_id
* nickname
* created_at

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships)

* One User can have many Contacts.
* One User can appear as a Contact for many Users.

### Constraints

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#constraints)

* Unique (user_id, contact_user_id)

---

## Conversation

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#conversation)

Stores conversations between users or groups.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-2)

* id
* type
* created_at
* updated_at

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships-1)

* One Conversation can have many Members.
* One Conversation can have many Messages.
* A Conversation can represent either a direct chat or a Group.

---

## Conversation Member

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#conversation-member)

Stores users participating in conversations.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-3)

* id
* conversation_id
* user_id
* role
* joined_at

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships-2)

* One Conversation can have many Members.
* One User can belong to many Conversations.

### Constraints

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#constraints-1)

* Unique (conversation_id, user_id)

---

## Message

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#message)

Stores messages sent within conversations.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-4)

* id
* conversation_id
* sender_id
* reply_to_id
* message_type
* content
* media_url
* media_name
* media_size
* is_deleted
* created_at
* updated_at

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships-3)

* One Conversation can have many Messages.
* One User can send many Messages.
* One Message can reply to another Message.
* One Message can have many Reactions.
* One Message can have many Message Status records.

---

## Message Status

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#message-status-1)

Stores the delivery and read status of messages.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-5)

* id
* message_id
* user_id
* status
* timestamp

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships-4)

* One Message can have many Message Status records.
* One User can have many Message Status records.

### Status Types

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#status-types)

* Sent
* Delivered
* Read

---

## Message Reaction

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#message-reaction)

Stores emoji reactions added to messages.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-6)

* id
* message_id
* user_id
* reaction
* created_at

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships-5)

* One Message can have many Reactions.
* One User can react to many Messages.

### Constraints

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#constraints-2)

* Unique (message_id, user_id)

---

## Group

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#group)

Stores group-specific information.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-7)

* id
* conversation_id
* name
* description
* group_picture
* created_by
* created_at

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships-6)

* One Group belongs to one Conversation.
* One Group can have many Members.
* One User can create many Groups.

---

## Group Member

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#group-member)

Stores users belonging to groups.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-8)

* id
* group_id
* user_id
* role
* joined_at

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships-7)

* One Group can have many Members.
* One User can belong to many Groups.

### Roles

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#roles)

* Admin
* Member

---

## Status

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#status)

Stores temporary updates shared by users.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-9)

* id
* user_id
* type
* content
* media_url
* expires_at
* created_at

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships-8)

* One User can create many Statuses.
* One Status can have many Views.

---

## Status View

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#status-view)

Stores users who have viewed a status.

### Fields

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#fields-10)

* id
* status_id
* viewer_id
* viewed_at

### Relationships

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#relationships-9)

* One Status can have many Views.
* One User can view many Statuses.

### Constraints

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#constraints-3)

* Unique (status_id, viewer_id)

---

# Planned Features

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#planned-features)

## Advanced Messaging

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#advanced-messaging)

* Message Search
* Message Pinning
* Starred Messages
* Unread Message Count
* Chat Mute
* Chat Archive

## Privacy

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#privacy)

* Last Seen Privacy
* Profile Picture Privacy
* Status Privacy
* Read Receipt Settings
* Block Users

## Media

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#media)

* Image Compression
* Video Compression
* Media Gallery
* File Size Validation
* Cloud Storage Optimization

## Notifications

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#notifications-1)

* Push Notifications
* Browser Notifications
* Notification Preferences
* Background Notifications

## Calls

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#calls)

* Call History
* Missed Calls
* Group Calls
* Call Notifications

---

# Learning Objectives

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#learning-objectives)

This project is designed to practice:

* FastAPI Application Architecture
* REST API Development
* FastAPI Dependency Injection
* JWT Authentication
* Password Hashing
* Pydantic Validation
* SQLAlchemy ORM
* PostgreSQL Database Design
* Database Relationships
* Alembic Migrations
* CRUD Operations
* React Component Architecture
* Redux Toolkit
* Global State Management
* React Router
* API Integration
* WebSockets
* Real-Time Communication
* WebRTC
* File Uploads
* Cloud Storage
* Redis
* Docker
* Docker Compose
* API Security
* Error Handling
* Pagination
* Cloud Deployment
* Git and GitHub

---

# Future Improvements

[svg](https://github.com/CodeWithVikas0810/whatsapp-clone-project/blob/main/docs/project_overview.md#future-improvements)

* End-to-end encryption
* Multi-device support
* Group video calls
* Message search optimization
* Push notifications
* Advanced privacy controls
* Redis-based presence management
* Background task processing
* Celery integration
* Message queue architecture
* CI/CD pipeline
* Automated testing
* Horizontal scaling
* Production monitoring
