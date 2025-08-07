# API Endpoints – Book

- `GET /api/books/` – List all books
- `GET /api/books/<id>/` – Get single book
- `POST /api/books/create/` – Create book (auth required)
- `PUT /api/books/<id>/update/` – Update book (auth required)
- `DELETE /api/books/<id>/delete/` – Delete book (auth required)

**Permissions**
- Read access is public.
- Write access is restricted to authenticated users.
