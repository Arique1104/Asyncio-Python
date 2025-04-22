from app.models.user import User

def test_valid_user():
    u = User(id=1, name="Test", email="test@example.com")
    assert u.email == "test@example.com"
    