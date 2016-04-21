import factory
from faker import Factory as FakerFactory

from scienceapi.projects import models


faker = FakerFactory.create()


class TagFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda o: faker.word())

    class Meta:
        model = models.Tag


class CategoryFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda o: faker.job())

    class Meta:
        model = models.Category


class ProjectFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda o: faker.word())
    project_url = factory.LazyAttribute(lambda o: faker.url())
    slug = factory.LazyAttribute(lambda o: faker.slug())
    github_owner = factory.LazyAttribute(lambda o: faker.user_name())
    github_repository = factory.LazyAttribute(lambda o: faker.slug())
    image_url = factory.LazyAttribute(lambda o: faker.image_url())
    institution = factory.LazyAttribute(lambda o: faker.company())
    description = factory.LazyAttribute(lambda o: faker.text())
    short_description = factory.LazyAttribute(
        lambda o: faker.text(max_nb_chars=300)
    )
    status = factory.LazyAttribute(lambda o: faker.pybool())
    license = factory.LazyAttribute(lambda o: faker.word())

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of tags were passed in, use them
            for tag in extracted:
                self.tags.add(tag)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of categories were passed in, use them
            for category in extracted:
                self.categories.add(category)

    class Meta:
        model = models.Project


class ResourceLinkFactory(factory.DjangoModelFactory):
    url = factory.LazyAttribute(lambda o: faker.url())
    title = factory.LazyAttribute(lambda o: faker.word())
    project = factory.SubFactory(ProjectFactory)

    class Meta:
        model = models.ResourceLink
