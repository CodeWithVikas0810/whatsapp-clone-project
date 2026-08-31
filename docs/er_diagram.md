# Entity Relationship Diagram

## Description

The application consists of ten main entities:

1. User
2. Contact
3. Conversation
4. Conversation Member
5. Message
6. Message Status
7. Message Reaction
8. Group
9. Group Member
10. Status
11. Status View

Relationships:

* A User can have multiple Contacts.
* A User can participate in multiple Conversations.
* A Conversation can have multiple Members.
* A Conversation can contain multiple Messages.
* A User can send multiple Messages.
* A Message can reply to another Message.
* A Message can have multiple Reactions.
* A Message can have multiple Message Status records.
* A Conversation can represent a Group.
* A Group can have multiple Members.
* A User can belong to multiple Groups.
* A User can create multiple Statuses.
* A Status can have multiple Views.
* A User can view multiple Statuses.

## Mermaid ER Diagram

```mermaid
erDiagram

    USER ||--o{ CONTACT : has

    USER ||--o{ CONVERSATION_MEMBER : joins
    CONVERSATION ||--o{ CONVERSATION_MEMBER : contains

    CONVERSATION ||--o{ MESSAGE : contains
    USER ||--o{ MESSAGE : sends

    MESSAGE ||--o{ MESSAGE_STATUS : has
    USER ||--o{ MESSAGE_STATUS : receives

    MESSAGE ||--o{ MESSAGE_REACTION : receives
    USER ||--o{ MESSAGE_REACTION : gives

    MESSAGE ||--o{ MESSAGE : replies_to

    CONVERSATION ||--o| GROUP : represents
    GROUP ||--o{ GROUP_MEMBER : contains
    USER ||--o{ GROUP_MEMBER : joins

    USER ||--o{ STATUS : creates
    STATUS ||--o{ STATUS_VIEW : receives
    USER ||--o{ STATUS_VIEW : views

    USER {
        uuid id PK
        string phone_number
        string username
        string password_hash
        string display_name
        string profile_picture
        string about
        boolean is_online
        datetime last_seen
        datetime created_at
        datetime updated_at
    }

    CONTACT {
        uuid id PK
        uuid user_id FK
        uuid contact_user_id FK
        string nickname
        datetime created_at
    }

    CONVERSATION {
        uuid id PK
        string type
        datetime created_at
        datetime updated_at
    }

    CONVERSATION_MEMBER {
        uuid id PK
        uuid conversation_id FK
        uuid user_id FK
        string role
        datetime joined_at
    }

    MESSAGE {
        uuid id PK
        uuid conversation_id FK
        uuid sender_id FK
        uuid reply_to_id FK
        string message_type
        text content
        string media_url
        string media_name
        bigint media_size
        boolean is_deleted
        datetime created_at
        datetime updated_at
    }

    MESSAGE_STATUS {
        uuid id PK
        uuid message_id FK
        uuid user_id FK
        string status
        datetime timestamp
    }

    MESSAGE_REACTION {
        uuid id PK
        uuid message_id FK
        uuid user_id FK
        string reaction
        datetime created_at
    }

    GROUP {
        uuid id PK
        uuid conversation_id FK
        string name
        string description
        string group_picture
        uuid created_by FK
        datetime created_at
    }

    GROUP_MEMBER {
        uuid id PK
        uuid group_id FK
        uuid user_id FK
        string role
        datetime joined_at
    }

    STATUS {
        uuid id PK
        uuid user_id FK
        string type
        text content
        string media_url
        datetime expires_at
        datetime created_at
    }

    STATUS_VIEW {
        uuid id PK
        uuid status_id FK
        uuid viewer_id FK
        datetime viewed_at
    }
```

## Future Enhancements

* End-to-End Encryption
* Message Search
* Pinned Messages
* Starred Messages
* Chat Archiving
* Chat Mute
* User Blocking
* Advanced Privacy Settings
* Push Notifications
* Call History
* Group Audio/Video Calls
* Multi-Device Support
* Redis-Based Presence
* Celery Background Tasks
* Message Queue Integration
* CI/CD Pipeline
