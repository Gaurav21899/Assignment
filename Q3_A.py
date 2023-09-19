import arcpy

# Setting the default workspace environment
arcpy.env.workspace = r"D:\Sem-3\Programming for GIS-3\Assignment\Practical_1_ProProject\01_Running_Python_Scripts.gdb"
arcpy.analysis.Buffer("Wilson_Schools","Wilson_Schools_Buffer_500","500 meters")

print("Process Completed")

