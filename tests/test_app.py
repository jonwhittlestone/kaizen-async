def test_home(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Kaizen": f"Personal metrics server - {response.url}api/kaizen"}
