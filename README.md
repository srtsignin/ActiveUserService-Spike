# ActiveUserService-Spike
A temporary substitute for the ActiveUserService

GET /
**Response:**

```json
{
    'activeUsers': list(active_users)
}
```

POST /
**Body:**
```json
{
    user: <username>
}
```

**Response:**

```json
{
    'userAdded': <username>,
    'activeUsers': list(active_users)
}
```

DELETE /
**Response:**

```json
{
    'result': 'Success',
    'activeUsers': list(active_users)
}
```