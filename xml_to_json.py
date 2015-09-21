
import pprint as pp
from unittest import TestCase

import xmltodict

from node import Node, Tree


class BadCriteriaException(Exception):
    """ Raised if the criteria is just flat out baaaad """


class XTJ:
    """ Handle the xml and turn it into the required JSON
        takes: xml data
    """

    CRITERIA_SQUAD = 'squad'
    CRITERIA_CHAPTER = 'chapter'

    CRITERIA = [CRITERIA_SQUAD, CRITERIA_CHAPTER]

    def xml_to_dict(self, xml):
        """ Turn the xml into a dictionary """
        return xmltodict.parse(xml)

    def org_by(self, criteria, xml):
        """ Organize The dict by a specific criteria
            Time Complexity: O(Nlog(N))
            Steps:
                pre. Validation
                1. Convert XML
                2. Create Tree
                3. Sort the Data to create consistency when viewing the data
                    O(Nlog(N)) -> Mergesort
                4. Convert to JSON
        """
        if criteria not in self.CRITERIA:
            raise BadCriteriaExceptions("Check Your Criteria")
        try:
            raw_dict = self.xml_to_dict(xml)
        except:
            raise Warning("Serving Static File")
            xml = ""
            with open ("sample.xml", "r") as myfile:
                self.data = myfile.read().replace('\n', '')
            raw_dict = self.xml_to_dict(xml)
        organized_tree = self.create_chart(criteria, raw_dict)
        return organized_tree

    def create_chart(self, criteria, raw_dict):
        """ Organize the Data """
        result = []
        organized_chart = {"result": result}
        criteria_string = 'gsx:'+ criteria
        name_string = 'gsx:name'

        team_dict = {}
        tree = Tree(self.create_root())

        for entry in raw_dict['feed']['entry']:
            team = entry[criteria_string]
            name = entry['gsx:name']
            desc = entry['gsx:role']
            member = Node(name, desc, leaf=True)

            if team in team_dict.keys():
                team_dict[team].append(member)
            else:
                team_dict[team] = []
                team_dict[team].append(member)

        for team, members in team_dict.iteritems():
            # print team
            # for member in members:
            #     print "\t"+member.name
            team_node = Node(team, "Associated Team Description")
            team_node.children = members
            tree.root.children.append(team_node)

        return tree


    def create_root(self):
        name = "Product and Engineering"
        desc = "It is the place with the coolest tech team in the world"
        children = []
        root = Node(name, desc, children)
        return root

    def sort(self):
        """ Sort it  """


class TestXTJ(TestCase):
    def setUp(self):
        """  """
        with open ("sample.xml", "r") as myfile:
            self.data = myfile.read().replace('\n', '')

    def test_xml_deconstruction(self):
        """  """
        xtj = XTJ()
        dict_data = xtj.xml_to_dict(self.data)
        squad = dict_data['feed']['entry'][0]['gsx:squad']
        chapter = dict_data['feed']['entry'][0]['gsx:chapter']
        print squad
        print chapter
        assert True

    def test_tree_construction(self):
        """  """
        xtj = XTJ()
        tree = xtj.org_by('squad', self.data)
        # print tree
        assert True

    def test_render_json_squad(self):
        xtj = XTJ()
        tree = xtj.org_by('squad', self.data)

        pp.pprint(tree.render_json())
        assert True

    def test_render_json_chapter(self):
        xtj = XTJ()
        tree = xtj.org_by('chapter', self.data)

        pp.pprint(tree.render_json())
        assert False
