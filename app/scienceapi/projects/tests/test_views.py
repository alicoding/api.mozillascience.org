from django.test import TestCase
from django.core.urlresolvers import reverse

from scienceapi.projects.tests.test_models import (
    ProjectFactory,
    ResourceLinkFactory,
    TagFactory,
    CategoryFactory,
)


class ProjectTests(TestCase):
    def setUp(self):
        super(ProjectTests, self).setUp()

    def test_get_all_projects(self):
        tag1 = TagFactory()
        tag2 = TagFactory()
        tag3 = TagFactory()
        tag4 = TagFactory()
        category1 = CategoryFactory()
        category2 = CategoryFactory()
        project1 = ProjectFactory.create(
            tags=(tag1, tag3),
            categories=[category1],
        )
        project2 = ProjectFactory.create(
            tags=(tag2, tag3, tag4),
        )
        project3 = ProjectFactory.create(
            tags=[tag4],
            categories=(category1, category2),
        )
        link1 = ResourceLinkFactory.build()
        link2 = ResourceLinkFactory.build()
        link3 = ResourceLinkFactory.build()
        link1.project = project1
        link2.project = project1
        link3.project = project2
        link1.save()
        link2.save()
        link3.save()

        response = self.client.get(reverse('project-all'))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data[2]['name'], project3.name)
