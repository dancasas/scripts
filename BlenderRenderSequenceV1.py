# TO RUN IT, in blender Pyhon terminal:
#
# 	filename = "/media/dan/data1/dev/scripts/BlenderRenderSequenceV1.py"
# 	exec(compile(open(filename).read(), filename, 'exec'))
#
# Script to render a sequence of ply files with Blender. First, setup your scene
# and material for the imported meshes. Scene must be in "OBJECT"-mode.
# Fill in variables in options.
# References.
# See: http://blender.stackexchange.com/questions/24133/modify-obj-after-import-using-python
# and: http://blenderartists.org/forum/showthread.php?320309-How-to-import-ply-files-from-script
import bpy


SEQUENCE_TO_PROCESS = "Surrey_stepdown"
#SEQUENCE_TO_PROCESS = "Helge_Unicampus"
#SEQUENCE_TO_PROCESS = "Helge_Unicampus_smooth" 
#SEQUENCE_TO_PROCESS = "Pablo" 
#SEQUENCE_TO_PROCESS = "Pablo_second"
#SEQUENCE_TO_PROCESS = "skirt"


if(SEQUENCE_TO_PROCESS == "Surrey_stepdown"):
	################################################
	#
	# Surrey stepdown settings
	#
	#################################################
	# Folder without ending "\\".
	meshFolder="/media/dan/data1/tmp/rigging/04/meshes_SMPL_30fps"
	
	# baseline Mesh folder
	meshFolder_baseline = "/tmp/rigged_fixed15"
	
	# Output folder (without ending "\\").
	#renderFolder = "D:\\dev\\skeletool\\results\\surrey_stepdown\\test012_20-50_20160614172508_rig000.00_lap0.001000_opt01_itr1000_fus0.00_stepdown_io_std10_white_depth8___\\tesselated" 
	#renderFolder="D:\\dev\\skeletool\\results\\surrey_stepdown\\big_hands_20160619173028_rig000.00_lap0.001000_opt01_itr1500_fus0.00_stepdown_io_std10_white_depth8___\\tesselated\\color_with_occlusions"
	renderFolder="/media/dan/data1/tmp/rigging/04/render_meshes_SMPL_30fps"
	
	# Material name for the imported object. The Material already needs to be created.
	materialName = ""
	# Amount of numbers in filepath, e.g., 000010.ply
	AmountOfNumbers = 5
	# If we want to smooth + smooth shading in the mesh
	MESH_SMOOTHING = True
	# If show vertex color or geometry
	USE_VERTEX_COLOR = False
	# If render baseline
	RENDER_BASELINE = False
	RENDER_REFINED = True
	
	imageFrameBaseName = "not_set"
	if(RENDER_BASELINE):
		# Base name for the output PNG frames
		imageFrameBaseName = "mesh_baseline."
	else:
		# Base name for the output PNG frames
		imageFrameBaseName = "rigging_SMPL_."
	
elif(SEQUENCE_TO_PROCESS == "Helge_Unicampus"):
	################################################
	#
	# Helge Unicampus settings
	#
	#################################################
	# Folder without ending "\\".
	#meshFolder = "D:\\dev\\skeletool\\results\\helge_unibus\\20160619164309_rig000.00_lap0.025000_opt01_itr1500_fus0.05_helge_unibus_o_std10_white_depth8___\\tesselated\\renum_tesseleted_ply"
	#meshFolder = "D:\\dev\\skeletool\\results\\helge_unibus\\20160619164309_rig000.00_lap0.025000_opt01_itr1500_fus0.05_helge_unibus_o_std10_white_depth8___\\tesselated_hand_fixed\\renum_recolor\\ply"
	meshFolder = "D:\\dev\\skeletool\\results\\helge_unibus\\20160619164309_rig000.00_lap0.025000_opt01_itr1500_fus0.05_helge_unibus_o_std10_white_depth8___\\tesselated_hand_fixed\\ply_smoothed_tesselated_color\\renum"
	# baseline Mesh folder
	meshFolder_baseline = "D:\\dev\\skeletool\\results\\helge_unibus\\baseline\\tesselated\\renum"  
	# Output folder (without ending "\\").
	#renderFolder = "D:\\dev\\skeletool\\results\\helge_unibus\\20160619164309_rig000.00_lap0.025000_opt01_itr1500_fus0.05_helge_unibus_o_std10_white_depth8___\\tesselated\\renum_tesseleted_ply"
	#renderFolder = "D:\\dev\\skeletool\\results\\helge_unibus\\20160619164309_rig000.00_lap0.025000_opt01_itr1500_fus0.05_helge_unibus_o_std10_white_depth8___\\tesselated_hand_fixed\\renum_recolor\\ply"
	renderFolder  = "D:\\dev\\skeletool\\results\\helge_unibus\\20160619164309_rig000.00_lap0.025000_opt01_itr1500_fus0.05_helge_unibus_o_std10_white_depth8___\\tesselated_hand_fixed\\ply_smoothed_tesselated_color\\renum"
	# Material name for the imported object. The Material already needs to be created.
	materialName = ""
	# Amount of numbers in filepath, e.g., 000010.ply
	AmountOfNumbers = 4 
	# If we want to smooth + smooth shading in the mesh
	MESH_SMOOTHING = True
	# If show vertex color or geometry
	USE_VERTEX_COLOR = False
	# If render baseline
	RENDER_BASELINE = False
	
	RENDER_REFINED = True
	
	imageFrameBaseName = "not_set"
	if(RENDER_BASELINE):
		# Base name for the output PNG frames
		imageFrameBaseName = "mesh_baseline."
	else:
		# Base name for the output PNG frames
		imageFrameBaseName = "mesh_color."
	
