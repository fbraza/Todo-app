class Todo():

    DONE_MARKER, UNDONE_MARKER = "\u2713", " "

    def __init__(self, description, priority="Normal", group=None):
        """
        Constructor of our Todo object

        Attributes:
        -----------
        - description: str, description of the task
        - priority: str, choose between High, Normal, Low
        - group: str, a tag to group your task, choose between (Family, Work, Sport, Health, Finance)
        - done: bool, specifies whether the task is done or not

        Return:
        -------
        - None
        """
        if not self.is_right_priority(priority) or not self.is_right_group(group):
            raise ValueError("Check your values for priority or group. Run --help for more details")
        self.description = description
        self.priority = priority
        self.group = group
        self.done = False

    def __str__(self):
        """
        String representation of our Todo object

        Return:
        -------
        - None
        """
        marker = Todo.DONE_MARKER if self.done else Todo.UNDONE_MARKER
        return """\n--- {} ---\n[{}] : {} : {}""".format(self.group, marker, self.description, self.priority)

    def is_done(self):
        """
        Check if the task is done

        Return:
        -------
        - Boolean
        """
        return self.done

    def is_right_priority(self, priority):
        """
        Check if the priority the user input is included in the possible choice provided by the API

        Return:
        -------
        - Boolean
        """
        return priority in ["High", "Normal", "Low"]

    def is_right_group(self, group):
        return group in ["Family", "Work", "Sport", "Health", "Finance", None]

    def set_done(self):
        self.done = True

    def redefine_priority(self, priority):
        if not self.is_right_priority(priority):
            raise ValueError("Choose between: High, Normal or Low")
        self.priority = priority

    def set_group(self, group):
        if not self.is_right_group(group):
            raise ValueError("Choose between: Family, Work, Sport, Health or Finance")
        self.group = group
