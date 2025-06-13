# curNode = nuke.selectedNode()
print("\n\n\n\n\n\n")

nuke.root().begin()
allNodes = nuke.root().nodes()
# TODO: check for no nodes


# TODO: Sort by heirarcy instead of height

def findTargetNode(startNode : nuke.Node) -> nuke.Node:
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

    print("done")
    vistedNodes.reverse()
    print(vistedNodes)

    nukescripts.clear_selection_recursive()
    
    for curNode in vistedNodes:

        print("current node:", curNode.name())
        curNode.redraw()
        isReformatTarget = checkOutOfBounds(curNode)



        if(isReformatTarget):
            # print(nuke.getColor(curNode.knob("tile_color").value()))
            curNode.knob("tile_color").setValue(4278190335)

            # TODO: filter only connected nodes
            print("selected nodes:", nuke.selectedNodes())

            curNode.setSelected(True)
            reformatNode = nuke.createNode("Reformat")
            reformatNode.setSelected(False)
            # curNode.setSelected(False)
            # break
            print("color to red")
        else:
            curNode.knob("tile_color").setValue(536805631)

        # if not out of bounds then the previous node is the top level target
        # if(not checkOutOfBounds(curNode)):
        #     problemNodes.append(prevNode)




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




print("responsible node:", findTargetNode(nuke.toNode("Fixer")))
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
#         # reformatNode = nuke.createNode("Reformat")
#         # break
#         print("color to red")
#     else:
#         curNode.knob("tile_color").setValue(536805631)
#         print("color to green")


# nuke.root().end()
