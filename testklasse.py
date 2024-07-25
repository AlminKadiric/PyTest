import app

class TestApp:
    def test_add(self):
        assert app.add(2,3) == 5
        
    def test_sub(self):
        assert app.sub(2,3) == -1