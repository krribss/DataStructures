class TreeNode:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self,hierarchy):
        spaces='   '*self.get_level()
        prefix=spaces +"|__" if self.parent else ""
        if hierarchy=='name':
            print(prefix + self.name)
        elif hierarchy=='designation':
            print(prefix + self.designation)
        else:
            print(prefix + self.name+" ("+self.designation+")")
        if self.children:
            for child in self.children:
                child.print_tree(hierarchy)


def build_management_tree():
    ceo=TreeNode("Nilupul","CEO")
    cto=TreeNode("Chinmay","CTO")
    hrhead=TreeNode("Gels","HR Head")
    ih=TreeNode("Vishwa","Infrastructure Head")
    ah=TreeNode("Aamir","Application Head")
    rm=TreeNode("Peter","Recruiter Manager")
    pm=TreeNode("waqas","Policy Manager")

    ceo.add_child(cto)
    ceo.add_child(hrhead)

    cto.add_child(ih)
    cto.add_child(ah)
    hrhead.add_child(rm)
    hrhead.add_child(pm)

    ih.add_child(TreeNode("Dhaval","Cloud Manager"))
    ih.add_child(TreeNode("Abhijit","App Manager"))

    ceo.print_tree("name")
    ceo.print_tree("designation")
    ceo.print_tree("both")

if __name__=='__main__':
    build_management_tree()
