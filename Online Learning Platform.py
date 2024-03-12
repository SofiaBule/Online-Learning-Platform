class OnlineLearningPlatform:
    def __init__(self):
        self.courses = {}

    def add_course(self, name, description):
        self.courses[name] = description

    def view_courses(self):
        for name, description in self.courses.items():
            print(f"{name}: {description}")

# Example usage:
platform = OnlineLearningPlatform()
platform.add_course("Python Programming", "Learn Python from scratch")
platform.add_course("Machine Learning", "Introduction to machine learning concepts")
platform.view_courses()
