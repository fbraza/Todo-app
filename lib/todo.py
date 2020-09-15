class Todo():

    DONE_MARKER, UNDONE_MARKER = "\u2713", " "

    def __init__(self, description: str, priority="Normal", done: bool = False):
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
        try:
            if not self.is_right_priority(priority):
                raise ValueError("\nError:\n  Only Low, Normal or High for priority. Run todo add --help for more details")
        except ValueError as message:
            print(message)
            return
        self.description = description
        self.priority = priority
        self.done = done

    def __str__(self):
        """
        String representation of our Todo object

        Return:
        -------
        - None
        """
        marker = Todo.DONE_MARKER if self.done else Todo.UNDONE_MARKER
        return "[{}] : {} : {}".format(marker, self.description, self.priority)

    def __lt__(self, other):
        """
        Less then method to compare task by priority
        Useful if we want to sort them by this tag

        Parameter:
        ----------
        other: Todo object

        Return:
        -------
        - boolean
        """
        priorities = ["High", "Normal", "Low"]
        return priorities.index(self.priority) < priorities.index(other.priority)

    def __eq__(self, other):
        """
        equal method to compare task by title
        There is little probability that an user write two times
        the same task. So we take the description of the task as
        am equality operand

        Parameter:
        ----------
        other: Todo object

        Return:
        -------
        - boolean
        """
        return self.description == other.description

    def is_done(self):
        """
        Check if the task is `done`

        Return:
        -------
        - Boolean
        """
        return self.done

    def set_done(self):
        """
        Setter method for the attribute `done

        Return:
        -------
        - None
        """
        self.done = True

    def redefine_priority(self, priority: str):
        """
        Setter method for the attribute `priority`

        Return:
        -------
        - None
        """
        try:
            if not self.is_right_priority(priority):
                raise ValueError("\nError:\n  Only Low, Normal or High for priority. Run todo add --help for more details")
        except ValueError as message:
            print(message)
            return
        self.priority = priority

    def is_right_priority(self, priority):
        """
        Check if the priority the user inputted is included in the possible choice provided by the API

        Return:
        -------
        - Boolean
        """
        return priority in ["High", "Normal", "Low"]
