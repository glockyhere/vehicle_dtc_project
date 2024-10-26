import unittest
from src.alerts.telegram_alerts import send_telegram_alert

class TestTelegramAlerts(unittest.TestCase):
    def test_send_alert(self):
        message = "Test alert for Vehicle V1234"
        status_code = send_telegram_alert(message)
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
