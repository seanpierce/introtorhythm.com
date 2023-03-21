from django.core.management.base import BaseCommand
from schedule import scheduler

class Command(BaseCommand):
    """
    Django module used to create a management command.
    """
    def handle(self, *args, **options):
        """
        When executed, this process will invoke the schedule software.
        """
        try:
            outcome = scheduler.run()
            self.stdout.write(outcome)
        except Exception as ex:
            self.stdout.write(str(ex))