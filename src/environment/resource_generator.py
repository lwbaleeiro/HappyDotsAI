import random
from environment.resource import Resource

class ResourceGemerator:
    def __init__(self, screen, num_resources):
        self.num_resources = num_resources
        self.screen = screen
        self.resources = []

    def generate_resources(self):
        resources = []
        for _ in range(self.num_resources):
            x = random.randint(0, self.screen.get_width())
            y = random.randint(0, self.screen.get_height())
            resource = Resource(x, y)
            resource.resource_type()
            resources.append(resource)
            

        self.resources = resources
    
    def draw(self):
        for resource in self.resources:
            resource.draw(self.screen)