elif(SEQUENCE_TO_PROCESS == "Helge_Unicampus_smooth"):
	# Folder without ending "\\".
	meshFolder = "D:\\dev\\skeletool\\results\\helge_unibus\\20160619164309_rig000.00_lap0.025000_opt01_itr1500_fus0.05_helge_unibus_o_std10_white_depth8___\\tesselated_hand_fixed\\renum\\smoothed"
	# baseline Mesh folder
	meshFolder_baseline = "D:\\dev\\skeletool\\results\\helge_unibus\\baseline\\original_hand_fix\\ply_renum_smoothed" 
	# Output folder (without ending "\\").
	renderFolder = "D:\\dev\\skeletool\\results\\helge_unibus\\baseline\\original_hand_fix\\ply_renum_smoothed"
	# Material name for the imported object. The Material already needs to be created.
	materialName = ""
	# Amount of numbers in filepath, e.g., 000010.ply
	AmountOfNumbers = 4 
	# If we want to smooth + smooth shading in the mesh
	MESH_SMOOTHING = True
	# If show vertex color or geometry
	USE_VERTEX_COLOR = False
	# If render baseline
	RENDER_BASELINE = False
	RENDER_REFINED = True
	
	imageFrameBaseName = "not_set"
	if(RENDER_BASELINE):
		# Base name for the output PNG frames
		imageFrameBaseName = "mesh_baseline."
	else:
		# Base name for the output PNG frames
		imageFrameBaseName = "mesh_smooth_shading."


elif(SEQUENCE_TO_PROCESS == "Pablo"):
	# Folder without ending "\\".
	#meshFolder = "D:\\dev\\skeletool\\results\\pablo_stretching\\20160628164245_rig100.00_lap0.045000_opt01_itr1500_fus0.05_pablo_stretching_o_std10_white_depth8___\\to_render\\ply_smoothed"
	meshFolder = "D:\\dev\\skeletool\\results\\pablo_stretching\\20160628164245_rig100.00_lap0.045000_opt01_itr1500_fus0.05_pablo_stretching_o_std10_white_depth8___\\to_render\\ply_smoothed_tesselated_color"
	# baseline Mesh folder
	meshFolder_baseline = "D:\\dev\\skeletool\\results\\pablo_stretching\\baseline\\ply_smoothed" 
	# Output folder (without ending "\\").
	#renderFolder = "D:\\dev\\skeletool\\results\\pablo_stretching\\baseline\\ply_smoothed"
	#renderFolder = "D:\\dev\\skeletool\\results\\pablo_stretching\\20160628164245_rig100.00_lap0.045000_opt01_itr1500_fus0.05_pablo_stretching_o_std10_white_depth8___\\to_render\\ply_smoothed"
	renderFolder = "D:\\dev\\skeletool\\results\\pablo_stretching\\20160628164245_rig100.00_lap0.045000_opt01_itr1500_fus0.05_pablo_stretching_o_std10_white_depth8___\\to_render\\ply_smoothed_tesselated_color"
	# Material name for the imported object. The Material already needs to be created.
	materialName = ""
	# Amount of numbers in filepath, e.g., 000010.ply
	AmountOfNumbers = 4 
	# If we want to smooth + smooth shading in the mesh
	MESH_SMOOTHING = True
	# If show vertex color or geometry
	USE_VERTEX_COLOR = True
	# If render baseline
	RENDER_BASELINE = False
	RENDER_REFINED = True
	
	imageFrameBaseName = "not_set"
	if(RENDER_BASELINE):
		# Base name for the output PNG frames
		imageFrameBaseName = "baseline."
	else:
		# Base name for the output PNG frames
		imageFrameBaseName = "mesh_color."
