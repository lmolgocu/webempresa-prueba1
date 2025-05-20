# core/custom_email_backend.py
from django.core.mail.backends.smtp import EmailBackend
import ssl
import certifi

class CustomEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False

        connection_class = self.connection_class
        try:
            self.connection = connection_class(
                self.host, self.port, timeout=self.timeout
            )
            self.connection.ehlo()
            if self.use_tls:
                context = ssl._create_unverified_context()
                self.connection.starttls(context=context)
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception:
            if self.fail_silently:
                return False
            raise
