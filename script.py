# curNode = nuke.selectedNode()
print("\n\n\n\n\n\n")

LABEL_TEXT = "boundsChecker__"

def reformatUnbounded(traversalList : list[nuke.Node]) -> nuke.Node:
    """
    Identifies and reformats nodes with oversized bounding boxes
    """
    originalSelectedNode = nuke.thisNode()
    nuke.root().begin()

    nukescripts.clear_selection_recursive()

    maxBorder = getMaxBorder()
    print("max Border:", maxBorder)
    
    for curNode in traversalList:

        print("current node:", curNode.name())
        # curNode.redraw()
        isReformatTarget = checkOutOfBounds(curNode, maxBorder)



        if(isReformatTarget):

            curNode.setSelected(True)
            reformatNode = nuke.createNode("Reformat")
            reformatNode.setSelected(False)
            reformatNode.knob("tile_color").setValue(4278190335)
            reformatNode.knob("label").setValue(LABEL_TEXT+curNode.name())
            reformatNode.hideControlPanel()

            # for debug:
            # curNode.knob("tile_color").setValue(4278190335)
        # else:
            # for debug:
            # curNode.knob("tile_color").setValue(536805631)

    # originalSelectedNode.showControlPanel()
    originalSelectedNode.setSelected(True)

def getUpperNodeTree(startNode: nuke.Node) -> list[nuke.Node]:
    """
    Gets all nodes connected to the input of the startNode
    """
    print("traversing tree")
    visitedNodes = list()
    traversalBuffer = list()
    traversalBuffer.append(startNode)

    while len(traversalBuffer) != 0:
        curNode = traversalBuffer.pop()
        for i in range(curNode.inputs()):
            inputNode = curNode.input(i)

            if(inputNode is not None):
                traversalBuffer.append(inputNode)
                if(inputNode not in visitedNodes):
                    visitedNodes.append(inputNode)

    visitedNodes.reverse()
    return visitedNodes



def checkOutOfBounds(node : nuke.Node, maxBorder: int = 200) -> bool:
    maxBoundDist = maxBorder
    print("maxBoundDist:", maxBoundDist)

    bbox = node.bbox()
    xMin = bbox.x()<-maxBoundDist 
    yMin = bbox.y()<-maxBoundDist

    xMax = (bbox.x()+bbox.w())>(node.width()+maxBoundDist)
    yMax = (bbox.y()+bbox.h())>(node.height()+maxBoundDist)
    status = xMin or yMin or xMax or yMax 
    return status


def getExecutingNode() -> nuke.Node:
    # static variable since thisNode gets changed later
    if not hasattr(getExecutingNode, "execNode"):
        getExecutingNode.execNode = nuke.thisNode()
    print("THIS NODE:", getExecutingNode.execNode.name())
    return getExecutingNode.execNode

def removeReformats(traversalList : list[nuke.Node]) -> nuke.Node:
    print("removing")

    for node in traversalList:
        if(node.Class()!="Reformat"):
            continue

        if(not node.knob("label").value().startswith(LABEL_TEXT)):
            continue

        nuke.delete(node)


def addNodes():
    """
    High level function to add reformat nodes
    """
    executingNode = getExecutingNode()

    removeReformats(getUpperNodeTree(executingNode))
    reformatUnbounded(getUpperNodeTree(executingNode))

def removeNodes():
    """
    High level function to remove reformat nodes
    """
    removeReformats(getUpperNodeTree(getExecutingNode()))

def getMaxBorder():
    return getExecutingNode().knob("maxBoundDist").value()

def debug():
    print('debug')
    print(getMaxBorder())