elif(SEQUENCE_TO_PROCESS == "Pablo_second"):
	# Folder without ending "\\".
	meshFolder = "D:\\dev\\skeletool\\results\\pablo_stretching_second\\20160705172133_rig100.00_lap0.045000_opt01_itr1500_fus0.05_pablo_stretching_o_std10_white_depth8___\\to_render\\ply_smooth_tesselated_color"
	# baseline Mesh folder
	meshFolder_baseline = "D:\\dev\\skeletool\\results\\pablo_stretching\\baseline\\ply_smoothed" 
	# Output folder (without ending "\\").
	renderFolder = "D:\\dev\\skeletool\\results\\pablo_stretching_second\\20160705172133_rig100.00_lap0.045000_opt01_itr1500_fus0.05_pablo_stretching_o_std10_white_depth8___\\to_render\\ply_smooth_tesselated_color"
	# Material name for the imported object. The Material already needs to be created.
	materialName = ""
	# Amount of numbers in filepath, e.g., 000010.ply
	AmountOfNumbers = 4 
	# If we want to smooth + smooth shading in the mesh
	MESH_SMOOTHING = True
	# If show vertex color or geometry
	USE_VERTEX_COLOR = False
	# If render baseline
	RENDER_BASELINE = False
	RENDER_REFINED = True
	
	imageFrameBaseName = "not_set"
	if(RENDER_BASELINE):
		# Base name for the output PNG frames
		imageFrameBaseName = "baseline."
	else:
		# Base name for the output PNG frames
		imageFrameBaseName = "mesh_color."
elif(SEQUENCE_TO_PROCESS == "skirt"):
	# Folder without ending "\\".
	meshFolder = "D:\\dev\\skeletool\\results\\with_depth7\\20160710171644_rig000.00_lap0.000500_opt01_itr1000_fus0.00_v3862_o_std10_SILHOUETTES_white_depth8___\\to_render\\ply_smoothed"
	#meshFolder = "D:\\dev\\skeletool\\results\\with_depth7\\20160710171644_rig000.00_lap0.000500_opt01_itr1000_fus0.00_v3862_o_std10_SILHOUETTES_white_depth8___\\to_render\\ply_smoothed_tesselated_color"
	
	# baseline Mesh folder
	meshFolder_baseline = "D:\\dev\\skeletool\\results\\pablo_stretching\\baseline\\ply_smoothed" 
	# Output folder (without ending "\\").
	renderFolder = "D:\\dev\\skeletool\\results\\with_depth7\\20160710171644_rig000.00_lap0.000500_opt01_itr1000_fus0.00_v3862_o_std10_SILHOUETTES_white_depth8___\\to_render\\ply_smoothed"
	#renderFolder = "D:\\dev\\skeletool\\results\\with_depth7\\20160710171644_rig000.00_lap0.000500_opt01_itr1000_fus0.00_v3862_o_std10_SILHOUETTES_white_depth8___\\to_render\\ply_smoothed_tesselated_color"
	# Material name for the imported object. The Material already needs to be created.
	materialName = ""
	# Amount of numbers in filepath, e.g., 000010.ply
	AmountOfNumbers = 4 
	# If we want to smooth + smooth shading in the mesh
	MESH_SMOOTHING = False
	# If show vertex color or geometry
	USE_VERTEX_COLOR = False
	# If render baseline
	RENDER_BASELINE = False
	RENDER_REFINED = True
	
	imageFrameBaseName = "not_set"
	if(RENDER_BASELINE):
		# Base name for the output PNG frames
		imageFrameBaseName = "baseline."
	else:
		# Base name for the output PNG frames
		imageFrameBaseName = "mesh_color."



# Constants.
M_PI = 3.1415926535897932

# Helper.
def Deg2Rad(degree):
	return degree * (M_PI / 180.0)

def SelectOnlyGivenObject(object):
	# Firs deselect all.
	for iterationObject in bpy.context.scene.objects:
		iterationObject.select = False
	# Then select the given object.
	object.select = True

