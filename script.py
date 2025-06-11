# curNode = nuke.selectedNode()
print("\n\n\n\n\n\n")

nuke.root().begin()
allNodes = nuke.root().nodes()
# TODO: check for no nodes

maxBoundDist = 200

# TODO: Sort by heirarcy instead of height

def checkOutOfBounds(startNode : nuke.Node) -> bool:
    bbox = curNode.bbox()
    return bbox.x()<-maxBoundDist or bbox.y()<-maxBoundDist or (bbox.x()+bbox.w())>(node.width()+maxBoundDist) or (bbox.y()+bbox.h())>(node.height()+maxBoundDist)




for curNode in allNodes:
    print("name:", curNode.name())
    print(bbox.x(), bbox.y(), bbox.w(), bbox.h())
    print(curNode.width(), curNode.height())

    isReformatTarget = checkOutOfBounds(curNode)

    print("is reformat target:", isReformatTarget)
    if(isReformatTarget):
        # print(nuke.getColor(curNode.knob("tile_color").value()))
        curNode.knob("tile_color").setValue(4278190335)
        # TODO: filter only connected nodes
        outputs = curNode.dependencies()
        print("outputs:", outputs)
        curNode.setSelected(True)
        reformatNode = nuke.createNode("Reformat")
        break
        print("color to red")
    else:
        curNode.knob("tile_color").setValue(536805631)
        print("color to green")


nuke.root().end()
