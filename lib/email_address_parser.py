import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split by comma or space
        raw_list = re.split(r'[,\s]+', self.addresses)

        # Define a simple email regex
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Filter only valid emails
        valid_emails = [email for email in raw_list if re.match(email_pattern, email)]

        # Remove duplicates and sort
        return sorted(set(valid_emails))