# Delete an object, see: http://blender.stackexchange.com/questions/27234/python-how-to-completely-remove-an-object
def DeleteObject(object):
	# Cache the currrent mode we are in.
	#oldMode = bpy.context.mode
	# Set it to object mode.
	#bpy.ops.object.mode_set(mode = 'OBJECT')
	# Select only the given object.
	SelectOnlyGivenObject(object)
	# Delete the object and set the mode back to where it was.
	bpy.ops.object.delete()
	#bpy.ops.object.mode_set(mode = oldMode)

def MeshPath(folder = "", frame = 0, fileEnding = ".obj", baseName = "", suffix = ""):
	return folder + "/" + baseName + str(frame).zfill(AmountOfNumbers) + "" + fileEnding

def RenderPath(folder = "", frame = 0, fileEnding = "png"):
	return folder + "/" + imageFrameBaseName + str(frame).zfill(AmountOfNumbers) + "." + fileEnding

def RenderSequence(startFrame = 0, endFrame = 1):
	# Loop over the frames.
	for currentFrame in range(startFrame, endFrame):
	
		if(RENDER_REFINED):
			# Import the object (Either obj or ply).
			fullPathToMesh = MeshPath(folder = meshFolder, frame = currentFrame, fileEnding = "-SMPL.obj", baseName = "frame-")
			# bpy.ops.import_scene.obj(filepath = full_path_to_file)
			print(fullPathToMesh)			
			bpy.ops.import_scene.obj(filepath = fullPathToMesh)
			
			importedObject = bpy.context.selected_objects[0]
			print(importedObject.name)
			
			# bpy.data.objects[imported[].name].select = True
			
			# Get the just imported object.
			# importedObject = bpy.context.object

			if(MESH_SMOOTHING):
				bpy.context.scene.objects.active = importedObject
				bpy.ops.object.mode_set(mode = 'EDIT')
				bpy.ops.mesh.faces_shade_smooth()
								
#				bpy.ops.mesh.vertices_smooth()
#				bpy.ops.mesh.vertices_smooth()
#				bpy.ops.mesh.vertices_smooth()				
#				bpy.ops.mesh.vertices_smooth()
#				bpy.ops.mesh.vertices_smooth()
#				bpy.ops.mesh.vertices_smooth()
#				bpy.ops.mesh.vertices_smooth()
#				bpy.ops.mesh.vertices_smooth()
#				bpy.ops.mesh.vertices_smooth()
#				bpy.ops.mesh.vertices_smooth()
#				bpy.ops.mesh.vertices_smooth()
				
				bpy.ops.object.mode_set(mode = 'OBJECT')
			else:
				bpy.ops.object.mode_set(mode = 'EDIT')
				bpy.ops.mesh.faces_shade_flat()
				bpy.ops.object.mode_set(mode = 'OBJECT')
			
			# scales PLY
			#importedObject.scale = (0.001, 0.001, 0.001)

			# Set its orientation. We need to do this,
			# as PreonLab meshes have another up-axis.
			importedObject.rotation_euler = (Deg2Rad(90), Deg2Rad(0), Deg2Rad(0))
			
			#if USE_VERTEX_COLOR:
			# Get material
			mat = bpy.data.materials.get("MyMaterial")
			if mat is None:
				# create material
				mat = bpy.data.materials.new(name="MyMaterial")
				
			mat.use_object_color
			mat.use_vertex_color_paint
			mat.emit = 1.0
			mat.diffuse_intensity = 0.0
			mat.specular_intensity = 0.0

			# Assign it to object
			if importedObject.data.materials:
				# assign to 1st material slot
				importedObject.data.materials[0] = mat
				print("Assigned to mat[0]")
			else:
			# no slots
				print("Assigned another mat")
				bpy.data.materials[:]
				importedObject.data.materials.append(mat)
			
			mat_id = importedObject.active_material_index
			
			print("Mat ID " + str(mat_id))
