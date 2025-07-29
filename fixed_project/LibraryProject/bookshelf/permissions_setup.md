# Django Permissions and Groups Setup for Bookshelf App

## 🎯 Objective
Control access to views in the Bookshelf app using Django's permissions and groups system.

---

## ✅ Custom Permissions

Custom permissions were defined in the `Book` model inside `bookshelf/models.py`:

```python
class Meta:
    permissions = [
        ("can_view", "Can view books"),
        ("can_create", "Can create books"),
        ("can_edit", "Can edit books"),
        ("can_delete", "Can delete books"),
    ]
