# ActiveUserService-Spike
A temporary substitute for the ActiveUserService

GET /

**Response:**

```js
{
    'activeUsers': list(active_users)
}
```

POST /

**Body:**

```js
{
    'user': '<username>'
}
```

**Response:**

```js
{
    'userAdded': '<username>',
    'activeUsers': list(active_users)
}
```

DELETE /

**Response:**

```js
{
    'result': 'Success',
    'activeUsers': list(active_users)
}
```