#			
#			bpy.ops.material.new()
			bpy.context.object.active_material.use_vertex_color_paint = True
			bpy.context.object.active_material.diffuse_intensity = 0
			bpy.context.object.active_material.specular_intensity = 0
			bpy.context.object.active_material.emit = 1
			bpy.context.object.active_material.ambient = 0
			bpy.context.object.active_material.translucency = 0

			mat_id = importedObject.active_material_index
			
			if(USE_VERTEX_COLOR):
				importedObject.data.materials[mat_id].use_object_color = True
				importedObject.data.materials[mat_id].use_vertex_color_paint = True
				importedObject.data.materials[mat_id].emit = 1.0
				importedObject.data.materials[mat_id].diffuse_intensity = 0.0
				importedObject.data.materials[mat_id].specular_intensity = 0.0
			else:
				importedObject.data.materials[mat_id].use_object_color = False
				importedObject.data.materials[mat_id].use_vertex_color_paint = False
				importedObject.data.materials[mat_id].emit = 0
				importedObject.data.materials[mat_id].diffuse_intensity = 0.5
				importedObject.data.materials[mat_id].specular_intensity = 1
				importedObject.data.materials[mat_id].diffuse_color = (0.8, 0.8, 0.8)		
				importedObject.data.materials[mat_id].ambient = 1.0
				
			
		if(RENDER_BASELINE):
			
			# Imports baselie mesh		
			# Import the object (Either obj or ply).
			fullPathToMesh = MeshPath(folder = meshFolder_baseline, frame = currentFrame, fileEnding = ".obj", baseName = "frame-")
			bpy.ops.import_scene.obj(filepath = fullPathToMesh)
			# bpy.ops.import_mesh.ply(filepath = fullPathToMesh)

			# Get the just imported object.
			# importedObject_baseline = bpy.context.object
			importedObject_baseline = bpy.context.selected_objects[0]
			
			if(MESH_SMOOTHING):
				bpy.ops.object.mode_set(mode = 'EDIT')
				bpy.ops.mesh.faces_shade_smooth()
				bpy.ops.object.editmode_toggle()
				bpy.ops.object.mode_set(mode = 'OBJECT')
			#else:
				#bpy.ops.object.mode_set(mode = 'EDIT')
				#bpy.ops.mesh.faces_shade_flat()
				#bpy.ops.object.mode_set(mode = 'OBJECT')
			
			# scales PLY
			#importedObject_baseline.scale = (0.001, 0.001, 0.001)

			# Set its orientation. We need to do this,
			# as PreonLab meshes have another up-axis.
			importedObject_baseline.rotation_euler = (Deg2Rad(90), Deg2Rad(0), Deg2Rad(0))
			
			# Get material
			mat = bpy.data.materials.get("Material_baseline")
			if mat is None:
				# create material
				mat = bpy.data.materials.new(name="Material_baseline")
				
			mat.use_object_color
			mat.use_vertex_color_paint
			mat.emit = 1.0
			mat.diffuse_intensity = 0.0
			mat.specular_intensity = 0.0

			# Assign it to object
			if importedObject_baseline.data.materials:
				# assign to 1st material slot
				importedObject_baseline.data.materials[0] = mat
				print("Assigned to mat[0]")
			else:
				# no slots
				print("Assigned another mat")
				bpy.data.materials[:]
				importedObject_baseline.data.materials.append(mat)
			
			mat_id = importedObject_baseline.active_material_index
			
			print("Mat ID baseline " + str(mat_id))
			
			if(USE_VERTEX_COLOR):
				importedObject_baseline.data.materials[mat_id].use_object_color = True
				importedObject_baseline.data.materials[mat_id].use_vertex_color_paint = True
				importedObject_baseline.data.materials[mat_id].emit = 1.0
				importedObject_baseline.data.materials[mat_id].diffuse_intensity = 0.0
				importedObject_baseline.data.materials[mat_id].specular_intensity = 0.0
			else:
				importedObject_baseline.data.materials[mat_id].use_object_color = False
				importedObject_baseline.data.materials[mat_id].use_vertex_color_paint = False
				importedObject_baseline.data.materials[mat_id].emit = 0.0
				importedObject_baseline.data.materials[mat_id].diffuse_intensity = 1.0
				importedObject_baseline.data.materials[mat_id].specular_intensity = 0.0		
				importedObject_baseline.data.materials[mat_id].diffuse_color = (1.0, 0.6, 0.5)
			
		# Render the scene.
		bpy.data.scenes['Scene'].render.filepath = RenderPath(folder = renderFolder, frame = currentFrame)
		bpy.data.scenes['Scene'].render.resolution_percentage = 20
		bpy.ops.render.render(write_still = True) 
		
		# change current frame
		bpy.context.scene.frame_set(currentFrame)
		
		# Delete the imported object again.
		if (RENDER_REFINED):
			DeleteObject(importedObject)
		
		if(RENDER_BASELINE):
			DeleteObject(importedObject_baseline)
		

# Run the script.
RenderSequence(startFrame = 0, endFrame = 920)
