import pytest
from app.src.views import upsert_user


@pytest.mark.parametrize(
        "name",
        [
            ("ivan"),
            ("petr"),
        ]
)
async def test_upsert_user(name, test_db):
    # pytest tests/src/test_src.py::test_upsert_user -rP

    item = {
        "name": name,
    }
    user, error = await upsert_user(item, test_db)
    assert hasattr(user, "id")
    
