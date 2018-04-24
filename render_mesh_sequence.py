# TO RUN IT, in blender Pyhon terminal:
#
# 	filename = "/home/dan/Downloads/render_mesh_sequence.py"
# 	exec(compile(open(filename).read(), filename, 'exec'))
#

meshFolder = "/tmp/test"
renderFolder = "/tmp/test"
AmountOfNumbers = 5

def DeleteObject(object):
	# Firs deselect all.
	for iterationObject in bpy.context.scene.objects:
		iterationObject.select = False
	# Then select the given object.
	object.select = True
	# Delete the object and set the mode back to where it was.
	bpy.ops.object.delete()

def RenderPath(folder = "", frame = 0, imageFrameBaseName="", fileEnding = "_render.png"):
	return folder + "/" + imageFrameBaseName + str(frame).zfill(AmountOfNumbers) + fileEnding

def MeshPath(folder = "", frame = 0, fileEnding = ".obj", baseName = "", suffix = ""):
	return folder + "/" + baseName + str(frame).zfill(AmountOfNumbers) + "" + fileEnding

def RenderSequence(startFrame = 0, endFrame = 1):

	# Loop over the frames.
	for currentFrame in range(startFrame, endFrame):
		fullPathToMesh = MeshPath(folder = meshFolder, frame = currentFrame, fileEnding = ".obj", baseName = "mesh.")

		print(fullPathToMesh)			
		bpy.ops.import_scene.obj(filepath = fullPathToMesh)
	
		importedObject = bpy.context.selected_objects[0]
		print(importedObject.name)

		# Render the scene.
		bpy.data.scenes['Scene'].render.filepath = RenderPath(folder = renderFolder, frame = currentFrame)
		bpy.data.scenes['Scene'].render.resolution_percentage = 50
		bpy.ops.render.render(write_still = True) 

		# change current frame
		bpy.context.scene.frame_set(currentFrame)

		DeleteObject(importedObject)

RenderSequence(startFrame = 0, endFrame = 3)

