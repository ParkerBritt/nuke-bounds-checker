# curNode = nuke.selectedNode()
print("\n\n\n\n\n\n")


# TODO: Sort by heirarcy instead of height

def reformatUnbounded(traversalList : list[nuke.Node]) -> nuke.Node:
    """
    Identifies and reformats nodes with oversized bounding boxes
    """
    nuke.root().begin()
    # TODO: handle nonetype inputs

    nukescripts.clear_selection_recursive()
    
    for curNode in traversalList:

        print("current node:", curNode.name())
        curNode.redraw()
        isReformatTarget = checkOutOfBounds(curNode)



        if(isReformatTarget):

            curNode.setSelected(True)
            reformatNode = nuke.createNode("Reformat")
            reformatNode.setSelected(False)
            reformatNode.knob("tile_color").setValue(4278190335)
            reformatNode.knob("label").setValue("bbox fixer")

            # for debug:
            # curNode.knob("tile_color").setValue(4278190335)
        # else:
            # for debug:
            # curNode.knob("tile_color").setValue(536805631)

def getUpperNodeTree(startNode: nuke.Node) -> list[nuke.Node]:
    """
    Gets all nodes connected to the input of the startNode
    """
    visitedNodes = list()
    traversalBuffer = list()
    traversalBuffer.append(startNode)

    while len(traversalBuffer) != 0:
        print("len:", len(traversalBuffer))
        curNode = traversalBuffer.pop()
        print("current node", curNode.name())
        print("inputs:", curNode.inputs())
        for i in range(curNode.inputs()):
            print("i:", i)
            inputNode = curNode.input(i)

            if(inputNode is not None):
                print("adding:", inputNode.name())
                traversalBuffer.append(inputNode)
                visitedNodes.append(inputNode)
            else:
                print("skipping")

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

print("thisNode:", getExecutingNode().name())
reformatUnbounded(getUpperNodeTree(getExecutingNode()))
