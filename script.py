# curNode = nuke.selectedNode()
print("\n\n\n\n\n\n")

nuke.root().begin()
allNodes = nuke.root().nodes()
# TODO: check for no nodes


# TODO: Sort by heirarcy instead of height

def findTargetNode(startNode : nuke.Node) -> nuke.Node:
    # TODO: handle nonetype inputs

    # find parent responsible for out of bounds box
    prevNode = startNode
    foundTarget = False
    while not foundTarget:
        curNode = prevNode.input(0)

        # if not out of bounds then the previous node is the top level target
        if(not checkOutOfBounds(curNode)):
            return prevNode


        prevNode = curNode

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




print("responsible node:", findTargetNode(nuke.toNode("Merge5")).name())
# for curNode in allNodes:
#     print("\n----\n")
#     print("name:", curNode.name())
#     print(bbox.x(), bbox.y(), bbox.w(), bbox.h())
#     print(curNode.width(), curNode.height())

#     isReformatTarget = checkOutOfBounds(curNode)

#     print("is reformat target:", isReformatTarget)
#     if(isReformatTarget):
#         # print(nuke.getColor(curNode.knob("tile_color").value()))
#         curNode.knob("tile_color").setValue(4278190335)

#         # TODO: filter only connected nodes

#         curNode.setSelected(True)
#         print("target node:", findTargetNode(curNode))
#         reformatNode = nuke.createNode("Reformat")
#         # break
#         print("color to red")
#     else:
#         curNode.knob("tile_color").setValue(536805631)
#         print("color to green")


# nuke.root().end()
