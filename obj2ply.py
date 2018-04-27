import numpy as np

meshToProcess = "MANO"
# meshToProcess = "CLAP"

if meshToProcess is "MANO":
    filePathInput = "/media/dan/data1/dev/MANOTracker/models/MANO_mesh_afterOpt.obj"
    filePathOutput = "/media/dan/data1/dev/MANOTracker/models/MANO_mesh_afterOpt.ply"
elif meshToProcess is "CLAP":
    filePathInput = "/media/dan/data1/dev/MANOTracker/models/hand_mesh_hires_closed_scaled.obj"
    filePathOutput = "/media/dan/data1/dev/MANOTracker/models/hand_mesh_hires_closed_scaled.ply"


numVertices = 0
numFaces = 0
vertices = np.empty((0, 3), float)
faces = np.empty((0, 3), int)

with open(filePathInput, 'r') as fileIn:

    # Reads input OBJ to count number of faces and vertices
    for line in fileIn:
        lineSplit = line.split(" ")

        # If current line defines a vertex
        if "v" in lineSplit:
            # Converts from string to float
            currentVertex = np.array([[float(lineSplit[1]), float(lineSplit[2]), float(lineSplit[3])]])
            # Appends to vertices array
            vertices = np.append(vertices, currentVertex, axis=0)

            numVertices += 1

        # If current line defines a face
        if "f" in lineSplit:
            #
            # Note: faces are defined in OBJ files using the following syntax:
            #
            # f 2819/2903/2819 2752/2836/2752 2748/2832/2748
            #    ^    ^     ^    ^   ^    ^     ^    ^     ^
            #    |    |     |    |   |    |     |    |     |
            #  vertex         vertex          vertex
            #   ID x           ID y            ID z

            componentX = lineSplit[1].split("/")
            componentY = lineSplit[2].split("/")
            componentZ = lineSplit[3].split("/")

            # Converts from string to ints
            currentFace = np.array([[int(componentX[0]), int(componentY[0]), int(componentZ[0])]])
            # Appends to faces array
            faces = np.append(faces, currentFace, axis=0)

            numFaces += 1

    print "Num vertices: %d" % numVertices
    print "Num faces:    %d" % numFaces
    print "Vertices size:%d x %d" % (vertices.shape[0], vertices.shape[1])
    print "Faces size:   %d x %d" % (faces.shape[0], faces.shape[1])

    # Gets maximum and minimum vertex position values
    maxValues = vertices.max(axis=0)
    minValues = vertices.min(axis=0)

    # Open target PLY to write
    with open(filePathOutput, 'w+') as fileOut:

        # Writes ply header
        fileOut.write("ply\n")
        fileOut.write("format ascii 1.0\n")
        fileOut.write("comment VCGLIB generated\n")
        fileOut.write("element vertex " + str(numVertices) + "\n")
        fileOut.write("property float x\n")
        fileOut.write("property float y\n")
        fileOut.write("property float z\n")
        fileOut.write("property uchar red\n")
        fileOut.write("property uchar green\n")
        fileOut.write("property uchar blue\n")
        fileOut.write("property uchar alpha\n")
        fileOut.write("element face " + str(numFaces) + "\n")
        fileOut.write("property list uchar int vertex_indices\n")
        fileOut.write("end_header\n")

        # Writes vertices
        for v in vertices:
            # Computes the color of the current vertex assuming we want to put it in a normalized unit cube
            red = int((v[0] - minValues[0]) / (maxValues[0] - minValues[0]) * 255)
            green = int((v[1] - minValues[1]) / (maxValues[1] - minValues[1]) * 255)
            blue = int((v[2] - minValues[2]) / (maxValues[2] - minValues[2]) * 255)

            # writes "x y z" of current vertex
            fileOut.write(str(v[0]) + " " + str(v[1]) + " " + str(v[2]) + " ")
            # write "red green blue alpha" of current vertex
            fileOut.write(str(red) + " " + str(green) + " " + str(blue) + " 255\n")


        # Writes faces
        for f in faces:
            # WARNING: Subtracts 1 to vertex ID because PLY indices start at 0 and OBJ at 1
            fileOut.write("3 " + str(f[0]-1) + " " + str(f[1]-1) + " " + str(f[2]-1) + "\n")
