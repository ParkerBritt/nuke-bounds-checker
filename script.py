# curNode = nuke.selectedNode()
print("\n\n\n\n\n\n")
allNodes = nuke.root().nodes()
for curNode in allNodes:
    print("name:", curNode.name())
    bbox = curNode.bbox()
    print(bbox.x(), bbox.y(), bbox.w(), bbox.h())
    print(curNode.width(), curNode.height())

    isReformatTarget = bbox.x()<-200 or bbox.y()<-200 or (bbox.x()+bbox.w())>(curNode.width()+200) or (bbox.y()+bbox.h())>(curNode.height()+200)
    print("is reformat target:", isReformatTarget)
    if(isReformatTarget):
        # print(nuke.getColor(curNode.knob("tile_color").value()))
        curNode.knob("tile_color").setValue(4278190335)
        print("color to red")
    else:
        curNode.knob("tile_color").setValue(536805631)
        print("color to green")


