import arcpy

arcpy.env.workspace = r"D:\Sem-3\Programming for GIS-3\Assignment\Practical_1_ProProject\01_Running_Python_Scripts.gdb"

# Input feature layer or feature class
input_layer = "Wilson_Schools"

# Buffer distances in feet
buffer_distances = [1000, 1200, 1600]

 # Output feature class name
output_layer = "Wilson_School_MultiRing_Buffer"

# Create buffer
arcpy.analysis.MultipleRingBuffer(input_layer, output_layer, buffer_distances, "Feet", "", "NONE")
print("Process Completed")




