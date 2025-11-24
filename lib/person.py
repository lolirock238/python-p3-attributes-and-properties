APPROVED_JOBS = ["Sales", "ITC", "Marketing", "HR", "Manager", "Engineer"]

class Person:
    APPROVED_JOBS = APPROVED_JOBS  # Class-level approved jobs

    def __init__(self, name="Anonymous", job="Sales"):
        self.name = name
        self.job = job

    # -----------------------------
    # Name property
    # -----------------------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    # -----------------------------
    # Job property
    # -----------------------------
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
