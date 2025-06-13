#!/usr/bin/env python

import json, os

buildText = ""

with open("./template.nk") as nukeTemplate:
    with open("./script.py") as nukeScript:
        nukeScriptTxt = nukeScript.read()
        scriptFormatedAdd = json.dumps(nukeScriptTxt+"\naddNodes()")
        scriptFormatedRemove = json.dumps(nukeScriptTxt+"\nremoveNodes()")

        buildText = nukeTemplate.read()
        buildText = buildText.replace("{SCRIPT_PLACEHOLDER_ADD}", scriptFormatedAdd)
        buildText = buildText.replace("{SCRIPT_PLACEHOLDER_REMOVE}", scriptFormatedRemove)



if(not os.path.exists("./build")):
    os.mkdir("./build")

with open("./build/BoundsCheckerNode.nk", "w") as buildNode:
    buildNode.write(buildText)
