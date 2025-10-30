import molotov

@molotov.scenario(weight=100)
async def test_api(session):
    async with session.get('http://localhost:5000/api') as resp:
        assert resp.status == 200, f"Ожидался 200, получен {resp.status}"
        data = await resp.json()
        assert data['status'] == 'ok', f"Ожидался status='ok', получен {data.get('status')}"
        assert 'message' in data, "Отсутствует поле 'message'"
