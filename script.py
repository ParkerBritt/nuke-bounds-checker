# curNode = nuke.selectedNode()
print("\n\n\n\n\n\n")

LABEL_TEXT = "__bbox_fixer__"

def reformatUnbounded(traversalList : list[nuke.Node]) -> nuke.Node:
    """
    Identifies and reformats nodes with oversized bounding boxes
    """
    originalSelectedNode = nuke.thisNode()
    nuke.root().begin()

    nukescripts.clear_selection_recursive()
    
    for curNode in traversalList:

        print("current node:", curNode.name())
        # curNode.redraw()
        isReformatTarget = checkOutOfBounds(curNode)



        if(isReformatTarget):

            curNode.setSelected(True)
            reformatNode = nuke.createNode("Reformat")
            reformatNode.setSelected(False)
            reformatNode.knob("tile_color").setValue(4278190335)
            reformatNode.knob("label").setValue(LABEL_TEXT)
            reformatNode.hideControlPanel()

            # for debug:
            # curNode.knob("tile_color").setValue(4278190335)
        # else:
            # for debug:
            # curNode.knob("tile_color").setValue(536805631)

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
                visitedNodes.append(inputNode)

    visitedNodes.reverse()
    return visitedNodes



def checkOutOfBounds(node : nuke.Node) -> bool:
    maxBoundDist = 200

    bbox = node.bbox()
    xMin = bbox.x()<-maxBoundDist 
    yMin = bbox.y()<-maxBoundDist

    xMax = (bbox.x()+bbox.w())>(node.width()+maxBoundDist)
    yMax = (bbox.y()+bbox.h())>(node.height()+maxBoundDist)
    status = xMin or yMin or xMax or yMax 
    print(bbox.x())
    return status


def getExecutingNode() -> nuke.Node:
    return nuke.thisNode()

def removeReformats(traversalList : list[nuke.Node]) -> nuke.Node:
    print("removing")

    for node in traversalList:
        if(node.Class()!="Reformat"):
            continue

        if(node.knob("label").value() != LABEL_TEXT):
            continue

        nuke.delete(node)
