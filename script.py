# curNode = nuke.selectedNode()
print("\n\n\n\n\n\n")


# TODO: Sort by heirarcy instead of height

def reformatUnbounded(startNode : nuke.Node) -> nuke.Node:
    nuke.root().begin()
    # TODO: handle nonetype inputs

    # find parent responsible for out of bounds box
    foundTarget = False

    vistedNodes = list()
    traversalBuffer = list()
    traversalBuffer.append(startNode)

    problemNodes = list()

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
                vistedNodes.append(inputNode)
            else:
                print("skipping")

    vistedNodes.reverse()
    print(vistedNodes)

    nukescripts.clear_selection_recursive()
    
    for curNode in vistedNodes:

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
    pass

reformatUnbounded(nuke.toNode("Fixer"))
