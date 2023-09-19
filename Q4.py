import arcpy

# Setting the default workspace environment
arcpy.env.workspace = r"D:\Sem-3\Programming for GIS-3\Assignment\Practical_1_ProProject\01_Running_Python_Scripts.gdb"
input_feature = "Wilson_Zoning"
output_feature = "Wilson_Zone_FeatureToPoint"
arcpy.management.FeatureToPoint(input_feature, output_feature, "CENTROID")

print("Procces Completed")

